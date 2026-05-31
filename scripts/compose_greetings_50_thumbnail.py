from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path('/opt/data/repos/spanish-lab')
SRC = Path('/opt/data/cache/images/openai_codex_gpt-image-2-medium_20260525_230322_b37c418c.png')
OUT_REPO = ROOT / 'thumbs' / 'a1-greetings-50-phrases.jpg'
OUT_PERSIST = Path('/opt/data/youtube/metadata/a1-greetings-50-phrases-thumbnail-draft.jpg')
OUT_QA = ROOT / 'output' / 'thumbs' / 'a1-greetings-50-phrases-thumbnail-draft.jpg'
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

# Cover-crop source to 16:9; generated image is 3:2-ish, so crop vertical center.
src = Image.open(SRC).convert('RGB')
sw, sh = src.size
target_ratio = W / H
if sw / sh > target_ratio:
    new_w = int(sh * target_ratio)
    left = (sw - new_w) // 2
    crop = src.crop((left, 0, left + new_w, sh))
else:
    new_h = int(sw / target_ratio)
    # Slightly high crop to protect heads and keep café/table visible.
    top = max(0, min(sh - new_h, int((sh - new_h) * 0.35)))
    crop = src.crop((0, top, sw, top + new_h))
base = crop.resize((W, H), Image.LANCZOS)

# Full-bleed blur/darken base for thumbnail contrast.
blur = base.filter(ImageFilter.GaussianBlur(6))
shade = Image.new('RGB', (W, H), (18, 13, 10))
canvas = Image.blend(blur, shade, 0.30)

# Bring the right-side scene back as crisp, blended with soft edge.
scene = base.copy()
mask = Image.new('L', (W, H), 0)
md = ImageDraw.Draw(mask)
md.rectangle((520, 0, W, H), fill=255)
# Feather left edge.
mask = mask.filter(ImageFilter.GaussianBlur(28))
canvas.paste(scene, (0, 0), mask)

# Warm translucent veil on far left for clean readability.
d = ImageDraw.Draw(canvas, 'RGBA')
d.rectangle((0, 0, 575, H), fill=(46, 31, 22, 95))

# Left cream panel with shadow.
shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.rounded_rectangle((54, 74, 582, 650), radius=38, fill=(0, 0, 0, 105))
shadow = shadow.filter(ImageFilter.GaussianBlur(16))
canvas = Image.alpha_composite(canvas.convert('RGBA'), shadow)
d = ImageDraw.Draw(canvas, 'RGBA')
rounded_rect(d, (38, 58, 566, 634), 38, fill=(255, 245, 222, 238), outline=(255, 255, 255, 190), width=3)

# Fonts
badge_f = font(FONT_BOLD, 32)
main_f = font(FONT_BOLD, 82)
num_f = font(FONT_BOLD, 118)
pill_f = font(FONT_BOLD, 34)
call_f = font(FONT_BOLD, 42)
small_f = font(FONT_REG, 25)

# Badge
rounded_rect(d, (78, 92, 486, 148), 25, fill=(239, 112, 92, 255))
d.text((102, 103), 'Español A1 · 50 frases', font=badge_f, fill=(255, 255, 255, 255))

# Main Korean title
# Use high-contrast charcoal, with subtle warm highlight.
d.text((82, 195), '스페인어 인사', font=main_f, fill=(33, 28, 24, 255))
d.text((82, 292), '50문장', font=num_f, fill=(33, 28, 24, 255))

# Korean topic pill
rounded_rect(d, (78, 438, 526, 495), 25, fill=(255, 255, 255, 245), outline=(33, 28, 24, 70), width=2)
text_center(d, (302, 464), '처음 만남부터 헤어질 때까지', pill_f, fill=(31, 31, 31, 255))

# Spanish callout pill
rounded_rect(d, (78, 528, 506, 590), 29, fill=(20, 151, 150, 255))
text_center(d, (292, 558), 'Hola → Nos vemos', call_f, fill=(255, 255, 255, 255), stroke_width=1, stroke_fill=(0, 82, 82, 220))

# Small brand mark / non-promotional cue
# Keep unobtrusive.
d.text((86, 604), 'Spanish Lab · 스페인어 연구소', font=small_f, fill=(84, 72, 60, 225))

# Subtle speech bubbles on right (simple graphic overlay, no fake text)
d.ellipse((970, 68, 1208, 151), fill=(255, 255, 255, 218), outline=(255, 255, 255, 255), width=3)
d.polygon([(1035, 145), (1065, 145), (1046, 174)], fill=(255, 255, 255, 218))
text_center(d, (1089, 108), '¡Hola!', font(FONT_BOLD, 50), fill=(28, 28, 28, 255))

d.ellipse((808, 566, 1085, 646), fill=(255, 255, 255, 220), outline=(255, 255, 255, 255), width=3)
d.polygon([(902, 566), (932, 566), (918, 536)], fill=(255, 255, 255, 220))
text_center(d, (946, 604), '¿Qué tal?', font(FONT_BOLD, 42), fill=(28, 28, 28, 255))

# Export
for p in [OUT_REPO, OUT_PERSIST, OUT_QA]:
    p.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert('RGB').save(p, quality=94, subsampling=0)
    print(p)
