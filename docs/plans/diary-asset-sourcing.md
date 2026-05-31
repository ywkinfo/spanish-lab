# Diary v2 — Asset Sourcing & QA Spec (historia-a1)

Companion to [format-mini-story-spec.md](format-mini-story-spec.md). Defines the
quality bar and sourcing procedure for the **scene images** and **SFX/ambient
audio** of the diary format, plus how to verify them with the gate.

> **Why this exists** — the Ep.1 pilot shipped *placeholder* assets that passed
> path/extension checks but were not real: square low-res JPEGs mislabelled as
> PNG, and 15 byte-identical silent audio stubs. `checks/validate_diary.py` now
> catches all of these as warnings at `make check` time (see §4). This doc is
> the spec for replacing them.

## 1. Measured current state (2026-05-30)

| Asset | Reality | Gate signal |
|---|---|---|
| `assets/story/*.png` (×8) | **1920×1080 PNG**, real scene art (regenerated 2026-05-30); caption panel still occludes lower-centre if props drift low | 0 warnings (format/resolution pass) |
| `assets/audio/sfx/*.wav` (×15) | **One file copied 15×** (single md5), **−91 dBFS = silence** | 15× silent + 1× duplicate-content |

Crop/occlusion preview: `output/qa/diary-crop-qa.png` (red = 16:9 keep-band,
dimmed = cut, blue = caption-panel occlusion zone).

## 2. Image regeneration spec

The diary background is **full-bleed** and gets a Ken Burns zoom `1.0 → 1.08`,
so the source must out-resolve the viewport with headroom.

- **Aspect: native 16:9.** Do not generate square and crop — compose for 16:9.
- **Resolution: ≥ 1600×900 (hard floor = 1.25× the 1280×720 viewport).**
  Recommended **1920×1080**. Below 1600 wide → upscaled/soft and the gate warns.
- **Format: real PNG** (or save `.jpg` if JPEG — just don't mislabel; the gate
  now checks content vs extension).
- **Caption safe area:** the subtitle panel covers the **bottom ~210 px (at
  720p)** plus margin. Keep faces and any plot-critical prop in the **top ~65%**
  of the frame. Nothing important in the bottom third.
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

After regenerating: `PROJECT=historia_a1_un_dia_de_lucia make check` must show
**0** image warnings.

## 3. SFX & ambient sourcing

Two layers (see format spec §"Audio Architecture"):

- **Layer 1 — ambient beds** (`STORY_SCENES[*].ambient_sfx`): looped over the
  whole scene via `AudioLoop`. **Must be ≥ ~10–20 s of real continuous room
  tone** (or a seamless loop). A 1-second clip looped over a 60 s scene
  machine-guns — do **not** ship short ambient beds.
- **Layer 2 — spot SFX** (`SFX_MANIFEST[*]`): one-shots anchored to a line.
  Short (0.5–3 s) is fine.

**Sources (CC0 / clearly-licensed):** freesound.org (filter *License: CC0*),
Pixabay sound effects, Zapsplat (attribution). **Record the real license** in
each `ambient_sfx_license` / `license` field — keep them accurate, not "CC0" by
default.

| Slot | Scene/line | Needs to sound like | Search terms |
|---|---|---|---|
| ambient ×8 | per scene | morning home / quiet home / metro interior / quiet typing room / soft classroom / Madrid street / café with rain / quiet night room | "room tone", "metro interior", "café ambience", "city street ambience", "rain window" |
| spot `door_close_footsteps` | s2 L6 | door shut + a few steps | "door close footsteps" |
| spot `metro_chime` | s3 L1 | metro arrival chime | "metro door chime" |
| spot `phone_typing_send` | s4 L1 | typing + send whoosh | "text message send" |
| spot `chair_murmur` | s5 L6 | chair scrape + classroom murmur | "classroom murmur" |
| spot `thunder_rain` | s7 L1 | distant thunder + rain onset | "thunder rain" |
| spot `doorbell_cups` | s7 L5 | café door bell + cups | "café door bell cups" |
| spot `night_tone_pen` | s8 L1 | quiet night + pen on paper | "pen writing paper" |

**Levels:** keep the project's `ambient_bed_db` / spot `volume_db` but verify by
ear with ducking on — ambient should sit clearly under narration, audible in
gaps. Normalise sources before placing.

**Verify each file is real:**
```sh
ffmpeg -i assets/audio/sfx/<file>.wav -af volumedetect -f null -   # mean/max must NOT be ~ -91 dB
```

## 4. Done = gate-clean, then linguist, then render

1. `PROJECT=historia_a1_un_dia_de_lucia make check` → **no** image/audio
   warnings (silent / duplicate / format-mismatch / low-res all gone).
2. Linguist approves the es/ko lines (flip the STATUS header in the project
   module).
3. `make render-diary` → `checks/probe_output.py` → `make publish-diary`.

Rendering before step 1 produces soft, upscaled images with an inaudible SFX
layer — technically "ok" to `probe_output.py` (BGM carries the level check) but
not shippable.
