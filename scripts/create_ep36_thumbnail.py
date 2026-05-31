from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

ROOT = Path('/Users/peter/spanish-lab')
SOURCE_OUT = ROOT / 'images' / 'ep36-en-el-medico-sintomas-source.png'
THUMB_REPO = ROOT / 'thumbs' / 'a2-ep36-en-el-medico-sintomas.jpg'
THUMB_OUT = ROOT / 'output' / 'thumbs' / 'frases-a2-ep36-en-el-medico-sintomas.jpg'
QA_OUT = ROOT / 'output' / 'qa' / 'en-el-medico-sintomas' / 'thumbnail.jpg'

W, H = 1280, 720
FONT_BOLD = ROOT / 'assets' / 'fonts' / 'NotoSansKR-Bold.ttf'
FONT_REG = ROOT / 'assets' / 'fonts' / 'NotoSansKR-Regular.ttf'


def font(size, bold=True):
    return ImageFont.truetype(str(FONT_BOLD if bold else FONT_REG), size)


def cover_crop(im, size, focus=(0.50, 0.50)):
    tw, th = size
    sw, sh = im.size
    scale = max(tw / sw, th / sh)
    nw, nh = int(sw * scale), int(sh * scale)
    resized = im.resize((nw, nh), Image.Resampling.LANCZOS)
    max_x, max_y = max(0, nw - tw), max(0, nh - th)
    x = int(max_x * focus[0])
    y = int(max_y * focus[1])
    return resized.crop((x, y, x + tw, y + th))


def text_size(draw, text, f, stroke=0):
    box = draw.textbbox((0, 0), text, font=f, stroke_width=stroke)
    return box[2] - box[0], box[3] - box[1]


def center_text(draw, box, text, f, fill, stroke_fill=None, stroke_width=0):
    x1, y1, x2, y2 = box
    tw, th = text_size(draw, text, f, stroke_width)
    draw.text(
        (x1 + (x2 - x1 - tw) / 2, y1 + (y2 - y1 - th) / 2 - 2),
        text,
        font=f,
        fill=fill,
        stroke_width=stroke_width,
        stroke_fill=stroke_fill,
    )


# Read the canonical source image that we already saved.
source = Image.open(SOURCE_OUT).convert('RGB')

# Ep.7-style full-bleed blurred/darkened background.
base = cover_crop(source, (W, H), focus=(0.50, 0.50))
bg = base.filter(ImageFilter.GaussianBlur(12))
bg = ImageEnhance.Brightness(bg).enhance(0.70)
bg = ImageEnhance.Color(bg).enhance(1.08)
canvas = bg.convert('RGBA')

# Sharp scene on the right, gently faded into the text panel.
scene = cover_crop(source, (860, 720), focus=(0.50, 0.50)).convert('RGBA')
scene = ImageEnhance.Contrast(scene).enhance(1.05)
scene = ImageEnhance.Color(scene).enhance(1.04)
mask = Image.new('L', scene.size, 255)
md = ImageDraw.Draw(mask)
for i in range(190):
    md.line([(i, 0), (i, scene.height)], fill=int(255 * (i / 190)))
scene.putalpha(mask)
canvas.alpha_composite(scene, (420, 0))

# Dark left gradient behind the cream panel.
ov = Image.new('RGBA', (W, H), (0, 0, 0, 0))
od = ImageDraw.Draw(ov)
for x in range(0, 650):
    alpha = int(50 * (1 - x / 650))
    od.line([(x, 0), (x, H)], fill=(0, 0, 0, alpha))
canvas = Image.alpha_composite(canvas, ov)
d = ImageDraw.Draw(canvas)

# Cream rounded text panel.
panel = (48, 82, 610, 642)
shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.rounded_rectangle((panel[0] + 10, panel[1] + 12, panel[2] + 10, panel[3] + 12), radius=38, fill=(0, 0, 0, 88))
shadow = shadow.filter(ImageFilter.GaussianBlur(10))
canvas = Image.alpha_composite(canvas, shadow)
d = ImageDraw.Draw(canvas)
d.rounded_rectangle(panel, radius=38, fill=(255, 246, 225, 239), outline=(255, 255, 255, 180), width=3)

# Badge.
badge = (82, 116, 358, 168)
d.rounded_rectangle(badge, radius=25, fill=(235, 111, 87, 255))
center_text(d, badge, 'Español A2 · Ep.36', font(25), fill=(255, 255, 255, 255))

# Main title: Me duele la cabeza.
d.text((88, 208), 'Me duele', font=font(74), fill=(255, 255, 255, 255), stroke_width=6, stroke_fill=(18, 18, 18, 255))
d.text((90, 310), 'la cabeza', font=font(74), fill=(255, 255, 255, 255), stroke_width=6, stroke_fill=(18, 18, 18, 255))

# Korean meaning pill: 머리가 아파요.
pill_ko = (82, 448, 548, 518)
d.rounded_rectangle(pill_ko, radius=35, fill=(255, 255, 255, 250), outline=(16, 16, 16, 45), width=2)
center_text(d, pill_ko, '머리가 아파요', font(35), fill=(24, 24, 24, 255))

# Teal learning-point pill: 증상 설명.
pill_teal = (82, 548, 492, 608)
d.rounded_rectangle(pill_teal, radius=30, fill=(20, 150, 148, 255))
center_text(d, pill_teal, '증상 설명', font(28), fill=(255, 255, 255, 255))

# Small souvenir accents.
for x, y, r, c in [
    (536, 136, 8, (255, 198, 88, 255)),
    (560, 160, 5, (255, 220, 135, 255)),
    (534, 602, 7, (105, 195, 215, 255)),
    (568, 600, 4, (70, 120, 190, 255)),
]:
    d.ellipse((x - r, y - r, x + r, y + r), fill=c)

final = canvas.convert('RGB')
for p in [THUMB_REPO, THUMB_OUT, QA_OUT]:
    p.parent.mkdir(parents=True, exist_ok=True)
    final.save(p, quality=94, subsampling=0)
print('source', SOURCE_OUT)
print('thumb_repo', THUMB_REPO)
print('thumb_output', THUMB_OUT)
print('qa', QA_OUT)
