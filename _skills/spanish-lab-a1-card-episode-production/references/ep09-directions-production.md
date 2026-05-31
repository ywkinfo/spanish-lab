# Ep.9 directions production notes

Session-specific details from producing Spanish Lab A1 Ep.9, useful for future directions/travel story-card episodes.

## Approved episode shape
- Title: `¿Dónde está el metro? | Español A1 · Ep.9`
- Scenario: after Ep.8 café payment, Jin leaves the café and asks Lucía/Diego how to get to the metro in a Madrid street.
- Teaching functions: ask for a place, understand `cerca`, follow `todo recto`, `a la derecha`, `en la esquina`, and recover with `No entiendo` / `¿Puedes repetir, por favor?`.
- Final implemented script used 30 dialogue lines, reduced from a 33-line first manuscript by cutting redundant confirmation/left-direction lines.

## Canonical files and paths
- Module: `projects/donde_esta_el_metro_a1.py`
- Source text: `a1-donde-esta-el-metro/descrip.md`
- Source art: `assets/generated/madrid-street-directions-thumbnail-source.png`
- Repo thumbnail: `thumbs/a1-donde-esta-el-metro.jpg`
- Thumbnail script: `scripts/make_ep09_thumbnail_ep7_style.py`
- Publish video: `output/publish/frases-a1-ep09-donde-esta-el-metro-16x9-v1.mp4`
- Publish thumbnail: `output/thumbs/frases-a1-ep09-donde-esta-el-metro.jpg`
- Metadata: `output/meta/frases-a1-ep09-donde-esta-el-metro-16x9-v1.{md,json}`
- QA contact sheet: `output/qa/donde-esta-el-metro-v1/contact-sheet.jpg`

## Module settings that worked
- `OUTPUT_NAME = "donde-esta-el-metro"`
- `PUBLIC_SLUG = "a1-donde-esta-el-metro"`
- `RENDER_VERSION = 1`
- `RENDER_TYPE = "cards"`
- `THUMBNAIL_PATH = "thumbs/a1-donde-esta-el-metro.jpg"`
- Characters: display `Jin`, `Lucía`, `Diego`; Jin can still use legacy asset path `assets/characters/peter-profile.png`.
- Brand BGM reused from `assets/audio/spanish-lab-brand-bgm.mp3` with the quiet-draft ducking settings from prior A1 episodes.

## Blocks and chapters
Final block structure:
1. `¿Dónde está el metro?` / `장소 묻기`
2. `Sigue todo recto` / `직진하기`
3. `A la derecha` / `오른쪽으로`
4. `¿Puedes repetir?` / `다시 말해 달라고 하기`

Final chapter timestamps from publish metadata:
```text
0:00 Introducción
0:12 ¿Dónde está el metro?
1:22 Sigue todo recto
2:18 A la derecha
3:08 ¿Puedes repetir?
4:36 Repaso final
```

## Validation chain used
```sh
.venv/bin/python -m py_compile projects/donde_esta_el_metro_a1.py
PROJECT=donde_esta_el_metro_a1 PYTHON=.venv/bin/python make check
PROJECT=donde_esta_el_metro_a1 PYTHON=.venv/bin/python make test
PROJECT=donde_esta_el_metro_a1 PYTHON=.venv/bin/python make lint-spanish
PROJECT=donde_esta_el_metro_a1 PYTHON=.venv/bin/python make preview-cards
PROJECT=donde_esta_el_metro_a1 PYTHON=.venv/bin/python make publish-cards
PROJECT=donde_esta_el_metro_a1 PYTHON=.venv/bin/python make verify
```

Successful output characteristics:
- 36 segments, 30 dialogue lines, 4 block headers, 6 chapters.
- Duration: `299.5s`.
- Verify: H.264/yuv420p, 1280x720, 30fps, AAC stereo 44100 Hz, audio duration `299.5s`, `ok: true`.
- A `decision log not found` warning during publish is non-blocking.

## Contact sheet QA command
```sh
mkdir -p output/qa/donde-esta-el-metro-v1
ffmpeg -y -loglevel error \
  -i output/publish/frases-a1-ep09-donde-esta-el-metro-16x9-v1.mp4 \
  -vf "select='eq(n,0)+eq(n,360)+eq(n,900)+eq(n,1440)+eq(n,2160)+eq(n,2880)+eq(n,3960)+eq(n,5040)+eq(n,7200)',scale=320:180,tile=3x3" \
  -frames:v 1 output/qa/donde-esta-el-metro-v1/contact-sheet.jpg
```
QA passed: Spanish readable, Hangul rendered, portrait placement acceptable, no clipping/overlap, intro/outro readable, directions visual continuity acceptable.
