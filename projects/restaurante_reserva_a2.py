"""A2 entry story-card episode: Jin makes a restaurant reservation."""

from __future__ import annotations

IMAGE_PATH = "images/ep32-restaurante-reserva-source.png"
DESCRIP_PATH = "a2-restaurante-reserva/descrip.md"
OUTPUT_NAME = "restaurante-reserva"
PUBLIC_SLUG = "a2-restaurante-reserva"
YOUTUBE_URL = ""
SERIES = "frases-a2"
SERIES_TITLE = "Español A2 -- Frases útiles"
EPISODE = 32
LEVEL = "A2 입문"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a2-ep32-restaurante-reserva.jpg"
YOUTUBE_TITLE = "Quiero reservar una mesa 🍽️ 테이블을 예약하고 싶어요 | Español A2 · Ep.32"
DESCRIPTION_INTRO = (
    "Jin sigue aprendiendo situaciones prácticas en el restaurante. "
    "En este episodio aprende a reservar una mesa por teléfono dando los detalles clave: "
    "número de personas, hora y nombre."
)
DESCRIPTION_OUTRO = (
    "Escucha primero, repite en voz alta y practica cambiando los detalles: "
    "una mesa para dos, tres o cuatro personas, a las ocho, a las nueve y a tu nombre."
)
KOREAN_TEASER = (
    "한국어 티저: EP.32 레스토랑 예약 편입니다. "
    "스페인어 식당 예약의 필수 패턴인 'Quiero reservar una mesa para [인원], a las [시간], a nombre de [이름]'을 연습해 봅니다. "
    "인원과 시간을 자유롭게 바꾸어 가며 전화 예약을 마스터해 보세요!"
)
BASE_TAGS = ["스페인어", "스페인어 입문", "스페인어 A2", "Spanish A2", "aprender español", "español para coreanos"]
EXTRA_TAGS = ["reservar una mesa", "restaurante español", "Spanish restaurant reservation", "스페인어 회화", "식당 예약 스페인어"]
BASE_HASHTAGS = ["#EspañolA2", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#Restaurante", "#Reserva", "#SpanishLab"]

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
    {"block_id": 1, "title_es": "La reserva", "title_ko": "예약", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "Los detalles", "title_ko": "인원과 시각", "color_block": "teal", "start": 9},
    {"block_id": 3, "title_es": "El nombre", "title_ko": "이름", "color_block": "amber", "start": 15},
    {"block_id": 4, "title_es": "Mini prueba", "title_ko": "미니 퀴즈", "color_block": "blue", "start": 24},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Diego", "Hoy aprendemos a hacer una reserva en un restaurante.", "오늘은 레스토랑 예약 방법을 배워요.", "A2", 1, "coral", 8.0),
    (2, "Lucía", "Jin quiere cenar en un restaurante español muy popular.", "Jin은 아주 인기 있는 스페인 레스토랑에서 저녁을 먹고 싶어 해요.", "contexto", 1, "coral", 9.0),
    (3, "Diego", "Llama por teléfono para reservar una mesa.", "테이블을 예약하기 위해 전화를 걸어요.", "teléfono", 1, "coral", 7.5),
    (4, "Lucía", "Primero dice: Quiero reservar.", "먼저 '예약하고 싶어요'라고 말해요.", "reserva", 1, "coral", 7.5),
    (5, "Jin", "Quiero reservar.", "예약하고 싶어요.", "modelo", 1, "coral", 6.5),
    (6, "Diego", "Muy bien. Reservar significa: asegurar una mesa.", "좋아요. Reservar는 테이블을 확보한다는 뜻이에요.", "significado", 1, "coral", 8.0),
    (7, "Lucía", "Escucha la primera parte: Quiero reservar una mesa.", "첫 부분을 들어 보세요: 테이블을 예약하고 싶어요.", "modelo", 1, "coral", 8.5),
    (8, "Jin", "Quiero reservar una mesa.", "테이블을 예약하고 싶어요.", "modelo", 1, "coral", 7.0),
    (9, "Diego", "Ahora añadimos el número de personas: para dos.", "이제 인원수를 더해요: 두 명을 위해.", "personas", 2, "teal", 8.5),
    (10, "Lucía", "Para dos significa: para dos personas.", "para dos는 ‘두 명’이라는 뜻이에요.", "significado", 2, "teal", 7.5),
    (11, "Jin", "Quiero reservar una mesa para dos.", "두 명 테이블을 예약하고 싶어요.", "modelo", 2, "teal", 8.0),
    (12, "Diego", "Muy natural. También podemos decir cuándo: a las ocho.", "아주 자연스러워요. 언제인지도 말할 수 있어요: 8시에.", "hora", 2, "teal", 9.0),
    (13, "Lucía", "A las ocho significa: a las 8 de la noche.", "a las ocho는 ‘8시에’라는 뜻이에요.", "significado", 2, "teal", 7.5),
    (14, "Jin", "Quiero reservar una mesa para dos, a las ocho.", "8시에 두 명 테이블을 예약하고 싶어요.", "modelo", 2, "teal", 9.0),
    (15, "Diego", "Por último, decimos el nombre para la reserva: a nombre de.", "마지막으로 예약을 위한 이름을 말해요: ~의 이름으로.", "nombre", 3, "amber", 9.5),
    (16, "Lucía", "A nombre de significa: bajo el nombre de.", "a nombre de는 ‘~의 이름으로’라는 뜻이에요.", "significado", 3, "amber", 8.0),
    (17, "Jin", "A nombre de Jin.", "Jin의 이름으로요.", "modelo", 3, "amber", 6.5),
    (18, "Diego", "Escucha la frase completa ahora.", "이제 전체 문장을 들어 보세요.", "completa", 3, "amber", 7.5),
    (19, "Jin", "Quiero reservar una mesa para dos, a las ocho, a nombre de Jin.", "Jin의 이름으로 8시에 두 명 테이블을 예약하고 싶어요.", "modelo", 3, "amber", 10.0),
    (20, "Lucía", "Excelente. Es una frase muy completa y útil.", "훌륭해요. 아주 완전하고 유용한 문장이에요.", "natural", 3, "amber", 8.5),
    (21, "Diego", "¿Y si son cuatro personas?", "만약 네 명이라면요?", "variación", 3, "amber", 7.0),
    (22, "Jin", "Quiero reservar una mesa para cuatro.", "네 명 테이블을 예약하고 싶어요.", "variación", 3, "amber", 7.5),
    (23, "Lucía", "Muy bien. Solo cambias el número.", "좋아요. 숫자만 바꾸면 돼요.", "explicación", 3, "amber", 7.0),
    (24, "Diego", "Mini prueba: ¿qué significa una mesa para dos?", "미니 퀴즈: una mesa para dos는 무슨 뜻일까요?", "quiz", 4, "blue", 8.5),
    (25, "Lucía", "Significa: 두 명 테이블.", "뜻은 ‘두 명 테이블’이에요.", "respuesta", 4, "blue", 7.0),
    (26, "Diego", "¿Cómo dices esta frase en español?", "이 문장을 스페인어로 어떻게 말할까요?", "pregunta", 4, "blue", 8.0),
    (27, "Jin", "Quiero reservar una mesa para dos, a las ocho, a nombre de Jin.", "Jin의 이름으로 8시에 두 명 테이블을 예약하고 싶어요.", "respuesta", 4, "blue", 10.0),
    (28, "Lucía", "¿Cómo dices ‘네 명 테이블을 예약하고 싶어요’?", "‘네 명 테이블을 예약하고 싶어요’를 어떻게 말할까요?", "pregunta", 4, "blue", 8.5),
    (29, "Jin", "Quiero reservar una mesa para cuatro.", "네 명 테이블을 예약하고 싶어요.", "respuesta", 4, "blue", 7.5),
    (30, "Diego", "Muy bien. Ya puedes reservar una mesa en español.", "좋아요. 이제 스페인어로 테이블을 예약할 수 있어요.", "cierre", 4, "blue", 8.5),
]

