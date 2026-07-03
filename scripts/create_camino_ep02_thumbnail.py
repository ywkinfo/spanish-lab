from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "images" / "camino_a2_ep02_la_ruta" / "scene_06_three_closer_over_map.png"
THUMB_REPO = ROOT / "thumbs" / "camino-a2-ep02-la-ruta-draft.jpg"

W, H = 1280, 720
FONT_BOLD = ROOT / "assets" / "fonts" / "NotoSansKR-Bold.ttf"
FONT_REG = ROOT / "assets" / "fonts" / "NotoSansKR-Regular.ttf"


def font(size, bold=True):
    p = FONT_BOLD if bold and FONT_BOLD.exists() else FONT_REG
    return ImageFont.truetype(str(p), size)


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


source = Image.open(SOURCE).convert("RGB")

# Full-bleed blurred background.
base = cover_crop(source, (W, H), focus=(0.58, 0.35))
bg = base.filter(ImageFilter.GaussianBlur(12))
bg = ImageEnhance.Brightness(bg).enhance(0.76)
bg = ImageEnhance.Color(bg).enhance(1.06)
canvas = bg.convert("RGBA")

# Sharp scene on the right, focused on the three faces and map.
scene = cover_crop(source, (860, 720), focus=(0.64, 0.24)).convert("RGBA")
scene = ImageEnhance.Contrast(scene).enhance(1.03)
scene = ImageEnhance.Color(scene).enhance(1.04)
mask = Image.new("L", scene.size, 255)
md = ImageDraw.Draw(mask)
for i in range(210):
    md.line([(i, 0), (i, scene.height)], fill=int(255 * (i / 210)))
scene.putalpha(mask)
canvas.alpha_composite(scene, (420, 0))

# Dark left gradient behind the cream panel.
ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
od = ImageDraw.Draw(ov)
for x in range(0, 680):
    alpha = int(48 * (1 - x / 680))
    od.line([(x, 0), (x, H)], fill=(0, 0, 0, alpha))
canvas = Image.alpha_composite(canvas, ov)

# Cream rounded text panel.
panel = (58, 72, 670, 650)
shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.rounded_rectangle(
    (panel[0] + 8, panel[1] + 10, panel[2] + 8, panel[3] + 10),
    radius=38,
    fill=(0, 0, 0, 80),
)
shadow = shadow.filter(ImageFilter.GaussianBlur(8))
canvas = Image.alpha_composite(canvas, shadow)
d = ImageDraw.Draw(canvas)
d.rounded_rectangle(
    panel,
    radius=38,
    fill=(255, 248, 231, 218),
    outline=(255, 255, 255, 180),
    width=3,
)

F_badge = font(28)
F_title = font(62)
F_ko = font(38, bold=False)
F_pill = font(34)
F_small = font(26)

# Badge.
badge_text = "Español A2+ · Camino Ep.2"
b = d.textbbox((0, 0), badge_text, font=F_badge)
badge = (90, 104, 90 + (b[2] - b[0]) + 56, 156)
d.rounded_rectangle(badge, radius=26, fill=(226, 91, 76, 245))
d.text((118, 116), badge_text, font=F_badge, fill="white")

# Main title: compact version of the key sentence.
x, y = 90, 198
for line in ["El más largo,", "pero bonito"]:
    d.text(
        (x, y),
        line,
        font=F_title,
        fill=(255, 255, 255),
        stroke_width=5,
        stroke_fill=(31, 35, 40),
    )
    y += 76

# Korean hook pill.
ko_text = "어느 길로?"
kb = d.textbbox((0, 0), ko_text, font=F_ko)
ko_box = (88, 380, 88 + (kb[2] - kb[0]) + 56, 445)
d.rounded_rectangle(ko_box, radius=28, fill=(255, 255, 255, 242))
d.text((116, 389), ko_text, font=F_ko, fill=(31, 35, 40))

# Teal learning-point pill.
grammar_text = "el más + 형용사"
gb = d.textbbox((0, 0), grammar_text, font=F_pill)
pill = (88, 485, 88 + (gb[2] - gb[0]) + 56, 548)
d.rounded_rectangle(pill, radius=30, fill=(42, 160, 150, 245))
d.text((118, 495), grammar_text, font=F_pill, fill="white")

# Grey series pill.
small_text = "Español en el Camino"
sb = d.textbbox((0, 0), small_text, font=F_small)
small = (90, 576, 90 + (sb[2] - sb[0]) + 44, 618)
d.rounded_rectangle(small, radius=20, fill=(31, 35, 40, 225))
d.text((112, 582), small_text, font=F_small, fill="white")

# Small accent dots.
for ax, ay, ar, ac in [
    (606, 126, 8, (255, 198, 88, 255)),
    (630, 150, 5, (255, 220, 135, 255)),
    (604, 592, 7, (105, 195, 215, 255)),
    (638, 590, 4, (70, 120, 190, 255)),
]:
    d.ellipse((ax - ar, ay - ar, ax + ar, ay + ar), fill=ac)

final = canvas.convert("RGB")
THUMB_REPO.parent.mkdir(parents=True, exist_ok=True)
final.save(THUMB_REPO, quality=94, subsampling=0)
print(f"Thumbnail generated successfully at {THUMB_REPO}")
