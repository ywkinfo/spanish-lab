# Ep.13 `Quiero volver` thumbnail-first reference

Session context: After Ep.12 `¿Qué tal el viaje?`, Peter asked to discuss Ep.13 direction, then explicitly asked to present the thumbnail shape first and approved creating a thumbnail draft before any script/video production.

## Continuity decision
The strongest Ep.13 visual bridge from Ep.12 is the line already spoken near the end of Ep.12:

- Ep.12: Jin returns from a Toledo trip and says `Quiero volver.`
- Ep.13 thumbnail: make `Quiero volver` the visible promise, with Korean `다시 가고 싶어` and learning point `Quiero + 동사원형`.

This avoids reverting to the previously rejected Shorts/plain-card feel and keeps the established A1 story-card continuity.

## Approved thumbnail concept shape
Use the Ep.7-style family:

- 1280x720 YouTube thumbnail.
- Left side: large cream rounded rectangle panel.
- Top badge: coral pill `Español A1 · Ep.13`.
- Main title: large white Spanish text with thick dark stroke, split as:
  - `Quiero`
  - `volver`
- Korean pill: `다시 가고 싶어`.
- Teal learning-point pill: `Quiero + 동사원형`.
- Right side: warm travel-aftertalk scene with Jin showing travel photos on a phone while Lucía and Diego react warmly.
- Background cues: Toledo-style arches/city view, train or station café, travel items such as ticket, camera, suitcase.
- No readable signs/logos/watermarks/numbers. Full heads/hair visible.

## Source-art prompt shape used
```text
Warm modern semi-flat YouTube thumbnail illustration for a Korean Spanish learning channel. A cozy travel-aftertalk scene in Spain, inspired by Toledo. On the right side, three friendly recurring characters: Jin, a Korean A1 Spanish learner with a small backpack, showing travel photos on his phone; Lucía, smiling warmly; Diego, gesturing like a friendly teacher. They are near a café table with subtle travel items like a train ticket, camera, and small suitcase. Background hints of Toledo-style arches or a Spanish train-station café, warm afternoon light. Leave the left 45 percent of the image clean and slightly darker for text overlay. No readable text, no logos, no watermark, no numbers. All characters' full heads and hair visible, clear friendly faces, clean composition, bright warm colors, 16:9.
```

## Draft paths from the session
- Generated source art cache: `/opt/data/cache/images/openai_codex_gpt-image-2-medium_20260518_070827_221c0e76.png`
- Canonical source art: `assets/generated/ep13-quiero-volver-source.png`
- Repo thumbnail draft: `thumbs/a1-quiero-volver.jpg`
- Output thumbnail draft: `output/thumbs/frases-a1-ep13-quiero-volver.jpg`
- QA preview: `output/qa/ep13-quiero-volver/thumbnail-draft.jpg`

## Composition technique notes
- Use Pillow in the repo venv (`.venv/bin/python`) because system Python may not include Pillow.
- For Ep.7-style composition, create a blurred/darkened full-bleed background, paste the clear scene directly on the right, then draw the cream left panel and text overlays.
- When pasting a scene with a separate gradient mask, use `canvas.paste(scene, (x, y), mask)` rather than `alpha_composite(..., mask)`, because Pillow `alpha_composite` does not accept a separate mask argument.
- Save both repo and output thumbnail paths so future video package artifacts remain in sync.

## QA checks before handoff
- Spanish and Korean text readable at thumbnail size.
- Hangul renders correctly.
- No clipping/overlap in badge/title/pills.
- Jin/Lucía/Diego heads and hair visible.
- No accidental readable text/logos/watermarks.
- Visual communicates travel follow-up + “I want to go back” through phone photos, Toledo/train cues, and warm reactions.

## Handoff wording
State clearly that only the thumbnail draft was made: no script, video render, or external upload. Deliver the QA preview with `MEDIA:/opt/data/repos/spanish-lab/output/qa/ep13-quiero-volver/thumbnail-draft.jpg` when available.