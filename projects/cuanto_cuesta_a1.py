"""A1 conversation episode: asking prices and paying in a small shop."""

from __future__ import annotations

IMAGE_PATH = ""
DESCRIP_PATH = "a1-cuanto-cuesta/descrip.md"
OUTPUT_NAME = "cuanto-cuesta"
PUBLIC_SLUG = "a1-cuanto-cuesta"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 6
LEVEL = "A1"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "cards"
THUMBNAIL_PATH = None
YOUTUBE_TITLE = "¿Cuánto cuesta? 얼마예요? 가격 묻고 계산하기 | Español A1 · Ep.6"
DESCRIPTION_INTRO = (
    "Practica una conversación real y sencilla entre Peter, Lucía y Diego en español A1. "
    "Después de la cafetería, los tres entran en una tienda, eligen bebidas, preguntan precios "
    "y pagan con tarjeta."
)
DESCRIPTION_OUTRO = (
    "Repite la conversación varias veces. Primero escucha, después lee en voz alta y finalmente "
    "cambia las palabras: agua, zumo, café, un euro, dos euros, tres euros."
)
KOREAN_TEASER = (
    "한국어 티저: EP.6부터는 Peter, Lucía, Diego의 실제 대화형 구성입니다. "
    "카페를 나온 뒤 가게에서 물건을 고르고, ¿Cuánto cuesta?, ¿Cuánto es?, Pago con tarjeta로 "
    "가격 묻기와 계산하기를 연습합니다."
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
    "cuanto cuesta español",
    "comprar en español",
    "precio español",
    "pagar con tarjeta español",
    "conversacion español A1",
    "스페인어 가격 묻기",
    "스페인어 계산하기",
]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#frasesenespañol", "#CuantoCuesta"]

CHARACTERS = {
    "Peter": "assets/characters/peter-profile.png",
    "Lucía": "assets/characters/lucia-profile.png",
    "Diego": "assets/characters/diego-profile.png",
}
CHARACTER_VOICES = {
    "Lucía": "es-ES-ElviraNeural",
    "Peter": "es-ES-AlvaroNeural",
    "Diego": "es-MX-JorgeNeural",
}

BLOCKS = [
    {"block_id": 1, "title_es": "Después del café", "title_ko": "카페를 나온 뒤", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "En la tienda", "title_ko": "가게에서 고르기", "color_block": "amber", "start": 8},
    {"block_id": 3, "title_es": "El precio", "title_ko": "가격 묻기", "color_block": "teal", "start": 16},
    {"block_id": 4, "title_es": "Pagar", "title_ko": "계산하기", "color_block": "blue", "start": 23},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Lucía", "¿Estás bien, Peter?", "Peter, 괜찮아?", "¿Estás bien?", 1, "coral", 8.5),
    (2, "Peter", "Sí, estoy bien, pero tengo sed.", "응, 괜찮아. 그런데 목말라.", "Tengo sed", 1, "coral", 9.0),
    (3, "Diego", "Hay una tienda aquí cerca.", "근처에 가게가 있어.", "Hay una tienda", 1, "coral", 8.5),
    (4, "Peter", "Perfecto. Quiero comprar agua.", "좋아. 물을 사고 싶어.", "Quiero comprar...", 1, "coral", 9.0),
    (5, "Lucía", "Muy bien. Vamos a la tienda.", "좋아. 가게에 가자.", "Vamos", 1, "coral", 8.5),
    (6, "Diego", "Después podemos practicar precios.", "그 다음 가격을 연습할 수 있어.", "precios", 1, "coral", 8.5),
    (7, "Peter", "Vale. Necesito hablar más en español.", "좋아. 스페인어로 더 말해야 해.", "Necesito...", 1, "coral", 9.0),
    (8, "Lucía", "Mira, hay agua, zumo y café.", "봐, 물, 주스, 커피가 있어.", "Hay agua", 2, "amber", 8.5),
    (9, "Peter", "Quiero una botella de agua.", "물 한 병 원해.", "una botella", 2, "amber", 8.5),
    (10, "Lucía", "Yo quiero un zumo de naranja.", "나는 오렌지 주스 원해.", "Yo quiero...", 2, "amber", 8.5),
    (11, "Peter", "Diego, ¿quieres algo?", "Diego, 뭐 좀 원해?", "¿Quieres algo?", 2, "amber", 8.5),
    (12, "Diego", "Sí, quiero un café frío.", "응, 차가운 커피 원해.", "un café frío", 2, "amber", 8.5),
    (13, "Lucía", "También hay una tostada pequeña.", "작은 토스타다도 있어.", "También hay...", 2, "amber", 8.5),
    (14, "Peter", "No, gracias. Solo agua.", "아니, 괜찮아. 물만.", "Solo agua", 2, "amber", 8.5),
    (15, "Diego", "Muy bien. Ahora preguntamos el precio.", "좋아. 이제 가격을 물어보자.", "preguntar el precio", 2, "amber", 9.0),
    (16, "Peter", "Lucía, ¿cuánto cuesta el agua?", "Lucía, 물은 얼마야?", "¿Cuánto cuesta?", 3, "teal", 9.0),
    (17, "Lucía", "El agua cuesta un euro.", "물은 1유로야.", "un euro", 3, "teal", 8.5),
    (18, "Peter", "¿Y el zumo de naranja?", "오렌지 주스는?", "¿Y...?", 3, "teal", 8.5),
    (19, "Lucía", "El zumo cuesta dos euros.", "주스는 2유로야.", "dos euros", 3, "teal", 8.5),
    (20, "Diego", "Mi café cuesta tres euros.", "내 커피는 3유로야.", "tres euros", 3, "teal", 8.5),
    (21, "Peter", "Entonces, en total son seis euros.", "그러면 총 6유로야.", "en total", 3, "teal", 9.0),
    (22, "Lucía", "Exacto. Uno, dos, tres... seis.", "맞아. 하나, 둘, 셋... 여섯.", "números", 3, "teal", 9.0),
    (23, "Peter", "La cuenta, por favor.", "계산서 주세요.", "La cuenta", 4, "blue", 8.5),
    (24, "Diego", "En una tienda, mejor: ¿cuánto es?", "가게에서는 ¿cuánto es?가 더 좋아.", "¿Cuánto es?", 4, "blue", 9.5),
    (25, "Peter", "Ah, vale. ¿Cuánto es?", "아, 좋아. 얼마예요?", "¿Cuánto es?", 4, "blue", 8.5),
    (26, "Lucía", "Son seis euros.", "6유로입니다.", "Son seis euros", 4, "blue", 8.0),
    (27, "Peter", "Pago con tarjeta.", "카드로 계산할게요.", "Pago con tarjeta", 4, "blue", 8.5),
    (28, "Diego", "Muy bien. También puedes decir: con tarjeta.", "좋아. Con tarjeta라고도 말할 수 있어.", "Con tarjeta", 4, "blue", 9.5),
    (29, "Peter", "Con tarjeta. Gracias.", "카드로요. 감사합니다.", "Gracias", 4, "blue", 8.5),
    (30, "Lucía", "Perfecto. Ya puedes comprar algo en español.", "완벽해. 이제 스페인어로 물건을 살 수 있어.", "comprar en español", 4, "blue", 9.0),
]

