# Ep.14 `Voy a practicar` Production Reference

Session-specific reference for Español A1 · Ep.14, a full story-card episode bridging from Ep.13 `Quiero + infinitivo` into simple future plans with `Voy a + infinitivo`.

## Content shape
- Episode: Ep.14
- Public slug: `voy-a-practicar`
- Project module: `projects/voy_a_practicar_a1.py`
- Source script: `a1-voy-a-practicar/descrip.md`
- CEFR: A1
- One learning point: `Voy a + infinitivo`
- Story function: Jin makes a simple plan for tomorrow after Ep.13's “quiero aprender más” direction.
- Useful A1 examples:
  - `Mañana voy a practicar español.`
  - `Voy a escuchar y repetir.`
  - `Voy a hablar un poco.`
  - `Voy a aprender más.`

## Production commands used
From `/opt/data/repos/spanish-lab`:
```sh
PYTHON=.venv/bin/python .venv/bin/python -m py_compile projects/voy_a_practicar_a1.py
PROJECT=voy_a_practicar_a1 PYTHON=.venv/bin/python make check
PROJECT=voy_a_practicar_a1 PYTHON=.venv/bin/python make test
PROJECT=voy_a_practicar_a1 PYTHON=.venv/bin/python make lint-spanish
PROJECT=voy_a_practicar_a1 PYTHON=.venv/bin/python make tts
PROJECT=voy_a_practicar_a1 PYTHON=.venv/bin/python make check
PROJECT=voy_a_practicar_a1 PYTHON=.venv/bin/python make preview-cards
PROJECT=voy_a_practicar_a1 PYTHON=.venv/bin/python make publish-cards
PROJECT=voy_a_practicar_a1 PYTHON=.venv/bin/python make verify
```

## Published artifact paths
- Final video: `output/publish/frases-a1-ep14-voy-a-practicar-16x9-v1.mp4`
- Thumbnail: `output/thumbs/frases-a1-ep14-voy-a-practicar.jpg`
- Metadata JSON: `output/meta/frases-a1-ep14-voy-a-practicar-16x9-v1.json`
- Description/chapters/script: `output/meta/frases-a1-ep14-voy-a-practicar-16x9-v1.md`
- QA contact sheet: `output/qa/voy-a-practicar/final-contact-sheet.jpg`

## QA and fixes learned
1. Visual contact-sheet QA caught two copy issues after an otherwise valid render:
   - Intro Spanish phrasing `voy a más un verbo` was unnatural/wrong. Fix to `voy a seguido de un verbo`.
   - First dialogue line redundantly began `Jin, ...` while the speaker label was already Jin. Fix to `Mañana voy a practicar español.` and remove `Jin,` from the Korean subtitle.
2. After any source/script copy fix found by visual QA, do not hand off the old render. Patch both the project module and `descrip.md`, remove stale final/publish/meta artifacts or bump `RENDER_VERSION`, rerun TTS/check/publish/verify, then regenerate the contact sheet.
3. When probing the versioned publish output directly, include the episode `PROJECT` environment. Running `checks/probe_output.py output/publish/...mp4` without `PROJECT=voy_a_practicar_a1` used the wrong default expected size and produced a false `expected 1024x576, got 1280x720` error. With the project env set, the publish output verified correctly.
4. `build.publish` may warn that the decision log is missing; this is not a render blocker unless decision-snapshot archiving is explicitly required.

## Contact sheet frame picks
For the 306s / 30fps final video, this 3x3 contact sheet covered intro, several body blocks, and outro:
```sh
mkdir -p output/qa/voy-a-practicar
ffmpeg -y -loglevel error \
  -i output/publish/frases-a1-ep14-voy-a-practicar-16x9-v1.mp4 \
  -vf "select='eq(n,0)+eq(n,510)+eq(n,1050)+eq(n,1860)+eq(n,3000)+eq(n,4200)+eq(n,5550)+eq(n,6900)+eq(n,8500)',scale=320:180,tile=3x3" \
  -frames:v 1 output/qa/voy-a-practicar/final-contact-sheet.jpg
```

QA checklist for this contact sheet:
- Spanish/Korean text readable.
- Hangul renders correctly, no tofu boxes.
- Character portraits and speaker labels align.
- No major clipping/overlap.
- Intro phrase says `voy a seguido de un verbo`.
- Line 01 says `Mañana voy a practicar español.`
- Outro recap readable.
