"""A1 story-card episode: Jin asks about spring in Madrid."""

from __future__ import annotations

IMAGE_PATH = "images/ep15-primavera-madrid-source.png"
DESCRIP_PATH = "a1-primavera-madrid/descrip.md"
OUTPUT_NAME = "primavera-madrid"
PUBLIC_SLUG = "a1-primavera-madrid"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 15
LEVEL = "A1"
LANGUAGE = "es"
RENDER_VERSION = 2
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a1-ep15-primavera-madrid.jpg"
YOUTUBE_TITLE = "¿Cómo es la primavera en Madrid? 🌸 마드리드의 봄은 어때? | Español A1 · Ep.15"
DESCRIPTION_INTRO = (
    "Jin mira una mañana de primavera en Madrid con Lucía y Diego. "
    "En este episodio A1 practicamos una pregunta muy útil: ¿Cómo es...? "
    "Aprende a preguntar y responder: ¿Cómo es la primavera en Madrid?, "
    "Es agradable, Es muy bonita, Hace sol y Hay muchas flores."
)
DESCRIPTION_OUTRO = (
    "Escucha primero, repite en voz alta y después crea tu propia respuesta: "
    "¿Cómo es la primavera en tu ciudad? Es agradable, es bonita, hace sol o hay muchas flores."
)
KOREAN_TEASER = (
    "한국어 티저: EP.15에서는 마드리드의 예쁜 봄을 보며 ‘어때요?’라고 특징을 묻는 "
    "A1 질문 ¿Cómo es...?를 연습합니다. ¿Cómo es la primavera en Madrid?와 "
    "Es agradable, Es muy bonita 같은 쉬운 대답을 따라 말해 보세요."
)
BASE_TAGS = [
    "스페인어",
    "스페인어 입문",
    "스페인어 A1",
    "Spanish A1",
    "aprender español",
    "español para principiantes",
]
EXTRA_TAGS = [
    "Cómo es",
    "primavera en Madrid",
    "Madrid primavera",
    "describir estaciones español",
    "conversacion español A1",
    "스페인어 회화",
    "스페인어 날씨 표현",
    "마드리드 봄",
]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#Madrid", "#Primavera"]

CHARACTERS = {
    "Jin": "assets/characters/peter-profile.png",
    "Lucía": "assets/characters/lucia-profile.png",
    "Diego": "assets/characters/diego-profile.png",
}
CHARACTER_VOICES = {
    "Lucía": "es-ES-ElviraNeural",
    "Jin": "es-ES-AlvaroNeural",
    "Diego": "es-MX-JorgeNeural",
}

