# Ep.13 `Quiero volver` production reference

Session context: after Ep.12 `¿Qué tal el viaje?`, Peter asked first for thumbnail direction, then approved thumbnail draft, then requested the full script/30-line story-card structure, then requested video production.

## Continuity decision
Ep.12 ends with Jin saying `Quiero volver.` and discussing rest after the trip. For Ep.13, the strongest bridge is to keep the exact expression as the visible hook and expand it into one A1 learning point:

- Core learning point: `Quiero + infinitivo` = “~하고 싶어”
- Public hook: `Quiero volver`
- Korean hook: `다시 가고 싶어`
- Avoid reverting to the rejected Shorts/card-only `Quiero + 명사` direction; this is a full A1 story-card episode.

## Thumbnail-first workflow used
Use the Ep.7-style thumbnail pattern, not a new layout:
- Generate source art showing Jin after the Toledo trip, showing travel photos to Lucía and Diego.
- Keep left 45% clean/darker for text; characters and travel scene on the right.
- Overlay: cream left rounded panel, coral badge, large white Spanish title with black stroke, Korean white pill, teal grammar pill.
- Final overlay copy:
  - Badge: `Español A1 · Ep.13`
  - Main: `Quiero / volver`
  - Korean: `다시 가고 싶어`
  - Pill: `Quiero + 동사원형`

Example source-art prompt shape:
```text
Warm modern semi-flat YouTube thumbnail illustration for a Korean Spanish learning channel. A cozy travel-aftertalk scene in Spain, inspired by Toledo. On the right side, Jin, a Korean A1 Spanish learner with a small backpack, shows travel photos on his phone; Lucía smiles warmly; Diego gestures like a friendly teacher. They are near a café table with travel items like a train ticket, camera, and small suitcase. Background hints of Toledo-style arches or a Spanish train-station café, warm afternoon light. Leave the left 45 percent clean and slightly darker for text overlay. No readable text, logos, watermark, or numbers. Full heads/hair visible, clear friendly faces, 16:9.
```

Example paths from the run:
- Source art: `assets/generated/ep13-quiero-volver-source.png`
- Repo thumbnail: `thumbs/a1-quiero-volver.jpg`
- Publish thumbnail: `output/thumbs/frases-a1-ep13-quiero-volver.jpg`
- QA thumbnail draft: `output/qa/ep13-quiero-volver/thumbnail-draft.jpg`

## Script shape
Full story-card pattern:
- 30 dialogue lines
- 4 blocks
- Intro around `14.0s`
- Block headers around `3.0s`
- Dialogue mostly `7.5–10.0s`
- Outro around `23.0s`
- Verified duration in the produced run: `310.0s` (~5m10s)

Blocks:
1. `Quiero volver` / `다시 가고 싶어`
2. `Quiero descansar` / `쉬고 싶어`
3. `Quiero ver las fotos` / `사진을 보고 싶어`
4. `Quiero practicar español` / `스페인어를 연습하고 싶어`

Final approved script adjustments made before production:
- Replace `Perfecto. Quiero más infinitivo.` with the more natural teacher line `Perfecto. Después de quiero, usamos un verbo.`
- Replace `Sí, quiero ver esa foto.` with simpler `Sí, quiero ver la foto.`

## Production module details
- Module: `projects/quiero_volver_a1.py`
- Source text: `a1-quiero-volver/descrip.md`
- Output slug: `quiero-volver`
- Public slug: `a1-quiero-volver`
- Episode: `13`
- Level: `A1`
- Render type: `cards`
- Title: `Quiero volver 😊 다시 가고 싶어 | Español A1 · Ep.13`
- Character voices:
  - `Lucía`: `es-ES-ElviraNeural`
  - `Jin`: `es-ES-AlvaroNeural`
  - `Diego`: `es-MX-JorgeNeural`
- BGM: reuse `assets/audio/spanish-lab-brand-bgm.mp3` with the established ducked settings from recent A1 episodes.

## Validation chain used
From repo root with explicit project and venv:

```sh
PYTHON=.venv/bin/python .venv/bin/python -m py_compile projects/quiero_volver_a1.py
PROJECT=quiero_volver_a1 PYTHON=.venv/bin/python make check
PROJECT=quiero_volver_a1 PYTHON=.venv/bin/python make test
PROJECT=quiero_volver_a1 PYTHON=.venv/bin/python make lint-spanish
PROJECT=quiero_volver_a1 PYTHON=.venv/bin/python make tts
PROJECT=quiero_volver_a1 PYTHON=.venv/bin/python make check
PROJECT=quiero_volver_a1 PYTHON=.venv/bin/python make preview-cards
PROJECT=quiero_volver_a1 PYTHON=.venv/bin/python make publish-cards
PROJECT=quiero_volver_a1 PYTHON=.venv/bin/python make verify
```

`make verify` reported `ok: true`, 1280x720 H.264, AAC 44100 Hz, video/audio duration `310.0s`, expected duration `310.0s`, faststart true.

## QA artifacts and frame picks
- Final video: `output/publish/frases-a1-ep13-quiero-volver-16x9-v1.mp4`
- Metadata: `output/meta/frases-a1-ep13-quiero-volver-16x9-v1.md/json`
- Thumbnail: `output/thumbs/frases-a1-ep13-quiero-volver.jpg`
- Contact sheet: `output/qa/quiero-volver/final-contact-sheet.jpg`

For this 310s episode at 30fps, a useful 3x3 contact sheet can use representative frames:
```sh
mkdir -p output/qa/quiero-volver
ffmpeg -y -loglevel error \
  -i output/publish/frases-a1-ep13-quiero-volver-16x9-v1.mp4 \
  -vf "select='eq(n,0)+eq(n,510)+eq(n,1050)+eq(n,1860)+eq(n,3000)+eq(n,4200)+eq(n,5550)+eq(n,6900)+eq(n,8700)',scale=320:180,tile=3x3" \
  -frames:v 1 output/qa/quiero-volver/final-contact-sheet.jpg
```

QA checks passed visually: Spanish/Korean readable, Hangul rendered, no tofu boxes, portraits placed correctly, intro/body/outro readable.

## Reusable lesson
When Peter approves “video production” after thumbnail + full script review, proceed to create the module, `descrip.md`, TTS, render, publish, verify, and contact sheet without asking another style question, provided the approved draft already matches the established A1 story-card style and non-public publishing boundary.