DESIGN = {
    "output_size": (1280, 720),
    "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
    "font_index": 0,
    "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
    "font_index_ko": 0,
    "font_size_title": 78,
    "font_size_es": 70,
    "min_font_size_es": 42,
    "font_size_ko": 33,
    "font_size_example": 30,
    "background_color": (248, 247, 242),
    "text_color": (31, 35, 40),
    "muted_text_color": (96, 101, 109),
    "intro_title": "¿Cuánto cuesta?",
    "intro_subtitle": "Español A1 · Ep.6",
    "intro_ko": "실제 3인 대화: 가격 묻고 계산하기",
    "thumbnail_title": "¿Cuánto cuesta?",
    "thumbnail_subtitle": "Español A1 · Ep.6",
    "thumbnail_ko": "가격 묻기 / 가게에서 계산하기",
    "outro_ko": "다음 영상: 숫자와 가격 더 연습하기",
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
                "Hoy Peter, Lucía y Diego entran en una tienda. "
                "Escucha una conversación real para preguntar precios y pagar."
            ),
            "duration_s": 12.0,
            "color_block": "neutral",
            "characters": ["Peter", "Lucía", "Diego"],
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
                }
            )
    segments.append(
        {
            "type": "outro",
            "text_es": (
                "Muy bien. Ahora puedes preguntar cuánto cuesta, decir cuánto es "
                "y pagar con tarjeta en una tienda."
            ),
            "duration_s": 12.0,
            "color_block": "neutral",
            "characters": ["Peter", "Lucía", "Diego"],
        }
    )
    return segments


SEGMENTS = _build_segments()
CHAPTERS = [
    {"segment": 1, "title": "Introducción"},
    {"segment": 2, "title": "Después del café"},
    {"segment": 10, "title": "En la tienda"},
    {"segment": 19, "title": "¿Cuánto cuesta?"},
    {"segment": 27, "title": "Pagar con tarjeta"},
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
    "bgm_path": None,
    "bgm_volume_db": -18.0,
    "narration_volume_db": 0.0,
    "ducking": False,
    "fade_in_s": 0.0,
    "fade_out_s": 0.0,
    "audio_codec": "aac",
    "audio_bitrate_kbps": 192,
    "sample_rate_hz": 44100,
}