BLOCKS = [
    {"block_id": 1, "title_es": "¿Cómo es la primavera?", "title_ko": "봄은 어때?", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "Es agradable", "title_ko": "좋고 쾌적해요", "color_block": "amber", "start": 8},
    {"block_id": 3, "title_es": "Hay muchas flores", "title_ko": "꽃이 많아요", "color_block": "teal", "start": 15},
    {"block_id": 4, "title_es": "Mini prueba", "title_ko": "미니 퀴즈", "color_block": "blue", "start": 23},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Diego", "Hoy hablamos de Madrid en primavera.", "오늘은 봄의 마드리드에 대해 이야기해요.", "Madrid en primavera", 1, "coral", 8.5),
    (2, "Jin", "Lucía, ¿cómo es la primavera en Madrid?", "Lucía, 마드리드의 봄은 어때?", "¿cómo es?", 1, "coral", 9.5),
    (3, "Lucía", "Es muy bonita.", "아주 예뻐.", "es muy bonita", 1, "coral", 7.5),
    (4, "Diego", "Repite la pregunta: ¿cómo es la primavera?", "질문을 따라 해 봐요: ¿cómo es la primavera?", "repite", 1, "coral", 9.5),
    (5, "Jin", "¿Cómo es la primavera?", "봄은 어때?", "¿cómo es la primavera?", 1, "coral", 8.0),
    (6, "Diego", "Muy bien. ¿Cómo es...? pregunta por la característica.", "아주 좋아요. ¿Cómo es...?는 특징을 묻는 말이에요.", "característica", 1, "coral", 10.5),
    (7, "Jin", "¿Cómo es la primavera en Madrid?", "마드리드의 봄은 어때?", "en Madrid", 1, "coral", 8.5),
    (8, "Lucía", "Es agradable.", "좋아, 쾌적해.", "es agradable", 2, "amber", 7.5),
    (9, "Jin", "Es agradable.", "좋아요, 쾌적해요.", "es agradable", 2, "amber", 7.5),
    (10, "Lucía", "Hace sol.", "햇볕이 나.", "hace sol", 2, "amber", 7.0),
    (11, "Lucía", "Hace sol, pero no hace mucho calor.", "햇볕이 나지만, 많이 덥지는 않아.", "no hace mucho calor", 2, "amber", 9.5),
    (12, "Jin", "Hace sol. No hace mucho calor.", "햇볕이 나요. 많이 덥지는 않아요.", "hace sol", 2, "amber", 8.5),
    (13, "Diego", "Perfecto. Despacio: es agradable.", "완벽해요. 천천히: es agradable.", "despacio", 2, "amber", 8.5),
    (14, "Jin", "Es agradable.", "좋아요, 쾌적해요.", "es agradable", 2, "amber", 7.5),
    (15, "Lucía", "En Madrid hay flores en primavera.", "마드리드는 봄에 꽃이 있어.", "hay flores", 3, "teal", 8.5),
    (16, "Jin", "¿Hay muchas flores?", "꽃이 많아?", "hay muchas flores", 3, "teal", 7.5),
    (17, "Lucía", "Sí, hay muchas flores.", "응, 꽃이 많아.", "hay muchas flores", 3, "teal", 7.5),
    (18, "Jin", "Hay muchas flores.", "꽃이 많아요.", "hay muchas flores", 3, "teal", 7.5),
    (19, "Diego", "Atención: hoy no decimos solo el tiempo.", "주의: 오늘은 날씨만 말하는 게 아니에요.", "no solo el tiempo", 3, "teal", 9.0),
    (20, "Diego", "Decimos cómo es la primavera.", "봄이 어떤지 말해요.", "cómo es", 3, "teal", 8.0),
    (21, "Lucía", "Es bonita y tranquila.", "예쁘고 평온해.", "bonita y tranquila", 3, "teal", 8.0),
    (22, "Jin", "Es bonita y tranquila.", "예쁘고 평온해요.", "bonita y tranquila", 3, "teal", 8.0),
    (23, "Diego", "Ahora una mini prueba.", "이제 미니 퀴즈예요.", "mini prueba", 4, "blue", 7.5),
    (24, "Diego", "Pregunta: ¿cómo es la primavera en Madrid?", "질문: 마드리드의 봄은 어때?", "pregunta", 4, "blue", 9.0),
    (25, "Jin", "Respuesta: es agradable.", "대답: 좋아요, 쾌적해요.", "respuesta", 4, "blue", 8.0),
    (26, "Lucía", "Otra respuesta: es muy bonita.", "또 다른 대답: 아주 예뻐요.", "otra respuesta", 4, "blue", 8.5),
    (27, "Diego", "Muy bien. Una frase completa.", "아주 좋아요. 완전한 문장 하나.", "frase completa", 4, "blue", 8.0),
    (28, "Jin", "La primavera en Madrid es agradable.", "마드리드의 봄은 좋아요.", "frase completa", 4, "blue", 9.0),
    (29, "Lucía", "Y es muy bonita.", "그리고 아주 예뻐요.", "muy bonita", 4, "blue", 7.5),
    (30, "Diego", "Excelente. Ya puedes preguntar: ¿cómo es...?", "훌륭해요. 이제 ¿cómo es...?라고 물을 수 있어요.", "¿cómo es...?", 4, "blue", 9.5),
]

