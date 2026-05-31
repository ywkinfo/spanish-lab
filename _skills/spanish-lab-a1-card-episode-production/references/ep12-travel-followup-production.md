# Ep.12 travel follow-up production reference

Session context: Ep.11 ended with `En el próximo episodio seguimos practicando español útil para viajar.` The user asked whether a proposed weekend topic connected naturally, then approved a thumbnail-first workflow and later full video production.

## Continuity decision
A generic weekend episode (`¿Qué tal el fin de semana?`) is weaker after Ep.11. The stronger bridge is:

- Ep.11: station/train practical phrases (`¿A qué hora sale?`, `¿Cuánto tarda?`, `¿En qué andén?`).
- Ep.12: after the train trip, talk about a short weekend/day trip.

Use `¿Qué tal el viaje?` as the public title and include `fin de semana` inside the dialogue/description rather than making weekend the main thumbnail hook.

## Topic and copy
- Episode: Ep.12
- Module: `projects/que_tal_el_viaje_a1.py`
- Slug/output: `que-tal-el-viaje`
- Title: `¿Qué tal el viaje? 🚆 여행 어땠어? | Español A1 · Ep.12`
- Thumbnail main: `¿Qué tal el viaje?`
- Korean thumbnail: `여행 어땠어?`
- Supporting pill: `fui en tren · Toledo`

Core expressions:
- `¿Qué tal el viaje?`
- `Fui a Toledo.`
- `Fui en tren.`
- `¿Qué hiciste allí?`
- `Visité la ciudad.`
- `Saqué fotos.`
- `Comí algo rico.`
- `Me gustó mucho.`

## Thumbnail-first workflow used
When the user asked for the thumbnail before full production:
1. Generate 16:9 source art with characters on the right and clean left negative space.
2. Compose Ep.7-style overlay: cream left panel, coral badge, large stroked Spanish title, white Korean pill, teal vocabulary pill.
3. Save both canonical repo thumbnail and publish-output thumbnail paths:
   - `assets/generated/ep12-que-tal-el-viaje-source.png`
   - `thumbs/a1-que-tal-el-viaje.jpg`
   - `output/thumbs/frases-a1-ep12-que-tal-el-viaje.jpg`
4. Run visual QA before continuing: check Hangul, Spanish readability, no accidental readable station text/logos, full heads/hair, and travel/train continuity.

## Production shape
A full A1 story-card episode followed the established longer pattern:
- 30 dialogue lines
- 4 blocks
- Intro `13.0s`
- Each block header `3.0s` as breathing space
- Dialogue durations mostly `8.0–9.5s`
- Outro `22.0s`
- Total verified duration `291.0s` (~4m51s)

Blocks:
1. `¿Qué tal el viaje?` / `여행 어땠어?`
2. `Fui en tren` / `기차로 갔어`
3. `¿Qué hiciste allí?` / `거기서 뭐 했어?`
4. `Me gustó mucho` / `정말 마음에 들었어`

## Validation chain used
From repo root with explicit project and venv:

```sh
PYTHON=.venv/bin/python .venv/bin/python -m py_compile projects/que_tal_el_viaje_a1.py
PROJECT=que_tal_el_viaje_a1 PYTHON=.venv/bin/python make check
PROJECT=que_tal_el_viaje_a1 PYTHON=.venv/bin/python make test
PROJECT=que_tal_el_viaje_a1 PYTHON=.venv/bin/python make lint-spanish
PROJECT=que_tal_el_viaje_a1 PYTHON=.venv/bin/python make tts
PROJECT=que_tal_el_viaje_a1 PYTHON=.venv/bin/python make check
PROJECT=que_tal_el_viaje_a1 PYTHON=.venv/bin/python make preview-cards
PROJECT=que_tal_el_viaje_a1 PYTHON=.venv/bin/python make publish-cards
PROJECT=que_tal_el_viaje_a1 PYTHON=.venv/bin/python make verify
```

After preview/publish, make contact sheets with representative frames and visually QA intro/body/outro readability. For this ~4m51s video, final contact-sheet frame picks included `eq(n,8520)` to land near the outro.

## Handoff artifacts
- Video: `output/publish/frases-a1-ep12-que-tal-el-viaje-16x9-v1.mp4`
- Thumbnail: `output/thumbs/frases-a1-ep12-que-tal-el-viaje.jpg`
- Metadata: `output/meta/frases-a1-ep12-que-tal-el-viaje-16x9-v1.md/json`
- QA: `output/qa/que-tal-el-viaje/final-contact-sheet.jpg`

## Reusable lesson
When a user asks whether the next A1 episode connects to a prior outro, inspect the prior module's outro text before committing to a topic. If the topic is useful but the continuity is weak, preserve the user’s topic as a sub-context and retitle/reframe around the promised continuity thread.