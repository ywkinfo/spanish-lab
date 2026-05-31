"""A1+ story-card episode: Jin asks for another color in a shop."""

from __future__ import annotations

IMAGE_PATH = "images/ep30-tiene-otro-color-source.png"
DESCRIP_PATH = "a1-tiene-otro-color/descrip.md"
OUTPUT_NAME = "tiene-otro-color"
PUBLIC_SLUG = "a1-tiene-otro-color"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 30
LEVEL = "A1+"
LANGUAGE = "es"
RENDER_VERSION = 2
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/ep30-tiene-otro-color.jpg"
YOUTUBE_TITLE = "¿Tiene otro color? 🛍️ 다른 색 있어요? | Español A1+ · Ep.30"
DESCRIPTION_INTRO = (
    "Jin está en una tienda y aprende una pregunta muy práctica antes de comprar: "
    "¿Tiene otro color?"
)
DESCRIPTION_OUTRO = (
    "Escucha, repite en voz alta y usa la frase como una unidad: "
    "¿Tiene otro color?, ¿tiene otro color?, ¿tiene otra talla?"
)
KOREAN_TEASER = (
    "한국어 티저: EP.30은 여행 쇼핑에서 바로 쓰는 A1+ 질문입니다. "
    "핵심은 하나, ¿Tiene otro color?입니다. "
    "마음에 드는 물건을 봤을 때 '다른 색 있어요?'를 자연스럽게 말해 보세요."
)
BASE_TAGS = ["스페인어", "스페인어 입문", "스페인어 A1", "Spanish A1", "aprender español", "español para coreanos"]
EXTRA_TAGS = ["¿Tiene otro color?", "스페인어 쇼핑", "스페인어 여행", "Spanish shopping", "Spanish Lab", "스페인어 회화"]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#TieneOtroColor", "#SpanishLab"]

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
    {"block_id": 1, "title_es": "¿Tiene otro color?", "title_ko": "다른 색 있어요?", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "Una pregunta útil", "title_ko": "덩어리로 기억하기", "color_block": "teal", "start": 8},
    {"block_id": 3, "title_es": "En la tienda", "title_ko": "가게에서 말하기", "color_block": "amber", "start": 16},
    {"block_id": 4, "title_es": "Mini prueba", "title_ko": "미니 퀴즈", "color_block": "blue", "start": 24},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Diego", "Estamos en una tienda de recuerdos.", "우리는 기념품 가게에 있어요.", "contexto", 1, "coral", 7.5),
    (2, "Lucía", "Jin mira una bufanda azul.", "Jin은 파란색 스카프를 보고 있어요.", "situación", 1, "coral", 7.5),
    (3, "Jin", "Me gusta esta bufanda.", "이 스카프가 마음에 들어요.", "objeto", 1, "coral", 7.0),
    (4, "Diego", "Muy bien. Hoy preguntamos por otra opción.", "좋아요. 오늘은 다른 선택지를 물어봐요.", "función", 1, "coral", 8.0),
    (5, "Diego", "La frase es: ¿Tiene otro color?", "표현은 ¿Tiene otro color?예요.", "clave", 1, "coral", 7.5),
    (6, "Jin", "¿Tiene otro color?", "다른 색 있어요?", "modelo", 1, "coral", 6.5),
    (7, "Lucía", "Sí. Es una pregunta muy natural.", "네. 아주 자연스러운 질문이에요.", "natural", 1, "coral", 7.5),
    (8, "Diego", "Primero, escucha la frase completa.", "먼저 전체 표현을 들어 보세요.", "escucha", 2, "teal", 7.0),
    (9, "Diego", "Literalmente: ¿tiene otro color?", "직역하면 다른 색을 가지고 있나요?예요.", "literal", 2, "teal", 8.0),
    (10, "Lucía", "Naturalmente: ¿hay otro color?", "자연스럽게는 “다른 색 있어요?”예요.", "natural", 2, "teal", 7.5),
    (11, "Diego", "Recuerda la frase como una unidad.", "표현 전체를 한 덩어리로 기억하세요.", "frase", 2, "teal", 8.0),
    (12, "Jin", "¿Tiene otro color?", "다른 색 있어요?", "repetición", 2, "teal", 6.5),
    (13, "Diego", "También puedes cambiar una palabra.", "단어 하나만 바꿀 수도 있어요.", "variación", 2, "teal", 7.5),
    (14, "Lucía", "¿Tiene otra talla?", "다른 사이즈 있어요?", "variación", 2, "teal", 7.0),
    (15, "Diego", "Pero el patrón es el mismo.", "하지만 패턴은 같아요.", "patrón", 2, "teal", 7.5),
    (16, "Diego", "Ahora practicamos en una mini conversación.", "이제 짧은 대화로 연습해요.", "diálogo", 3, "amber", 7.5),
    (17, "Lucía", "¿Le gusta esta bufanda?", "이 스카프 마음에 드세요?", "pregunta", 3, "amber", 7.0),
    (18, "Jin", "Sí, me gusta mucho.", "네, 정말 마음에 들어요.", "respuesta", 3, "amber", 6.5),
    (19, "Jin", "¿Tiene otro color?", "다른 색 있어요?", "pregunta", 3, "amber", 6.8),
    (20, "Lucía", "Sí, tenemos rojo y verde.", "네, 빨간색과 초록색이 있어요.", "respuesta", 3, "amber", 7.0),
    (21, "Jin", "Perfecto. ¿Puedo ver el rojo?", "좋아요. 빨간색을 볼 수 있을까요?", "respuesta", 3, "amber", 7.5),
    (22, "Diego", "Muy bien. Suena claro y educado.", "아주 좋아요. 분명하고 예의 있게 들려요.", "feedback", 3, "amber", 7.5),
    (23, "Jin", "¿Tiene otro color?", "다른 색 있어요?", "shadowing", 3, "amber", 6.8),
    (24, "Diego", "Mini prueba. ¿Cómo dices esta pregunta?", "미니 퀴즈. 이 질문을 어떻게 말할까요?", "quiz", 4, "blue", 8.0),
    (25, "Jin", "¿Tiene otro color?", "다른 색 있어요?", "respuesta", 4, "blue", 6.5),
    (26, "Lucía", "Muy bien. Ahora con otra palabra.", "아주 좋아요. 이제 다른 단어로요.", "variación", 4, "blue", 7.0),
    (27, "Jin", "¿Tiene otra talla?", "다른 사이즈 있어요?", "respuesta", 4, "blue", 7.0),
    (28, "Diego", "¿Qué significa en coreano natural?", "자연스러운 한국어 뜻은 무엇일까요?", "quiz", 4, "blue", 8.0),
    (29, "Lucía", "Significa: ¿hay otro color disponible?", "“다른 색 있어요?”라는 뜻이에요.", "respuesta", 4, "blue", 8.0),
]

