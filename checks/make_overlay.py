"""Generate a source-image overlay showing all segment frames."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from build.subtitles import load_font  # noqa: E402
from segments import IMAGE_PATH, SEGMENTS  # noqa: E402

OUTPUT_PATH = ROOT / "output" / "debug" / "segments_overlay.jpg"


def main() -> int:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    image = Image.open(ROOT / IMAGE_PATH).convert("RGB")
    draw = ImageDraw.Draw(image, "RGBA")
    font = load_font(18)
    colors = [
        (230, 57, 70, 220),
        (29, 53, 87, 220),
        (42, 157, 143, 220),
        (244, 162, 97, 220),
        (131, 56, 236, 220),
        (255, 183, 3, 220),
    ]
    for index, segment in enumerate(SEGMENTS, start=1):
        frame = segment["frame"]
        color = colors[(index - 1) % len(colors)]
        x, y, w, h = frame["x"], frame["y"], frame["w"], frame["h"]
        draw.rectangle((x, y, x + w, y + h), outline=color, width=4)
        label = f"{index:02d} {' '.join(segment['text'].split()[:4])}"
        bbox = draw.textbbox((x + 6, y + 6), label, font=font, stroke_width=1)
        draw.rectangle((bbox[0] - 4, bbox[1] - 3, bbox[2] + 4, bbox[3] + 3), fill=(0, 0, 0, 170))
        draw.text((x + 6, y + 6), label, font=font, fill=(255, 255, 255, 255), stroke_width=1)

    image.save(OUTPUT_PATH, quality=92)
    print(json.dumps({"ok": True, "output": str(OUTPUT_PATH)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
