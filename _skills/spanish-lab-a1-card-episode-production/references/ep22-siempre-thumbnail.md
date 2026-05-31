# Ep.22 `Siempre + presente` thumbnail workflow

Use this as a concrete thumbnail-first reference for A1+ routine/frequency episodes after Ep.21 `A veces + presente`.

## Continuity decision
- Previous episode: Ep.21 `A veces me levanto temprano` (`a veces + presente`).
- Natural next step: contrast occasional routine with stable routine using `siempre + presente`.
- Approved/used thumbnail learning point: `Siempre + presente`.
- Core phrase: `Siempre tomo café por la mañana.`

## Source image direction
Generate a direct 16:9/landscape source image rather than a square crop when possible:
- right side: Jin, coffee cup, morning study/café or Madrid apartment mood;
- left 45%: clean negative space for overlay;
- warm Spanish Lab palette: cream/coral/teal;
- no readable text/logos/watermarks;
- no cropped head/hair/hands;
- keep narration clarity in mind later: visual should suggest routine, not add extra grammar points.

Prompt pattern used:
```text
Create a warm, clean 16:9 YouTube thumbnail background image for a Korean beginner Spanish lesson, Spanish Lab style. Scene: a cozy Madrid apartment kitchen or small sunny café table in the morning. On the RIGHT side, show a friendly Korean adult learner named Jin holding a coffee cup, with soft morning sunlight, a notebook and Spanish flashcards on the table, calm study mood. Optional subtle silhouettes or small portraits of two friendly Spanish-speaking guides in the background, but keep Jin and the coffee as the focus. The LEFT 45% of the image must be clean negative space with soft warm background only, no objects blocking it, for large title overlay. Modern semi-realistic illustration, bright but not noisy, clean shapes, warm cream/coral/teal palette, no readable text, no logos, no watermarks, no cropped heads, no extra fingers, no clutter.
```

## Overlay copy
Ep.7-style thumbnail overlay:
- badge: `Español A1+ · Ep.22`
- main title: `Siempre`
- subtitle: `tomo café` / `por la mañana`
- Korean pill: `항상 커피 마셔요`
- teal pill: `항상 = Siempre`
- footer note: `Siempre + 현재형`

Note: the first Korean pill draft `항상 아침에 커피` was readable but felt incomplete, so revise thumbnail Korean copy toward a complete learner-facing phrase when there is room.

## Paths used
- source image: `images/ep22-siempre-tomo-cafe-source.png`
- repo thumbnail: `thumbs/a1-ep22-siempre-tomo-cafe.jpg`
- publish thumbnail: `output/thumbs/frases-a1-ep22-siempre-tomo-cafe.jpg`
- QA thumbnail: `output/qa/siempre-tomo-cafe/thumbnail.jpg`
- generation script: `scripts/create_ep22_thumbnail.py`
- prompt archive: `/opt/data/prompts/image-generation/ep22-siempre-thumbnail-prompt.md`

## QA checklist
- Confirm all image outputs are 1280x720.
- Run visual QA on both the source and the finished overlay.
- Source QA: left text space, Jin/coffee visible, no distracting fake text/logos, no malformed hands/head crops.
- Finished QA: Spanish/Korean readability, Hangul rendering, no clipping/overlap, balanced panel, Jin/coffee still clear.
- Do not create episode module or full video files when Peter only asks for thumbnail production.
- Do not externally publish.
