# Ep.21 `A veces me levanto temprano` production reference

Use this when producing a Spanish Lab A1+ bridge episode that upgrades underused Ep.1 phrase-bank material with a single frequency adverb.

## Planning decision

Peter asked whether Ep.21 could combine `a veces` with content from the 50 Ep.1 phrases that had not yet been treated as focused episodes. The winning direction was:

- Title direction: `A veces me levanto temprano 🌅 가끔 일찍 일어나요 | Español A1+ · Ep.21`
- CEFR: `A1+`
- One learning point: `A veces + presente` = “가끔 ~해요”
- Continuity: reuse Ep.1 routine/daily-life phrase-bank items rather than making another broad 50-phrase list.

Good Ep.1 expressions to mine for this pattern:

- `Me levanto temprano.`
- `Tengo tiempo.`
- `Voy al trabajo.`
- `Voy a estudiar español.` / simplified in story as `estudio español`
- `Me gusta leer.` and `Me gusta aprender idiomas` are possible but less central for `a veces`.

## Thumbnail-first workflow

1. Generate a direct 16:9 thumbnail/background image:
   - warm morning apartment/study corner in Madrid;
   - Jin on the right, waking/studying with coffee/notebook;
   - leave the left side clean for title overlay;
   - no text/logos/watermarks; avoid cropped head/hands.
2. Compose an Ep.7-style overlay:
   - cream left text panel;
   - coral badge: `Español A1+ · Ep.21`;
   - main Spanish: `A veces` + smaller `me levanto temprano`;
   - Korean pill: `가끔 일찍 일어나요`;
   - teal pill: `가끔 = A veces`;
   - footer note: `A veces + 현재형`.
3. Save both repo and output copies so handoff and publish artifacts match:
   - `images/ep21-a-veces-me-levanto-temprano-source.png`
   - `thumbs/a1-ep21-a-veces-me-levanto-temprano.jpg`
   - `output/thumbs/frases-a1-ep21-a-veces-me-levanto-temprano.jpg`
   - `output/qa/a-veces-me-levanto-temprano/thumbnail.jpg`

## Episode shape

Use a full A1 story-card style, not a plain Shorts card:

- module: `projects/a_veces_me_levanto_temprano_a1.py`
- source: `a1-a-veces-me-levanto-temprano/descrip.md`
- source image: `images/ep21-a-veces-me-levanto-temprano-source.png`
- thumbnail: `thumbs/a1-ep21-a-veces-me-levanto-temprano.jpg`
- output slug: `a-veces-me-levanto-temprano`
- 30 dialogue lines, 4 blocks, about 4m48s.

Recommended blocks:

1. `Por la mañana` — reintroduce Ep.1 phrase `Me levanto temprano`.
2. `A veces` — add the single new frequency word and repeat the full model.
3. `Mi rutina` — controlled swaps: `A veces tengo tiempo`, `A veces voy al trabajo en metro`, `A veces estudio español por la noche`.
4. `Mini prueba` — ask what `a veces` means and produce the target sentence.

Keep `A veces + present tense` as the only learning point. Treat `en metro` and `por la noche` as contextual vocabulary, not new grammar points.

## Validation chain used

From repo root:

```sh
python3 -m py_compile projects/a_veces_me_levanto_temprano_a1.py
PROJECT=a_veces_me_levanto_temprano_a1 PYTHON=.venv/bin/python make check
PROJECT=a_veces_me_levanto_temprano_a1 PYTHON=.venv/bin/python make test
PROJECT=a_veces_me_levanto_temprano_a1 PYTHON=.venv/bin/python make lint-spanish
PROJECT=a_veces_me_levanto_temprano_a1 PYTHON=.venv/bin/python make tts
PROJECT=a_veces_me_levanto_temprano_a1 PYTHON=.venv/bin/python make publish-cards
PROJECT=a_veces_me_levanto_temprano_a1 PYTHON=.venv/bin/python make verify
```

Expected successful publish artifacts:

- `output/publish/frases-a1-ep21-a-veces-me-levanto-temprano-16x9-v1.mp4`
- `output/meta/frases-a1-ep21-a-veces-me-levanto-temprano-16x9-v1.json`
- `output/meta/frases-a1-ep21-a-veces-me-levanto-temprano-16x9-v1.md`
- `output/thumbs/frases-a1-ep21-a-veces-me-levanto-temprano.jpg`

## QA notes

- Visual contact sheet should confirm Korean text renders correctly, no tofu boxes, no major clipping/overlap, and portrait placement is acceptable.
- `make verify` should report 1280x720, H.264, AAC, 30 fps, and equal video/audio duration.
- A missing decision-log warning during publish is non-blocking unless Peter specifically requests decision-log archiving.
- Stop at a reviewable local bundle. Do not auto-upload or externally publish.
