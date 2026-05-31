# Ep.8 La cuenta continuity notes

Session-specific production guidance distilled from Ep.7 → Ep.8 planning.

## Continuity decisions
- Ep.8 continues directly from Ep.7's café image-description story.
- Use the Spanish Lab canonical brand BGM (`assets/audio/spanish-lab-brand-bgm.mp3`) rather than inventing a new sound identity.
- From Ep.8 onward, the Korean learner persona should be displayed as **Jin** instead of Peter. Legacy portrait asset filenames may remain `peter-profile.png`; change user-facing script/dialogue names.

## Ep.8 scenario
Working title: `La cuenta, por favor | Español A1 · Ep.8`.

Teaching function: ask for the bill, understand a simple total, pay, and close politely in a café.

Core phrases:
- `La cuenta, por favor.`
- `¿Cuánto es?`
- `Son cinco euros.`
- `Pago con tarjeta.`
- `Aquí tiene.`
- `Gracias.` / `De nada.`
- `Hasta luego.`

Recommended structure: 4 blocks, roughly 30 dialogue lines, 4–5 minutes, matching Ep.7's longer A1 story-card format.

## Thumbnail/source image direction
Create the thumbnail-source image before full episode implementation if the user asks for visual direction first.

Prompt pattern that worked:
> A clean, warm, modern illustration for a Spanish Lab A1 YouTube thumbnail. Scene: Lucía, a friendly young Spanish woman, seated at a small Spanish café table in warm morning light after coffee and tapas. On the table: an almost empty coffee cup, a small tapas plate, a simple blank receipt/bill, and a bank card, clearly suggesting “asking for the bill / paying at a café”. Lucía is visible from head to upper body with her full head and hair fully inside the frame, slightly on the right side, with enough empty space on the left for large title text to be added later. Cozy Spanish café background, soft beige and warm terracotta palette, clean vector-like digital illustration, polished educational YouTube thumbnail style, high contrast, no text, no letters, no numbers, no logos, no watermark, no readable writing on receipt.

Final thumbnail composition that worked:
- Use a blurred/darkened full-bleed background from the generated image.
- Put the generated source image inside a right-side rounded card so Lucía's head remains fully visible.
- Put a light rounded text panel on the left.
- Text stack: red episode badge, large Spanish title `La cuenta, por favor`, teal Korean pill `카페에서 계산하기`, then small phrase cue `¿Cuánto es? · Pago con tarjeta`.
- Size badge/pill widths from measured text bounds (`ImageDraw.textbbox`) to avoid clipped labels.
- Save both source thumbnail and publish thumbnail paths so handoff media matches publish artifacts: `thumbs/a1-la-cuenta.jpg` and `output/thumbs/frases-a1-ep08-la-cuenta.jpg`.

QA criteria:
- Lucía's head/hair fully visible, no crop.
- Left-side Spanish/Korean text readable and not overlapping the subject.
- Coffee/tapas plus receipt/card clearly signal café payment.
- No tofu boxes in Korean.
- No readable accidental text, logos, numbers, or watermark in generated art.
- Warm café mood and visual continuity with Ep.7.

## Ep.8 implementation outcome
- Module used: `projects/la_cuenta_a1.py`.
- Source rows: `a1-la-cuenta/descrip.md` with 30 dialogue lines.
- Learner display name: `Jin` throughout user-facing copy/dialogue; no `Peter` text in new Ep.8 files.
- Duration target matched Ep.7 style: 36 segments, 30 dialogue lines, 4 blocks, about 4m49s.
- Brand BGM reused via `assets/audio/spanish-lab-brand-bgm.mp3` with the quiet-draft settings (`bgm_volume_db=-4.0`, ducking on).
- Validation chain used: `make check`, `make test`, `make lint-spanish`, `make preview-cards`, `make publish-cards`, `make verify`.
- Video contact sheet QA should explicitly verify visible `Jin`, no tofu, no clipping/overlap, and acceptable character placement.
