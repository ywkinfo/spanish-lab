"""Package preview frames and transcript context for advisory QA."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import segments as project_segments  # noqa: E402
from build.segment_adapter import display_text, get_render_type  # noqa: E402
from segments import CHAPTERS, OUTPUT_NAME, SEGMENTS  # noqa: E402

OUTPUT_DIR = ROOT / "output"
PREVIEW_PATH = OUTPUT_DIR / "preview.mp4"
MANIFEST_PATH = OUTPUT_DIR / "audio" / "tts" / "manifest.json"
FRAME_DIR = OUTPUT_DIR / "debug" / "preview_qa_frames"
PACKAGE_PATH = OUTPUT_DIR / "debug" / "preview_qa_input.json"
MAX_FRAMES = 10


def load_manifest() -> dict[str, Any] | None:
    if not MANIFEST_PATH.exists():
        return None
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def selected_times(manifest: dict[str, Any] | None) -> list[dict[str, Any]]:
    if not manifest or not isinstance(manifest.get("segments"), list):
        return []
    manifest_segments = manifest["segments"]
    by_index = {int(segment["index"]): segment for segment in manifest_segments}
    picks: list[dict[str, Any]] = []

    for chapter in CHAPTERS or []:
        index = int(chapter["segment"])
        segment = by_index.get(index)
        if segment:
            picks.append({"kind": "chapter", "segment": index, "timestamp_s": float(segment["start_s"])})

    if len(picks) < MAX_FRAMES:
        step = max(1, len(manifest_segments) // max(1, MAX_FRAMES - len(picks)))
        for segment in manifest_segments[::step]:
            if len(picks) >= MAX_FRAMES:
                break
            start = float(segment["start_s"])
            end = float(segment["end_s"])
            picks.append({"kind": "midpoint", "segment": int(segment["index"]), "timestamp_s": round((start + end) / 2, 3)})

    seen: set[tuple[int, float]] = set()
    unique = []
    for pick in sorted(picks, key=lambda item: (float(item["timestamp_s"]), str(item["kind"]))):
        key = (int(pick["segment"]), round(float(pick["timestamp_s"]), 3))
        if key in seen:
            continue
        seen.add(key)
        unique.append({**pick, "timestamp_s": round(float(pick["timestamp_s"]), 3)})
    return unique[:MAX_FRAMES]


def extract_frame(timestamp_s: float, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-hide_banner",
            "-loglevel",
            "error",
            "-ss",
            f"{timestamp_s:.3f}",
            "-i",
            str(PREVIEW_PATH),
            "-frames:v",
            "1",
            str(out_path),
        ],
        check=True,
    )


def package() -> dict[str, Any]:
    if not PREVIEW_PATH.exists():
        raise FileNotFoundError(f"preview not found: {PREVIEW_PATH}")
    manifest = load_manifest()
    picks = selected_times(manifest)
    frames = []
    for index, pick in enumerate(picks, start=1):
        frame_path = FRAME_DIR / f"qa_{index:02d}_seg_{int(pick['segment']):02d}_{pick['kind']}.png"
        extract_frame(float(pick["timestamp_s"]), frame_path)
        frames.append({**pick, "frame": frame_path.relative_to(ROOT).as_posix()})

    payload = {
        "project": OUTPUT_NAME,
        "preview": PREVIEW_PATH.relative_to(ROOT).as_posix(),
        "manifest": MANIFEST_PATH.relative_to(ROOT).as_posix() if MANIFEST_PATH.exists() else None,
        "frames": frames,
        "segments": [
            {"index": index, "text": display_text(segment, get_render_type(project_segments))}
            for index, segment in enumerate(SEGMENTS, start=1)
        ],
        "policy": "advisory_only_human_preview_required",
    }
    PACKAGE_PATH.parent.mkdir(parents=True, exist_ok=True)
    PACKAGE_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return payload


def main() -> int:
    try:
        payload = package()
    except (FileNotFoundError, subprocess.CalledProcessError, json.JSONDecodeError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1
    print(json.dumps({"ok": True, "path": PACKAGE_PATH.relative_to(ROOT).as_posix(), "frames": len(payload["frames"])}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
