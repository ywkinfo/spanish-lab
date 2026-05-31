from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

ROOT = Path('/opt/data/repos/spanish-lab')
SRC = Path('/opt/data/cache/images/openai_codex_gpt-image-2-medium_20260522_111108_94bbc02c.png')
SOURCE_OUT = ROOT / 'images' / 'ep21-a-veces-me-levanto-temprano-source.png'
THUMB_REPO = ROOT / 'thumbs' / 'a1-ep21-a-veces-me-levanto-temprano.jpg'
THUMB_OUT = ROOT / 'output' / 'thumbs' / 'frases-a1-ep21-a-veces-me-levanto-temprano.jpg'
QA_OUT = ROOT / 'output' / 'qa' / 'a-veces-me-levanto-temprano' / 'thumbnail.jpg'

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


SOURCE_OUT.parent.mkdir(parents=True, exist_ok=True)
source_original = Image.open(SRC).convert('RGB')
# Generated image is 3:2-ish; crop to 16:9 while preserving Jin's head and desk.
source16 = cover_crop(source_original, (W, H), focus=(0.55, 0.48))
source16.save(SOURCE_OUT)
source = Image.open(SOURCE_OUT).convert('RGB')

# Ep.7-style full-bleed blurred/darkened background.
base = cover_crop(source, (W, H), focus=(0.55, 0.50))
bg = base.filter(ImageFilter.GaussianBlur(12))
bg = ImageEnhance.Brightness(bg).enhance(0.72)
bg = ImageEnhance.Color(bg).enhance(1.05)
canvas = bg.convert('RGBA')

# Sharp morning-study scene on the right, gently faded into the left text area.
scene = cover_crop(source, (820, 720), focus=(0.82, 0.50)).convert('RGBA')
scene = ImageEnhance.Contrast(scene).enhance(1.04)
scene = ImageEnhance.Color(scene).enhance(1.06)
mask = Image.new('L', scene.size, 255)
md = ImageDraw.Draw(mask)
for i in range(170):
    md.line([(i, 0), (i, scene.height)], fill=int(255 * (i / 170)))
scene.putalpha(mask)
canvas.alpha_composite(scene, (460, 0))

# Dark gradient behind the left panel for contrast.
ov = Image.new('RGBA', (W, H), (0, 0, 0, 0))
od = ImageDraw.Draw(ov)
for x in range(0, 620):
    alpha = int(48 * (1 - x / 620))
    od.line([(x, 0), (x, H)], fill=(0, 0, 0, alpha))
canvas = Image.alpha_composite(canvas, ov)
d = ImageDraw.Draw(canvas)

# Cream rounded text panel.
panel = (48, 84, 590, 640)
shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.rounded_rectangle((panel[0] + 10, panel[1] + 12, panel[2] + 10, panel[3] + 12), radius=38, fill=(0, 0, 0, 90))
shadow = shadow.filter(ImageFilter.GaussianBlur(10))
canvas = Image.alpha_composite(canvas, shadow)
d = ImageDraw.Draw(canvas)
d.rounded_rectangle(panel, radius=38, fill=(255, 246, 225, 238), outline=(255, 255, 255, 180), width=3)

# Badge.
badge = (82, 118, 350, 170)
d.rounded_rectangle(badge, radius=25, fill=(235, 111, 87, 255))
center_text(d, badge, 'Español A1+ · Ep.21', font(25), fill=(255, 255, 255, 255))

# Main title: keep one learning point visually dominant.
main_f = font(66)
lines = ['A veces']
y = 212
for line in lines:
    d.text((92, y), line, font=main_f, fill=(255, 255, 255, 255), stroke_width=5, stroke_fill=(18, 18, 18, 255))
    y += 78

sub_f = font(43)
d.text((94, 304), 'me levanto', font=sub_f, fill=(255, 255, 255, 255), stroke_width=4, stroke_fill=(18, 18, 18, 255))
d.text((94, 356), 'temprano', font=sub_f, fill=(255, 255, 255, 255), stroke_width=4, stroke_fill=(18, 18, 18, 255))

# Korean pill.
pill_ko = (82, 452, 488, 520)
d.rounded_rectangle(pill_ko, radius=34, fill=(255, 255, 255, 250), outline=(16, 16, 16, 45), width=2)
center_text(d, pill_ko, '가끔 일찍 일어나요', font(34), fill=(24, 24, 24, 255))

# Teal learning-point pill.
pill_teal = (82, 552, 360, 610)
d.rounded_rectangle(pill_teal, radius=29, fill=(20, 150, 148, 255))
center_text(d, pill_teal, '가끔 = A veces', font(28), fill=(255, 255, 255, 255))

# Footer note.
d.text((384, 567), 'A veces + 현재형', font=font(23), fill=(78, 68, 58, 235))

# Small morning accent dots.
for x, y, r, c in [
    (530, 132, 8, (255, 198, 88, 255)),
    (544, 154, 5, (255, 220, 135, 255)),
    (528, 595, 7, (105, 195, 215, 255)),
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
