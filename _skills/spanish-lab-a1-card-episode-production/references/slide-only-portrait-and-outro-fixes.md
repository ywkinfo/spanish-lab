# Slide-only portrait and outro fixes

Use when the user asks to revise only a specific still/slide area and says not to touch the video.

## Lucía-only circular portrait candidate
Problem observed: the circular Lucía portrait showed coffee/table/card clutter and did not make Lucía the sole centered subject.

Reusable approach:
1. Do not alter `projects/<module>.py`, `CHARACTERS`, or rendered videos yet.
2. Crop the source scene around Lucía only, excluding table objects as much as possible.
3. Save a reusable square asset, e.g.:
   ```text
   assets/generated/lucia-cafe-bill-lucia-centered-portrait.png
   ```
4. Save a circular framed QA preview under:
   ```text
   output/qa/<slug>/lucia-centered-portrait-preview.png
   ```
5. Verify that Lucía is centered, head/upper body are natural, and coffee/card/table clutter is absent before applying it to the project.

Concrete Ep.8 crop from `assets/generated/lucia-cafe-bill-thumbnail-source.png` (1536x1024):
```python
CROP = (800, 24, 1500, 724)  # left, top, right, bottom
```
Resize that crop to 1024x1024 for the candidate asset.

## Outro Spanish/Korean overlap
Problem observed: Ep.8 outro slide had a long Spanish wrap-up sentence; the final word `lugar` wrapped down into the Korean outro line.

Fix options before rerendering:
- Create a still-only QA slide first.
- Reduce Spanish body font size or max lines.
- Move the Spanish body block upward.
- Shorten or manually break the Spanish text so the last line ends well above the Korean line.
- Keep at least ~35–50 px vertical separation above the Korean text at y≈590–610.

Only after approval should the renderer/project be patched and the episode rerendered.
