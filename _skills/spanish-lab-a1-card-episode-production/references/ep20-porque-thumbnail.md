# Ep.20 `Porque tengo sueño` thumbnail-first reference

Use this when Peter asks to make a Spanish Lab A1+ thumbnail before full Ep.20-style episode production.

## Context
- Episode: Ep.20
- Working title: `Porque tengo sueño`
- Korean title/pill: `졸려서요`
- CEFR: A1+
- One learning point: `porque + short reason` for answering `¿Por qué?`.
- Continuity: follows Ep.18 `Me gusta, pero...` and Ep.19 `Prefiero café`; after choosing coffee, Jin explains the reason: `porque tengo sueño`.

## Thumbnail source-art prompt pattern
Generate a direct 16:9 landscape image, not a square crop, with:
- Jin, Lucía, and Diego in a cozy Madrid café;
- Jin sleepy but friendly, coffee cup visible;
- Lucía and Diego smiling/asking him a question;
- visual idea: “because I’m sleepy” / giving a reason;
- characters and café scene on the RIGHT half;
- clean warm blurred/soft negative space on the LEFT for overlay;
- no readable text, signs, logos, watermarks, cropped heads/hair, or clutter.

A successful source image in the session was saved as:

```text
images/ep20-porque-tengo-sueno-source.png
```

## Ep.7-style overlay copy
- Coral badge: `Español A1+ · Ep.20`
- Main Spanish title, large white with black stroke: `Porque` / `tengo` / `sueño`
- Korean white pill: `졸려서요`
- Teal callout pill: `¿Por qué?`
- Small footer: `porque + 이유`

## Composition notes
Use the established Ep.7-style thumbnail pattern:
- blurred/dimmed full-bleed background;
- sharper café scene composited on the right with a soft left-edge fade;
- large cream rounded text panel on the left;
- Noto Sans KR fonts for Korean text;
- crop/focus around the right side while preserving all heads/hair.

The implementation script created during this session was:

```text
scripts/create_ep20_thumbnail.py
```

## Output paths used
```text
thumbs/a1-ep20-porque-tengo-sueno.jpg
output/thumbs/frases-a1-ep20-porque-tengo-sueno.jpg
output/qa/porque-tengo-sueno/thumbnail.jpg
```

## QA criteria
Verify before handoff:
- thumbnail is 1280x720 RGB;
- Spanish and Korean text are readable;
- no clipping or overlap in badge/title/pills/footer;
- Ep.7-style layout is preserved: cream left panel, coral badge, large Spanish title, Korean pill, teal callout, right-side scene;
- character heads/hair are not cropped;
- no accidental readable background text/logos;
- source repo thumbnail and publish-output thumbnail are both updated;
- no external posting/upload performed.
