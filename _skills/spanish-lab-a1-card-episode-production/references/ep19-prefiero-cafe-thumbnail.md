# Ep.19 `Prefiero café` thumbnail-first reference

Use this as a concrete example when Peter asks to make a Spanish Lab A1/A1+ thumbnail before full episode production.

## Context
- Episode: Ep.19
- Working title: `Prefiero café`
- Korean title/pill: `저는 커피가 더 좋아요`
- CEFR: A1+
- One learning point: `Prefiero + noun` for expressing a simple preference between options.
- Continuity: follows Ep.18 `Me gusta + noun, pero...`; Jin is tired/hot in Madrid and chooses between coffee and tea in a café.

## Thumbnail source-art prompt pattern
Generate a 16:9 landscape image directly, not a square crop, with:
- Jin, Lucía, and Diego in a cozy Madrid café near a sunny plaza;
- Jin looking slightly tired but smiling and choosing a drink;
- visible coffee and tea cups to support the `¿Café o té?` choice;
- warm Spanish café atmosphere, soft late-morning light, modern semi-realistic educational style;
- characters and scene interest on the RIGHT half;
- clean warm blurred/soft negative space on the LEFT for overlay;
- no readable text/signs/logos/watermarks and no cropped heads/hair.

A successful source generated in this session was saved as:

```text
images/ep19-prefiero-cafe-source.png
```

## Ep.7-style overlay copy
- Coral badge: `Español A1+ · Ep.19`
- Main Spanish title, large white with black stroke: `Prefiero` / `café`
- Korean white pill: `저는 커피가 더 좋아요`
- Teal callout pill: `¿Café o té?`
- Small learning-point footer: `Prefiero + 명사`

## Manual composition notes
The generated source was 1536x1024, so crop to 16:9 while preserving all heads/hair before resizing to 1280x720. A robust layout:
- blurred/dimmed full-bleed background;
- composite a sharper version back in with a left-to-right alpha mask so the right-side people/table stay crisp;
- large cream rounded panel on the left, with badge, large title, Korean pill, teal callout, and small footer;
- use Noto Sans KR fonts from `assets/fonts/` for Korean text.

## Output paths used
```text
thumbs/a1-ep19-prefiero-cafe.jpg
output/thumbs/frases-a1-ep19-prefiero-cafe.jpg
```

## QA criteria
Verify before handoff:
- thumbnail is 1280x720 RGB;
- Hangul and Spanish text are readable;
- no text clipping or overlap;
- layout matches Ep.7-style: cream left panel, coral badge, large Spanish title, Korean pill, teal callout, right-side scene;
- all character heads/hair remain uncropped;
- no accidental readable background text/logos;
- no external posting/upload performed.
