"""Non-blocking frame proposal placeholder.

The deterministic pack step is usable today. A multimodal model adapter can later
replace this placeholder while keeping the output schema stable.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = ROOT / "output" / "debug" / "frame_proposal_input.json"
OUTPUT_PATH = ROOT / "output" / "debug" / "proposed_frames.json"


def main() -> int:
    if not INPUT_PATH.exists():
        print(json.dumps({"ok": False, "error": f"frame proposal package not found: {INPUT_PATH}"}, indent=2), file=sys.stderr)
        return 1
    payload = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    result = {
        "ok": True,
        "status": "model_not_configured",
        "project": payload.get("project"),
        "policy": "hint_only_producer_decides",
        "suggestions": [],
        "message": "Run propose-frames-pack now; configure a multimodal model adapter before expecting frame suggestions.",
    }
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "path": OUTPUT_PATH.relative_to(ROOT).as_posix(), "status": result["status"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
