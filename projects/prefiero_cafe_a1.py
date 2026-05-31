"""A1+ story-card episode: Jin chooses between coffee and tea with prefiero."""

from __future__ import annotations

IMAGE_PATH = "images/ep19-prefiero-cafe-source.png"
DESCRIP_PATH = "a1-prefiero-cafe/descrip.md"
OUTPUT_NAME = "prefiero-cafe"
PUBLIC_SLUG = "a1-prefiero-cafe"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 19
LEVEL = "A1+"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a1-ep19-prefiero-cafe.jpg"
YOUTUBE_TITLE = "Prefiero café ☕ 저는 커피가 더 좋아요 | Español A1+ · Ep.19"
DESCRIPTION_INTRO = (
    "Jin sigue en Madrid con Lucía y Diego. Hace calor, entran en una cafetería "
    "y Jin aprende a elegir entre dos opciones con una frase simple: prefiero café. "
    "Practicamos prefiero café, prefiero té y prefiero esta cafetería."
)
DESCRIPTION_OUTRO = (
    "Escucha primero, repite en voz alta y después di tu propia preferencia: "
    "prefiero café, prefiero té, o prefiero esta cafetería."
)
KOREAN_TEASER = (
    "한국어 티저: EP.19에서는 둘 중 하나를 고를 때 쓰는 표현을 연습합니다. 핵심 표현은 하나, "
    "Prefiero + 명사입니다. '저는 커피가 더 좋아요', '저는 이 카페가 더 좋아요'처럼 말해 보세요."
)
BASE_TAGS = ["스페인어", "스페인어 입문", "스페인어 A1", "Spanish A1", "aprender español", "español para principiantes"]
EXTRA_TAGS = ["Prefiero", "preferir en español", "Spanish preferences", "Spanish cafe", "스페인어 회화", "스페인어 카페"]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#Madrid", "#Prefiero"]

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
    {"block_id": 1, "title_es": "Hace calor", "title_ko": "더워요", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "¿Café o té?", "title_ko": "커피 아니면 차?", "color_block": "teal", "start": 8},
    {"block_id": 3, "title_es": "Prefiero esta cafetería", "title_ko": "저는 이 카페가 더 좋아요", "color_block": "amber", "start": 19},
    {"block_id": 4, "title_es": "Mini prueba", "title_ko": "미니 퀴즈", "color_block": "blue", "start": 25},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Diego", "Hoy Jin aprende una frase para elegir: prefiero café.", "오늘 Jin은 고르는 표현을 배워요: 저는 커피가 더 좋아요.", "prefiero", 1, "coral", 10.0),
    (2, "Lucía", "Hace calor en Madrid.", "마드리드는 더워요.", "contexto", 1, "coral", 7.5),
    (3, "Diego", "Jin está un poco cansado.", "Jin은 조금 피곤해요.", "contexto", 1, "coral", 7.5),
    (4, "Lucía", "¿Estás bien, Jin?", "괜찮아요, Jin?", "pregunta", 1, "coral", 7.0),
    (5, "Jin", "Sí, pero hace calor.", "네, 그런데 더워요.", "repaso", 1, "coral", 7.5),
    (6, "Diego", "Vamos a una cafetería.", "카페에 가요.", "cafetería", 1, "coral", 7.0),
    (7, "Jin", "Buena idea.", "좋은 생각이에요.", "respuesta", 1, "coral", 6.5),
    (8, "Lucía", "Ya estamos en la cafetería.", "이제 우리는 카페에 있어요.", "cafetería", 2, "teal", 8.0),
    (9, "Lucía", "Jin, ¿café o té?", "Jin, 커피 아니면 차?", "opciones", 2, "teal", 7.5),
    (10, "Jin", "Café... té... no sé.", "커피... 차... 모르겠어요.", "duda", 2, "teal", 7.5),
    (11, "Diego", "Puedes decir: prefiero café.", "이렇게 말할 수 있어요: 저는 커피가 더 좋아요.", "modelo", 2, "teal", 8.5),
    (12, "Jin", "Prefiero café.", "저는 커피가 더 좋아요.", "prefiero café", 2, "teal", 7.0),
    (13, "Diego", "Muy bien. Prefiero significa: es mi opción.", "좋아요. prefiero는 내 선택이라는 뜻이에요.", "significado", 2, "teal", 9.5),
    (14, "Diego", "Yo prefiero té.", "저는 차가 더 좋아요.", "té", 2, "teal", 7.0),
    (15, "Lucía", "Yo prefiero café con leche.", "저는 카페 콘 레체가 더 좋아요.", "café con leche", 2, "teal", 8.0),
    (16, "Lucía", "¿Y tú, Jin?", "그리고 너는, Jin?", "pregunta", 2, "teal", 6.5),
    (17, "Jin", "Prefiero café con leche.", "저는 카페 콘 레체가 더 좋아요.", "respuesta", 2, "teal", 8.0),
    (18, "Diego", "Perfecto: prefiero más una cosa.", "완벽해요: prefiero는 한 가지를 더 좋아한다는 뜻이에요.", "patrón", 2, "teal", 9.0),
    (19, "Lucía", "Ahora mira afuera.", "이제 밖을 봐요.", "afuera", 3, "amber", 7.0),
    (20, "Lucía", "¿Prefieres el parque o esta cafetería?", "공원이 더 좋아요, 아니면 이 카페가 더 좋아요?", "prefieres", 3, "amber", 9.0),
    (21, "Jin", "Prefiero esta cafetería.", "저는 이 카페가 더 좋아요.", "cafetería", 3, "amber", 8.0),
    (22, "Diego", "¿Por qué?", "왜요?", "por qué", 3, "amber", 6.0),
    (23, "Jin", "Porque hace calor.", "왜냐하면 더우니까요.", "razón", 3, "amber", 7.5),
    (24, "Jin", "Me gusta el parque, pero prefiero esta cafetería.", "공원은 좋아요. 그런데 저는 이 카페가 더 좋아요.", "conexión", 3, "amber", 10.0),
    (25, "Diego", "Mini prueba: ¿qué significa prefiero café?", "미니 퀴즈: prefiero café는 무슨 뜻일까요?", "quiz", 4, "blue", 9.5),
    (26, "Lucía", "Significa: café es mi opción.", "뜻은 커피가 내 선택이라는 거예요.", "respuesta", 4, "blue", 8.0),
    (27, "Diego", "Pregunta: ¿café o té?", "질문: 커피 아니면 차?", "pregunta", 4, "blue", 7.5),
    (28, "Jin", "Respuesta: prefiero café.", "대답: 저는 커피가 더 좋아요.", "respuesta", 4, "blue", 7.5),
    (29, "Diego", "Otra frase: prefiero esta cafetería.", "다른 문장: 저는 이 카페가 더 좋아요.", "otra frase", 4, "blue", 8.5),
    (30, "Diego", "Excelente. Ya puedes decir una preferencia.", "훌륭해요. 이제 선호를 말할 수 있어요.", "cierre", 4, "blue", 9.0),
]

