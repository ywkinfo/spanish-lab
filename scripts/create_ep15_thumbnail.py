from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

ROOT = Path('/opt/data/repos/spanish-lab')
SRC = Path('/opt/data/cache/images/openai_codex_gpt-image-2-medium_20260518_214346_6fa4e2ef.png')
SOURCE_OUT = ROOT / 'images' / 'ep15-primavera-madrid-source.png'
THUMB_REPO = ROOT / 'thumbs' / 'a1-ep15-primavera-madrid.jpg'
THUMB_OUT = ROOT / 'output' / 'thumbs' / 'frases-a1-ep15-primavera-madrid.jpg'
QA_OUT = ROOT / 'output' / 'qa' / 'ep15-primavera-madrid' / 'thumbnail.jpg'

W, H = 1280, 720
FONT_BOLD = ROOT / 'assets' / 'fonts' / 'NotoSansKR-Bold.ttf'
FONT_REG = ROOT / 'assets' / 'fonts' / 'NotoSansKR-Regular.ttf'

def font(size, bold=True):
    return ImageFont.truetype(str(FONT_BOLD if bold else FONT_REG), size)

def cover_crop(im, size, focus=(0.62, 0.50)):
    tw, th = size
    sw, sh = im.size
    scale = max(tw / sw, th / sh)
    nw, nh = int(sw * scale), int(sh * scale)
    resized = im.resize((nw, nh), Image.Resampling.LANCZOS)
    max_x, max_y = max(0, nw - tw), max(0, nh - th)
    x = int(max_x * focus[0])
    y = int(max_y * focus[1])
    return resized.crop((x, y, x + tw, y + th))

def contain_width(im, target_h):
    scale = target_h / im.height
    return im.resize((int(im.width * scale), target_h), Image.Resampling.LANCZOS)

def text_size(draw, text, f, stroke=0):
    box = draw.textbbox((0, 0), text, font=f, stroke_width=stroke)
    return box[2]-box[0], box[3]-box[1]

def center_text(draw, box, text, f, fill, stroke_fill=None, stroke_width=0):
    x1, y1, x2, y2 = box
    tw, th = text_size(draw, text, f, stroke_width)
    draw.text((x1 + (x2-x1-tw)/2, y1 + (y2-y1-th)/2 - 2), text, font=f, fill=fill,
              stroke_width=stroke_width, stroke_fill=stroke_fill)

# Persist source
SOURCE_OUT.parent.mkdir(parents=True, exist_ok=True)
Image.open(SRC).convert('RGB').save(SOURCE_OUT)
source = Image.open(SOURCE_OUT).convert('RGB')

# Full-bleed blurred/darkened background
base = cover_crop(source, (W, H), focus=(0.70, 0.50))
bg = base.filter(ImageFilter.GaussianBlur(12))
bg = ImageEnhance.Brightness(bg).enhance(0.70)
bg = ImageEnhance.Color(bg).enhance(1.08)
canvas = bg.convert('RGBA')

# Sharp spring scene on right; direct composite with soft fade, not a separate card frame
scene = cover_crop(source, (760, 720), focus=(0.80, 0.50)).convert('RGBA')
# subtle vignette so left panel pops
scene = ImageEnhance.Contrast(scene).enhance(1.03)
scene = ImageEnhance.Color(scene).enhance(1.06)
mask = Image.new('L', scene.size, 255)
md = ImageDraw.Draw(mask)
for i in range(120):
    md.line([(i, 0), (i, scene.height)], fill=int(255 * (i / 120)))
scene.putalpha(mask)
canvas.alpha_composite(scene, (520, 0))

# Dark translucent gradient on far left behind panel
ov = Image.new('RGBA', (W, H), (0,0,0,0))
od = ImageDraw.Draw(ov)
for x in range(0, 620):
    alpha = int(58 * (1 - x/620))
    od.line([(x,0),(x,H)], fill=(0,0,0,alpha))
canvas = Image.alpha_composite(canvas, ov)

d = ImageDraw.Draw(canvas)

# Cream rounded text panel
panel = (48, 88, 560, 635)
shadow = Image.new('RGBA', (W,H), (0,0,0,0))
sd = ImageDraw.Draw(shadow)
sd.rounded_rectangle((panel[0]+10, panel[1]+12, panel[2]+10, panel[3]+12), radius=38, fill=(0,0,0,95))
shadow = shadow.filter(ImageFilter.GaussianBlur(10))
canvas = Image.alpha_composite(canvas, shadow)
d = ImageDraw.Draw(canvas)
d.rounded_rectangle(panel, radius=38, fill=(255, 246, 225, 238), outline=(255,255,255,180), width=3)

# Badge
badge = (82, 122, 332, 174)
d.rounded_rectangle(badge, radius=25, fill=(235, 111, 87, 255))
center_text(d, badge, 'Español A1 · Ep.15', font(26), fill=(255,255,255,255))

# Main title: white + black stroke, Ep.7-like high contrast
main_f = font(62)
lines = ['¿Cómo es', 'la primavera?']
y = 223
for line in lines:
    d.text((92, y), line, font=main_f, fill=(255,255,255,255), stroke_width=5, stroke_fill=(18,18,18,255))
    y += 76

# Korean pill
pill_ko = (82, 415, 518, 482)
d.rounded_rectangle(pill_ko, radius=32, fill=(255,255,255,250), outline=(16,16,16,45), width=2)
center_text(d, pill_ko, '마드리드의 봄은 어때?', font(31), fill=(24,24,24,255))

# Teal phrase pill
pill_teal = (82, 525, 485, 586)
d.rounded_rectangle(pill_teal, radius=30, fill=(20, 150, 148, 255))
center_text(d, pill_teal, 'Madrid en primavera', font(30), fill=(255,255,255,255))

# Small floral accent dots
for x,y,r,c in [(516,135,8,(255,188,178,255)),(530,157,5,(255,210,210,255)),(500,585,7,(255,188,178,255))]:
    d.ellipse((x-r,y-r,x+r,y+r), fill=c)

final = canvas.convert('RGB')
for p in [THUMB_REPO, THUMB_OUT, QA_OUT]:
    p.parent.mkdir(parents=True, exist_ok=True)
    final.save(p, quality=94, subsampling=0)
print('source', SOURCE_OUT)
print('thumb_repo', THUMB_REPO)
print('thumb_output', THUMB_OUT)
print('qa', QA_OUT)
