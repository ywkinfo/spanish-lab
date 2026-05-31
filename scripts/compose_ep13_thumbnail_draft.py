from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

ROOT = Path('/opt/data/repos/spanish-lab')
SRC = Path('/opt/data/cache/images/openai_codex_gpt-image-2-medium_20260518_070827_221c0e76.png')
SOURCE_OUT = ROOT / 'assets/generated/ep13-quiero-volver-source.png'
THUMB_REPO = ROOT / 'thumbs/a1-quiero-volver.jpg'
THUMB_OUT = ROOT / 'output/thumbs/frases-a1-ep13-quiero-volver.jpg'
QA_OUT = ROOT / 'output/qa/ep13-quiero-volver/thumbnail-draft.jpg'
FONT_BOLD = ROOT / 'assets/fonts/NotoSansKR-Bold.ttf'
FONT_REG = ROOT / 'assets/fonts/NotoSansKR-Regular.ttf'

for p in [SOURCE_OUT.parent, THUMB_REPO.parent, THUMB_OUT.parent, QA_OUT.parent]:
    p.mkdir(parents=True, exist_ok=True)

W, H = 1280, 720
src = Image.open(SRC).convert('RGB')
src.save(SOURCE_OUT)

# cover crop to 16:9, biased to the right so characters and train remain visible.
def cover_crop(img, size, focus_x=0.58, focus_y=0.50):
    sw, sh = img.size
    tw, th = size
    scale = max(tw / sw, th / sh)
    nw, nh = int(sw * scale + 0.5), int(sh * scale + 0.5)
    im = img.resize((nw, nh), Image.Resampling.LANCZOS)
    max_x, max_y = nw - tw, nh - th
    x = int(max(0, min(max_x, max_x * focus_x)))
    y = int(max(0, min(max_y, max_y * focus_y)))
    return im.crop((x, y, x + tw, y + th))

base = cover_crop(src, (W, H), 0.54, 0.50)
# blurred, darkened full-bleed background
bg = base.filter(ImageFilter.GaussianBlur(12))
bg = ImageEnhance.Brightness(bg).enhance(0.72)
bg = ImageEnhance.Color(bg).enhance(1.08)
canvas = bg.convert('RGBA')

# clear scene on the right, directly composited (not a separate white card)
scene = cover_crop(src, (850, H), 0.62, 0.50).convert('RGBA')
# soft left fade mask to blend into panel/background
mask = Image.new('L', (850, H), 255)
md = ImageDraw.Draw(mask)
for x in range(110):
    alpha = int(255 * (x / 110))
    md.line((x, 0, x, H), fill=alpha)
canvas.paste(scene, (430, 0), mask)

# left cream panel
panel = Image.new('RGBA', (510, 610), (0,0,0,0))
pd = ImageDraw.Draw(panel)
# shadow
shadow = Image.new('RGBA', (530, 630), (0,0,0,0))
sd = ImageDraw.Draw(shadow)
sd.rounded_rectangle((14, 14, 524, 624), radius=34, fill=(0,0,0,70))
shadow = shadow.filter(ImageFilter.GaussianBlur(10))
canvas.alpha_composite(shadow, (32, 50))
pd.rounded_rectangle((0, 0, 510, 610), radius=34, fill=(250, 239, 218, 242), outline=(255,255,255,150), width=2)
canvas.alpha_composite(panel, (45, 60))

d = ImageDraw.Draw(canvas)

def font(size, bold=True):
    return ImageFont.truetype(str(FONT_BOLD if bold else FONT_REG), size)

def rounded_text_box(draw, xy, text, fnt, fill, text_fill, pad_x=22, pad_y=10, radius=20, stroke=None):
    x, y = xy
    bbox = draw.textbbox((0,0), text, font=fnt, stroke_width=stroke[0] if stroke else 0)
    tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
    box = (x, y, x + tw + pad_x*2, y + th + pad_y*2)
    draw.rounded_rectangle(box, radius=radius, fill=fill)
    if stroke:
        draw.rounded_rectangle(box, radius=radius, outline=stroke[1], width=stroke[0])
    draw.text((x+pad_x, y+pad_y-bbox[1]), text, font=fnt, fill=text_fill)
    return box

# Badge
rounded_text_box(d, (82, 92), 'Español A1 · Ep.13', font(25), fill=(224,91,76,255), text_fill=(255,255,255,255), pad_x=20, pad_y=9, radius=18)

# Main title with white fill and thick dark stroke
main_font = font(86)
for text, y in [('Quiero', 182), ('volver', 282)]:
    d.text((85, y), text, font=main_font, fill=(255,255,255,255), stroke_width=6, stroke_fill=(35,37,42,255))

# Korean pill
rounded_text_box(d, (82, 423), '다시 가고 싶어', font(36), fill=(255,255,255,245), text_fill=(30,34,40,255), pad_x=24, pad_y=12, radius=24)

# Grammar pill
rounded_text_box(d, (82, 520), 'Quiero + 동사원형', font(30), fill=(38,150,142,255), text_fill=(255,255,255,255), pad_x=22, pad_y=11, radius=22)

# Small brand label
brand = 'Spanish Lab'
bf = font(22)
bb = d.textbbox((0,0), brand, font=bf)
d.rounded_rectangle((1082, 657, 1245, 695), radius=16, fill=(25,31,38,170))
d.text((1102, 664-bb[1]), brand, font=bf, fill=(255,255,255,235))

# subtle vignette
vig = Image.new('RGBA', (W,H), (0,0,0,0))
vd = ImageDraw.Draw(vig)
vd.rectangle((0,0,W,H), outline=(0,0,0,50), width=8)
canvas.alpha_composite(vig)

out = canvas.convert('RGB')
for path in [THUMB_REPO, THUMB_OUT, QA_OUT]:
    out.save(path, quality=94, subsampling=1)
print('source', SOURCE_OUT)
print('thumb_repo', THUMB_REPO)
print('thumb_out', THUMB_OUT)
print('qa', QA_OUT)