DESIGN = {
    "output_size": (1280, 720),
    "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
    "font_index": 0,
    "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
    "font_index_ko": 0,
    "font_size_title": 66,
    "font_size_es": 62,
    "min_font_size_es": 34,
    "font_size_ko": 32,
    "font_size_example": 30,
    "background_color": (248, 247, 242),
    "text_color": (31, 35, 40),
    "muted_text_color": (96, 101, 109),
    "intro_title": "Prefiero café",
    "intro_subtitle": "Español A1+ · Ep.19",
    "intro_ko": "저는 커피가 더 좋아요",
    "intro_scene_image_path": "images/ep19-prefiero-cafe-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "Prefiero café",
    "thumbnail_subtitle": "Español A1+ · Ep.19",
    "thumbnail_ko": "저는 커피가 더 좋아요",
    "outro_ko": "이제 스페인어로 선호를 말할 수 있어요",
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
            "text_es": "Hoy Jin aprende a elegir con una frase simple: prefiero café.",
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
                "Muy bien. Ahora puedes decir: prefiero café, "
                "prefiero té o prefiero esta cafetería."
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
    {"segment": 2, "title": "Hace calor"},
    {"segment": 10, "title": "¿Café o té?"},
    {"segment": 22, "title": "Prefiero esta cafetería"},
    {"segment": 29, "title": "Mini prueba"},
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
