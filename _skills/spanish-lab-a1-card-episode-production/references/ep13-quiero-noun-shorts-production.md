# Ep.13 `Quiero + 명사` / Candidate A Shorts-style card production

Session-specific reference for turning an approved daily Candidate A Shorts draft into a reviewable Spanish Lab A1 video package.

## Context
- Candidate A package existed under `/opt/data/content/lessons/a1-quiero-noun.md` and related `/opt/data/youtube/*` + `/opt/data/data/*` files.
- Peter approved production and requested Spain/mainland + Latin American variants shown together.
- Final product was a **manual-review video package**, not an external post/upload.

## Project shape used
- Repo: `/opt/data/repos/spanish-lab`
- Module: `projects/quiero_noun_a1.py`
- Source: `a1-quiero-noun/descrip.md`
- `OUTPUT_NAME = "quiero-noun"`
- `PUBLIC_SLUG = "a1-quiero-noun"`
- `SERIES = "frases-a1"`
- `EPISODE = 13`
- `LEVEL = "A1"`
- `RENDER_TYPE = "cards"`

## Learning point and variant handling
Keep exactly one learning point:

```text
Quiero + noun/noun phrase = “I want ~ / ~ 주세요”
```

Regional vocabulary should be a small side-by-side note, not a second grammar point:

```text
Spain: Quiero un billete.
Latin America: Quiero un boleto.
```

For card source rows, use simple pipe rows with the variant note in Korean/example columns rather than adding prose:

```text
4 | Quiero un billete. | 표 한 장 주세요. 스페인 본토 | En España: Quiero un billete.
5 | Quiero un boleto. | 표 한 장 주세요. 라틴아메리카 | En América Latina: Quiero un boleto.
```

## Duration/TTS pitfall
A short-card script with 8s phrase cards was too tight for Edge TTS once example lines and repeat pauses were included. Render failed with TTS-overlap errors on every phrase and the outro.

Fix used:
- phrase cards: `duration_s = 10.0`, `repeat_pause_s = 0.75`
- outro: `duration_s = 14.0`
- final duration: 73s

Use this as a starting point for Shorts-style A1 card videos that include examples or regional notes. Keep cards shorter only if TTS fit has been verified.

## Commands that passed
```sh
.venv/bin/python -m py_compile projects/quiero_noun_a1.py
PROJECT=quiero_noun_a1 PYTHON=.venv/bin/python make check
PROJECT=quiero_noun_a1 PYTHON=.venv/bin/python make test
PROJECT=quiero_noun_a1 PYTHON=.venv/bin/python make lint-spanish
PROJECT=quiero_noun_a1 PYTHON=.venv/bin/python make publish-cards
PROJECT=quiero_noun_a1 PYTHON=.venv/bin/python make verify
```

`make check` initially warned that the old TTS manifest did not match segment count; after rendering, rerunning `make check` had no warnings.

## Output artifacts
```text
output/publish/frases-a1-ep13-quiero-noun-16x9-v1.mp4
output/thumbs/frases-a1-ep13-quiero-noun.jpg
output/meta/frases-a1-ep13-quiero-noun-16x9-v1.json
output/meta/frases-a1-ep13-quiero-noun-16x9-v1.md
output/qa/quiero-noun/final-contact-sheet.jpg
```

Technical verify result:
- 1280x720
- 30fps
- duration 73.0s
- AAC audio, 44.1kHz
- audio duration 73.0s
- `ok: true`

## QA contact sheet for ~73s cards
Useful frame numbers for a 73s / 30fps card video:

```sh
mkdir -p output/qa/quiero-noun
ffmpeg -y -loglevel error \
  -i output/publish/frases-a1-ep13-quiero-noun-16x9-v1.mp4 \
  -vf "select='eq(n,0)+eq(n,210)+eq(n,360)+eq(n,660)+eq(n,960)+eq(n,1260)+eq(n,1560)+eq(n,1920)+eq(n,2160)',scale=320:180,tile=3x3" \
  -frames:v 1 output/qa/quiero-noun/final-contact-sheet.jpg
```

QA findings from contact sheet:
- Spanish text readable.
- Hangul rendered correctly.
- `billete` and `boleto` variants visible.
- No obvious clipping/overlap.

## Handoff wording
Report as a review package, not as published content. Include `MEDIA:` for the MP4 and contact sheet when available, plus exact paths for video, thumbnail, metadata, description, source, and project module.