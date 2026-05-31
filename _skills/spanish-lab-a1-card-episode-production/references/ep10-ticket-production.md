# Ep.10 metro-ticket production notes

Session-specific details from producing Spanish Lab A1 Ep.10, useful for future ticket-buying / transit story-card episodes.

## Approved episode shape
- Title: `Un billete, por favor 🎫 지하철표 사기 | Español A1 · Ep.10`
- Scenario: direct continuation from Ep.9. After finding the Madrid metro station, Jin buys a ticket with help from Lucía and Diego.
- Teaching functions: ask for one ticket, state destination, ask price, pay/hand over money, choose `solo ida` vs `ida y vuelta`.
- Final implemented script used 30 dialogue lines, 4 learning-function blocks, and the recurring Jin/Lucía/Diego story-card format.

## Canonical files and paths
- Module: `projects/un_billete_por_favor_a1.py`
- Source text: `a1-un-billete-por-favor/descrip.md`
- Source art: `assets/generated/metro-ticket-thumbnail-source.png`
- Repo thumbnail: `thumbs/a1-un-billete-por-favor.jpg`
- Thumbnail script: `scripts/make_ep10_thumbnail_ep7_style.py`
- Publish video: `output/publish/frases-a1-ep10-un-billete-por-favor-16x9-v1.mp4`
- Publish thumbnail: `output/thumbs/frases-a1-ep10-un-billete-por-favor.jpg`
- Metadata: `output/meta/frases-a1-ep10-un-billete-por-favor-16x9-v1.{md,json}`
- QA contact sheet: `output/qa/un-billete-por-favor-v1/contact-sheet.jpg`

## Module settings that worked
- `OUTPUT_NAME = "un-billete-por-favor"`
- `PUBLIC_SLUG = "a1-un-billete-por-favor"`
- `RENDER_VERSION = 1`
- `RENDER_TYPE = "cards"`
- `THUMBNAIL_PATH = "thumbs/a1-un-billete-por-favor.jpg"`
- Characters: display `Jin`, `Lucía`, `Diego`; Jin uses legacy asset path `assets/characters/peter-profile.png`.
- Brand BGM reused from `assets/audio/spanish-lab-brand-bgm.mp3` with the same quiet-draft ducking settings as Ep.8/Ep.9.

## Blocks and chapters
Final block structure:
1. `Un billete, por favor` / `표 한 장 주세요`
2. `Voy al centro` / `시내로 가요`
3. `¿Cuánto cuesta?` / `얼마예요?`
4. `Solo ida` / `편도요`

Final chapter timestamps from publish metadata:
```text
0:00 Introducción
0:12 Un billete, por favor
1:22 Voy al centro
2:18 ¿Cuánto cuesta?
3:06 Solo ida
4:30 Repaso final
```

## Validation chain used
```sh
.venv/bin/python -m py_compile projects/un_billete_por_favor_a1.py
PROJECT=un_billete_por_favor_a1 PYTHON=.venv/bin/python make check
PROJECT=un_billete_por_favor_a1 PYTHON=.venv/bin/python make test
PROJECT=un_billete_por_favor_a1 PYTHON=.venv/bin/python make lint-spanish
PROJECT=un_billete_por_favor_a1 PYTHON=.venv/bin/python make preview-cards
PROJECT=un_billete_por_favor_a1 PYTHON=.venv/bin/python make publish-cards
PROJECT=un_billete_por_favor_a1 PYTHON=.venv/bin/python make verify
```

Successful output characteristics:
- 36 segments, 30 dialogue lines, 4 block headers, 6 chapters.
- Duration: `293.5s`.
- Verify: H.264/yuv420p, 1280x720, 30fps, AAC stereo 44100 Hz, audio duration `293.5s`, `ok: true`.
- A `decision log not found` warning during publish is non-blocking.

## Contact sheet QA command
Use representative frames that include the actual outro near the end. A first pass using frame `7200` did not reach the outro in a ~293.5s/30fps video; `8520` did.

```sh
mkdir -p output/qa/un-billete-por-favor-v1
ffmpeg -y -loglevel error \
  -i output/publish/frases-a1-ep10-un-billete-por-favor-16x9-v1.mp4 \
  -vf "select='eq(n,0)+eq(n,360)+eq(n,900)+eq(n,1440)+eq(n,2160)+eq(n,2880)+eq(n,3960)+eq(n,5040)+eq(n,8520)',scale=320:180,tile=3x3" \
  -frames:v 1 output/qa/un-billete-por-favor-v1/contact-sheet.jpg
```

QA passed: Spanish and Korean were readable, Hangul rendered, portrait placement was acceptable, no clipping/overlap, intro/outro readable, and thumbnail text/scene were clear with no accidental readable generated text or logo.