DESIGN = {
    "output_size": (1280, 720),
    "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
    "font_index": 0,
    "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
    "font_index_ko": 0,
    "font_size_title": 64,
    "font_size_es": 60,
    "min_font_size_es": 30,
    "font_size_ko": 32,
    "font_size_example": 30,
    "background_color": (248, 247, 242),
    "text_color": (31, 35, 40),
    "muted_text_color": (96, 101, 109),
    "intro_title": "Quiero reservar una mesa",
    "intro_subtitle": "Español A2 · Ep.32",
    "intro_ko": "테이블을 예약하고 싶어요",
    "intro_scene_image_path": "images/ep32-restaurante-reserva-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "Quiero reservar una mesa",
    "thumbnail_subtitle": "Español A2 · Ep.32",
    "thumbnail_ko": "테이블을 예약하고 싶어요",
    "outro_ko": "이제 스페인어로 식당 예약을 멋지게 할 수 있어요",
    "conversation_label": "Conversación A2",
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
            "text_es": "Hoy Jin aprende a reservar una mesa por teléfono dando los detalles clave: personas, hora y nombre.",
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
                "Muy bien. Ahora puedes reservar una mesa con todos los detalles: "
                "una mesa para dos, tres o cuatro personas, a las ocho, a las nueve y a tu nombre."
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
    {"segment": 2, "title": "La reserva"},
    {"segment": 11, "title": "Los detalles"},
    {"segment": 18, "title": "El nombre"},
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
