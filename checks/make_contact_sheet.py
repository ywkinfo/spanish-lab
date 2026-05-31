"""Generate a 4x4 contact sheet of first frames with subtitles."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from build.camera import composite_rgba, crop_and_resize, output_size_for_design  # noqa: E402
from build.design import apply_grade  # noqa: E402
from build.subtitles import load_font, render_subtitle_image  # noqa: E402
from segments import DESIGN, IMAGE_PATH, SEGMENTS  # noqa: E402

OUTPUT_PATH = ROOT / "output" / "debug" / "contact_sheet.jpg"


def main() -> int:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    source = Image.open(ROOT / IMAGE_PATH).convert("RGB")
    if DESIGN:
        source = apply_grade(source, DESIGN.get("grade"))
    output_size = output_size_for_design(DESIGN)
    cell_w, cell_h = 320, 180
    cols = 4
    rows = math.ceil(len(SEGMENTS) / cols)
    label_h = 24
    sheet = Image.new("RGB", (cols * cell_w, rows * (cell_h + label_h)), (20, 20, 20))
    draw = ImageDraw.Draw(sheet)
    font = load_font(16)

    for idx, segment in enumerate(SEGMENTS):
        row = idx // cols
        col = idx % cols
        zoom = segment.get("zoom", {}).get("start", 1.0)
        frame_array = crop_and_resize(source, segment["frame"], zoom, output_size=output_size)
        base = Image.fromarray(frame_array).convert("RGB")
        subtitle = render_subtitle_image(segment["text"], video_size=output_size, design=DESIGN)
        composed = composite_rgba(base, subtitle)
        thumb = composed.resize((cell_w, cell_h), Image.Resampling.LANCZOS)
        x = col * cell_w
        y = row * (cell_h + label_h)
        sheet.paste(thumb, (x, y + label_h))
        draw.rectangle((x, y, x + cell_w, y + label_h), fill=(0, 0, 0))
        draw.text((x + 8, y + 4), f"{idx + 1:02d}", font=font, fill=(255, 255, 255))

    sheet.save(OUTPUT_PATH, quality=92)
    print(json.dumps({"ok": True, "output": str(OUTPUT_PATH)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
