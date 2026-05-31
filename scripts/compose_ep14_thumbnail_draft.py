from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets/generated/ep14-voy-a-practicar-source.png"
OUT_REPO = ROOT / "thumbs/a1-voy-a-practicar.jpg"
OUT_PUBLISH = ROOT / "output/thumbs/frases-a1-ep14-voy-a-practicar.jpg"
OUT_QA = ROOT / "output/qa/ep14-voy-a-practicar/thumbnail-draft.jpg"
FONT_BOLD = ROOT / "assets/fonts/NotoSansKR-Bold.ttf"
FONT_REG = ROOT / "assets/fonts/NotoSansKR-Regular.ttf"

W, H = 1280, 720

def font(size: int, bold: bool = True):
    return ImageFont.truetype(str(FONT_BOLD if bold else FONT_REG), size=size)

def cover_crop(img: Image.Image, size=(W, H), focus=(0.62, 0.48)) -> Image.Image:
    iw, ih = img.size
    tw, th = size
    scale = max(tw / iw, th / ih)
    nw, nh = int(iw * scale + 0.5), int(ih * scale + 0.5)
    resized = img.resize((nw, nh), Image.Resampling.LANCZOS)
    fx, fy = focus
    left = int((nw - tw) * fx)
    top = int((nh - th) * fy)
    left = max(0, min(left, nw - tw))
    top = max(0, min(top, nh - th))
    return resized.crop((left, top, left + tw, top + th))

def rounded(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

def centered_pill(draw, center_x, y, text, fnt, fill, text_fill, pad_x=34, pad_y=12, radius=28):
    bbox = draw.textbbox((0, 0), text, font=fnt)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    box = (center_x - tw // 2 - pad_x, y, center_x + tw // 2 + pad_x, y + th + pad_y * 2)
    rounded(draw, box, radius, fill)
    draw.text((center_x - tw / 2, y + pad_y - bbox[1]), text, font=fnt, fill=text_fill)
    return box

def main():
    src = Image.open(SOURCE).convert("RGB")
    base = cover_crop(src, (W, H), focus=(0.66, 0.48))

    # Full-bleed background, blurred/darkened for visual unity.
    bg = base.filter(ImageFilter.GaussianBlur(12)).convert("RGBA")
    dark = Image.new("RGBA", (W, H), (38, 31, 28, 72))
    canvas = Image.alpha_composite(bg, dark)

    # Clear scene on the right, no separate white card frame.
    scene = cover_crop(src, (760, 720), focus=(0.74, 0.48)).convert("RGBA")
    mask = Image.new("L", (760, 720), 255)
    grad = Image.new("L", (760, 720), 255)
    gd = ImageDraw.Draw(grad)
    for x in range(150):
        alpha = int(255 * (x / 150))
        gd.line((x, 0, x, 720), fill=alpha)
    mask.paste(grad.crop((0, 0, 150, 720)), (0, 0))
    canvas.paste(scene, (520, 0), mask)

    draw = ImageDraw.Draw(canvas)

    # Left cream panel with soft shadow.
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle((54, 66, 580, 654), radius=38, fill=(0, 0, 0, 80))
    shadow = shadow.filter(ImageFilter.GaussianBlur(16))
    canvas = Image.alpha_composite(canvas, shadow)
    draw = ImageDraw.Draw(canvas)
    panel = (38, 48, 562, 636)
    rounded(draw, panel, 38, (252, 239, 210, 236))

    # Badge.
    badge_font = font(31)
    rounded(draw, (78, 82, 428, 134), 26, (226, 91, 78, 255))
    draw.text((101, 94), "Español A1 · Ep.14", font=badge_font, fill=(255, 255, 255, 255))

    # Main title, Ep.7-style white with dark stroke.
    title_font = font(98)
    title_lines = ["Voy a", "practicar"]
    y = 174
    for line in title_lines:
        draw.text((88, y), line, font=title_font, fill=(255, 255, 255, 255),
                  stroke_width=7, stroke_fill=(30, 34, 38, 255))
        y += 106

    # Korean pill.
    ko_font = font(39)
    centered_pill(draw, 300, 422, "연습할 거야", ko_font, (255, 255, 255, 250), (31, 35, 40, 255), pad_x=42, pad_y=13, radius=30)

    # Grammar callout.
    call_font = font(32)
    centered_pill(draw, 300, 522, "Voy a + 동사원형", call_font, (43, 151, 143, 255), (255, 255, 255, 255), pad_x=32, pad_y=13, radius=28)

    # Subtle edge vignette.
    vignette = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    vd = ImageDraw.Draw(vignette)
    vd.rectangle((0, 0, W, 28), fill=(0, 0, 0, 22))
    vd.rectangle((0, H - 28, W, H), fill=(0, 0, 0, 22))
    canvas = Image.alpha_composite(canvas, vignette)

    for out in [OUT_REPO, OUT_PUBLISH, OUT_QA]:
        out.parent.mkdir(parents=True, exist_ok=True)
        canvas.convert("RGB").save(out, quality=94, subsampling=1)
        print(out)

if __name__ == "__main__":
    main()
