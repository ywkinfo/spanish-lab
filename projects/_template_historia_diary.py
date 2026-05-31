"""DRAFT v2 (diary format) -- [TODO: SERIES_TITLE] Ep.[TODO: EPISODE]: "[TODO: TITLE_ES]".

Comprehensible-input mini-historia (SERIES "[TODO: SERIES]"). v2 diary format
adds STORY_SCENES with per-scene lines, ambient SFX slots, and pause timings.
Legacy PHRASES / BLOCKS / DIALOGUE / MINI_QUIZ kept for cards fallback.

STATUS: draft
"""

from __future__ import annotations

IMAGE_PATH = ""
DESCRIP_PATH = "[TODO: FOLDER]/descrip.md"
OUTPUT_NAME = "[TODO: OUTPUT_NAME]"
PUBLIC_SLUG = "[TODO: PUBLIC_SLUG]"
YOUTUBE_URL = ""
SERIES = "[TODO: SERIES]"
SERIES_TITLE = "[TODO: SERIES_TITLE]"
EPISODE = 1
LEVEL = "[TODO: LEVEL]"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "diary"
THUMBNAIL_PATH = None
YOUTUBE_TITLE = "[TODO: YOUTUBE_TITLE]"
DESCRIPTION_INTRO = (
    "[TODO: DESCRIPTION_INTRO]"
)
DESCRIPTION_OUTRO = (
    "[TODO: DESCRIPTION_OUTRO]"
)
KOREAN_TEASER = (
    "[TODO: KOREAN_TEASER]"
)
BASE_TAGS = [
    "스페인어",
    "스페인어 입문",
    "스페인어 A1",
]
EXTRA_TAGS = [
    "스페인어 이야기",
    "스페인어 듣기 연습",
]
BASE_HASHTAGS = ["#EspañolA1", "#스페인어"]
EXTRA_HASHTAGS = ["#스페인어이야기"]

# ---------------------------------------------------------------------------
# Legacy cards data (fallback)
# ---------------------------------------------------------------------------
PHRASES = [
    (1, "Es por la mañana.", "아침이에요.", "Es por la mañana."),
]
BLOCKS = [
    {"block_id": 1, "title_es": "[TODO: BLOCK]", "title_ko": "[TODO: 블록]", "color_block": "coral", "start": 1},
]
DIALOGUE = [
    ("Lucía", "Hola.", "안녕."),
]
MINI_QUIZ = [
    ("¿Cómo dices '먼저'?", "Primero"),
]

# ---------------------------------------------------------------------------
# Visual design
# ---------------------------------------------------------------------------
DESIGN = {
    "output_size": (1920, 1080),
    "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
    "font_index": 0,
    "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
    "font_index_ko": 0,
    "font_size_title": 82,
    "font_size_es": 84,
    "min_font_size_es": 52,
    "font_size_ko": 36,
    "font_size_example": 34,
    "background_color": (248, 247, 242),
    "text_color": (31, 35, 40),
    "muted_text_color": (96, 101, 109),
    "intro_title": "[TODO: INTRO_TITLE]",
    "intro_subtitle": "[TODO: INTRO_SUBTITLE]",
    "intro_ko": "[TODO: INTRO_KO]",
    "thumbnail_title": "[TODO: THUMB_TITLE]",
    "thumbnail_subtitle": "[TODO: THUMB_SUBTITLE]",
    "thumbnail_ko": "[TODO: THUMB_KO]",
    "outro_ko": "다음 이야기에서 또 만나요",
    "color_blocks": {
        "coral": (224, 91, 76),
        "amber": (230, 158, 62),
        "teal": (44, 150, 142),
        "blue": (70, 120, 196),
        "green": (92, 148, 86),
        "neutral": (42, 48, 57),
    },
}

