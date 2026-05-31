---
name: historia-new
description: Initialize and plan a new Spanish Lab long-form 'historia-a1' diary project from template, including story planning, visual sizing, and 3-layer SFX configuration.
---

# Skill: Creating a New Historia Diary Episode (`historia-new`)

This skill defines the turnkey workflow for authoring a new long-form mini-story episode (`RENDER_TYPE = "diary"`) in the Spanish Lab repository.

## Execution Trigger
To start a new episode, provide the episode ID, series slug, and topic:
```bash
# Example: Create ep02-lucia-finds-keys.py about Lucía finding her keys in Madrid
```

## Step-by-Step Workflow

### 1. Initialize from Template
- Copy `projects/_template_historia_diary.py` to `projects/<series_slug>_ep<num>_<topic_slug>.py`.
- Fill in metadata fields: `OUTPUT_NAME`, `PUBLIC_SLUG`, `YOUTUBE_TITLE`, `DESCRIPTION_INTRO`, etc.
- Set `STATUS = "draft"` in the module docstring. Keep `RENDER_TYPE = "diary"`.

### 2. Story Planning & Scripting
- Create 8 detailed scenes in `STORY_SCENES`.
- Each scene must carry A1/A2 Spanish comprehensible narration and dialogues using vocabulary blocks, with corresponding Korean translations.
- Set transition timings: `pause_s` should be 2.0s to 5.0s depending on the scene ending.
- Ensure duration bounds: The estimated duration of all lines in a scene + the scene `pause_s` should ideally sit between **45s and 105s** (the validator will warn if outside this range).

### 3. Visual Sourcing & Safe Area Constraints
- Set `image_path` for each scene (native 16:9 aspect, resolution **≥ 1600x900**, ideal 1920x1080).
- **Caption Safe Area**: The dynamic caption panel draws at the bottom center. Ensure critical visual props (like Lucía's blue notebook or phone messages) and faces reside in the **top 65%** of the canvas.

### 4. Audio & 3-Layer SFX Sourcing
- Set `ambient_sfx` loop beds (Layer 1) for scenes, registering licenses in `assets/audio/LICENSE.md`.
- Wire spot effects in `SFX_MANIFEST` (Layer 2) anchored to specific scene line indexes.
- Wire structural segment beds in `SEGMENT_SFX` (Layer 3) to fill the gaps in `intro`, `montage`, and `outro`.
- Ensure no silent wav files are used (gate blocks peak ≤ -50 dBFS).

### 5. Review and Approval Gate
- Run `PROJECT=<module> make check` to static-validate.
- Run `PROJECT=<module> make test` to run test suites.
- Obtain explicit linguist review on all Spanish/Korean scripts. Once approved, update the module header to **approved** status.
- **Do not proceed to final render or publish until approved status is active.**
