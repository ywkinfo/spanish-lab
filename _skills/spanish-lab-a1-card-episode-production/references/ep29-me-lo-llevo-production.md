# Ep.29 `Me lo llevo` thumbnail + production precedent

Use this reference when producing a post-Ep.28 Spanish Lab A1+/A2-entry shopping episode or when avoiding duplicate next-topic suggestions after `para llevar`.

## Continuity correction
- Peter confirmed Ep.28 already covered `Quiero un café para llevar` / `Quiero + noun + para llevar`.
- Peter rejected `numbers 0–10` as too basic for Ep.29.
- Repo/archive search also showed `¿Cuánto cuesta?` and `¿Dónde está...?` had already appeared prominently, so avoid proposing them as fresh Ep.29 core phrases.
- Approved Ep.29 direction: `Me lo llevo` = “이걸로 할게요 / 이거 살게요”, taught as one chunk for shopping/souvenir situations.

## Produced artifact pattern
- Project module: `projects/me_lo_llevo_a1.py`
- Source script: `a1-me-lo-llevo/descrip.md`
- Source image: `images/ep29-me-lo-llevo-source.png`
- Thumbnail script: `scripts/create_ep29_thumbnail.py`
- Repo thumbnail: `thumbs/a1-ep29-me-lo-llevo.jpg`
- Publish thumbnail: `output/thumbs/frases-a1-ep29-me-lo-llevo.jpg`
- Publish video: `output/publish/frases-a1-ep29-me-lo-llevo-16x9-v1.mp4`
- Metadata: `output/meta/frases-a1-ep29-me-lo-llevo-16x9-v1.{md,json}`
- QA: `output/qa/me-lo-llevo/contact-sheet-v1.jpg`, plus full-size intro/outro frames.

## Thumbnail direction
Prompt pattern:
- 16:9 warm souvenir shop/market stall in Spain.
- Put Jin/Lucía/Diego on the right; keep left 45% clean negative space.
- No readable text/logos/signs; no cropped heads.
- Compose Ep.7-style overlay: cream left panel, coral `Español A1+ · Ep.29` badge, large Spanish title `Me lo llevo`, Korean pill `이걸로 할게요`, teal pill `쇼핑 스페인어`.

## Validation chain used
```sh
.venv/bin/python -m py_compile projects/me_lo_llevo_a1.py
PROJECT=me_lo_llevo_a1 PYTHON=.venv/bin/python make check
PROJECT=me_lo_llevo_a1 PYTHON=.venv/bin/python make test
PROJECT=me_lo_llevo_a1 PYTHON=.venv/bin/python make lint-spanish
PROJECT=me_lo_llevo_a1 PYTHON=.venv/bin/python make tts
PROJECT=me_lo_llevo_a1 PYTHON=.venv/bin/python make check
PROJECT=me_lo_llevo_a1 PYTHON=.venv/bin/python make publish-cards
PROJECT=me_lo_llevo_a1 PYTHON=.venv/bin/python make verify
PROJECT=me_lo_llevo_a1 PYTHON=.venv/bin/python .venv/bin/python checks/probe_output.py output/publish/frases-a1-ep29-me-lo-llevo-16x9-v1.mp4
```

## QA notes
- Full runtime landed around 4m24s (`263.6s`), matching the current full A1 story-card style.
- `make publish-cards` may warn about a missing decision log; treat as non-blocking unless Peter explicitly needs decision-log archiving.
- Generate both a 3x3 contact sheet and full-size intro/outro frames. The intro image panel used `contain` so all character heads remained visible.

## Copy guidance
Keep the learning point singular:
- Main phrase: `Me lo llevo.`
- Literal Korean: “그것을 가지고 가요.”
- Natural Korean: “이걸로 할게요 / 이거 살게요.”
- Mention `lo` briefly only as support; do not turn the episode into a pronoun grammar lesson.
