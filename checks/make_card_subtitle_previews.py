"""Render each card as a standalone PNG for visual QA."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from build.card_timeline import build_card_timings  # noqa: E402
from build.render_cards import render_card_image  # noqa: E402
from segments import DESIGN, SEGMENTS  # noqa: E402

OUTPUT_DIR = ROOT / "output" / "debug" / "card_previews"


def main() -> int:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    timings = build_card_timings(SEGMENTS, design=DESIGN)
    details = []
    for index, (segment, timing) in enumerate(zip(SEGMENTS, timings), start=1):
        output = OUTPUT_DIR / f"card_{index:02d}.png"
        render_card_image(segment, timing, DESIGN).save(output)
        details.append({"card": index, "type": segment.get("type"), "output": str(output)})
    print(json.dumps({"ok": True, "outputs": details}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
