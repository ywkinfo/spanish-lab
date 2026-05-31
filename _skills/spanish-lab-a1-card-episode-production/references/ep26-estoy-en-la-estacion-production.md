# Ep.26 `Estoy en la estación` production reference

Use as a precedent for A1+/A2- bridge episodes where Peter approves a thumbnail-first direction and then says `영상제작 진행`.

## Episode shape
- Module: `projects/estoy_en_la_estacion_a1.py`
- Source directory: `a1-estoy-en-la-estacion/descrip.md`
- Source image: `images/ep26-estoy-en-la-estacion-source.png`
- Thumbnail script: `scripts/create_ep26_thumbnail.py`
- Output slug: `estoy-en-la-estacion`
- Publish artifact: `output/publish/frases-a1-ep26-estoy-en-la-estacion-16x9-v2.mp4`
- Thumbnail artifact: `output/thumbs/frases-a1-ep26-estoy-en-la-estacion.jpg`
- Level: `A1+`
- One learning point: `estar en + lugar`
- Main phrase: `Estoy en la estación.`
- Duration target achieved: ~4m41s with 30 dialogue lines and 4 function blocks.

## Content pattern
Structure the lesson as a practical travel-message scene:
1. Context / question: `¿Dónde estás?`
2. Build the target: `estoy` → `estoy en` → `estoy en la estación`
3. Change only the place: `el hotel`, `el café`, `aquí`
4. Mini quiz and common-error guard: not `soy en la estación`, but `estoy en la estación`

Keep Spanish-facing display/narration Spanish-only. Put literal/natural Korean explanations in `text_ko`, not inside `text_es`.

## Thumbnail pattern
Peter approved the right-scene / left-overlay direction:
- station or platform scene on the right with Jin holding a phone;
- cream rounded panel on the left;
- badge `Español A1+ · Ep.26`;
- large Spanish title `Estoy en / la estación`;
- Korean pill `나 역에 있어요`;
- teal learning-point pill `위치 말하기 = estar`.

Run visual QA on the composed thumbnail, not just on the source image. Check that all Spanish/Korean text is readable and no accidental readable station text/logos appear.

## QA pitfall and fix
The first full render v1 passed technical checks but the full-size intro frame showed the title/subtitle/body grouping too tight. Contact sheets can make this look acceptable, so extract a full-size intro frame when the intro title is long or wraps.

For this episode, the fix was:
- bump `RENDER_VERSION` from 1 to 2;
- reduce project `DESIGN["font_size_title"]` from `64` to `58` so `Estoy en la estación` fits as one visually clean title line;
- rerun `make check`, `make publish-cards`, `make verify`;
- regenerate `contact-sheet-v2.jpg` and `intro-frame-v2.png`.

This preserved the established renderer and avoided infra changes.

## Validation chain used
```sh
PROJECT=estoy_en_la_estacion_a1 PYTHON=.venv/bin/python make check
PROJECT=estoy_en_la_estacion_a1 PYTHON=.venv/bin/python make test
PROJECT=estoy_en_la_estacion_a1 PYTHON=.venv/bin/python make lint-spanish
PROJECT=estoy_en_la_estacion_a1 PYTHON=.venv/bin/python make tts
PROJECT=estoy_en_la_estacion_a1 PYTHON=.venv/bin/python make check
PROJECT=estoy_en_la_estacion_a1 PYTHON=.venv/bin/python make publish-cards
PROJECT=estoy_en_la_estacion_a1 PYTHON=.venv/bin/python make verify
```

For long renders, run `publish-cards && verify` in the background and poll to completion instead of restarting.

## QA frame commands
```sh
mkdir -p output/qa/estoy-en-la-estacion
ffmpeg -y -loglevel error \
  -i output/publish/frases-a1-ep26-estoy-en-la-estacion-16x9-v2.mp4 \
  -vf "select='eq(n,0)+eq(n,360)+eq(n,900)+eq(n,1440)+eq(n,2160)+eq(n,2880)+eq(n,3960)+eq(n,5040)+eq(n,8040)',scale=320:180,tile=3x3" \
  -frames:v 1 output/qa/estoy-en-la-estacion/contact-sheet-v2.jpg
ffmpeg -y -loglevel error \
  -i output/publish/frases-a1-ep26-estoy-en-la-estacion-16x9-v2.mp4 \
  -frames:v 1 output/qa/estoy-en-la-estacion/intro-frame-v2.png
```
