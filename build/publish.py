"""Prepare rendered videos and sidecar metadata for YouTube upload."""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any
import warnings

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from build.audio import text_hash, voice_for_segment  # noqa: E402
from build.camera import crop_and_resize  # noqa: E402
from build.design import apply_grade  # noqa: E402
from build.render_cards import synthesize_card_thumbnail  # noqa: E402
from build.segment_adapter import RENDER_TYPE_CARDS, RENDER_TYPE_DIARY, description_text, narration_text  # noqa: E402
from segments import (  # noqa: E402
    AUDIO,
    CHAPTERS,
    DESCRIPTION_INTRO,
    DESCRIPTION_OUTRO,
    DESIGN,
    EPISODE,
    IMAGE_PATH,
    LANGUAGE,
    LEVEL,
    OUTPUT_NAME,
    RENDER_VERSION,
    RENDER_TYPE,
    SEGMENTS,
    SERIES,
    SERIES_TITLE,
    THUMBNAIL_PATH,
    YOUTUBE_TITLE,
)

PROJECT = os.environ.get("PROJECT", "reunion_madrid")
PROJECT_MODULE = importlib.import_module(f"projects.{PROJECT}")
OUTPUT_DIR = ROOT / "output"
PUBLISH_DIR = OUTPUT_DIR / "publish"
META_DIR = OUTPUT_DIR / "meta"
THUMBS_DIR = OUTPUT_DIR / "thumbs"
MANIFEST_PATH = OUTPUT_DIR / "audio" / "tts" / "manifest.json"
MEMORY_DIR = Path.home() / ".claude" / "projects" / "-Users-peter-Moex" / "memory"
DECISION_LOG_DIR = MEMORY_DIR / "episode-decisions"
ASPECT = "16x9"
THUMBNAIL_SIZE = (1280, 720)
MIN_CHAPTER_SECONDS = 10.0
DEFAULT_TAGS = [
    "스페인어",
    "Spanish B2",
    "aprender español",
    "DELE B2",
    "스페인어 청해",
    "Descripción de imagen",
]
HASHTAGS = ["#SpanishB2", "#DELEB2", "#aprenderespañol"]


