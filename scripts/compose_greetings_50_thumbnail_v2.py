from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path('/opt/data/repos/spanish-lab')
SRC = Path('/opt/data/cache/images/openai_codex_gpt-image-2-medium_20260525_231138_bac891e4.png')
OUT_REPO = ROOT / 'thumbs' / 'a1-greetings-50-phrases-v2.jpg'
OUT_PERSIST = Path('/opt/data/youtube/metadata/a1-greetings-50-phrases-thumbnail-v2.jpg')
OUT_QA = ROOT / 'output' / 'thumbs' / 'a1-greetings-50-phrases-thumbnail-v2.jpg'
FONT_BOLD = ROOT / 'assets/fonts/NotoSansKR-Bold.ttf'
FONT_REG = ROOT / 'assets/fonts/NotoSansKR-Regular.ttf'

W, H = 1280, 720

def font(path, size):
    return ImageFont.truetype(str(path), size)

def rounded_rect(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

def text_center(draw, xy, text, fnt, fill, stroke_width=0, stroke_fill=None):
    x, y = xy
    bbox = draw.textbbox((0, 0), text, font=fnt, stroke_width=stroke_width)
    tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
    draw.text((x - tw/2, y - th/2), text, font=fnt, fill=fill, stroke_width=stroke_width, stroke_fill=stroke_fill)

src = Image.open(SRC).convert('RGB')
sw, sh = src.size
target_ratio = W / H
if sw / sh > target_ratio:
    new_w = int(sh * target_ratio)
    left = int((sw - new_w) * 0.55)
    crop = src.crop((left, 0, left + new_w, sh))
else:
    new_h = int(sw / target_ratio)
    top = max(0, min(sh - new_h, int((sh - new_h) * 0.32)))
    crop = src.crop((0, top, sw, top + new_h))
base = crop.resize((W, H), Image.LANCZOS)

# Photorealistic base, lightly blurred/darkened on the far left only.
canvas = base.convert('RGBA')
left_blur = base.filter(ImageFilter.GaussianBlur(7)).convert('RGBA')
mask = Image.new('L', (W, H), 0)
md = ImageDraw.Draw(mask)
md.rectangle((0, 0, 600, H), fill=225)
mask = mask.filter(ImageFilter.GaussianBlur(36))
canvas.paste(left_blur, (0, 0), mask)

# Warm contrast veil for readability.
d = ImageDraw.Draw(canvas, 'RGBA')
d.rectangle((0, 0, 585, H), fill=(45, 31, 20, 80))

# Left cream panel with soft shadow, matching Spanish Lab Ep.7-style direction.
shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.rounded_rectangle((53, 74, 590, 651), radius=40, fill=(0, 0, 0, 105))
shadow = shadow.filter(ImageFilter.GaussianBlur(16))
canvas = Image.alpha_composite(canvas, shadow)
d = ImageDraw.Draw(canvas, 'RGBA')
rounded_rect(d, (36, 56, 574, 634), 40, fill=(255, 246, 225, 235), outline=(255, 255, 255, 185), width=3)

badge_f = font(FONT_BOLD, 32)
main_f = font(FONT_BOLD, 82)
num_f = font(FONT_BOLD, 118)
pill_f = font(FONT_BOLD, 34)
call_f = font(FONT_BOLD, 42)
small_f = font(FONT_REG, 25)

# Badge
rounded_rect(d, (78, 92, 486, 148), 25, fill=(239, 112, 92, 255))
d.text((102, 103), 'Español A1 · 50 frases', font=badge_f, fill=(255, 255, 255, 255))

# Main title
for offset, alpha in [((3, 3), 70), ((1, 1), 80)]:
    d.text((82+offset[0], 195+offset[1]), '스페인어 인사', font=main_f, fill=(255, 255, 255, alpha))
    d.text((82+offset[0], 292+offset[1]), '50문장', font=num_f, fill=(255, 255, 255, alpha))
d.text((82, 195), '스페인어 인사', font=main_f, fill=(32, 27, 23, 255))
d.text((82, 292), '50문장', font=num_f, fill=(32, 27, 23, 255))

# Korean topic pill
rounded_rect(d, (78, 438, 526, 495), 25, fill=(255, 255, 255, 246), outline=(33, 28, 24, 70), width=2)
text_center(d, (302, 464), '처음 만남부터 헤어질 때까지', pill_f, fill=(31, 31, 31, 255))

# Spanish callout pill
rounded_rect(d, (78, 528, 506, 590), 29, fill=(20, 151, 150, 255))
text_center(d, (292, 558), 'Hola → Nos vemos', call_f, fill=(255, 255, 255, 255), stroke_width=1, stroke_fill=(0, 82, 82, 220))

d.text((86, 604), 'Spanish Lab · 스페인어 연구소', font=small_f, fill=(84, 72, 60, 225))

for p in [OUT_REPO, OUT_PERSIST, OUT_QA]:
    p.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert('RGB').save(p, quality=94, subsampling=0)
    print(p)
