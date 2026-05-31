# Ep.14 `Voy a practicar` thumbnail-first reference

Session context: After consulting Ep.13 `Quiero volver`, Peter approved moving into thumbnail production for Ep.14. The selected continuity bridge was Ep.13's desire line (`quiero aprender más`) becoming a concrete near-future plan with `Voy a + infinitivo`.

## Continuity decision
Ep.13 ends with Jin saying he wants to learn more. For Ep.14, the strongest next visible hook is:

- Core learning point: `Voy a + infinitivo` = `~할 거야 / ~할 예정이야`
- Public hook: `Voy a practicar`
- Korean hook: `연습할 거야`
- Thumbnail grammar pill: `Voy a + 동사원형`

This keeps the A1 ladder logical: `Quiero + infinitivo` (wanting) → `Voy a + infinitivo` (planning). Do not pivot to unrelated topics unless Peter explicitly requests it.

## Thumbnail concept shape
Use the established Ep.7-style family:

- 1280x720 YouTube thumbnail.
- Left side: cream rounded rectangle panel with soft shadow.
- Badge: coral pill `Español A1 · Ep.14`.
- Main title: large white Spanish text with thick dark stroke, split as:
  - `Voy a`
  - `practicar`
- Korean white pill: `연습할 거야`.
- Teal grammar pill: `Voy a + 동사원형`.
- Right side: warm Spanish study-café / small desk scene after the trip, with Jin motivated, Lucía encouraging, Diego pointing to a simple practice plan; include subtle Toledo/travel memory cues such as phone photos, train ticket, camera, notebook.
- Avoid readable random text, logos, watermarks, numbers, and cropped heads/hair.

## Source-art prompt used
```text
Warm modern semi-flat YouTube thumbnail illustration for a Korean Spanish learning channel. A cozy Spanish study-café scene after a trip. On the right side, three friendly recurring characters: Jin, a Korean A1 Spanish learner with a notebook and phone photos open, looking motivated; Lucía smiling warmly and encouraging him; Diego pointing to a simple practice plan on the table like a friendly teacher. Subtle travel memory cues from Toledo: small train ticket, camera, travel photos, and notebook, but the focus is now on making a study plan for tomorrow. Leave the left 45 percent of the image clean and slightly darker for text overlay. Warm afternoon light, bright clean colors, friendly faces, full heads and hair visible, no cropped heads. No readable text, no logos, no watermark, no numbers, no random letters. 16:9 composition.
```

## Draft paths from the session
- Generated source art cache: `/opt/data/cache/images/openai_codex_gpt-image-2-medium_20260518_183920_8169d6d5.png`
- Canonical source art: `assets/generated/ep14-voy-a-practicar-source.png`
- Composition script: `scripts/compose_ep14_thumbnail_draft.py`
- Repo thumbnail: `thumbs/a1-voy-a-practicar.jpg`
- Output thumbnail: `output/thumbs/frases-a1-ep14-voy-a-practicar.jpg`
- QA preview: `output/qa/ep14-voy-a-practicar/thumbnail-draft.jpg`

## Composition notes
- The image provider returned a landscape image that was not exactly 16:9 (`1536x1024`); compose/crop it to 1280x720 with right-side focus rather than assuming exact aspect ratio.
- Create a blurred/darkened full-bleed background, paste a clear right-side scene directly onto it, then draw the cream left panel and text overlays.
- Save both the repo thumbnail and output thumbnail so future publish artifacts stay in sync.

## QA checks passed
- Spanish title and Korean text readable at thumbnail size.
- Hangul renders correctly; no tofu boxes observed.
- Badge/title/pills remain inside the left panel with no major clipping/overlap.
- Jin/Lucía/Diego are visible on the right; heads/hair are not cropped.
- No obvious watermark/logo/large accidental text observed.
- The visual communicates study/practice planning after the trip.

## Handoff wording
State clearly that only the thumbnail draft was made: no full script, no video render, no external upload. Deliver the QA preview with:

```text
MEDIA:/opt/data/repos/spanish-lab/output/qa/ep14-voy-a-practicar/thumbnail-draft.jpg
```
