"""Create a non-blocking preview QA advisory from a packaged preview context."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = ROOT / "output" / "debug" / "preview_qa_input.json"
OUTPUT_PATH = ROOT / "output" / "debug" / "preview_qa_advisory.json"


def build_advisory(payload: dict[str, Any]) -> dict[str, Any]:
    concerns = []
    if not payload.get("frames"):
        concerns.append({"level": "concern", "message": "No keyframes were packaged; human preview review is required."})
    if not payload.get("manifest"):
        concerns.append({"level": "concern", "message": "No TTS manifest was packaged; timing QA is limited."})

    return {
        "ok": True,
        "status": "advisory_only",
        "model": None,
        "human_preview_required": True,
        "project": payload.get("project"),
        "frames_reviewed": len(payload.get("frames", [])),
        "concerns": concerns,
        "message": "Deterministic advisory generated. No multimodal model is configured in v1.",
    }


def main() -> int:
    if not INPUT_PATH.exists():
        print(json.dumps({"ok": False, "error": f"preview QA package not found: {INPUT_PATH}"}, indent=2), file=sys.stderr)
        return 1
    payload = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    advisory = build_advisory(payload)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(advisory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "path": OUTPUT_PATH.relative_to(ROOT).as_posix(), "status": "advisory_only"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
