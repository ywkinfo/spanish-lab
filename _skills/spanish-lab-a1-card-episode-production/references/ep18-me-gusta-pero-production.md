# Ep.18 `Me gusta, pero...` production reference

Use as a reference for future Spanish Lab A1+/A2- story-card episodes that raise difficulty while preserving exactly one learning point.

## Continuity / duplicate-avoidance lesson
- Peter rejected `¿Cuánto cuesta?` for Ep.18 because it had already been used prominently in earlier episodes (especially Ep.6, also price elements in Ep.5/Ep.10).
- Before proposing a next episode idea, search existing project/meta artifacts for the proposed phrase or chapter label, not only the immediately previous episode.
- If a phrase has appeared before, either pivot to a new learning point or explicitly frame it as a review/synthesis episode and get Peter's approval.

## Episode direction
- Module/slug: `me_gusta_pero_a1` / `me-gusta-pero`
- Episode: `EPISODE = 18`, `LEVEL = "A1+"`, `RENDER_TYPE = "cards"`
- One learning point: `Me gusta + noun, pero...`
- Difficulty intent: Peter liked `gustar` but asked to raise the overall content difficulty. The solution was not to add multiple grammar points, but to extend basic `Me gusta` into a small opinion pattern: `Me gusta la chaqueta, pero hace calor.`
- Continuity: Ep.17 clothing (`Llevo una chaqueta`) naturally leads to asking whether Jin likes the jacket, then adding a simple contrast with weather/crowds.

## Thumbnail-first workflow
When Peter asks for the thumbnail first:
1. Generate a 16:9 source image directly with characters/scene on the right and clean left negative space.
2. Compose an Ep.7-style thumbnail overlay:
   - coral badge: `Español A1+ · Ep.18`
   - large Spanish title: `Me gusta, pero...`
   - Korean pill: `좋아요, 그런데...`
   - teal callout: `Me gusta, pero hace calor`
3. Save both repo and output thumbnail paths before full video production:
   - `thumbs/a1-ep18-me-gusta-pero.jpg`
   - `output/thumbs/frases-a1-ep18-me-gusta-pero.jpg`
4. Run visual QA for Hangul rendering, text clipping, character head/hair cropping, and accidental readable text/logos.

## Production shape used
- Full A1+ story-card episode, about 5 minutes.
- 30 dialogue lines, 4 blocks, intro and outro.
- Blocks:
  1. `¿Te gusta?`
  2. `Me gusta, pero...`
  3. `Me gusta Madrid`
  4. `Mini prueba`
- Keep examples within the one learning point. `A mí también`, `hay mucha gente`, and `hace calor` appear only as support for the opinion pattern, not as separate teaching points.

## Useful validation chain
```sh
PROJECT=me_gusta_pero_a1 PYTHON=.venv/bin/python make check
PROJECT=me_gusta_pero_a1 PYTHON=.venv/bin/python make test
PROJECT=me_gusta_pero_a1 PYTHON=.venv/bin/python make lint-spanish
PROJECT=me_gusta_pero_a1 PYTHON=.venv/bin/python make tts
PROJECT=me_gusta_pero_a1 PYTHON=.venv/bin/python make publish-cards
PROJECT=me_gusta_pero_a1 PYTHON=.venv/bin/python make verify
```

Generate a contact sheet from the publish artifact and visually confirm intro, block headers, dialogue cards, and outro:
```sh
mkdir -p output/qa/me-gusta-pero
ffmpeg -y -loglevel error \
  -i output/publish/frases-a1-ep18-me-gusta-pero-16x9-v1.mp4 \
  -vf "select='eq(n,0)+eq(n,420)+eq(n,900)+eq(n,1500)+eq(n,2700)+eq(n,4200)+eq(n,5700)+eq(n,7200)+eq(n,9000)',scale=320:180,tile=3x3" \
  -frames:v 1 output/qa/me-gusta-pero/final-contact-sheet-v1.jpg
```

## Delivered artifact pattern
- `projects/me_gusta_pero_a1.py`
- `a1-me-gusta-pero/descrip.md`
- `images/ep18-me-gusta-pero-source.png`
- `thumbs/a1-ep18-me-gusta-pero.jpg`
- `output/thumbs/frases-a1-ep18-me-gusta-pero.jpg`
- `output/publish/frases-a1-ep18-me-gusta-pero-16x9-v1.mp4`
- `output/meta/frases-a1-ep18-me-gusta-pero-16x9-v1.md`
- `output/meta/frases-a1-ep18-me-gusta-pero-16x9-v1.json`
- `output/qa/me-gusta-pero/final-contact-sheet-v1.jpg`
