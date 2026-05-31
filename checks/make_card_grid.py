"""Generate a contact sheet of card slides."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from build.card_timeline import build_card_timings  # noqa: E402
from build.render_cards import render_card_image  # noqa: E402
from build.subtitles import load_font  # noqa: E402
from segments import DESIGN, SEGMENTS  # noqa: E402

OUTPUT_PATH = ROOT / "output" / "debug" / "card_grid.png"


def main() -> int:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    timings = build_card_timings(SEGMENTS, design=DESIGN)
    cell_w, cell_h = 320, 180
    label_h = 28
    cols = 4
    rows = math.ceil(len(SEGMENTS) / cols)
    sheet = Image.new("RGB", (cols * cell_w, rows * (cell_h + label_h)), (28, 30, 34))
    draw = ImageDraw.Draw(sheet)
    font = load_font(16)
    for idx, (segment, timing) in enumerate(zip(SEGMENTS, timings)):
        row = idx // cols
        col = idx % cols
        x = col * cell_w
        y = row * (cell_h + label_h)
        card = render_card_image(segment, timing, DESIGN).resize((cell_w, cell_h), Image.Resampling.LANCZOS)
        sheet.paste(card, (x, y + label_h))
        draw.rectangle((x, y, x + cell_w, y + label_h), fill=(0, 0, 0))
        label = f"{idx + 1:02d} {segment.get('type', '')}"
        draw.text((x + 8, y + 5), label, font=font, fill=(255, 255, 255))
    sheet.save(OUTPUT_PATH)
    print(json.dumps({"ok": True, "output": str(OUTPUT_PATH), "cards": len(SEGMENTS)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
