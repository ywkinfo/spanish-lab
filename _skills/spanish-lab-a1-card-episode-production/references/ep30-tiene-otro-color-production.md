# Ep.30 `¿Tiene otro color?` production reference

Use this as a compact precedent for shopping-option A1+ episodes that continue from `Me lo llevo`.

## Topic and structure
- Episode: Ep.30
- Module: `projects/tiene_otro_color_a1.py`
- Slug/output: `tiene-otro-color`
- Level: `A1+`
- One learning point: `¿Tiene otro color?` as a chunk for asking whether another color/option is available in a shop.
- Useful safe variant: `¿Tiene otra talla?` may appear as a word-swap practice item, but keep the main learning point singular.
- Story context: Jin in a souvenir/clothing shop; Lucía as shop assistant; Diego as guide.
- Runtime target used: about 4.4 minutes (`264.6s`) with 29 dialogue lines + 4 block headers + intro/outro.

## Thumbnail-first path
- Generate 16:9 source art with right-side shop interaction and clean left negative space.
- Compose Ep.7-style thumbnail with:
  - `Español A1+ · Ep.30`
  - `¿Tiene otro color?`
  - `다른 색 있어요?`
  - `쇼핑할 때 바로 쓰는 표현`
- Store both repo and publish-output thumbnails when manually composing:
  - `thumbs/ep30-tiene-otro-color.jpg`
  - `output/thumbs/frases-a1-ep30-tiene-otro-color.jpg`

## QA pitfall found in this session
A first render passed automated checks but contact-sheet QA exposed Korean text in Spanish-facing display fields:
- `text_es="Naturalmente: 다른 색 있어요?"`
- `text_es="Significa: 다른 색 있어요?"`

Fix by keeping Spanish-facing fields Spanish-only and putting the Korean explanation in `text_ko`:
- `text_es="Naturalmente: ¿hay otro color?"`
- `text_ko="자연스럽게는 “다른 색 있어요?”예요."`
- `text_es="Significa: ¿hay otro color disponible?"`
- `text_ko="“다른 색 있어요?”라는 뜻이에요."`

After patching a post-render copy issue, bump `RENDER_VERSION` (v1 → v2 here), rerun TTS/check/publish/verify, and regenerate the contact sheet.

## Fast verification command
Before final render, run a small Hangul scan over Spanish-facing segment fields, in addition to the normal validation chain:

```sh
PROJECT=tiene_otro_color_a1 .venv/bin/python - <<'PY'
import importlib, re
p=importlib.import_module('projects.tiene_otro_color_a1')
hangul=re.compile('[가-힣]')
bad=[]
for i,s in enumerate(p.SEGMENTS,1):
    for key in ('text_es','title_es'):
        if key in s and hangul.search(str(s[key])):
            bad.append((i,key,s[key]))
print({'segments': len(p.SEGMENTS), 'dialogue': sum(1 for s in p.SEGMENTS if s.get('type')=='dialogue'), 'blocks': sum(1 for s in p.SEGMENTS if s.get('type')=='block_header'), 'render_version': p.RENDER_VERSION, 'hangul_in_spanish_fields': bad})
PY
```

Expected: `hangul_in_spanish_fields: []`.

## Verification chain used
```sh
python3 -m py_compile projects/tiene_otro_color_a1.py
PROJECT=tiene_otro_color_a1 PYTHON=.venv/bin/python make check
PROJECT=tiene_otro_color_a1 PYTHON=.venv/bin/python make test
PROJECT=tiene_otro_color_a1 PYTHON=.venv/bin/python make lint-spanish
PROJECT=tiene_otro_color_a1 PYTHON=.venv/bin/python make tts
PROJECT=tiene_otro_color_a1 PYTHON=.venv/bin/python make check
PROJECT=tiene_otro_color_a1 PYTHON=.venv/bin/python make publish-cards
PROJECT=tiene_otro_color_a1 PYTHON=.venv/bin/python make verify
```

## QA frame pattern
For ~4.4 minute full A1 story-card episodes at 30fps, a late frame near `eq(n,7560)` lands in the outro:

```sh
mkdir -p output/qa/tiene-otro-color
ffmpeg -y -loglevel error \
  -i output/publish/frases-a1-ep30-tiene-otro-color-16x9-v2.mp4 \
  -vf "select='eq(n,0)+eq(n,360)+eq(n,900)+eq(n,1440)+eq(n,2160)+eq(n,2880)+eq(n,3960)+eq(n,5040)+eq(n,7560)',scale=320:180,tile=3x3" \
  -frames:v 1 output/qa/tiene-otro-color/contact-sheet-v2.jpg
ffmpeg -y -loglevel error \
  -i output/publish/frases-a1-ep30-tiene-otro-color-16x9-v2.mp4 \
  -frames:v 1 output/qa/tiene-otro-color/intro-frame-v2.png
```

Check: title/subtitle/body spacing, Hangul rendering, no Korean in Spanish display fields, portraits, `Conversación A1+` label, and outro readability.