DESIGN = {
    "output_size": (1280, 720),
    "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
    "font_index": 0,
    "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
    "font_index_ko": 0,
    "font_size_title": 66,
    "font_size_es": 68,
    "min_font_size_es": 38,
    "font_size_ko": 32,
    "font_size_example": 30,
    "background_color": (248, 247, 242),
    "text_color": (31, 35, 40),
    "muted_text_color": (96, 101, 109),
    "intro_title": "Primavera en Madrid",
    "intro_subtitle": "Español A1 · Ep.15",
    "intro_ko": "마드리드의 봄은 어때?",
    "intro_scene_image_path": "images/ep15-primavera-madrid-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "¿Cómo es la primavera?",
    "thumbnail_subtitle": "Español A1 · Ep.15",
    "thumbnail_ko": "마드리드의 봄은 어때?",
    "outro_ko": "이제 스페인어로 특징을 물어볼 수 있어요",
    "outro_font_size_es": 28,
    "outro_text_width_ratio": 0.76,
    "outro_max_lines": 5,
    "outro_text_y": 388,
    "outro_ko_y": 630,
    "character_images": CHARACTERS,
    "show_character_portraits": True,
    "color_blocks": {
        "coral": (224, 91, 76),
        "amber": (230, 158, 62),
        "teal": (44, 150, 142),
        "blue": (70, 120, 196),
        "green": (92, 148, 86),
        "violet": (138, 104, 190),
        "neutral": (42, 48, 57),
    },
}


def _build_segments() -> list[dict]:
    segments: list[dict] = [
        {
            "type": "intro",
            "text_es": (
                "Hoy Jin mira la primavera en Madrid. Practicamos una pregunta útil: ¿cómo es...?"
            ),
            "duration_s": 14.0,
            "color_block": "neutral",
            "characters": ["Jin", "Lucía", "Diego"],
        }
    ]
    for block in BLOCKS:
        segments.append(
            {
                "type": "block_header",
                "block_id": block["block_id"],
                "title_es": block["title_es"],
                "title_ko": block["title_ko"],
                "color_block": block["color_block"],
                "duration_s": 3.0,
            }
        )
        for line_num, speaker, text_es, text_ko, focus, block_id, color_block, duration_s in DIALOGUE:
            if block_id != block["block_id"]:
                continue
            segments.append(
                {
                    "type": "dialogue",
                    "line_num": line_num,
                    "speaker": speaker,
                    "text_es": text_es,
                    "text_ko": text_ko,
                    "focus": focus,
                    "block_id": block_id,
                    "color_block": color_block,
                    "duration_s": duration_s,
                    "character": speaker,
                }
            )
    segments.append(
        {
            "type": "outro",
            "text_es": (
                "Muy bien. Ahora puedes preguntar por una estación o un lugar: ¿cómo es la primavera? "
                "¿Cómo es Madrid? Y puedes responder: es agradable, es bonita, hay flores y hace sol."
            ),
            "duration_s": 24.0,
            "color_block": "neutral",
            "characters": ["Jin", "Lucía", "Diego"],
        }
    )
    return segments


SEGMENTS = _build_segments()
CHAPTERS = [
    {"segment": 1, "title": "Introducción"},
    {"segment": 2, "title": "¿Cómo es la primavera?"},
    {"segment": 11, "title": "Es agradable"},
    {"segment": 19, "title": "Hay muchas flores"},
    {"segment": 27, "title": "Mini prueba"},
    {"segment": len(SEGMENTS), "title": "Repaso final"},
]
AUDIO = {
    "tts_engine": "edge",
    "edge_voice": "es-ES-ElviraNeural",
    "edge_rate": "-8%",
    "edge_pitch": "+0Hz",
    "edge_volume": "+0%",
    "voice": "es-ES-ElviraNeural",
    "character_voices": CHARACTER_VOICES,
    "rate_wpm": 142,
    "lead_padding_s": 0.2,
    "tail_padding_s": 0.35,
    "min_duration_s": 3.0,
    "readability_floor_ratio": 0.0,
    "bgm_path": "assets/audio/spanish-lab-brand-bgm.mp3",
    "bgm_volume_db": -4.0,
    "narration_volume_db": 0.0,
    "ducking": True,
    "ducking_threshold": 0.04,
    "ducking_ratio": 6,
    "ducking_attack_ms": 80,
    "ducking_release_ms": 450,
    "fade_in_s": 0.0,
    "fade_out_s": 2.0,
    "audio_codec": "aac",
    "audio_bitrate_kbps": 192,
    "sample_rate_hz": 44100,
}
