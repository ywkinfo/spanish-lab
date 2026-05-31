# Ep.15 `Primavera en Madrid` Production Reference

Session-specific reference for Español A1 · Ep.15, a full story-card episode built from a thumbnail-first spring image concept.

## Content shape
- Episode: Ep.15
- Public slug: `a1-primavera-madrid`
- Project module: `projects/primavera_madrid_a1.py`
- Source script: `a1-primavera-madrid/descrip.md`
- CEFR: A1
- One learning point: `¿Cómo es + noun/place?` to ask about characteristics.
- Story function: Jin asks Lucía and Diego about the beautiful spring in Madrid.
- Useful A1 examples:
  - `¿Cómo es la primavera en Madrid?`
  - `Es agradable.`
  - `Es muy bonita.`
  - `La primavera en Madrid es agradable.`

## Thumbnail-first image workflow Peter liked
Peter explicitly approved the image-generation workflow used here and asked to keep using it for future Spanish Lab images:
1. Generate a direct 16:9 landscape thumbnail/background draft with a clear prompt.
2. Compose the scene with characters/visual focus on the right.
3. Leave clean empty space on the left for title overlay.
4. Avoid fake readable text, logos, clutter, cropped heads, and distorted hands.
5. Then add the Ep.7-style overlay: cream left panel, coral episode badge, large high-contrast Spanish title, Korean pill, teal callout pill.

## Thumbnail composition notes
- Generated source image path: `images/ep15-primavera-madrid-source.png`.
- Repo thumbnail path: `thumbs/a1-ep15-primavera-madrid.jpg`.
- Output thumbnail path: `output/thumbs/frases-a1-ep15-primavera-madrid.jpg`.
- Used a reusable Pillow composition script: `scripts/create_ep15_thumbnail.py`.
- Final overlay text:
  - badge: `Español A1 · Ep.15`
  - main: `¿Cómo es la primavera?`
  - Korean: `마드리드의 봄은 어때?`
  - teal callout: `Madrid en primavera`

## Production commands used
From `/opt/data/repos/spanish-lab`:
```sh
PYTHON=.venv/bin/python .venv/bin/python -m py_compile projects/primavera_madrid_a1.py
PROJECT=primavera_madrid_a1 PYTHON=.venv/bin/python make check
PROJECT=primavera_madrid_a1 PYTHON=.venv/bin/python make test
PROJECT=primavera_madrid_a1 PYTHON=.venv/bin/python make lint-spanish
PROJECT=primavera_madrid_a1 PYTHON=.venv/bin/python make tts
PROJECT=primavera_madrid_a1 PYTHON=.venv/bin/python make check
PROJECT=primavera_madrid_a1 PYTHON=.venv/bin/python make publish-cards
PROJECT=primavera_madrid_a1 PYTHON=.venv/bin/python make verify
PROJECT=primavera_madrid_a1 PYTHON=.venv/bin/python .venv/bin/python checks/probe_output.py output/publish/frases-a1-ep15-primavera-madrid-16x9-v2.mp4
```

## Published artifact paths
- Final video: `output/publish/frases-a1-ep15-primavera-madrid-16x9-v2.mp4`
- Thumbnail: `output/thumbs/frases-a1-ep15-primavera-madrid.jpg`
- Metadata JSON: `output/meta/frases-a1-ep15-primavera-madrid-16x9-v2.json`
- Description/chapters/script: `output/meta/frases-a1-ep15-primavera-madrid-16x9-v2.md`
- QA contact sheet: `output/qa/primavera-madrid/final-contact-sheet-v2.jpg`

## QA and fixes learned
1. The first contact-sheet QA caught an intro readability issue: the long intro title `¿Cómo es la primavera?` plus intro narration text felt cramped/overlapping at contact-sheet scale.
2. Fix by changing the intro slide title to a shorter visual title (`Primavera en Madrid`) while keeping the learning point and YouTube title as `¿Cómo es la primavera en Madrid?`.
3. Also corrected outro gender agreement from `es bonito` to `es bonita` when referring to `la primavera`.
4. After copy/layout fixes, bump `RENDER_VERSION`, regenerate TTS, rerender/publish, verify, and regenerate the contact sheet. Do not hand off the older render.

## Contact sheet frame picks
For the 299s / 30fps final video, this covered intro, body blocks, mini quiz, and outro:
```sh
mkdir -p output/qa/primavera-madrid
ffmpeg -y -loglevel error \
  -i output/publish/frases-a1-ep15-primavera-madrid-16x9-v2.mp4 \
  -vf "select='eq(n,0)+eq(n,510)+eq(n,1050)+eq(n,1860)+eq(n,3000)+eq(n,4200)+eq(n,5550)+eq(n,6900)+eq(n,8500)',scale=320:180,tile=3x3" \
  -frames:v 1 output/qa/primavera-madrid/final-contact-sheet-v2.jpg
```

QA checklist for this contact sheet:
- Spanish/Korean text readable.
- Hangul renders correctly, no tofu boxes.
- Character portraits and speaker labels align.
- No major clipping/overlap.
- Intro title reads `Primavera en Madrid` and intro body remains readable.
- Outro agreement says `es bonita` for `la primavera`.
