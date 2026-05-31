#!/usr/bin/env python3
"""Compose Ep.8 thumbnail in the same visual style as Ep.7."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "assets/generated/lucia-cafe-bill-thumbnail-source.png"
OUT = ROOT / "thumbs/a1-la-cuenta.jpg"
PUBLISH_OUT = ROOT / "output/thumbs/frases-a1-ep08-la-cuenta.jpg"
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
    od.rounded_rectangle((x1 + 10, y1 + 14, x2 + 10, y2 + 14), radius=radius, fill=(0, 0, 0, 62))
    overlay = overlay.filter(ImageFilter.GaussianBlur(10))
    base.alpha_composite(overlay)
    d = ImageDraw.Draw(base)
    d.rounded_rectangle(box, radius=radius, fill=CREAM + (248,))


def draw_pill(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], fill: tuple[int, int, int], text: str, fnt, text_fill=(255, 255, 255), stroke=0) -> None:
    draw.rounded_rectangle(xy, radius=(xy[3] - xy[1]) // 2, fill=fill)
    bbox = draw.textbbox((0, 0), text, font=fnt, stroke_width=stroke)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = (xy[0] + xy[2] - tw) // 2 - bbox[0]
    y = (xy[1] + xy[3] - th) // 2 - bbox[1] - 1
    draw.text((x, y), text, font=fnt, fill=text_fill, stroke_width=stroke, stroke_fill=(0, 0, 0))


def main() -> None:
    src = Image.open(SRC).convert("RGB")

    # Full-bleed warm blurred image background, like Ep.7.
    bg = cover(src, (W, H), x_focus=0.58, y_focus=0.52).filter(ImageFilter.GaussianBlur(12))
    bg = bg.point(lambda p: int(p * 0.78))
    canvas = bg.convert("RGBA")

    # Right-side clean 1:1 visual anchor, no frame/card, matching Ep.7's large image area.
    right = cover(src, (720, 720), x_focus=0.78, y_focus=0.50).convert("RGBA")
    canvas.alpha_composite(right, (560, 0))

    # Soft dark fade at far left/right edge for depth behind panel.
    shade = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shade)
    sd.rectangle((0, 0, 575, H), fill=(0, 0, 0, 42))
    shade = shade.filter(ImageFilter.GaussianBlur(24))
    canvas.alpha_composite(shade)

    # Ep.7-style left cream panel.
    panel = (42, 56, 592, 614)
    rounded_panel_with_shadow(canvas, panel, 28)
    draw = ImageDraw.Draw(canvas)

    badge_f = font(FONT_BOLD, 34)
    title_f = font(FONT_BOLD, 70)
    ko_f = font(FONT_BOLD, 58)
    bottom_f = font(FONT_BOLD, 52)

    # Top coral badge.
    draw_pill(draw, (66, 62, 406, 120), CORAL, "Español A1 · Ep.8", badge_f)

    # Main outlined Spanish title, Ep.7-like large white text with black stroke.
    y = 184
    for line in ["La cuenta,", "por favor"]:
        draw.text((68, y), line, font=title_f, fill=(255, 255, 255), stroke_width=5, stroke_fill=(0, 0, 0))
        y += 82

    # Korean white pill.
    draw_pill(draw, (66, 380, 505, 470), (255, 255, 255), "카페에서 계산하기", ko_f, text_fill=INK)

    # Bottom teal focus phrase.
    draw_pill(draw, (66, 500, 515, 582), TEAL, "¿Cuánto es?", bottom_f)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    PUBLISH_OUT.parent.mkdir(parents=True, exist_ok=True)
    rgb = canvas.convert("RGB")
    rgb.save(OUT, "JPEG", quality=94, optimize=True)
    rgb.save(PUBLISH_OUT, "JPEG", quality=94, optimize=True)
    print(OUT)
    print(PUBLISH_OUT)


if __name__ == "__main__":
    main()
