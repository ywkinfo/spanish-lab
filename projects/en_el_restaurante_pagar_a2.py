"""A2 entry story-card episode: Jin pays the bill at a restaurant."""

from __future__ import annotations

IMAGE_PATH = "images/ep35-en-el-restaurante-pagar-source.png"
DESCRIP_PATH = "a2-en-el-restaurante-pagar/descrip.md"
OUTPUT_NAME = "en-el-restaurante-pagar"
PUBLIC_SLUG = "a2-en-el-restaurante-pagar"
YOUTUBE_URL = ""
SERIES = "frases-a2"
SERIES_TITLE = "Español A2 -- Frases útiles"
EPISODE = 35
LEVEL = "A2 입문"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a2-ep35-en-el-restaurante-pagar.jpg"
YOUTUBE_TITLE = "Invito yo 💳 내가 낼게 | Español A2 · Ep.35"
DESCRIPTION_INTRO = (
    "Jin y Lucía terminan de cenar en el restaurante. "
    "En este episodio Jin aprende a pedir la cuenta, a invitar a Lucía diciendo Invito yo, y a preguntar si puede pagar con tarjeta."
)
DESCRIPTION_OUTRO = (
    "Escucha primero, repite en voz alta y practica las expresiones: "
    "Invito yo, ¿Pagamos a medias?, y ¿Se puede pagar con tarjeta?."
)
KOREAN_TEASER = (
    "한국어 티저: EP.35 식사 계산 편입니다. "
    "식사 후 대접할 때 쓰는 'Invito yo(내가 낼게)'와 각자 나눠 낼 때 쓰는 '¿Pagamos a medias?(우리 반반씩 낼까요?)'를 배웁니다. "
    "카드로 결제할 수 있는지 묻는 실용 표현까지 익혀 보세요!"
)
BASE_TAGS = ["스페인어", "스페인어 입문", "스페인어 A2", "Spanish A2", "aprender español", "español para coreanos"]
EXTRA_TAGS = ["pagar la cuenta", "invito yo", "pagar con tarjeta", "Spanish restaurant bill", "스페인어 회화", "식당 계산 스페인어"]
BASE_HASHTAGS = ["#EspañolA2", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#InvitoYo", "#Tarjeta", "#SpanishLab"]

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
    {"block_id": 1, "title_es": "La cuenta", "title_ko": "계산서 요청", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "Dividir la cuenta", "title_ko": "반반씩 내기", "color_block": "teal", "start": 10},
    {"block_id": 3, "title_es": "El pago", "title_ko": "카드 결제", "color_block": "amber", "start": 15},
    {"block_id": 4, "title_es": "Mini prueba", "title_ko": "미니 퀴즈", "color_block": "blue", "start": 24},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Diego", "Hoy aprendemos a pagar la cuenta en un restaurante.", "오늘은 식당에서 계산하는 방법을 배워요.", "A2", 1, "coral", 8.0),
    (2, "Lucía", "Jin y Lucía han terminado de comer.", "Jin과 Lucía는 식사를 마쳤어요.", "contexto", 1, "coral", 8.0),
    (3, "Diego", "Es hora de pagar. Jin quiere invitar a Lucía.", "계산할 시간이에요. Jin은 루시아에게 사고 싶어 해요.", "invitar", 1, "coral", 8.5),
    (4, "Lucía", "Primero pide la factura al camarero.", "먼저 점원에게 계산서를 요청해요.", "la cuenta", 1, "coral", 7.5),
    (5, "Jin", "La cuenta, por favor.", "계산서 주세요.", "modelo", 1, "coral", 6.5),
    (6, "Diego", "Muy bien. Y para invitar, Jin dice: Invito yo.", "좋아요. 그리고 대접하기 위해 Jin이 말해요: 내가 낼게.", "invito yo", 1, "coral", 8.5),
    (7, "Jin", "Invito yo.", "내가 낼게.", "modelo", 1, "coral", 6.0),
    (8, "Lucía", "Invito yo significa: yo pago todo.", "Invito yo는 '내가 전부 낼게'라는 뜻이에요.", "significado", 1, "coral", 7.5),
    (9, "Diego", "Pero Lucía prefiere pagar su parte.", "하지만 루시아는 자기 몫을 내고 싶어 해요.", "parte", 1, "coral", 8.0),
    (10, "Lucía", "Lucía propone: ¿Pagamos a medias?", "루시아가 제안해요: 반반씩 낼까요?", "a medias", 2, "teal", 8.0),
    (11, "Lucía", "¿Pagamos a medias?", "우리 반반씩 낼까요?", "modelo", 2, "teal", 6.5),
    (12, "Diego", "A medias significa: al cincuenta por ciento cada uno.", "a medias는 '각자 50%씩'이라는 뜻이에요.", "significado", 2, "teal", 8.5),
    (13, "Jin", "No, de ninguna manera. Invito yo.", "아니요, 절대 안 돼요. 제가 살게요.", "modelo", 2, "teal", 8.0),
    (14, "Lucía", "De ninguna manera expresa un rechazo rotundo y educado.", "De ninguna manera는 공손하고 단호한 거절을 표현해요.", "educado", 2, "teal", 8.5),
    (15, "Diego", "Como Jin insiste, Lucía acepta: Gracias por la cena.", "Jin이 고집을 부려서 루시아가 받아들여요: 저녁 잘 먹었어.", "aceptar", 3, "amber", 9.0),
    (16, "Lucía", "Muchas gracias por la cena, Jin.", "저녁 정말 잘 먹었어, Jin.", "modelo", 3, "amber", 7.5),
    (17, "Jin", "De nada. Un placer.", "천만에요. 즐거웠어요.", "modelo", 3, "amber", 6.5),
    (18, "Diego", "Ahora Jin le habla al camarero para pagar.", "이제 Jin이 계산을 하려고 점원에게 말해요.", "pagar", 3, "amber", 8.0),
    (19, "Lucía", "Pregunta si aceptan tarjeta de crédito.", "신용카드를 받는지 물어봐요.", "tarjeta", 3, "amber", 7.5),
    (20, "Jin", "¿Se puede pagar con tarjeta?", "카드로 결제할 수 있나요?", "modelo", 3, "amber", 7.0),
    (21, "Diego", "Muy bien. Tarjeta se refiere a la tarjeta de crédito o débito.", "좋아요. Tarjeta는 신용카드나 체크카드를 뜻해요.", "significado", 3, "amber", 8.5),
    (22, "Lucía", "El camarero responde que sí. Jin paga la cuenta.", "점원이 된다고 답해요. Jin이 계산을 합니다.", "camarero", 3, "amber", 8.0),
    (23, "Diego", "Excelente. Has pagado la cena como un caballero.", "훌륭해요. 멋지게 저녁을 샀어요.", "éxito", 3, "amber", 8.0),
    (24, "Diego", "Mini prueba: ¿cómo dices '내가 낼게'?", "미니 퀴즈: '내가 낼게'를 어떻게 말할까요?", "quiz", 4, "blue", 8.0),
    (25, "Lucía", "Dices: Invito yo.", "Invito yo라고 해요.", "respuesta", 4, "blue", 7.0),
    (26, "Diego", "¿Cómo dices esta frase en español?", "이 문장을 스페인어로 어떻게 말할까요?", "pregunta", 4, "blue", 7.5),
    (27, "Lucía", "¿Pagamos a medias?", "¿Pagamos a medias?라고 해요.", "respuesta", 4, "blue", 7.0),
    (28, "Diego", "¿Cómo preguntas '카드로 결제할 수 있나요'?", "어떻게 '카드로 결제할 수 있나요'라고 물어볼까요?", "pregunta", 4, "blue", 8.0),
    (29, "Jin", "¿Se puede pagar con tarjeta?", "카드로 결제할 수 있나요?", "respuesta", 4, "blue", 7.0),
    (30, "Diego", "Muy bien. Ya sabes pagar en un restaurante español.", "좋아요. 이제 스페인 레스토랑에서 결제할 수 있어요.", "cierre", 4, "blue", 8.5),
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
    "intro_title": "Invito yo",
    "intro_subtitle": "Español A2 · Ep.35",
    "intro_ko": "내가 낼게",
    "intro_scene_image_path": "images/ep35-en-el-restaurante-pagar-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "Invito yo",
    "thumbnail_subtitle": "Español A2 · Ep.35",
    "thumbnail_ko": "내가 낼게",
    "outro_ko": "이제 스페인어로 멋지게 한턱낼 수 있어요",
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
            "text_es": "Hoy Jin aprende a pedir la cuenta, a invitar diciendo Invito yo y a preguntar si puede pagar con tarjeta.",
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
                "Muy bien. Ahora puedes pagar la cuenta y proponer compartir los gastos en español: "
                "Invito yo, ¿Pagamos a medias? y ¿Se puede pagar con tarjeta?."
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
    {"segment": 2, "title": "La cuenta"},
    {"segment": 12, "title": "Dividir la cuenta"},
    {"segment": 18, "title": "El pago"},
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
