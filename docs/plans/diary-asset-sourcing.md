# Diary v2 — Asset Sourcing & QA Spec (historia-a1)

Companion to [format-mini-story-spec.md](format-mini-story-spec.md). Defines the
quality bar and sourcing procedure for the **scene images** and **SFX/ambient
audio** of the diary format, plus how to verify them with the gate.

> **Why this exists** — The Ep.1 pilot originally shipped *placeholder* assets that passed
> path/extension checks but were not real: square low-res JPEGs mislabelled as
> PNG, and 15 byte-identical silent audio stubs. `checks/validate_diary.py` Rule 9 now
> blocks all of these as errors at `make check` time (see §4). This doc defines the spec
> for sourcing and maintaining those assets.

## 1. Measured current state (2026-05-31)

| Asset | Reality | Gate signal |
|---|---|---|
| `assets/story/*.png` (×8) | **1920×1080 PNG**, real scene art; caption panel dynamically sizes, eliminating overlap risks | 0 errors / 0 warnings |
| `assets/audio/sfx/*.wav` (×18) | **18 distinct, procedural CC0 files** generated via deterministic numpy DSP scripts. No silence, no duplicates. | 0 errors / 0 warnings |

Crop/occlusion preview: `output/qa/diary-crop-qa.png` (red = 16:9 keep-band,
dimmed = cut, blue = caption-panel occlusion zone).

## 2. Image regeneration spec

The diary background is **full-bleed** and gets a Ken Burns zoom `1.0 → 1.08`,
so the source must out-resolve the viewport with headroom.

- **Aspect: native 16:9.** Do not generate square and crop — compose for 16:9.
- **Resolution: ≥ 1600×900 (hard floor = 1.25× the 1280×720 viewport).**
  Recommended **1920×1080**. Below 1600 wide → upscaled/soft and the gate warns.
- **Format: real PNG** (or save `.jpg` if JPEG — just don't mislabel; the gate
  checks content vs extension).
- **Caption safe area:** the subtitle panel covers the bottom center, but its height is computed dynamically based on text length. To be safe, keep faces and any plot-critical prop in the **top ~65%** of the frame. Nothing important in the bottom third.
- **Continuity:** Lucía (low bun, denim shirt) and Diego must stay consistent
  across scenes 4/6/7. The **blue notebook** is the recurring plot prop (scenes
  2, 3, 4, 6, 7, 8) — keep it recognisably blue and **above** the panel zone.

### Per-scene shot list (prop that must clear the caption panel)

| # | Scene | Frame for 16:9, keep above panel |
|---|---|---|
| 1 | Por la mañana | Lucía at window, morning light; cup/tostada mid-frame |
| 2 | Un pequeño error | Packing bag **and** the blue notebook left on the table (the whole plot hinges on it being visible) |
| 3 | En el metro | Lucía seated, searching her bag in a crowded car |
| 4 | Un mensaje a Diego | Phone screen visible **high** in frame (not low in her lap) |
| 5 | En la universidad | Classroom, Lucía raising her hand toward the profesora |
| 6 | Por las calles | Madrid street; phone with Diego's message readable, upper frame |
| 7 | Lluvia y churros | Two-shot Diego + Lucía, the blue notebook handed over, churros — busy lower area, frame tight and high |
| 8 | El diario de la noche | Desk at night, lamp, Lucía writing in the diary |

After regenerating: `PROJECT=historia_a1_un_dia_de_lucia make check` must show **0** errors/warnings.

## 3. SFX & ambient sourcing

Three layers (see format spec §"Audio Architecture"):

- **Layer 1 — ambient beds** (`STORY_SCENES[*].ambient_sfx`): looped over the
  whole scene via `AudioLoop`. **Must be ≥ ~10–20 s of real continuous room
  tone** (or a seamless loop). A 1-second clip looped over a 60 s scene
  machine-guns — do **not** ship short ambient beds.
- **Layer 2 — spot SFX** (`SFX_MANIFEST[*]`): one-shots anchored to a line.
  Short (0.5–3 s) is fine.
- **Layer 3 — segment SFX** (`SEGMENT_SFX[*]`): structural beds for non-scene blocks (intro, montage, outro).

### Procedural Audio Sourcing
For the base build, we utilize mathematical synthesis (`scripts/synthesize_diary_sfx.py`) to generate compliant CC0 wav clips.
- **Ambient Beds (8 tracks)**: Madrid morning (low-pass + highs hiss), quiet morning (room tone), metro inside (squeal + joint clicks), soft typing (random keystrokes), classroom murmur (mid voice peaks), street traffic (Doppler pans), cafe rain (high rain noise), quiet night (AC hum).
- **Spot SFX (7 tracks)**: Door close (low thud + footsteps), metro chime (3 notes), text send (ticks + whoosh), chair scrape (friction noise), thunder rain (noise transient), cafe bell (2 tones), night tone (440Hz + pencil scratch).
- **Segment SFX (3 tracks)**: Intro morning (sunrise sweep + birds), montage shimmer (warm pads), outro calm (bell chords).

For production-ready version 1.1+, replace these mathematical assets with real CC0 recordings (soured from freesound.org, Pixabay, etc.) to achieve maximum natural organic quality, while keeping their exact filenames and registering licenses in `assets/audio/LICENSE.md`.

## 4. Done = gate-clean, then linguist, then render

1. `PROJECT=historia_a1_un_dia_de_lucia make check` → **no** image/audio
   warnings or errors.
2. Linguist approves the es/ko lines (flip the STATUS header to `"approved"` in the project
   module).
3. Run `make render-diary` → verification (`checks/probe_output.py`) → `python -m build.publish` to package the bundle.
