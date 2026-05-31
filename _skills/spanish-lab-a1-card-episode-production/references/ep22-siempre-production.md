# Ep.22 production reference — `Siempre tomo café`

Use this as a compact precedent for later A1+/routine-frequency story-card episodes.

## Learning design
- Episode: Ep.22
- Level: A1+
- One learning point: `siempre + presente` to say a fixed routine / “always do X”.
- Continuity: follows Ep.21 `A veces + presente` by contrasting occasional routines with fixed routines.
- Scenario: Jin in a morning kitchen/café context; `Siempre tomo café por la mañana` as the anchor line.
- Keep Korean learner focus: literal/natural Korean support and simple shadowing around `siempre`.

## Production artifacts used
- Project module: `projects/siempre_tomo_cafe_a1.py`
- Source script: `a1-siempre-tomo-cafe/descrip.md`
- Final accepted local render: `output/publish/frases-a1-ep22-siempre-tomo-cafe-16x9-v3.mp4`
- Metadata: `output/meta/frases-a1-ep22-siempre-tomo-cafe-16x9-v3.md` and `.json`
- Thumbnail: `output/thumbs/frases-a1-ep22-siempre-tomo-cafe.jpg`
- QA frames: `output/qa/siempre-tomo-cafe/contact-sheet-v3.jpg`, `frame-intro-v3.png`

## Commands / validation chain
```sh
python3 -m py_compile projects/siempre_tomo_cafe_a1.py
PROJECT=siempre_tomo_cafe_a1 PYTHON=.venv/bin/python make check
PROJECT=siempre_tomo_cafe_a1 PYTHON=.venv/bin/python make test
PROJECT=siempre_tomo_cafe_a1 PYTHON=.venv/bin/python make lint-spanish
PROJECT=siempre_tomo_cafe_a1 PYTHON=.venv/bin/python make tts
PROJECT=siempre_tomo_cafe_a1 PYTHON=.venv/bin/python make publish-cards
PROJECT=siempre_tomo_cafe_a1 PYTHON=.venv/bin/python make verify
```

Representative final contact sheet for a ~286s / 30fps video used late-frame `eq(n,8520)` to include the outro/recap.

## Pitfall found and fix
The initial render had an intro title/body spacing problem: `Siempre tomo café por la mañana` and then `Siempre tomo café` both looked acceptable in a small contact sheet but were too tight/overlapping at full 1280x720 intro-frame inspection. Fix by shortening the intro display title to the core learning point (`Siempre`), bumping `RENDER_VERSION`, rerendering, and verifying a full-size intro frame plus the contact sheet.

Do not rely on contact sheet alone for intro typography when the title is long or line-wrapped. Extract the first frame at full resolution and run visual QA before handoff.

## Handoff note
Final package was local-only and approval-gated: no external upload/posting performed. Report the final version explicitly (`v3`) when earlier versions were rejected internally for visual QA.