# ---------------------------------------------------------------------------
# v2 diary: STORY_SCENES
# ---------------------------------------------------------------------------
STORY_SCENES = [
    {
        "scene_id": 1,
        "title_es": "[TODO: SCENE_1_TITLE_ES]",
        "title_ko": "[TODO: SCENE_1_TITLE_KO]",
        "image_path": "", # e.g. "assets/story/scene_01.png"
        "ambient_sfx": "", # e.g. "assets/audio/sfx/morning.wav"
        "ambient_sfx_license": "CC0",
        "pause_s": 2.0,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "[TODO: LINE_ES]",
                "text_ko": "[TODO: LINE_KO]",
            },
        ],
    },
    {
        "scene_id": 2,
        "title_es": "[TODO: SCENE_2_TITLE_ES]",
        "title_ko": "[TODO: SCENE_2_TITLE_KO]",
        "image_path": "",
        "ambient_sfx": "",
        "ambient_sfx_license": "CC0",
        "pause_s": 2.0,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "[TODO: LINE_ES]",
                "text_ko": "[TODO: LINE_KO]",
            },
        ],
    },
    {
        "scene_id": 3,
        "title_es": "[TODO: SCENE_3_TITLE_ES]",
        "title_ko": "[TODO: SCENE_3_TITLE_KO]",
        "image_path": "",
        "ambient_sfx": "",
        "ambient_sfx_license": "CC0",
        "pause_s": 2.0,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "[TODO: LINE_ES]",
                "text_ko": "[TODO: LINE_KO]",
            },
        ],
    },
    {
        "scene_id": 4,
        "title_es": "[TODO: SCENE_4_TITLE_ES]",
        "title_ko": "[TODO: SCENE_4_TITLE_KO]",
        "image_path": "",
        "ambient_sfx": "",
        "ambient_sfx_license": "CC0",
        "pause_s": 2.0,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "[TODO: LINE_ES]",
                "text_ko": "[TODO: LINE_KO]",
            },
        ],
    },
    {
        "scene_id": 5,
        "title_es": "[TODO: SCENE_5_TITLE_ES]",
        "title_ko": "[TODO: SCENE_5_TITLE_KO]",
        "image_path": "",
        "ambient_sfx": "",
        "ambient_sfx_license": "CC0",
        "pause_s": 2.0,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "[TODO: LINE_ES]",
                "text_ko": "[TODO: LINE_KO]",
            },
        ],
    },
    {
        "scene_id": 6,
        "title_es": "[TODO: SCENE_6_TITLE_ES]",
        "title_ko": "[TODO: SCENE_6_TITLE_KO]",
        "image_path": "",
        "ambient_sfx": "",
        "ambient_sfx_license": "CC0",
        "pause_s": 2.0,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "[TODO: LINE_ES]",
                "text_ko": "[TODO: LINE_KO]",
            },
        ],
    },
    {
        "scene_id": 7,
        "title_es": "[TODO: SCENE_7_TITLE_ES]",
        "title_ko": "[TODO: SCENE_7_TITLE_KO]",
        "image_path": "",
        "ambient_sfx": "",
        "ambient_sfx_license": "CC0",
        "pause_s": 2.0,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "[TODO: LINE_ES]",
                "text_ko": "[TODO: LINE_KO]",
            },
        ],
    },
    {
        "scene_id": 8,
        "title_es": "[TODO: SCENE_8_TITLE_ES]",
        "title_ko": "[TODO: SCENE_8_TITLE_KO]",
        "image_path": "",
        "ambient_sfx": "",
        "ambient_sfx_license": "CC0",
        "pause_s": 2.0,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "[TODO: LINE_ES]",
                "text_ko": "[TODO: LINE_KO]",
            },
        ],
    },
]

SFX_MANIFEST = [
    {
        "id": "[TODO: SFX_ID]",
        "kind": "spot",
        "scene_id": 1,
        "line_index": 1,
        "offset_s": 0.0,
        "path": "", # e.g. "assets/audio/sfx/chime.wav"
        "volume_db": -10.6,
        "license": "CC0",
    },
]

SEGMENT_SFX = [
    {
        "id": "intro_sfx",
        "kind": "segment",
        "segment_type": "intro",
        "mode": "bed",
        "offset_s": 0.0,
        "path": "", # e.g. "assets/audio/sfx/intro.wav"
        "volume_db": -4.9,
        "license": "CC0",
    },
    {
        "id": "montage_sfx",
        "kind": "segment",
        "segment_type": "montage",
        "mode": "bed",
        "offset_s": 0.0,
        "path": "", # e.g. "assets/audio/sfx/montage.wav"
        "volume_db": -4.9,
        "license": "CC0",
    },
    {
        "id": "outro_sfx",
        "kind": "segment",
        "segment_type": "outro",
        "mode": "bed",
        "offset_s": 0.0,
        "path": "", # e.g. "assets/audio/sfx/outro.wav"
        "volume_db": -4.9,
        "license": "CC0",
    },
]

