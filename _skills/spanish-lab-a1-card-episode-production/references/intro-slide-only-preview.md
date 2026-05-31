# Intro slide-only preview fixes

Use when a user flags a problem on the first/intro slide but explicitly says not to touch the video.

## Problem pattern
- Intro slide uses `intro_scene_image_path` and the renderer's left image panel uses cover-crop behavior.
- For wide/character scene art, cover-crop can cut off the character's body near the vertical divider.
- Long intro titles can approach the right edge; glyph overhang (for example the final `r` in `favor`) can appear clipped in screenshots or video frames.

## Safe response pattern
1. Do **not** rerender the episode video or publish artifacts yet.
2. Generate a standalone still preview under `output/qa/<slug>/`, for example `intro-slide-fixed.png`.
3. For the scene panel, use a contain-fit foreground image rather than pure cover-crop:
   - optional blurred cover background to avoid empty margins;
   - foreground image scaled with `min(panel_w/src_w, panel_h/src_h)`;
   - leave 20-40 px safe margins around the foreground image;
   - rounded mask/shadow is OK if it does not reintroduce cropping.
4. For intro title text, measure/wrap with `ImageDraw.textbbox` against the text column width instead of assuming one line always fits.
5. Verify the still visually before showing it:
   - full character/body visible;
   - title fully visible including final glyphs;
   - Korean text is readable and not tofu;
   - the generated file is a still preview, not a changed video.
6. Show the still with `MEDIA:/absolute/path`, and state clearly that the video was not touched.

## Implementation note
If the user approves the still, then patch `build/render_cards.py` or project-level design settings and rerender/publish/verify in the normal pipeline. Until approval, keep changes isolated to QA preview files or a throwaway script.
