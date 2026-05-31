# Mini-Story Diary v2 Format Specification

This document defines the specification for the "AV Diary" (`RENDER_TYPE = "diary"`) format used in `historia-a1` and other mini-story series.

## Data Schemas

### Story Scenes (`STORY_SCENES`)

`STORY_SCENES` is a list of dictionaries representing the chronological scenes in the video.

#### Scene Dictionary Schema

| Field | Type | Description |
|---|---|---|
| `scene_id` | `int` | Unique, ascending identifier starting from 1. |
| `title_es` | `str` | Title in Spanish (non-empty). |
| `title_ko` | `str` | Title in Korean (non-empty). |
| `image_path` | `str` | Scene-level background image path relative to the repo root. |
| `ambient_sfx` | `str` | Ambient background track (Layer 1) path relative to the repo root. |
| `ambient_sfx_license` | `str` | License citation for the ambient track (required if `ambient_sfx` is non-empty). |
| `pause_s` | `float`/`int` | Transition pause duration at the end of the scene. |
| `lines` | `list[dict]` | List of line dictionaries belonging to this scene. |

#### Line Dictionary Schema

| Field | Type | Description |
|---|---|---|
| `kind` | `str` | Subtitle category (e.g., `"narration"`, `"dialogue"`). |
| `speaker` | `str` | Character name if kind is dialogue (otherwise empty). |
| `text_es` | `str` | Spanish line text. |
| `text_ko` | `str` | Korean translation text. |
| `duration_s` | `float` (optional) | Minimum timeline boundary constraint for this line. |
| `min_hold_s` | `float` (optional) | Override for the minimum line holding time. |
| `processing_pause_s` | `float` (optional) | Override for the cognitive pause after narration ends. |
| `image_path` | `str` (optional) | Multi-beat background image override path. |

### Sound Effects (`SFX_MANIFEST`)

`SFX_MANIFEST` registers spot audio effects (Layer 2) layered on top of the narration.

| Field | Type | Description |
|---|---|---|
| `id` | `str` | Unique sound effect event identifier. |
| `kind` | `str` | Must be `"spot"`. |
| `scene_id` | `int` | Scene ID to which the spot effect belongs. |
| `line_index` | `int` (optional) | 1-based line index in the scene to anchor the effect. |
| `offset_s` | `float` | Start delay offset relative to the anchor (falls back to legacy `start_s`). |
| `path` | `str` | Path to the audio file relative to the repo root. |
| `volume_db` | `float` | Relative volume adjustments in decibels. |
| `license` | `str` | License citation for the spot effect. |

### Out-of-Scene Segment SFX (`SEGMENT_SFX`)

`SEGMENT_SFX` registers structural audio beds or spots (Layer 3) that play outside the standard scene context (e.g. during the intro, montage, or outro).

| Field | Type | Description |
|---|---|---|
| `id` | `str` | Unique segment sound effect identifier. |
| `kind` | `str` | Must be `"segment"`. |
| `segment_type` | `str` | Must be one of: `"intro"`, `"montage"`, `"outro"`. |
| `mode` | `str` | Either `"bed"` (loops audio across the segment) or `"spot"` (one-shot effect). |
| `offset_s` | `float` | Start delay offset relative to the segment start time. |
| `path` | `str` | Path to the audio file relative to the repo root. |
| `volume_db` | `float` | Relative volume adjustments in decibels. |
| `license` | `str` | License citation for the segment effect. |

---

## Timing and Pacing

### Audio Engine Configuration (`AUDIO`)

The pacing behavior is parameterized inside the project's `AUDIO` configuration:

```python
AUDIO = {
    # ...
    "processing_pause_s": 2.5,  # Cognitive silence duration after speech ends
    "min_hold_s": 2.5,          # Minimum screen duration for a diary line
    "ambient_bed_db": -11.9,    # Default volume for Layer 1 ambient beds
    "bgm_volume_db": 6.0,       # Default volume for BGM (usually scaled in gain)
}
```

### Segment Duration Rules

For each segment type, duration is resolved as:

1. **`diary_line`**:
   - If TTS is synthesized: `duration = max(tts_duration + lead + tail + processing_pause_s, min_hold_s)`
   - If TTS is not synthesized: Uses static estimate `duration_for_text(text)`.
   - If `duration_s` is explicitly defined: `min_hold_s = max(min_hold_s, duration_s)`.
2. **`scene_header` / `intro` / `outro`**:
   - Resolved purely from text length or explicit `duration_s` (no processing pause added).
3. **`pause`**:
   - Retains the exact scene `pause_s` duration.

---

## Audio Architecture (3-Layer SFX & Mastering)

### Mixing Pipeline
The audio is compiled in two stages using ffmpeg and moviepy:
1. **Stage 1 (`mix_sfx_layer`)**: Combines raw Narration, Scene-level Ambient beds (Layer 1), Spot effects (Layer 2), and Segment structural beds (Layer 3) into `output/audio/narration_sfx.wav`.
2. **Stage 2 (`mix_with_bgm`)**: Mixes the composite SFX track with BGM, applying sidechain compression (ducking) and final mastering filters:
   - `sidechaincompress`: Compresses BGM volume when narration is active.
   - `amix=normalize=0`: Mixes BGM and SFX without automatic volume normalization.
   - `alimiter=limit=0.9`: Prevents peak clipping (caps peak at ~-0.9 dBFS).
   - `loudnorm=I=-14:TP=-1.5:LRA=11`: Normalizes the mix to target `-14 LUFS` and `-1.5 dBFS` peak.

### Level Balancing Guidelines
To prevent BGM from burying environmental details:
- **Measure Pre-Loudnorm Levels**: Extract values from `output/audio/narration_sfx.wav` and the raw BGM to gauge absolute differences before the loudnorm auto-gain scaling kicks in.
- **Ambience Priority**: Ensure scene ambience leads the piano/BGM by **+8 to +9 dB** during gaps.
- **BGM Gain Offsets**: Note that very quiet BGM sources (e.g. `fur_elise` at ~-40 dB mean) require positive gain settings (e.g. `bgm_volume_db = 6.0`) to remain softly audible under the loudnorm compression.

---

## Video Layout & Camera

1. **Background Layer**:
   - Standard Ken Burns zoom-in `z = 1.0 -> 1.08`.
   - Art-directed pans require source image resolution of at least `1.25x` viewport width (e.g. 1600x900 for a 1280x720 output).
   - Background crop and pan animations run continuously across continuous segments using the same background image (grouped "beats").
2. **Caption Overlay**:
   - Rendered as a separate RGBA Layer overlaid statically.
   - Text wrapping and badges are composited without inheriting camera movement.
   - The caption panel height is calculated dynamically based on wrapped line lengths and badge existence to prevent overlapping subtitles.