DESIGN = {
    "output_size": (1280, 720),
    "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
    "font_index": 0,
    "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
    "font_index_ko": 0,
    "font_size_title": 56,
    "font_size_es": 58,
    "min_font_size_es": 30,
    "font_size_ko": 32,
    "font_size_example": 30,
    "background_color": (248, 247, 242),
    "text_color": (31, 35, 40),
    "muted_text_color": (96, 101, 109),
    "intro_title": "¿Tiene otro color?",
    "intro_subtitle": "Español A1+ · Ep.30",
    "intro_ko": "다른 색 있어요?",
    "intro_scene_image_path": "images/ep30-tiene-otro-color-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "¿Tiene otro color?",
    "thumbnail_subtitle": "Español A1+ · Ep.30",
    "thumbnail_ko": "다른 색 있어요?",
    "outro_ko": "이제 스페인어로 쇼핑할 때 '다른 색 있어요?'를 말할 수 있어요",
    "conversation_label": "Conversación A1+",
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
            "text_es": "Hoy Jin aprende una pregunta para comprar con calma: ¿Tiene otro color?",
            "duration_s": 15.0,
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
                "Muy bien. Ahora puedes preguntar por otra opción en una tienda: "
                "¿Tiene otro color?, ¿tiene otro color?, ¿tiene otra talla?"
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
    {"segment": 2, "title": "¿Tiene otro color?"},
    {"segment": 10, "title": "Una pregunta útil"},
    {"segment": 19, "title": "En la tienda"},
    {"segment": 28, "title": "Mini prueba"},
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
