# Ep.28 `Quiero un café para llevar` production reference

Use this as the precedent for a practical A1+ café/travel episode that replaced the originally planned `el/la` article topic after Peter judged it too basic.

## Decision / planning context
- Peter rejected Ep.28 `el / la + noun` as too basic (`너무 기본 문법이라 건너 띄고 다음 소재`).
- The episode pivoted to practical café/travel language: `Quiero + product + para llevar`.
- Keep exactly one learning point: ordering something to go / takeaway.
- CEFR label: `A1+`.
- Public-facing phrase: `Quiero un café para llevar.`
- Short alternate phrase: `Para llevar, por favor.`

## Assets and paths
- Module: `projects/quiero_cafe_para_llevar_a1.py`
- Source text: `a1-quiero-cafe-para-llevar/descrip.md`
- Source image: `images/ep28-quiero-cafe-para-llevar-source.png`
- Generated source art: `assets/generated/ep28-quiero-cafe-para-llevar/source-cafe-para-llevar.png`
- Repo thumbnail: `thumbs/a1-ep28-quiero-cafe-para-llevar.jpg`
- Final publish artifact: `output/publish/frases-a1-ep28-quiero-cafe-para-llevar-16x9-v4.mp4`
- Final metadata: `output/meta/frases-a1-ep28-quiero-cafe-para-llevar-16x9-v4.md` and `.json`
- Final QA: `output/qa/ep28-quiero-cafe-para-llevar-v4/contact-sheet.jpg`, `intro-frame.png`

## Thumbnail pattern
- Ep.7-style thumbnail.
- Left cream panel with:
  - badge: `Español A1+ · Ep.28`
  - main title: `Para llevar`
  - Korean pill: `포장해 주세요`
  - teal phrase pill: `Quiero un café / para llevar`
- Right-side warm Madrid station café scene with Jin receiving takeaway coffee.
- Generate the background as direct 16:9 art with clean left space; then compose overlay with Pillow.
- Update both repo and output thumbnail paths.

## Script shape
- About 30 dialogue lines, 4 blocks, ~4m51s.
- Blocks:
  1. `Para llevar` / `포장 / 가져가기`
  2. `Quiero un café` / `커피 하나 원해요`
  3. `Cambia el producto` / `메뉴만 바꾸기`
  4. `Mini prueba` / `미니 퀴즈`
- Core examples:
  - `Quiero un café para llevar.`
  - `Para llevar, por favor.`
  - `Quiero un té para llevar.`
  - `Quiero un bocadillo para llevar.`

## QA / corrections made
- Avoid Korean inside Spanish-facing display text. A draft line had Korean embedded in Spanish text; replace with Spanish-only display text such as `En coreano natural, es una petición para llevar.` while keeping Korean explanation in `text_ko`.
- Avoid unnatural grammar-meta phrasing like `Quiero más un nombre, más para llevar.` Use natural wording: `La estructura es: quiero, un producto, y para llevar.`
- Use `producto` rather than `nombre` for menu-ordering context; `nombre` felt too abstract and grammar-heavy.
- For the intro source scene, use `DESIGN["intro_scene_fit"] = "contain"` if `cover` crops a visible character at the side. Verify the full-size intro frame, not only the contact sheet.
- Set `RENDER_VERSION` upward for each corrected rerender; final accepted local package was v4.

## Validation commands used
```sh
python3 -m py_compile projects/quiero_cafe_para_llevar_a1.py
PROJECT=quiero_cafe_para_llevar_a1 PYTHON=.venv/bin/python make tts
PROJECT=quiero_cafe_para_llevar_a1 PYTHON=.venv/bin/python make check
PROJECT=quiero_cafe_para_llevar_a1 PYTHON=.venv/bin/python make test
PROJECT=quiero_cafe_para_llevar_a1 PYTHON=.venv/bin/python make lint-spanish
PROJECT=quiero_cafe_para_llevar_a1 PYTHON=.venv/bin/python make publish-cards
PROJECT=quiero_cafe_para_llevar_a1 PYTHON=.venv/bin/python make verify
```

Final verify reported 1280x720 H.264/yuv420p, AAC 44.1kHz, duration/audio duration 291.5s, `ok: true`.
