# Ep.10 metro ticket thumbnail notes

Session-specific guidance for the A1 Ep.10 `Un billete, por favor` thumbnail and similar ticket-buying/travel episodes.

## Scenario and continuity
- Continue directly from Ep.9: Jin, Lucía, and Diego have reached the Madrid metro and Jin now needs to buy a ticket.
- Strong visual concept: inside a Madrid metro station at a ticket machine. Jin looks curious/slightly nervous, Lucía points to the machine screen, and Diego smiles while holding a small ticket/card.
- Keep display character names from Ep.8 onward: Jin, Lucía, Diego.

## Source art prompt pattern
Use a landscape source image with the scene/trio on the right and clean negative space on the left:

> A clean, warm, modern illustration for a Spanish Lab A1 YouTube thumbnail. Scene: inside a Madrid metro station near a ticket machine. Three friendly young adults are standing on the right side: Jin, a Korean learner, looks at the ticket machine with a curious and slightly nervous expression; Lucía, a friendly Spanish woman, points gently at the ticket machine screen and helps him buy a metro ticket; Diego stands nearby smiling and holding a small metro ticket or travel card. The scene clearly suggests buying a metro ticket in Spain. Warm beige, coral, teal, and soft blue palette, clean vector-like digital illustration, polished educational YouTube thumbnail style, high contrast. Leave clear empty space on the left side for large title text overlay. No text, no letters, no numbers, no logos, no watermark, no readable signs, no real metro branding. Preserve full heads and hair, friendly expressions, clean composition, not cluttered.

Negative prompt / cautions:
```text
No readable text, no logos, no brand marks, no real metro logo, no watermark, no distorted hands, no cropped heads, no scary expressions, no cluttered background, no tiny unreadable ticket machine details.
```

## Ep.7/Ep.8/Ep.9-style thumbnail composition
Recommended final overlay:
- left cream rounded panel with shadow;
- coral badge: `Español A1 · Ep.10`;
- large outlined title split across two lines: `Un billete,` / `por favor`;
- Korean white pill: `지하철표 사기`;
- teal bottom pill: `¿Cuánto cuesta?`.

Known paths used in the first Ep.10 thumbnail draft:
- Source art: `assets/generated/metro-ticket-thumbnail-source.png`
- Repo thumbnail: `thumbs/a1-un-billete-por-favor.jpg`
- Publish thumbnail: `output/thumbs/frases-a1-ep10-un-billete-por-favor.jpg`
- QA thumbnail: `output/qa/un-billete-por-favor-v0/thumbnail.jpg`
- Composition script: `scripts/make_ep10_thumbnail_ep7_style.py`

## QA criteria
- Spanish and Korean text are readable at thumbnail size; Hangul renders correctly.
- Main title and `¿Cuánto cuesta?` pill are not clipped.
- Three-character ticket-machine scene is still visible; the title panel may cover bodies but not faces or the core interaction.
- Character heads/hair are not cropped.
- No readable accidental generated text, logos, brand marks, or watermark.
