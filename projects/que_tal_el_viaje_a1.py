"""A1 travel follow-up story episode: Jin talks about his weekend trip."""

from __future__ import annotations

IMAGE_PATH = "assets/generated/ep12-que-tal-el-viaje-source.png"
DESCRIP_PATH = "a1-que-tal-el-viaje/descrip.md"
OUTPUT_NAME = "que-tal-el-viaje"
PUBLIC_SLUG = "a1-que-tal-el-viaje"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 12
LEVEL = "A1"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a1-que-tal-el-viaje.jpg"
YOUTUBE_TITLE = "¿Qué tal el viaje? 🚆 여행 어땠어? | Español A1 · Ep.12"
DESCRIPTION_INTRO = (
    "Después de preguntar la hora y tomar el tren, Jin vuelve de un viaje corto a Toledo. "
    "Lucía y Diego le preguntan: ¿Qué tal el viaje?, ¿Fuiste en tren?, ¿Qué hiciste allí? "
    "y ¿Te gustó? Practicamos frases A1 para hablar de un fin de semana y de un viaje sencillo."
)
DESCRIPTION_OUTRO = (
    "Escucha primero, repite en voz alta y después cuenta tu propio viaje: "
    "Fui a Toledo, fui en tren, visité la ciudad, saqué fotos y me gustó mucho."
)
KOREAN_TEASER = (
    "한국어 티저: EP.12는 EP.11에서 기차를 탄 뒤 이어지는 여행 후 회화입니다. "
    "Jin과 함께 ¿Qué tal el viaje?, Fui en tren, ¿Qué hiciste allí?, Me gustó mucho를 연습합니다."
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
    "que tal el viaje",
    "viaje en español",
    "fin de semana en español",
    "tren en español",
    "Toledo en español",
    "conversacion español A1",
    "스페인어 여행",
    "스페인어 주말",
    "스페인어 기차",
]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#frasesenespañol", "#viaje"]

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
    {"block_id": 1, "title_es": "¿Qué tal el viaje?", "title_ko": "여행 어땠어?", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "Fui en tren", "title_ko": "기차로 갔어", "color_block": "amber", "start": 4},
    {"block_id": 3, "title_es": "¿Qué hiciste allí?", "title_ko": "거기서 뭐 했어?", "color_block": "teal", "start": 11},
    {"block_id": 4, "title_es": "Me gustó mucho", "title_ko": "정말 마음에 들었어", "color_block": "blue", "start": 19},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Lucía", "Hola, Jin. ¿Qué tal el viaje?", "안녕, Jin. 여행 어땠어?", "¿Qué tal el viaje?", 1, "coral", 8.5),
    (2, "Jin", "Muy bien. Fui a Toledo el fin de semana.", "아주 좋았어. 주말에 톨레도에 갔어.", "fui a Toledo", 1, "coral", 9.5),
    (3, "Diego", "¡Qué bien!", "좋다!", "¡Qué bien!", 1, "coral", 7.0),
    (4, "Lucía", "¿Fuiste en tren?", "기차로 갔어?", "¿Fuiste en tren?", 2, "amber", 8.0),
    (5, "Jin", "Sí, fui en tren.", "응, 기차로 갔어.", "fui en tren", 2, "amber", 8.0),
    (6, "Jin", "El viaje fue corto.", "여행은 짧았어.", "fue corto", 2, "amber", 8.0),
    (7, "Diego", "¿Cuánto tardó?", "얼마나 걸렸어?", "¿Cuánto tardó?", 2, "amber", 8.0),
    (8, "Jin", "Tardó veinte minutos.", "20분 걸렸어.", "tardó", 2, "amber", 8.0),
    (9, "Lucía", "Entonces fue rápido.", "그러면 빨랐네.", "fue rápido", 2, "amber", 8.0),
    (10, "Jin", "Sí, fue rápido y cómodo.", "응, 빠르고 편했어.", "rápido y cómodo", 2, "amber", 8.5),
    (11, "Diego", "¿Qué hiciste allí?", "거기서 뭐 했어?", "¿Qué hiciste allí?", 3, "teal", 8.0),
    (12, "Jin", "Visité la ciudad.", "도시를 구경했어.", "visité", 3, "teal", 8.0),
    (13, "Lucía", "¿Viste la catedral?", "대성당을 봤어?", "¿Viste?", 3, "teal", 8.0),
    (14, "Jin", "Sí, vi la catedral.", "응, 대성당을 봤어.", "vi", 3, "teal", 8.0),
    (15, "Jin", "También saqué fotos.", "사진도 찍었어.", "saqué fotos", 3, "teal", 8.0),
    (16, "Diego", "¿Sacaste muchas fotos?", "사진을 많이 찍었어?", "¿Sacaste?", 3, "teal", 8.0),
    (17, "Jin", "Sí, saqué muchas fotos.", "응, 사진을 많이 찍었어.", "saqué", 3, "teal", 8.0),
    (18, "Lucía", "¡Qué bonito!", "정말 예쁘겠다!", "¡Qué bonito!", 3, "teal", 7.0),
    (19, "Lucía", "¿Comiste algo rico?", "맛있는 것도 먹었어?", "¿Comiste?", 4, "blue", 8.0),
    (20, "Jin", "Sí, comí algo rico.", "응, 맛있는 걸 먹었어.", "comí", 4, "blue", 8.0),
    (21, "Jin", "Comí una tortilla pequeña.", "작은 토르티야를 먹었어.", "tortilla", 4, "blue", 8.5),
    (22, "Diego", "¿Te gustó?", "마음에 들었어?", "¿Te gustó?", 4, "blue", 8.0),
    (23, "Jin", "Sí, me gustó mucho.", "응, 정말 마음에 들었어.", "me gustó mucho", 4, "blue", 8.0),
    (24, "Lucía", "Toledo es muy bonito.", "톨레도는 정말 예뻐.", "Toledo", 4, "blue", 8.0),
    (25, "Jin", "Quiero volver.", "다시 가고 싶어.", "quiero volver", 4, "blue", 8.0),
    (26, "Diego", "¿Quieres volver el próximo fin de semana?", "다음 주말에 다시 가고 싶어?", "próximo fin de semana", 4, "blue", 9.5),
    (27, "Jin", "Tal vez. Pero hoy descanso.", "아마도. 하지만 오늘은 쉬어.", "hoy descanso", 4, "blue", 8.5),
    (28, "Lucía", "Muy bien. Después del viaje, descanso.", "좋아. 여행 후에는 휴식이지.", "después del viaje", 4, "blue", 9.0),
    (29, "Diego", "Y ahora, español.", "그리고 이제 스페인어지.", "ahora", 4, "blue", 7.5),
    (30, "Jin", "Sí. Viaje y español. Perfecto.", "응. 여행과 스페인어. 완벽해.", "perfecto", 4, "blue", 8.5),
]

