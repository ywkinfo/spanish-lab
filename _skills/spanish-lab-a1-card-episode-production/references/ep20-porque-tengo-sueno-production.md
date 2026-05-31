# Ep.20 `Porque tengo sueño` production reference

Use this as a concrete example for Spanish Lab A1+ bridge episodes that continue a prior lesson and raise difficulty by one small speaking function.

## Context
- Episode: Ep.20
- Title: `Porque tengo sueño 😴 졸려서요 | Español A1+ · Ep.20`
- CEFR: A1+
- One learning point: `porque + short reason`
- Continuity: follows Ep.18 `Me gusta, pero...` and Ep.19 `Prefiero café`; Jin has chosen coffee and now learns to answer `¿Por qué?` with a short reason.
- Target style: established full A1 story-card episode, not a Shorts-only/simple phrase card.

## Thumbnail-first workflow
Peter asked for the thumbnail first, then approved video production. The successful pattern was:
1. Generate a direct 16:9 café background image with characters and scene interest on the right and clean left negative space.
2. Compose an Ep.7-style thumbnail: cream left panel, coral badge, large stroked Spanish title, Korean pill, teal callout.
3. Save both repo and publish-output thumbnail copies before full production.
4. After Peter says `영상 제작 진행`, treat that as approval to create the full reviewable episode bundle from the thumbnail direction.

Paths used:
```text
images/ep20-porque-tengo-sueno-source.png
thumbs/a1-ep20-porque-tengo-sueno.jpg
output/thumbs/frases-a1-ep20-porque-tengo-sueno.jpg
output/qa/porque-tengo-sueno/thumbnail.jpg
scripts/create_ep20_thumbnail.py
```

Overlay copy used:
```text
Español A1+ · Ep.20
Porque tengo sueño
졸려서요
¿Por qué?
porque + 이유
```

## Episode/source structure
Project module:
```text
projects/porque_tengo_sueno_a1.py
```

Script source:
```text
a1-porque-tengo-sueno/descrip.md
```

Output slug:
```text
OUTPUT_NAME = "porque-tengo-sueno"
PUBLIC_SLUG = "a1-porque-tengo-sueno"
EPISODE = 20
LEVEL = "A1+"
RENDER_TYPE = "cards"
```

Recommended story blocks:
1. `Hace calor` — reconnect to the café context.
2. `¿Por qué?` — introduce the question and short answer.
3. `Porque tengo sueño` — combine preference + reason.
4. `Mini prueba` — quick comprehension and production check.

Good example lines:
```text
¿Por qué?
Porque tengo sueño.
Prefiero café porque tengo sueño.
Quiero agua porque tengo sed.
Me quedo aquí porque hace calor.
```

## Language QA notes
- Keep the learning point singular: `porque + short reason`.
- It is acceptable in this A1+ bridge to reuse Ep.19 content (`Prefiero café`) as context, but do not make `preferir` the new teaching point.
- Keep explanations short and situational; avoid a full grammar lecture on subordinate clauses.
- For Spanish-facing display text, avoid mixing Korean inside `text_es` when possible. If a line must explain Korean meaning, prefer Spanish-only display plus Korean in `text_ko`; otherwise the slide can look less polished even if validators pass.
- Good A1+ ceiling: short reason sentences, not long causal/conditional structures.

## Validation chain that passed
```sh
python3 -m py_compile projects/porque_tengo_sueno_a1.py
PROJECT=porque_tengo_sueno_a1 PYTHON=.venv/bin/python make check
PROJECT=porque_tengo_sueno_a1 PYTHON=.venv/bin/python make test
PROJECT=porque_tengo_sueno_a1 PYTHON=.venv/bin/python make lint-spanish
PROJECT=porque_tengo_sueno_a1 PYTHON=.venv/bin/python make tts
PROJECT=porque_tengo_sueno_a1 PYTHON=.venv/bin/python make publish-cards
PROJECT=porque_tengo_sueno_a1 PYTHON=.venv/bin/python make verify
```

Final verified publish artifact:
```text
output/publish/frases-a1-ep20-porque-tengo-sueno-16x9-v1.mp4
```

Verification reported:
- `ok: true`
- duration: `294.0s`
- expected duration: `294.0s`
- codec: H.264 / AAC
- faststart: true

## QA contact sheet
Create a 3x3 visual QA sheet from the published video:
```sh
mkdir -p output/qa/porque-tengo-sueno
ffmpeg -y -loglevel error \
  -i output/publish/frases-a1-ep20-porque-tengo-sueno-16x9-v1.mp4 \
  -vf "select='eq(n,0)+eq(n,360)+eq(n,900)+eq(n,1440)+eq(n,2160)+eq(n,2880)+eq(n,3960)+eq(n,5040)+eq(n,8520)',scale=320:180,tile=3x3" \
  -frames:v 1 output/qa/porque-tengo-sueno/contact-sheet.jpg
```

QA expectations:
- Spanish/Korean readable;
- no tofu boxes;
- no major clipping/overlap;
- character portraits visible and not crowding the text;
- intro/outro readable;
- no external upload performed.

## Handoff wording
For the final handoff, include the upload-ready video path, thumbnail path, metadata paths, QA sheet, validation commands passed, and explicit `Peter 검토 대기`. Do not imply that YouTube upload/publishing happened.