# Ep.27 `Hay una farmacia cerca` thumbnail precedent

Use as a thumbnail-first precedent for `Hay + noun` / nearby-place A1+ episodes.

## Direction
- Learning point: `Hay + 명사` = “~이 있어요”.
- Main phrase: `Hay una farmacia cerca.`
- Visual: warm Spanish city street near station/metro, green pharmacy cross, café/storefront context, Jin/Lucía/Diego on the right.
- Composition: Ep.7-style thumbnail with left cream panel and right-side scene; leave left 45% clean when generating source art.

## Overlay copy used
- Badge: `Español A1+ · Ep.27`
- Main title: `Hay una / farmacia / cerca`
- Korean pill: `근처에 약국이 있어요`
- Teal callout: `¿Hay una farmacia cerca?`

## Prompt/storage pattern
- Save the prompt under `/opt/data/prompts/image-generation/<slug>-thumbnail.md` with source image path and output targets.
- Update both:
  - repo thumbnail: `thumbs/a1-ep27-hay-una-farmacia-cerca.jpg`
  - publish thumbnail: `output/thumbs/frases-a1-ep27-hay-una-farmacia-cerca.jpg`

## Implementation notes
- The image tool may return a `landscape` file that is not true 16:9 (Ep.27 source was 1536x1024). Crop explicitly to 1280x720 before overlay.
- For right-side characters plus top-right sign, use a crop biased slightly right/top so the pharmacy cross and heads remain visible.
- Use a blurred/darkened full-bleed background plus a faded sharp right-side composite to keep text legible while preserving the scene.
- Measure every overlay with `ImageDraw.textbbox`. Long Spanish callouts can clip if the pill width is clamped after measuring at a larger font. Choose the smaller font first, then measure and draw the pill.
- Avoid adding small channel text at the bottom of the panel if vertical space is tight; it can collide with the panel border/shadow and is not necessary for the thumbnail.

## QA criteria
- 1280x720 final image.
- Main Spanish title and Korean pill readable with no clipping.
- Teal callout fully inside the panel.
- Pharmacy/station context visible.
- Character heads/hair not cropped.
- No fake readable text/logos/watermarks in the generated scene.
