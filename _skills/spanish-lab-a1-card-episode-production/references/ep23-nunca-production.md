# Ep.23 production reference — `Nunca tomo café por la noche`

Use this as a compact precedent for A1+ frequency/negative-routine episodes that follow `a veces` and `siempre`.

## Learning design
- Episode: Ep.23
- Level: A1+
- One learning point: `nunca + presente` to say what someone does not do / “never do X”.
- Continuity: completes a useful mini-ladder after Ep.21 `a veces + presente` and Ep.22 `siempre + presente`.
- Scenario: Jin studies at night with a coffee on the table and says `Nunca tomo café por la noche`.
- Keep Korean support simple: `nunca = 절대 안 / 전혀 안`; avoid adding a second grammar point beyond the negative/frequency pattern.

## User correction captured
Peter attached a previous first slide and noted that, on the right text area, the top three divisions should be visually distinct with generous spacing:
1. main title;
2. level/episode subtitle;
3. intro/body sentence.

For Ep.23 this was handled by:
- keeping `DESIGN["intro_title"]` short: `Nunca`;
- using a compact intro sentence: `Hoy Jin aprende a decir lo que no hace: nunca tomo café por la noche.`;
- verifying the full-size 1280x720 intro frame, not only the contact sheet.

## Production artifacts used
- Project module: `projects/nunca_tomo_cafe_a1.py`
- Source script: `a1-nunca-tomo-cafe/descrip.md`
- Final local render: `output/publish/frases-a1-ep23-nunca-tomo-cafe-16x9-v1.mp4`
- Metadata: `output/meta/frases-a1-ep23-nunca-tomo-cafe-16x9-v1.md` and `.json`
- Thumbnail: `output/thumbs/frases-a1-ep23-nunca-tomo-cafe.jpg`
- QA frames: `output/qa/nunca-tomo-cafe/frame-intro-v1.png`, `contact-sheet-v1.jpg`

## Commands / validation chain
```sh
python3 -m py_compile projects/nunca_tomo_cafe_a1.py
PROJECT=nunca_tomo_cafe_a1 PYTHON=.venv/bin/python make check
PROJECT=nunca_tomo_cafe_a1 PYTHON=.venv/bin/python make test
PROJECT=nunca_tomo_cafe_a1 PYTHON=.venv/bin/python make lint-spanish
PROJECT=nunca_tomo_cafe_a1 PYTHON=.venv/bin/python make tts
PROJECT=nunca_tomo_cafe_a1 PYTHON=.venv/bin/python make publish-cards
PROJECT=nunca_tomo_cafe_a1 PYTHON=.venv/bin/python make verify
PROJECT=nunca_tomo_cafe_a1 PYTHON=.venv/bin/python .venv/bin/python checks/probe_output.py \
  output/publish/frases-a1-ep23-nunca-tomo-cafe-16x9-v1.mp4
```

## QA emphasis
- Extract and inspect a full-size intro frame whenever Peter flags first-slide typography or spacing.
- Check that title/subtitle/body are separated enough to read as three distinct divisions.
- Also verify Korean line, source image crop, no clipping, no tofu boxes, and contact-sheet consistency.

## Handoff note
Final package was local-only and approval-gated: no external upload/posting performed.
