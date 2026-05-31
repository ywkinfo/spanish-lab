# Ep.29 `Me lo llevo` thumbnail precedent

Use this as a precedent when producing or revising the Ep.29 thumbnail/visual direction after Peter rejected too-basic follow-ups.

## Continuity decision
- Ep.28 already used `Quiero un café para llevar` / `Quiero + product + para llevar`; do not repeat it for Ep.29.
- Peter also rejected numbers 0–10 as too basic for Ep.29.
- `¿Cuánto cuesta?` and `¿Dónde está...?` have strong prior-use warnings (`¿Cuánto cuesta?` in ticket/café material, `¿Dónde está el metro?` in Ep.9), so avoid presenting them as fresh main Ep.29 topics unless explicitly framed as review/remake.
- Approved practical replacement direction: `Me lo llevo` = “이걸로 할게요 / 이거 살게요”, taught as a chunk at A1+/A2-entry in a shopping/souvenir scene.

## Thumbnail source prompt pattern
Generate a direct 16:9 source image with:
- warm modern Spanish souvenir shop / market stall;
- characters on the right: Jin holding a small mug/postcard, Lucía smiling, Diego encouraging;
- left 45% clean negative space for overlay;
- no readable text, logos, signs, cropped heads, or objects crossing into the left text zone.

Session source image path:
`/opt/data/repos/spanish-lab/images/ep29-me-lo-llevo-source.png`

## Overlay copy
Ep.7-style left panel:
- badge: `Español A1+ · Ep.29`
- large title: `Me lo` / `llevo`
- Korean pill: `이걸로 할게요`
- teal pill: `쇼핑 스페인어`

## Composition notes
- Use the standard full-bleed blurred/darkened background with a sharp right-side scene faded into the left panel.
- Cream rounded text panel on the left keeps the Spanish/Korean overlay readable.
- The final QA thumbnail should show all three character heads/faces fully visible, no overlay collisions, no clipped text, and no accidental readable text/logos.

## Artifact paths from the precedent
- Script: `/opt/data/repos/spanish-lab/scripts/create_ep29_thumbnail.py`
- Source image: `/opt/data/repos/spanish-lab/images/ep29-me-lo-llevo-source.png`
- Repo thumbnail: `/opt/data/repos/spanish-lab/thumbs/a1-ep29-me-lo-llevo.jpg`
- Output thumbnail: `/opt/data/repos/spanish-lab/output/thumbs/frases-a1-ep29-me-lo-llevo.jpg`
- QA image: `/opt/data/repos/spanish-lab/output/qa/me-lo-llevo/thumbnail.jpg`

## Verification used
- Ran the thumbnail composition script with `.venv/bin/python scripts/create_ep29_thumbnail.py`.
- Verified all image artifacts exist and are 1280×720 with Pillow from `.venv/bin/python`.
- Visual QA checked Spanish/Korean readability, clear left panel, visible characters, no head cropping, no accidental text/logos.
