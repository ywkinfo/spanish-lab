"""A2 entry story-card episode: Jin orders food at a restaurant."""

from __future__ import annotations

IMAGE_PATH = "images/ep34-en-el-restaurante-pedir-source.png"
DESCRIP_PATH = "a2-en-el-restaurante-pedir/descrip.md"
OUTPUT_NAME = "en-el-restaurante-pedir"
PUBLIC_SLUG = "a2-en-el-restaurante-pedir"
YOUTUBE_URL = ""
SERIES = "frases-a2"
SERIES_TITLE = "Español A2 -- Frases útiles"
EPISODE = 34
LEVEL = "A2 입문"
LANGUAGE = "es"
RENDER_VERSION = 2
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a2-ep34-en-el-restaurante-pedir.jpg"
YOUTUBE_TITLE = "¿Qué nos recomienda? 🍽️ 어떤 걸 추천해요? | Español A2 · Ep.34"
DESCRIPTION_INTRO = (
    "Jin y Lucía van a cenar a un restaurante español. "
    "En este episodio Jin aprende a pedir recomendaciones al camarero y a pedir la comida de forma educada."
)
DESCRIPTION_OUTRO = (
    "Escucha primero, repite en voz alta y practica las expresiones: "
    "¿Qué nos recomienda?, Para mí la paella, y Para dos personas, por favor."
)
KOREAN_TEASER = (
    "한국어 티저: EP.34 레스토랑 주문 편입니다. "
    "스페인 식당에서 음식을 주문할 때 유용한 패턴인 '¿Qué nos recomienda?(어떤 걸 추천해요?)'와 'Para mí, (음식)(저는 ~로 할게요)'을 배웁니다. "
    "파에야와 물을 점원에게 친절하고 공손하게 주문해 보세요!"
)
BASE_TAGS = ["스페인어", "스페인어 입문", "스페인어 A2", "Spanish A2", "aprender español", "español para coreanos"]
EXTRA_TAGS = ["pedir en restaurante", "paella de marisco", "recomienda", "Spanish ordering food", "스페인어 회화", "식당 주문 스페인어"]
BASE_HASHTAGS = ["#EspañolA2", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#Restaurante", "#Paella", "#SpanishLab"]

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
    {"block_id": 1, "title_es": "El menú", "title_ko": "메뉴 읽기", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "La recomendación", "title_ko": "추천 요청", "color_block": "teal", "start": 10},
    {"block_id": 3, "title_es": "El pedido", "title_ko": "주문하기", "color_block": "amber", "start": 15},
    {"block_id": 4, "title_es": "Mini prueba", "title_ko": "미니 퀴즈", "color_block": "blue", "start": 24},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Diego", "Hoy aprendemos a pedir comida en un restaurante.", "오늘은 레스토랑에서 음식을 주문하는 방법을 배워요.", "A2", 1, "coral", 8.0),
    (2, "Lucía", "Jin y Lucía están listos para cenar.", "Jin과 Lucía는 저녁을 먹을 준비가 되었어요.", "contexto", 1, "coral", 8.0),
    (3, "Diego", "El camarero se acerca a la mesa.", "점원이 테이블로 다가옵니다.", "camarero", 1, "coral", 7.0),
    (4, "Lucía", "Jin quiere pedir una recomendación.", "Jin은 추천을 요청하고 싶어 해요.", "recomendación", 1, "coral", 7.5),
    (5, "Diego", "Una frase muy útil es: ¿Qué nos recomienda?", "매우 유용한 표현은 ‘¿Qué nos recomienda?’예요.", "recomienda", 1, "coral", 8.5),
    (6, "Jin", "¿Qué nos recomienda?", "어떤 걸 추천해요?", "modelo", 1, "coral", 6.5),
    (7, "Lucía", "Recomienda significa: aconsejar algo bueno.", "recomienda는 ‘추천하다’라는 뜻이에요.", "significado", 1, "coral", 8.0),
    (8, "Diego", "Nos se refiere a nosotros, a los clientes.", "nos는 ‘우리에게’ 즉 손님들을 가리켜요.", "nos", 1, "coral", 8.0),
    (9, "Jin", "¿Qué nos recomienda para cenar?", "저녁으로 어떤 걸 추천하세요?", "modelo", 1, "coral", 7.5),
    (10, "Lucía", "Lucía actúa como la camarera: Les recomiendo la paella.", "루시아가 점원 역할극을 해요: 파에야를 추천합니다.", "camarera", 2, "teal", 8.5),
    (11, "Lucía", "Les recomiendo la paella de marisco.", "해산물 파에야를 추천합니다.", "modelo", 2, "teal", 7.5),
    (12, "Diego", "Les se usa para dirigirse a ustedes de forma cortés.", "les는 ‘당신들에게’ 정중하게 말할 때 사용해요.", "les", 2, "teal", 8.0),
    (13, "Jin", "¡Perfecto! Para mí, la paella.", "완벽해요! 저는 파에야로 할게요.", "modelo", 2, "teal", 7.5),
    (14, "Lucía", "Para mí es la forma estándar de elegir un plato.", "Para mí는 음식을 선택할 때 쓰는 표준 표현이에요.", "para mí", 2, "teal", 8.5),
    (15, "Diego", "Literalmente significa: para mí.", "직역하면 ‘나를 위해’라는 뜻이에요.", "literal", 3, "amber", 7.0),
    (16, "Jin", "Para mí, la paella de marisco.", "저는 해산물 파에야로 할게요.", "modelo", 3, "amber", 7.5),
    (17, "Lucía", "Lucía pregunta: ¿Para cuántas personas?", "루시아가 물어요: 몇 분이서 드시나요?", "pregunta", 3, "amber", 7.5),
    (18, "Jin", "Para dos personas, por favor.", "두 명이서 먹을게요, 부탁합니다.", "modelo", 3, "amber", 7.0),
    (19, "Diego", "Muy natural y educado.", "아주 자연스럽고 공손해요.", "educado", 3, "amber", 6.5),
    (20, "Lucía", "Y para beber, ¿qué desean?", "그리고 음료는 무엇으로 하시겠어요?", "pregunta", 3, "amber", 7.0),
    (21, "Jin", "Agua, por favor.", "물 주세요.", "modelo", 3, "amber", 6.0),
    (22, "Diego", "Excelente. Has pedido la paella y el agua sin problemas.", "훌륭해요. 문제없이 파에야와 물을 주문했어요.", "éxito", 3, "amber", 8.5),
    (23, "Lucía", "Ahora el camarero trae la comida.", "이제 점원이 음식을 가져옵니다.", "comida", 3, "amber", 7.0),
    (24, "Diego", "Mini prueba: ¿cómo preguntas por una recomendación?", "미니 퀴즈: 어떻게 추천을 물어볼까요?", "quiz", 4, "blue", 8.0),
    (25, "Lucía", "Dices: ¿Qué nos recomienda?", "¿Qué nos recomienda?라고 말해요.", "respuesta", 4, "blue", 7.0),
    (26, "Diego", "¿Cómo dices esta frase en español?", "이 문장을 스페인어로 어떻게 말할까요?", "pregunta", 4, "blue", 7.5),
    (27, "Jin", "Para mí, la paella de marisco.", "저는 해산물 파에야로 할게요.", "respuesta", 4, "blue", 7.5),
    (28, "Lucía", "¿Cómo dices ‘두 명분이요, 부탁합니다’?", "‘두 명분이요, 부탁합니다’를 어떻게 말할까요?", "pregunta", 4, "blue", 8.0),
    (29, "Jin", "Para dos personas, por favor.", "두 명이서 먹을게요, 부탁합니다.", "respuesta", 4, "blue", 7.0),
    (30, "Diego", "Muy bien. Ya sabes pedir en un restaurante español.", "좋아요. 이제 스페인 레스토랑에서 주문할 수 있어요.", "cierre", 4, "blue", 8.5),
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
    "intro_title": "¿Qué nos recomienda?",
    "intro_subtitle": "Español A2 · Ep.34",
    "intro_ko": "어떤 걸 추천해요?",
    "intro_scene_image_path": "images/ep34-en-el-restaurante-pedir-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "¿Qué recomienda?",
    "thumbnail_subtitle": "Español A2 · Ep.34",
    "thumbnail_ko": "어떤 걸 추천해요?",
    "outro_ko": "이제 스페인어로 식당 주문을 멋지게 할 수 있어요",
    "conversation_label": "Conversación A2",
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
            "text_es": "Hoy Jin aprende a pedir recomendaciones y a ordenar comida de forma educada en un restaurante.",
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
                "Muy bien. Ahora puedes pedir una recomendación y ordenar comida en español: "
                "¿Qué nos recomienda?, para mí la paella de marisco y para dos personas, por favor."
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
    {"segment": 2, "title": "El menú"},
    {"segment": 12, "title": "La recomendación"},
    {"segment": 18, "title": "El pedido"},
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