# ---------------------------------------------------------------------------
# Segment builder (v2 diary)
# ---------------------------------------------------------------------------

def _build_diary_segments() -> list[dict]:
    """Generate SEGMENTS from STORY_SCENES for the diary render pipeline."""
    segments: list[dict] = [
        {
            "type": "intro",
            "text_es": (
                "[TODO: INTRO_TEXT_ES]"
            ),
            "duration_s": 16.0,
        }
    ]
    for scene in STORY_SCENES:
        # Scene header
        segments.append(
            {
                "type": "scene_header",
                "scene_id": scene["scene_id"],
                "title_es": scene["title_es"],
                "title_ko": scene["title_ko"],
                "duration_s": 3.0,
            }
        )
        # Lines
        for line in scene["lines"]:
            resolved_img = line.get("image_path") or scene.get("image_path", "")
            seg = {
                "type": "diary_line",
                "scene_id": scene["scene_id"],
                "kind": line["kind"],
                "speaker": line["speaker"],
                "text_es": line["text_es"],
                "text_ko": line["text_ko"],
                "image_path": resolved_img,
            }
            if "duration_s" in line:
                seg["duration_s"] = line["duration_s"]
            if "min_hold_s" in line:
                seg["min_hold_s"] = line["min_hold_s"]
            if "processing_pause_s" in line:
                seg["processing_pause_s"] = line["processing_pause_s"]
            segments.append(seg)
        # Pause after scene
        last_line_img = scene["lines"][-1].get("image_path") or scene.get("image_path", "") if scene["lines"] else scene.get("image_path", "")
        segments.append(
            {
                "type": "pause",
                "scene_id": scene["scene_id"],
                "duration_s": scene["pause_s"],
                "image_path": last_line_img,
            }
        )
    # Montage
    segments.append(
        {
            "type": "montage",
            "duration_s": 6.0,
        }
    )
    # Outro
    segments.append(
        {
            "type": "outro",
            "text_es": (
                "[TODO: OUTRO_TEXT_ES]"
            ),
            "duration_s": 15.0,
        }
    )
    return segments


SEGMENTS = _build_diary_segments()
CHAPTERS = [
    {"segment": 1, "title": "Introducción"},
    {"segment": 2, "title": "[TODO: SCENE_1_TITLE]"},
    {"segment": 5, "title": "[TODO: SCENE_2_TITLE]"},
    {"segment": 8, "title": "[TODO: SCENE_3_TITLE]"},
    {"segment": 11, "title": "[TODO: SCENE_4_TITLE]"},
    {"segment": 14, "title": "[TODO: SCENE_5_TITLE]"},
    {"segment": 17, "title": "[TODO: SCENE_6_TITLE]"},
    {"segment": 20, "title": "[TODO: SCENE_7_TITLE]"},
    {"segment": 23, "title": "[TODO: SCENE_8_TITLE]"},
    {"segment": len(SEGMENTS), "title": "Repaso final"},
]
AUDIO = {
    "tts_engine": "edge",
    "edge_voice": "es-ES-ElviraNeural",
    "edge_rate": "+8%",
    "edge_pitch": "+0Hz",
    "edge_volume": "+0%",
    "voice": "es-ES-ElviraNeural",
    "rate_wpm": 160,
    "lead_padding_s": 0.25,
    "tail_padding_s": 0.4,
    "min_duration_s": 3.0,
    "readability_floor_ratio": 0.0,
    "processing_pause_s": 2.5,
    "min_hold_s": 2.5,
    "ambient_bed_db": -11.9,
    "bgm_path": "assets/audio/fur_elise_inspired_soft_piano.wav",
    "bgm_volume_db": 6.0,
    "narration_volume_db": 0.0,
    "ducking": True,
    "ducking_threshold": 0.05,
    "ducking_ratio": 4,
    "ducking_attack_ms": 80,
    "ducking_release_ms": 550,
    "fade_in_s": 4.0,
    "fade_out_s": 5.0,
    "audio_codec": "aac",
    "audio_bitrate_kbps": 192,
    "sample_rate_hz": 44100,
}
