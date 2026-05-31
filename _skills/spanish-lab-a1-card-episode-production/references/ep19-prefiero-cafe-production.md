# Ep.19 `Prefiero café` production reference

Use this as a reference for future Spanish Lab A1+ story-card episodes that start thumbnail-first and then move into full local video production.

## Episode direction
- Module/slug: `prefiero_cafe_a1` / `prefiero-cafe`
- Episode: `EPISODE = 19`, `LEVEL = "A1+"`, `RENDER_TYPE = "cards"`
- One learning point: `Prefiero + noun` for expressing a simple preference between options.
- Continuity: follows Ep.18 `Me gusta + noun, pero...` by moving from a small opinion to a simple choice/preference.
- Story context: Madrid is hot, Jin is tired, Lucía and Diego take him to a café. Jin chooses between coffee/tea, then between the park/café.

## Thumbnail-first workflow used
1. Generate a direct 16:9/landscape source image with the café scene and characters on the right, clean negative space on the left, no readable signs/logos/text, and uncropped heads.
2. Compose an Ep.7-style overlay:
   - coral badge: `Español A1+ · Ep.19`
   - main title: `Prefiero café`
   - Korean pill: `저는 커피가 더 좋아요`
   - teal callout: `¿Café o té?`
3. Save both repo and output thumbnail paths:
   - `thumbs/a1-ep19-prefiero-cafe.jpg`
   - `output/thumbs/frases-a1-ep19-prefiero-cafe.jpg`
4. Run visual QA before full production: Hangul readable, no clipping/overlap, no cropped heads/hair, no accidental readable background text.

## Production shape used
- Full A1+ story-card episode, about 4:49 / 289s.
- 30 dialogue lines, 4 blocks, intro and outro.
- Blocks:
  1. `Hace calor`
  2. `¿Café o té?`
  3. `Prefiero esta cafetería`
  4. `Mini prueba`
- Keep the episode centered on one learning point. `hace calor`, `¿por qué?`, and `Me gusta el parque, pero...` are continuity/support phrases, not additional teaching points.
- Core examples:
  - `Prefiero café.`
  - `Prefiero té.`
  - `Prefiero café con leche.`
  - `Prefiero esta cafetería.`
  - `Me gusta el parque, pero prefiero esta cafetería.`

## Useful validation chain
```sh
PROJECT=prefiero_cafe_a1 PYTHON=.venv/bin/python make check
PROJECT=prefiero_cafe_a1 PYTHON=.venv/bin/python make test
PROJECT=prefiero_cafe_a1 PYTHON=.venv/bin/python make lint-spanish
PROJECT=prefiero_cafe_a1 PYTHON=.venv/bin/python make tts
PROJECT=prefiero_cafe_a1 PYTHON=.venv/bin/python make publish-cards
PROJECT=prefiero_cafe_a1 PYTHON=.venv/bin/python make verify
```

After `make tts`, rerun `make check` so the TTS-fit validation runs without stale-manifest warnings.

Probe the final publish artifact with the project environment set:
```sh
PROJECT=prefiero_cafe_a1 PYTHON=.venv/bin/python \
  .venv/bin/python checks/probe_output.py \
  output/publish/frases-a1-ep19-prefiero-cafe-16x9-v1.mp4
```

Generate a contact sheet from the publish artifact and visually confirm intro, block headers, dialogue cards, and outro:
```sh
mkdir -p output/qa/prefiero-cafe
ffmpeg -y -loglevel error \
  -i output/publish/frases-a1-ep19-prefiero-cafe-16x9-v1.mp4 \
  -vf "select='eq(n,0)+eq(n,420)+eq(n,900)+eq(n,1500)+eq(n,2400)+eq(n,3600)+eq(n,5100)+eq(n,6900)+eq(n,8400)',scale=320:180,tile=3x3" \
  -frames:v 1 output/qa/prefiero-cafe/final-contact-sheet-v1.jpg
```

## Delivered artifact pattern
- `projects/prefiero_cafe_a1.py`
- `a1-prefiero-cafe/descrip.md`
- `images/ep19-prefiero-cafe-source.png`
- `thumbs/a1-ep19-prefiero-cafe.jpg`
- `output/thumbs/frases-a1-ep19-prefiero-cafe.jpg`
- `output/publish/frases-a1-ep19-prefiero-cafe-16x9-v1.mp4`
- `output/meta/frases-a1-ep19-prefiero-cafe-16x9-v1.md`
- `output/meta/frases-a1-ep19-prefiero-cafe-16x9-v1.json`
- `output/qa/prefiero-cafe/final-contact-sheet-v1.jpg`
