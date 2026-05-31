# Ep.27 `Hay una farmacia cerca` production reference

Use as a precedent for thumbnail-approved A1+ episodes where Peter then says `영상 제작` and the next package should be a full Spanish Lab story-card episode, not a Shorts-only draft.

## Episode shape
- Module: `projects/hay_una_farmacia_cerca_a1.py`
- Source directory: `a1-hay-una-farmacia-cerca/descrip.md`
- Source image: `images/ep27-hay-una-farmacia-cerca-source.png`
- Output slug: `hay-una-farmacia-cerca`
- Publish artifact: `output/publish/frases-a1-ep27-hay-una-farmacia-cerca-16x9-v1.mp4`
- Thumbnail artifact: `output/thumbs/frases-a1-ep27-hay-una-farmacia-cerca.jpg`
- Level: `A1+`
- One learning point: `hay + noun` for existence/availability
- Main phrase: `Hay una farmacia cerca.`
- Duration target achieved: `297.0s` (~4:57) with 30 dialogue lines and 4 function blocks.

## Content pattern
Continue naturally from Ep.26 (`estar en + lugar`) by contrasting exact location with existence/availability:
1. Context: Jin is near the station and needs a pharmacy.
2. Target phrase: `Hay una farmacia cerca.`
3. Question form uses the same word: `¿Hay una farmacia cerca?`
4. Controlled noun/place swaps: `Hay un café aquí`, `Hay un baño en la estación`, `¿Hay un supermercado cerca?`
5. Short answer: `Sí, hay uno cerca.`
6. Bridge back to Ep.26-style exact location: `¿Dónde está la farmacia?`

Keep exactly one learning point. The location nouns are vocabulary support only, not a separate grammar lesson.

## Spanish-facing display/narration pitfall
Keep Spanish-facing `text_es` Spanish-only. During Ep.27 drafting, lines like `Naturalmente, en coreano suena como: 근처에 약국이 있어요` and quiz prompts containing Korean inside Spanish text had to be replaced with Spanish-only prompts:
- `Naturalmente, es una frase sencilla para viajar.`
- `Mini prueba: traduce esta frase al español.`
- `Ahora conviértela en una pregunta.`

Put literal/natural Korean prompts in `text_ko` / descrip Korean column only.

## Thumbnail/source-art pattern
Peter approved the thumbnail-first direction:
- warm Spanish street near a train/metro station;
- pharmacy cross and café context visible;
- Jin/Lucía/Diego on the right;
- left side clean negative space for Ep.7-style overlay;
- finished overlay copy: `Español A1+ · Ep.27`, `Hay una / farmacia / cerca`, `근처에 약국이 있어요`, `¿Hay una farmacia cerca?`.

When composing the final thumbnail, fit the teal callout pill by measuring the text or reducing font size; the first attempt clipped the long `¿Hay una farmacia cerca?` pill until the callout font was reduced.

## Validation chain used
```sh
PROJECT=hay_una_farmacia_cerca_a1 PYTHON=.venv/bin/python .venv/bin/python -m py_compile projects/hay_una_farmacia_cerca_a1.py
PROJECT=hay_una_farmacia_cerca_a1 PYTHON=.venv/bin/python make check
PROJECT=hay_una_farmacia_cerca_a1 PYTHON=.venv/bin/python make test
PROJECT=hay_una_farmacia_cerca_a1 PYTHON=.venv/bin/python make lint-spanish
PROJECT=hay_una_farmacia_cerca_a1 PYTHON=.venv/bin/python make tts
PROJECT=hay_una_farmacia_cerca_a1 PYTHON=.venv/bin/python make check
PROJECT=hay_una_farmacia_cerca_a1 PYTHON=.venv/bin/python make publish-cards
PROJECT=hay_una_farmacia_cerca_a1 PYTHON=.venv/bin/python make verify
PROJECT=hay_una_farmacia_cerca_a1 PYTHON=.venv/bin/python .venv/bin/python checks/probe_output.py output/publish/frases-a1-ep27-hay-una-farmacia-cerca-16x9-v1.mp4
```

For long renders, run `publish-cards && verify` in the background and poll; this render completed cleanly after a timeout-clamped wait.

## QA frame commands
```sh
mkdir -p output/qa/hay-una-farmacia-cerca
ffmpeg -y -loglevel error \
  -i output/publish/frases-a1-ep27-hay-una-farmacia-cerca-16x9-v1.mp4 \
  -vf "select='eq(n,0)+eq(n,360)+eq(n,900)+eq(n,1440)+eq(n,2160)+eq(n,2880)+eq(n,3960)+eq(n,5940)+eq(n,8520)',scale=320:180,tile=3x3" \
  -frames:v 1 output/qa/hay-una-farmacia-cerca/contact-sheet-v1.jpg
ffmpeg -y -loglevel error \
  -i output/publish/frases-a1-ep27-hay-una-farmacia-cerca-16x9-v1.mp4 \
  -frames:v 1 output/qa/hay-una-farmacia-cerca/intro-frame-v1.png
```

QA passed: readable Spanish/Korean, Hangul rendered, portraits visible, intro spacing acceptable, and video/audio duration both exactly `297.0s`.
