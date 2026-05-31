# Spanish Lab Ep.7-style thumbnail pattern

Use when the user asks for a later episode thumbnail to match Ep.7 as closely as possible.

## Visual target
- 1280x720 YouTube thumbnail.
- Full-bleed warm café/image background, blurred and slightly darkened.
- Right side: large scene image directly composited, not inside a separate white card/frame. Preserve the character's full head/hair and key table objects.
- Left side: large cream rounded rectangle panel with soft shadow.
- Top of panel: coral rounded pill badge, e.g. `Español A1 · Ep.N`.
- Main Spanish title: very large bold white lettering with thick black stroke, split into short lines.
- Korean topic: black Hangul inside a white rounded pill.
- Bottom callout: teal rounded pill with a short high-value Spanish phrase.

## Implementation notes
- Prefer regenerating the final thumbnail from the approved source image with Pillow rather than only changing project metadata.
- Update both repo thumbnail and publish thumbnail paths, e.g.:
  - `thumbs/a1-<slug>.jpg`
  - `output/thumbs/frases-a1-epNN-<slug>.jpg`
- Use measured text bounding boxes or generous fixed pill widths so Korean/Spanish never clips.
- For source images wider than 1:1, crop the right-side image around the character with a high x-focus (around 0.7-0.8) and mid y-focus. For 1:1 source art, crop/scale so the head is fully visible.
- Verify with visual QA that Spanish/Korean text is readable, Hangul renders, there is no overlap, and character hair/head is not cropped.

## Example from Ep.8 revision
Ep.8 was revised to match Ep.7 by replacing a two-card layout with: cream left panel, coral badge, outlined `La cuenta, por favor`, Korean white pill `카페에서 계산하기`, teal phrase pill `¿Cuánto es?`, and a large right-side Lucía café/payment scene without a separate image card.