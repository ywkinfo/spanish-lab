# Ep.23 `Nunca + presente` thumbnail workflow

Use this as a thumbnail-first reference for A1+ frequency/routine episodes after Ep.21 `a veces` and Ep.22 `siempre`.

## Continuity decision
- Previous frequency/routine sequence:
  - Ep.21: `A veces + presente` / occasional routine.
  - Ep.22: `Siempre + presente` / fixed routine.
- Natural next step: complete the frequency contrast with `nunca + presente`.
- Thumbnail learning point: `Nunca + presente`.
- Core phrase: `Nunca tomo café por la noche.`
- Status in the source session: thumbnail-only production; no episode module or full video files were created.

## Source image direction
Generate a direct 16:9/landscape source image when possible:
- right side: Jin in a cozy Madrid apartment kitchen or café corner at night/late evening;
- visual action: Jin gently pushes away or avoids a cup of coffee;
- table details: notebook and Spanish flashcards are acceptable, but avoid readable text;
- background: warm lamp light plus subtle dark-blue night window;
- left 45%: clean negative space for overlay;
- no readable text/logos/watermarks;
- no cropped head/hair/hands;
- keep the visual focused on “I don’t drink coffee at night,” not a second grammar point.

Prompt pattern used:
```text
Create a warm, clean 16:9 YouTube thumbnail background image for a Korean beginner Spanish lesson, Spanish Lab style. Scene: a cozy Madrid apartment kitchen or small café corner at night / late evening. On the RIGHT side, show a friendly Korean adult learner named Jin gently pushing away or avoiding a cup of coffee, with a notebook and Spanish flashcards on the table, calm study mood, warm lamp light and soft dark blue evening window. The visual idea is: “I don’t drink coffee at night.” The LEFT 45% of the image must be clean negative space with soft warm background only, no objects blocking it, for large title overlay. Modern semi-realistic illustration, bright but not noisy, clean shapes, warm cream/coral/teal palette with subtle night-blue accents, no readable text, no logos, no watermarks, no cropped heads, no extra fingers, no clutter.
```

## Overlay copy
Ep.7-style thumbnail overlay:
- badge: `Español A1+ · Ep.23`
- main title: `Nunca`
- subtitle: `tomo café` / `por la noche`
- Korean pill: `밤에는 커피 안 마셔요`
- teal pill: `절대 안 해요 = Nunca`
- footer note: `Nunca + 현재형`

## Paths used
- source image: `images/ep23-nunca-tomo-cafe-source.png`
- repo thumbnail: `thumbs/a1-ep23-nunca-tomo-cafe.jpg`
- publish thumbnail: `output/thumbs/frases-a1-ep23-nunca-tomo-cafe.jpg`
- QA thumbnail: `output/qa/nunca-tomo-cafe/thumbnail.jpg`
- generation script: `scripts/create_ep23_thumbnail.py`
- prompt archive: `/opt/data/prompts/image-generation/ep23-nunca-thumbnail-prompt.md`

## QA checklist
- Confirm all image outputs are 1280x720.
- Run visual QA on both source and finished overlay.
- Source QA: clean left space, Jin/coffee/avoidance gesture visible, no fake readable text/logos, no cropped head/hands.
- Finished QA: Spanish/Korean readable, no clipping/overlap, balanced left panel/right character composition, coffee and hand gesture remain visible.
- If Peter only asks for thumbnail production, do not create or modify episode modules/full video files yet.
- Do not externally publish.
