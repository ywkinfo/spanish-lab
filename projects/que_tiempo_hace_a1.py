"""A1 story-card episode: Jin asks about the weather in Madrid."""

from __future__ import annotations

IMAGE_PATH = "images/ep16-que-tiempo-hace-source.png"
DESCRIP_PATH = "a1-que-tiempo-hace/descrip.md"
OUTPUT_NAME = "que-tiempo-hace"
PUBLIC_SLUG = "a1-que-tiempo-hace"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 16
LEVEL = "A1"
LANGUAGE = "es"
RENDER_VERSION = 2
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a1-ep16-que-tiempo-hace.jpg"
YOUTUBE_TITLE = "¿Qué tiempo hace? ☀️ 날씨가 어때? | Español A1 · Ep.16"
DESCRIPTION_INTRO = (
    "Jin mira el cielo de Madrid con Lucía y Diego. En este episodio A1 practicamos "
    "una pregunta muy útil para hablar del tiempo: ¿Qué tiempo hace? Aprende respuestas "
    "simples con hace: hace sol, hace frío, hace calor, hace viento y hace buen tiempo."
)
DESCRIPTION_OUTRO = (
    "Escucha primero, repite en voz alta y después responde con tu ciudad: "
    "¿Qué tiempo hace hoy? Hace sol, hace frío, hace calor, hace viento o hace buen tiempo."
)
KOREAN_TEASER = (
    "한국어 티저: EP.16에서는 날씨를 묻는 A1 질문 ¿Qué tiempo hace?를 연습합니다. "
    "Hace sol, Hace frío, Hace calor처럼 hace로 간단히 대답해 보세요."
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
    "Qué tiempo hace",
    "clima español A1",
    "weather in Spanish",
    "hace sol",
    "hace frío",
    "hace calor",
    "스페인어 날씨",
    "스페인어 회화",
]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#Madrid", "#날씨표현"]

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
    {"block_id": 1, "title_es": "¿Qué tiempo hace?", "title_ko": "날씨가 어때?", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "Hace sol", "title_ko": "해가 나요", "color_block": "amber", "start": 8},
    {"block_id": 3, "title_es": "Hace frío / calor", "title_ko": "추워요 / 더워요", "color_block": "teal", "start": 15},
    {"block_id": 4, "title_es": "Mini prueba", "title_ko": "미니 퀴즈", "color_block": "blue", "start": 23},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Diego", "Hoy hablamos del tiempo en Madrid.", "오늘은 마드리드의 날씨에 대해 이야기해요.", "el tiempo", 1, "coral", 8.5),
    (2, "Jin", "Lucía, ¿qué tiempo hace hoy?", "Lucía, 오늘 날씨가 어때?", "¿qué tiempo hace?", 1, "coral", 9.0),
    (3, "Lucía", "Hoy hace buen tiempo.", "오늘은 날씨가 좋아.", "hace buen tiempo", 1, "coral", 8.0),
    (4, "Diego", "Repite la pregunta: ¿qué tiempo hace?", "질문을 따라 해 봐요: ¿qué tiempo hace?", "repite", 1, "coral", 9.5),
    (5, "Jin", "¿Qué tiempo hace?", "날씨가 어때?", "pregunta", 1, "coral", 8.0),
    (6, "Diego", "Muy bien. Para el tiempo usamos mucho hace.", "아주 좋아요. 날씨에는 hace를 많이 써요.", "hace", 1, "coral", 9.5),
    (7, "Jin", "Hace buen tiempo.", "날씨가 좋아요.", "hace buen tiempo", 1, "coral", 8.0),
    (8, "Lucía", "Mira el cielo. Hace sol.", "하늘을 봐. 해가 나.", "hace sol", 2, "amber", 8.0),
    (9, "Jin", "Hace sol.", "해가 나요.", "hace sol", 2, "amber", 7.0),
    (10, "Diego", "Literalmente: hace sol.", "직역하면: ‘해를 만들어요’에 가까워요.", "traducción literal", 2, "amber", 9.5),
    (11, "Diego", "Naturalmente: hace sol.", "자연스러운 한국어로는: 해가 나요.", "traducción natural", 2, "amber", 8.5),
    (12, "Lucía", "Sí. Hace sol y hace buen tiempo.", "맞아. 해가 나고 날씨가 좋아.", "sol + buen tiempo", 2, "amber", 8.5),
    (13, "Jin", "Hace sol y hace buen tiempo.", "해가 나고 날씨가 좋아요.", "frase completa", 2, "amber", 9.0),
    (14, "Diego", "Perfecto. Una vez más: hace sol.", "완벽해요. 한 번 더: hace sol.", "shadowing", 2, "amber", 8.5),
    (15, "Lucía", "Por la mañana hace un poco de frío.", "아침에는 조금 추워.", "hace frío", 3, "teal", 9.5),
    (16, "Jin", "Hace frío.", "추워요.", "hace frío", 3, "teal", 7.0),
    (17, "Diego", "Hace frío habla del tiempo.", "Hace frío는 ‘날씨가 추워요’라는 뜻이에요.", "significado", 3, "teal", 9.5),
    (18, "Lucía", "Pero al mediodía hace calor.", "하지만 정오에는 더워.", "hace calor", 3, "teal", 8.5),
    (19, "Jin", "Hace calor.", "더워요.", "hace calor", 3, "teal", 7.0),
    (20, "Diego", "Frío y calor también van con hace.", "frío와 calor도 hace와 함께 써요.", "hace + clima", 3, "teal", 9.0),
    (21, "Lucía", "A veces hace viento.", "가끔 바람이 불어.", "hace viento", 3, "teal", 8.0),
    (22, "Jin", "Hace viento.", "바람이 불어요.", "hace viento", 3, "teal", 7.0),
    (23, "Diego", "Ahora una mini prueba.", "이제 미니 퀴즈예요.", "mini prueba", 4, "blue", 7.5),
    (24, "Diego", "Pregunta: ¿qué tiempo hace hoy?", "질문: 오늘 날씨가 어때?", "pregunta", 4, "blue", 8.5),
    (25, "Jin", "Respuesta uno: hace sol.", "대답 하나: 해가 나요.", "respuesta 1", 4, "blue", 8.0),
    (26, "Lucía", "Respuesta dos: hace buen tiempo.", "대답 둘: 날씨가 좋아요.", "respuesta 2", 4, "blue", 8.5),
    (27, "Diego", "Si tienes frío, di: hace frío.", "추우면 이렇게 말해요: hace frío.", "hace frío", 4, "blue", 8.5),
    (28, "Jin", "Hoy en Madrid hace sol.", "오늘 마드리드는 해가 나요.", "frase completa", 4, "blue", 8.5),
    (29, "Lucía", "Y hace buen tiempo.", "그리고 날씨가 좋아요.", "buen tiempo", 4, "blue", 7.5),
    (30, "Diego", "Excelente. Ya puedes preguntar por el tiempo.", "훌륭해요. 이제 날씨를 물어볼 수 있어요.", "cierre", 4, "blue", 9.5),
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
    "intro_title": "¿Qué tiempo hace?",
    "intro_subtitle": "Español A1 · Ep.16",
    "intro_ko": "날씨가 어때?",
    "intro_scene_image_path": "images/ep16-que-tiempo-hace-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "¿Qué tiempo hace?",
    "thumbnail_subtitle": "Español A1 · Ep.16",
    "thumbnail_ko": "오늘 날씨가 어때?",
    "outro_ko": "이제 스페인어로 날씨를 물어볼 수 있어요",
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
            "text_es": "Hoy Jin mira el cielo de Madrid. Practicamos una pregunta útil: ¿qué tiempo hace?",
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
                "duration_s": 3.5,
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
                "Muy bien. Ahora puedes preguntar: ¿qué tiempo hace? "
                "Y puedes responder con hace: hace sol, hace frío, hace calor, hace viento o hace buen tiempo."
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
    {"segment": 2, "title": "¿Qué tiempo hace?"},
    {"segment": 11, "title": "Hace sol"},
    {"segment": 19, "title": "Hace frío y calor"},
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