DESIGN = {
    "output_size": (1280, 720),
    "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
    "font_index": 0,
    "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
    "font_index_ko": 0,
    "font_size_title": 70,
    "font_size_es": 68,
    "min_font_size_es": 38,
    "font_size_ko": 32,
    "font_size_example": 30,
    "background_color": (248, 247, 242),
    "text_color": (31, 35, 40),
    "muted_text_color": (96, 101, 109),
    "intro_title": "¿Qué tal el viaje?",
    "intro_subtitle": "Español A1 · Ep.12",
    "intro_ko": "여행 어땠어?",
    "intro_scene_image_path": "assets/generated/ep12-que-tal-el-viaje-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "¿Qué tal el viaje?",
    "thumbnail_subtitle": "Español A1 · Ep.12",
    "thumbnail_ko": "여행 어땠어?",
    "outro_ko": "이제 스페인어로 주말 여행 이야기를 할 수 있어요",
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
                "Hoy seguimos el viaje de Jin. Ya tomó el tren. "
                "Ahora habla con Lucía y Diego sobre su fin de semana en Toledo."
            ),
            "duration_s": 13.0,
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
                "Muy bien. Ahora puedes hablar de un viaje sencillo: ¿Qué tal el viaje? "
                "Fui en tren. Visité la ciudad. Saqué fotos. Comí algo rico. Me gustó mucho."
            ),
            "duration_s": 22.0,
            "color_block": "neutral",
            "characters": ["Jin", "Lucía", "Diego"],
        }
    )
    return segments


SEGMENTS = _build_segments()
CHAPTERS = [
    {"segment": 1, "title": "Introducción"},
    {"segment": 2, "title": "¿Qué tal el viaje?"},
    {"segment": 6, "title": "Fui en tren"},
    {"segment": 14, "title": "¿Qué hiciste allí?"},
    {"segment": 23, "title": "Me gustó mucho"},
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
