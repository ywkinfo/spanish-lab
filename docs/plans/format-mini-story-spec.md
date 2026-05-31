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

---

## Timing and Pacing

### Audio Engine Configuration (`AUDIO`)

The pacing behavior is parameterized inside the project's `AUDIO` configuration:

```python
AUDIO = {
    # ...
    "processing_pause_s": 2.5,  # Cognitive silence duration after speech ends
    "min_hold_s": 2.5,          # Minimum screen duration for a diary line
    "ambient_bed_db": -20.0,    # Default volume for Layer 1 ambient beds
    "bgm_volume_db": -20.0,     # Default volume for BGM (Layer 1 bed takes priority)
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

## Audio Architecture (2-Layer SFX)

1. **Layer 1: Ambient Bed (`ambient_sfx`)**:
   - Looped using moviepy's `AudioLoop` over the entire span of the corresponding scene (from the scene's header start until the next scene's header start or end of video).
2. **Layer 2: Spot Polies (`SFX_MANIFEST`)**:
   - Anchored to a specific line (`line_index`) within a scene. Start time is dynamically adjusted to `line_start_s + offset_s`.
   - Volumetric mixing with decibel conversions.

---

## Video Layout & Camera

1. **Background Layer**:
   - Standard Ken Burns zoom-in `z = 1.0 -> 1.08`.
   - Art-directed pans require source image resolution of at least `1.25x` viewport width.
   - Background crop and pan animations run continuously across continuous segments using the same background image (grouped "beats").
2. **Caption Overlay**:
   - Rendered as a separate RGBA Layer overlaid statically.
   - Text wrapping and badges are composited without inheriting camera movement.