class PublishError(RuntimeError):
    """Raised when publish assets cannot be generated safely."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare a rendered project for YouTube publishing.")
    parser.add_argument(
        "--skip-render-check",
        action="store_true",
        help="Skip shared manifest validation and omit chapters. Use only for existing MP4 packaging.",
    )
    return parser.parse_args()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def versioned_prefix() -> str:
    return f"{SERIES}-ep{int(EPISODE):02d}-{OUTPUT_NAME}-{ASPECT}-v{int(RENDER_VERSION)}"


def thumbnail_prefix() -> str:
    return f"{SERIES}-ep{int(EPISODE):02d}-{OUTPUT_NAME}"


def decision_log_name(episode: int | str = EPISODE, slug: str = OUTPUT_NAME) -> str:
    return f"ep{int(episode):02d}-{slug}.jsonl"


def decision_log_path(log_dir: Path = DECISION_LOG_DIR, episode: int | str = EPISODE, slug: str = OUTPUT_NAME) -> Path:
    return log_dir / decision_log_name(episode, slug)


def parse_rate(rate: str | None) -> float:
    if not rate:
        return 0.0
    try:
        return float(Fraction(rate))
    except (ValueError, ZeroDivisionError):
        return 0.0


def ffprobe(path: Path) -> dict[str, Any]:
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-print_format",
            "json",
            "-show_format",
            "-show_streams",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    probe = json.loads(result.stdout)
    video_stream = next((stream for stream in probe["streams"] if stream.get("codec_type") == "video"), None)
    if not video_stream:
        raise PublishError(f"no video stream found in {rel(path)}")

    fps = parse_rate(video_stream.get("avg_frame_rate") or video_stream.get("r_frame_rate"))
    duration = float(probe.get("format", {}).get("duration", 0.0))
    return {
        "path": rel(path),
        "width": int(video_stream.get("width", 0)),
        "height": int(video_stream.get("height", 0)),
        "fps": round(fps, 3),
        "duration_s": round(duration, 3),
    }


def load_manifest() -> dict[str, Any]:
    if not MANIFEST_PATH.exists():
        raise PublishError(
            f"audio manifest not found: {rel(MANIFEST_PATH)}. "
            "Run `PROJECT=<name> make render` before publishing this project."
        )
    try:
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise PublishError(f"audio manifest is invalid JSON: {exc}") from exc


def validate_manifest(manifest: dict[str, Any]) -> None:
    manifest_segments = manifest.get("segments")
    if not isinstance(manifest_segments, list):
        raise PublishError("audio manifest is missing a `segments` list")
    if len(manifest_segments) != len(SEGMENTS):
        raise PublishError(
            "audio manifest does not match current project: "
            f"manifest has {len(manifest_segments)} segments, current project has {len(SEGMENTS)}. "
            "Run `PROJECT=<name> make render` and publish again."
        )

    audio_cfg = AUDIO or {}
    rate_wpm = int(audio_cfg.get("rate_wpm", manifest.get("rate_wpm", 175)))
    expected_hashes = [
        text_hash(narration_text(segment, RENDER_TYPE), voice_for_segment(segment, audio_cfg), rate_wpm)
        for segment in SEGMENTS
    ]
    actual_hashes = [str(segment.get("text_hash", "")) for segment in manifest_segments]
    if actual_hashes != expected_hashes:
        raise PublishError(
            "audio manifest text hashes do not match current project. "
            "This usually means another PROJECT was rendered last. "
            "Run `PROJECT=<name> make render` and publish again."
        )


def format_timestamp(seconds: float) -> str:
    total = int(seconds)
    hours, remainder = divmod(total, 3600)
    minutes, secs = divmod(remainder, 60)
    if hours:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    return f"{minutes}:{secs:02d}"


def auto_chapters(manifest: dict[str, Any], duration_s: float) -> list[dict[str, Any]]:
    manifest_segments = manifest["segments"]
    if CHAPTERS:
        segments_by_index = {int(segment["index"]): segment for segment in manifest_segments}
        chapters = []
        for chapter in CHAPTERS:
            index = int(chapter["segment"])
            if index not in segments_by_index:
                raise PublishError(f"chapter references missing segment #{index}")
            chapters.append(
                {
                    "start_s": round(float(segments_by_index[index]["start_s"]), 3),
                    "title": str(chapter["title"]),
                }
            )
    else:
        chapters = []
        for segment in manifest_segments:
            start_s = float(segment["start_s"])
            if not chapters or start_s - float(chapters[-1]["start_s"]) >= MIN_CHAPTER_SECONDS:
                chapters.append({"start_s": round(start_s, 3), "title": f"Parte {segment['index']}"})

    validate_chapters(chapters, duration_s)
    return chapters


def validate_chapters(chapters: list[dict[str, Any]], duration_s: float) -> None:
    if len(chapters) < 3:
        raise PublishError("YouTube chapters require at least three timestamps")
    if round(float(chapters[0]["start_s"]), 3) != 0.0:
        raise PublishError("the first YouTube chapter must start at 0:00")

    for current, next_chapter in zip(chapters, chapters[1:]):
        gap = float(next_chapter["start_s"]) - float(current["start_s"])
        if gap < MIN_CHAPTER_SECONDS:
            raise PublishError(
                "YouTube chapters must be at least 10 seconds long: "
                f"`{current['title']}` is {gap:.3f}s before the next chapter"
            )

    final_gap = duration_s - float(chapters[-1]["start_s"])
    if final_gap < MIN_CHAPTER_SECONDS:
        raise PublishError(
            "YouTube chapters must be at least 10 seconds long: "
            f"final chapter `{chapters[-1]['title']}` is {final_gap:.3f}s"
        )


def make_title() -> str:
    if YOUTUBE_TITLE:
        return str(YOUTUBE_TITLE)
    readable = OUTPUT_NAME.replace("-", " ").title()
    return f"{readable} | {SERIES_TITLE} · Ep.{int(EPISODE)}"


def korean_teaser() -> str:
    return str(getattr(PROJECT_MODULE, "KOREAN_TEASER", "") or "").strip()


def make_description(chapters: list[dict[str, Any]], teaser: str | None = None) -> str:
    lines: list[str] = []
    if chapters:
        lines.extend(f"{format_timestamp(float(chapter['start_s']))} {chapter['title']}" for chapter in chapters)
        lines.append("")

    if DESCRIPTION_INTRO:
        lines.extend([str(DESCRIPTION_INTRO), ""])

    teaser_text = korean_teaser() if teaser is None else str(teaser).strip()
    if teaser_text:
        lines.extend([teaser_text, ""])

    lines.append("Guion del video:")
    for index, segment in enumerate(SEGMENTS, start=1):
        text = description_text(segment, RENDER_TYPE)
        if not text:
            continue
        if RENDER_TYPE == RENDER_TYPE_CARDS:
            lines.append(text)
        else:
            lines.append(f"{index:02d}. {text}")

    if DESCRIPTION_OUTRO:
        lines.extend(["", str(DESCRIPTION_OUTRO)])

    project_hashtags = list(getattr(PROJECT_MODULE, "EXTRA_HASHTAGS", []) or [])
    base_hashtags = list(getattr(PROJECT_MODULE, "BASE_HASHTAGS", HASHTAGS) or [])
    merged_hashtags = list(dict.fromkeys(project_hashtags + base_hashtags))
    lines.extend(
        [
            "",
            f"Serie: {SERIES_TITLE}",
            f"Nivel: {LEVEL}",
            " ".join(merged_hashtags),
            "",
        ]
    )
    return "\n".join(lines)


def ensure_thumbnail(path: Path) -> None:
    if path.exists():
        return
    if THUMBNAIL_PATH:
        source_path = ROOT / THUMBNAIL_PATH
        if not source_path.exists():
            raise PublishError(f"thumbnail source not found: {THUMBNAIL_PATH}")
        shutil.copy2(source_path, path)
        return
    if RENDER_TYPE == RENDER_TYPE_CARDS:
        synthesize_card_thumbnail(SEGMENTS, DESIGN, path)
        return
    if RENDER_TYPE == RENDER_TYPE_DIARY:
        from build.render_diary import render_diary_segment_image
        from build.diary_timeline import build_diary_timings
        timings = build_diary_timings(SEGMENTS, design=DESIGN, tts_durations=None, audio_cfg=AUDIO)
        image = render_diary_segment_image(SEGMENTS[0], timings[0], DESIGN)
        image.save(path, format="JPEG", quality=92, optimize=True)
        return
    source = Image.open(ROOT / IMAGE_PATH).convert("RGB")
    source = apply_grade(source, DESIGN.get("grade"))
    first_segment = SEGMENTS[0]
    zoom = float(first_segment.get("zoom", {}).get("start", 1.0))
    frame = crop_and_resize(source, first_segment["frame"], zoom, output_size=THUMBNAIL_SIZE)
    Image.fromarray(frame).save(path, format="JPEG", quality=92, optimize=True)


def ensure_no_versioned_overwrite(paths: list[Path]) -> None:
    existing = [rel(path) for path in paths if path.exists()]
    if existing:
        raise PublishError(
            "publish artifact already exists; bump RENDER_VERSION before republishing: " + ", ".join(existing)
        )


def load_decision_events(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        warnings.warn(
            f"decision log not found: {path}. Publish will continue without a decision snapshot.",
            RuntimeWarning,
            stacklevel=2,
        )
        return []

    events: list[dict[str, Any]] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            raise PublishError(f"decision log is invalid JSONL at {path}:{line_no}: {exc}") from exc
        if not isinstance(event, dict):
            raise PublishError(f"decision log event must be an object at {path}:{line_no}")
        events.append(event)
    return events


def write_decision_snapshot(
    path: Path,
    source_log: Path,
    *,
    episode: int | str = EPISODE,
    slug: str = OUTPUT_NAME,
) -> bool:
    events = load_decision_events(source_log)
    if not events:
        return False

    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "episode": int(episode),
        "slug": slug,
        "source_log": str(source_log),
        "events": events,
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return True


def build_metadata(
    video: dict[str, Any],
    thumbnail_path: Path,
    description_path: Path,
    chapters: list[dict[str, Any]],
    decisions_path: Path | None = None,
) -> dict:
    project_tags = list(getattr(PROJECT_MODULE, "EXTRA_TAGS", []) or [])
    base_tags = list(getattr(PROJECT_MODULE, "BASE_TAGS", DEFAULT_TAGS) or [])
    merged_tags = list(dict.fromkeys(project_tags + base_tags))
    youtube = {
        "title": make_title(),
        "description_md": rel(description_path),
        "tags": merged_tags,
        "category": "Education",
        "default_audio_language": LANGUAGE,
        "made_for_kids": False,
        "playlist": SERIES_TITLE,
    }
    if decisions_path is not None:
        youtube["decisions_json"] = rel(decisions_path)

    return {
        "series": {"slug": SERIES, "title": SERIES_TITLE},
        "episode": int(EPISODE),
        "slug": OUTPUT_NAME,
        "level": LEVEL,
        "language": LANGUAGE,
        "version": int(RENDER_VERSION),
        "video": video,
        "thumbnail": rel(thumbnail_path),
        "youtube": youtube,
        "chapters": chapters,
    }


def publish(skip_render_check: bool = False) -> dict[str, Any]:
    source_video = OUTPUT_DIR / f"{OUTPUT_NAME}.mp4"
    if not source_video.exists():
        raise PublishError(f"rendered video not found: {rel(source_video)}")

    PUBLISH_DIR.mkdir(parents=True, exist_ok=True)
    META_DIR.mkdir(parents=True, exist_ok=True)
    THUMBS_DIR.mkdir(parents=True, exist_ok=True)

    prefix = versioned_prefix()
    video_path = PUBLISH_DIR / f"{prefix}.mp4"
    json_path = META_DIR / f"{prefix}.json"
    description_path = META_DIR / f"{prefix}.md"
    decisions_path = META_DIR / f"{prefix}-decisions.json"
    thumbnail_path = THUMBS_DIR / f"{thumbnail_prefix()}.jpg"
    ensure_no_versioned_overwrite([video_path, json_path, description_path, decisions_path])

    manifest = None
    if not skip_render_check:
        manifest = load_manifest()
        validate_manifest(manifest)

    shutil.copy2(source_video, video_path)
    video = ffprobe(video_path)
    chapters = auto_chapters(manifest, video["duration_s"]) if manifest else []
    description = make_description(chapters)
    ensure_thumbnail(thumbnail_path)
    has_decisions = write_decision_snapshot(decisions_path, decision_log_path())
    metadata = build_metadata(video, thumbnail_path, description_path, chapters, decisions_path if has_decisions else None)

    description_path.write_text(description, encoding="utf-8")
    json_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    return {
        "ok": True,
        "project": OUTPUT_NAME,
        "video": rel(video_path),
        "metadata": rel(json_path),
        "description": rel(description_path),
        "thumbnail": rel(thumbnail_path),
        "chapters": len(chapters),
        "render_check": not skip_render_check,
    }


def main() -> int:
    args = parse_args()
    try:
        result = publish(skip_render_check=args.skip_render_check)
    except (PublishError, subprocess.CalledProcessError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
