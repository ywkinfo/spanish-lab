#!/usr/bin/env python3
"""Compose Ep.9 thumbnail in the Ep.7/Ep.8 Spanish Lab style."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "assets/generated/madrid-street-directions-thumbnail-source.png"
OUT = ROOT / "thumbs/a1-donde-esta-el-metro.jpg"
PUBLISH_OUT = ROOT / "output/thumbs/frases-a1-ep09-donde-esta-el-metro.jpg"
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
    od.rounded_rectangle((x1 + 10, y1 + 14, x2 + 10, y2 + 14), radius=radius, fill=(0, 0, 0, 70))
    overlay = overlay.filter(ImageFilter.GaussianBlur(10))
    base.alpha_composite(overlay)
    d = ImageDraw.Draw(base)
    d.rounded_rectangle(box, radius=radius, fill=CREAM + (248,))


def text_size(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, stroke: int = 0) -> tuple[int, int]:
    bbox = draw.textbbox((0, 0), text, font=fnt, stroke_width=stroke)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


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
    bg = cover(src, (W, H), x_focus=0.50, y_focus=0.48).filter(ImageFilter.GaussianBlur(14))
    bg = bg.point(lambda p: int(p * 0.78))
    canvas = bg.convert("RGBA")

    # Sharp main scene. The generated art already leaves clean left-side space and keeps the trio on the right.
    sharp = cover(src, (W, H), x_focus=0.50, y_focus=0.48).convert("RGBA")
    canvas.alpha_composite(sharp, (0, 0))

    # Darken just enough behind the cream title panel.
    shade = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shade)
    sd.rectangle((0, 0, 610, H), fill=(0, 0, 0, 34))
    shade = shade.filter(ImageFilter.GaussianBlur(24))
    canvas.alpha_composite(shade)

    panel = (42, 56, 604, 624)
    rounded_panel_with_shadow(canvas, panel, 30)
    draw = ImageDraw.Draw(canvas)

    badge_f = font(FONT_BOLD, 34)
    title_f = font(FONT_BOLD, 64)
    ko_f = font(FONT_BOLD, 62)
    bottom_f = font(FONT_BOLD, 41)

    draw_pill(draw, (66, 62, 406, 120), CORAL, "Español A1 · Ep.9", badge_f)

    # Large outlined title, split for readability on mobile.
    y = 168
    for line in ["¿Dónde está", "el metro?"]:
        draw.text((68, y), line, font=title_f, fill=(255, 255, 255), stroke_width=5, stroke_fill=(0, 0, 0))
        y += 82

    draw_pill(draw, (66, 374, 346, 468), (255, 255, 255), "길 묻기", ko_f, text_fill=INK)
    draw_pill(draw, (66, 510, 546, 588), TEAL, "Todo recto · Derecha", bottom_f)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    PUBLISH_OUT.parent.mkdir(parents=True, exist_ok=True)
    rgb = canvas.convert("RGB")
    rgb.save(OUT, "JPEG", quality=94, optimize=True)
    rgb.save(PUBLISH_OUT, "JPEG", quality=94, optimize=True)
    print(OUT)
    print(PUBLISH_OUT)


if __name__ == "__main__":
    main()
