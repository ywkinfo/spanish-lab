#!/usr/bin/env python3
"""Compose Ep.10 thumbnail in the Ep.7/Ep.8/Ep.9 Spanish Lab style."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "assets/generated/metro-ticket-thumbnail-source.png"
OUT = ROOT / "thumbs/a1-un-billete-por-favor.jpg"
PUBLISH_OUT = ROOT / "output/thumbs/frases-a1-ep10-un-billete-por-favor.jpg"
QA_OUT = ROOT / "output/qa/un-billete-por-favor-v0/thumbnail.jpg"
FONT_BOLD = ROOT / "assets/fonts/NotoSansKR-Bold.ttf"
FONT_REG = ROOT / "assets/fonts/NotoSansKR-Regular.ttf"

W, H = 1280, 720
CORAL = (224, 91, 76)
TEAL = (44, 150, 142)
CREAM = (250, 246, 236)
INK = (20, 24, 30)


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size=size)


def cover(im: Image.Image, size: tuple[int, int], *, x_focus: float = 0.5, y_focus: float = 0.5) -> Image.Image:
    tw, th = size
    sw, sh = im.size
    scale = max(tw / sw, th / sh)
    nw, nh = int(sw * scale + 0.5), int(sh * scale + 0.5)
    im = im.resize((nw, nh), Image.Resampling.LANCZOS)
    max_x = max(0, nw - tw)
    max_y = max(0, nh - th)
    left = int(max_x * x_focus)
    top = int(max_y * y_focus)
    return im.crop((left, top, left + tw, top + th))


def rounded_panel_with_shadow(base: Image.Image, box: tuple[int, int, int, int], radius: int = 28) -> None:
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    x1, y1, x2, y2 = box
    od.rounded_rectangle((x1 + 10, y1 + 14, x2 + 10, y2 + 14), radius=radius, fill=(0, 0, 0, 72))
    overlay = overlay.filter(ImageFilter.GaussianBlur(10))
    base.alpha_composite(overlay)
    d = ImageDraw.Draw(base)
    d.rounded_rectangle(box, radius=radius, fill=CREAM + (248,))


def draw_pill(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    fill: tuple[int, int, int],
    text: str,
    fnt: ImageFont.FreeTypeFont,
    text_fill=(255, 255, 255),
    stroke: int = 0,
) -> None:
    draw.rounded_rectangle(xy, radius=(xy[3] - xy[1]) // 2, fill=fill)
    bbox = draw.textbbox((0, 0), text, font=fnt, stroke_width=stroke)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = (xy[0] + xy[2] - tw) // 2 - bbox[0]
    y = (xy[1] + xy[3] - th) // 2 - bbox[1] - 1
    draw.text((x, y), text, font=fnt, fill=text_fill, stroke_width=stroke, stroke_fill=(0, 0, 0))


def main() -> None:
    src = Image.open(SRC).convert("RGB")

    # Warm blurred full-bleed background.
    bg = cover(src, (W, H), x_focus=0.52, y_focus=0.42).filter(ImageFilter.GaussianBlur(14))
    bg = bg.point(lambda p: int(p * 0.78))
    canvas = bg.convert("RGBA")

    # Sharp main scene. Keep trio/ticket machine on the right, while preserving left text area.
    sharp = cover(src, (W, H), x_focus=0.52, y_focus=0.42).convert("RGBA")
    canvas.alpha_composite(sharp, (0, 0))

    # Slight darkening behind the cream title panel.
    shade = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shade)
    sd.rectangle((0, 0, 610, H), fill=(0, 0, 0, 36))
    shade = shade.filter(ImageFilter.GaussianBlur(24))
    canvas.alpha_composite(shade)

    panel = (42, 56, 604, 642)
    rounded_panel_with_shadow(canvas, panel, 30)
    draw = ImageDraw.Draw(canvas)

    badge_f = font(FONT_BOLD, 34)
    title_f = font(FONT_BOLD, 63)
    ko_f = font(FONT_BOLD, 54)
    bottom_f = font(FONT_BOLD, 43)

    draw_pill(draw, (66, 62, 406, 120), CORAL, "Español A1 · Ep.10", badge_f)

    # Large outlined title, split for readability on mobile.
    y = 160
    for line in ["Un billete,", "por favor"]:
        draw.text((68, y), line, font=title_f, fill=(255, 255, 255), stroke_width=5, stroke_fill=(0, 0, 0))
        y += 86

    draw_pill(draw, (66, 374, 430, 462), (255, 255, 255), "지하철표 사기", ko_f, text_fill=INK)
    draw_pill(draw, (66, 512, 520, 592), TEAL, "¿Cuánto cuesta?", bottom_f)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    PUBLISH_OUT.parent.mkdir(parents=True, exist_ok=True)
    QA_OUT.parent.mkdir(parents=True, exist_ok=True)
    rgb = canvas.convert("RGB")
    for path in (OUT, PUBLISH_OUT, QA_OUT):
        rgb.save(path, "JPEG", quality=94, optimize=True)
        print(path)


if __name__ == "__main__":
    main()
