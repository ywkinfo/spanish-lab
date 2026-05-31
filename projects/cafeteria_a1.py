"""A1 story-card episode: ordering and paying in a café."""

from __future__ import annotations

IMAGE_PATH = ""
DESCRIP_PATH = "a1-cafeteria/descrip.md"
OUTPUT_NAME = "cafeteria"
PUBLIC_SLUG = "a1-cafeteria"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 5
LEVEL = "A1"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "cards"
THUMBNAIL_PATH = None
YOUTUBE_TITLE = "Un café, por favor ☕ 주문하고 계산하기 | Español A1 · Ep.5"
DESCRIPTION_INTRO = (
    "Practica una escena sencilla en una cafetería en español A1. "
    "Aprende a pedir té, zumo o una tostada, preguntar el precio, pedir la cuenta "
    "y pagar con tarjeta o en efectivo con Peter, Lucía y Diego."
)
DESCRIPTION_OUTRO = (
    "Repite este episodio varias veces hasta que puedas pedir y pagar en una cafetería "
    "con frases cortas y naturales. En el próximo episodio podemos practicar precios, "
    "números y compras con más detalle."
)
KOREAN_TEASER = (
    "한국어 티저: 카페에서 주문하고 계산할 때 바로 쓸 수 있는 스페인어 A1 표현입니다. "
    "Quiero un té, ¿Cuánto cuesta?, La cuenta, por favor, Con tarjeta를 "
    "Peter, Lucía y Diego의 짧은 카페 장면으로 연습합니다."
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
    "cafeteria español",
    "pedir cafe español",
    "cuanto cuesta español",
    "la cuenta por favor",
    "con tarjeta español",
    "스페인어 카페 주문",
    "스페인어 계산하기",
]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#frasesenespañol", "#Cafetería"]

CHARACTERS = {
    "Peter": "assets/characters/peter-profile.png",
    "Lucía": "assets/characters/lucia-profile.png",
    "Diego": "assets/characters/diego-profile.png",
}

PHRASES = [
    (1, "¿Qué quieres?", "뭐 마실래? / 뭐 원해?", "Lucía: Peter, ¿qué quieres?", "Lucía"),
    (2, "Quiero un té.", "차 한 잔 주세요.", "Quiero un té, por favor.", "Peter"),
    (3, "Quiero un zumo de naranja.", "오렌지 주스 주세요.", "Quiero un zumo de naranja.", "Peter"),
    (4, "Quiero una tostada.", "토스타다 하나 주세요.", "Quiero una tostada, por favor.", "Lucía"),
    (5, "¿Cuánto cuesta?", "얼마예요?", "¿Cuánto cuesta el café?", "Peter"),
    (6, "Cuesta tres euros.", "3유로예요.", "El café cuesta tres euros.", "Diego"),
    (7, "La cuenta, por favor.", "계산서 주세요.", "Camarero, la cuenta, por favor.", "Peter"),
    (8, "¿Con tarjeta o en efectivo?", "카드로, 현금으로?", "¿Pagas con tarjeta o en efectivo?", "Diego"),
    (9, "Con tarjeta.", "카드로요.", "Pago con tarjeta.", "Peter"),
    (10, "Gracias, adiós.", "감사합니다, 안녕히 계세요.", "Gracias, adiós. ¡Hasta luego!", "Lucía"),
]
BLOCKS = [
    {"block_id": 1, "title_es": "Elegir", "title_ko": "원하는 것 고르기", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "Pedir", "title_ko": "주문하기", "color_block": "amber", "start": 2},
    {"block_id": 3, "title_es": "Precio", "title_ko": "가격 묻기", "color_block": "teal", "start": 5},
    {"block_id": 4, "title_es": "Pagar", "title_ko": "계산하기", "color_block": "blue", "start": 7},
]
DIALOGUE = [
    ("Lucía", "Peter, ¿qué quieres?", "Peter, 뭐 마실래?"),
    ("Peter", "Quiero un té, por favor.", "차 한 잔 주세요."),
    ("Lucía", "Yo quiero una tostada.", "나는 토스타다 하나 주세요."),
    ("Peter", "¿Cuánto cuesta?", "얼마예요?"),
    ("Diego", "Cuesta tres euros.", "3유로예요."),
    ("Peter", "La cuenta, por favor. Con tarjeta.", "계산서 주세요. 카드로요."),
]
MINI_QUIZ = [
    ("¿Cómo dices “뭐 원해?”", "¿Qué quieres?"),
    ("¿Cómo pides un té?", "Quiero un té, por favor."),
    ("¿Cómo preguntas “얼마예요?”", "¿Cuánto cuesta?"),
    ("¿Cómo pides la cuenta?", "La cuenta, por favor."),
    ("¿Cómo dices “카드로요”?", "Con tarjeta."),
]
DESIGN = {
    "output_size": (1280, 720),
    "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
    "font_index": 0,
    "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
    "font_index_ko": 0,
    "font_size_title": 82,
    "font_size_es": 72,
    "min_font_size_es": 44,
    "font_size_ko": 34,
    "font_size_example": 32,
    "background_color": (248, 247, 242),
    "text_color": (31, 35, 40),
    "muted_text_color": (96, 101, 109),
    "intro_title": "Un café, por favor",
    "intro_subtitle": "Español A1 · Ep.5",
    "intro_ko": "주문하고 계산하기",
    "thumbnail_title": "Un café, por favor",
    "thumbnail_subtitle": "Español A1 · Ep.5",
    "thumbnail_ko": "주문하기 / 가격 묻기 / 카드로 계산",
    "outro_ko": "다음 영상: 가격과 숫자 연습",
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


def _phrase_for_number(number: int) -> tuple:
    for phrase in PHRASES:
        if phrase[0] == number:
            return phrase
    raise ValueError(f"Unknown phrase number: {number}")


def _build_segments() -> list[dict]:
    segments: list[dict] = [
        {
            "type": "intro",
            "text_es": (
                "Hoy entramos en una cafetería. Practicamos cómo pedir algo, "
                "preguntar cuánto cuesta y pagar con tarjeta o en efectivo."
            ),
            "duration_s": 11.0,
            "color_block": "neutral",
            "characters": ["Peter", "Lucía", "Diego"],
        }
    ]
    block_ranges = {
        1: [1],
        2: [2, 3, 4],
        3: [5, 6],
        4: [7, 8, 9, 10],
    }
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
        for number in block_ranges[block["block_id"]]:
            phrase_number, text_es, text_ko, example_es, character = _phrase_for_number(number)
            segments.append(
                {
                    "type": "phrase",
                    "frase_num": phrase_number,
                    "text_es": text_es,
                    "text_ko": text_ko,
                    "example_es": example_es,
                    "block_id": block["block_id"],
                    "color_block": block["color_block"],
                    "duration_s": 12.0,
                    "repeat_pause_s": 1.0,
                    "character": character,
                }
            )
    segments.append(
        {
            "type": "outro",
            "text_es": (
                "Muy bien. Ahora puedes pedir algo en una cafetería, preguntar el precio, "
                "pedir la cuenta y decir con tarjeta."
            ),
            "duration_s": 11.0,
            "color_block": "neutral",
            "characters": ["Peter", "Lucía", "Diego"],
        }
    )
    return segments


SEGMENTS = _build_segments()
CHAPTERS = [
    {"segment": 1, "title": "Introducción"},
    {"segment": 2, "title": "¿Qué quieres?"},
    {"segment": 4, "title": "Quiero un té"},
    {"segment": 7, "title": "¿Cuánto cuesta?"},
    {"segment": 10, "title": "La cuenta, por favor"},
    {"segment": len(SEGMENTS), "title": "Repaso final"},
]
AUDIO = {
    "tts_engine": "edge",
    "edge_voice": "es-ES-ElviraNeural",
    "edge_rate": "-8%",
    "edge_pitch": "+0Hz",
    "edge_volume": "+0%",
    "voice": "es-ES-ElviraNeural",
    "rate_wpm": 142,
    "lead_padding_s": 0.25,
    "tail_padding_s": 0.4,
    "min_duration_s": 3.0,
    "readability_floor_ratio": 0.0,
    "bgm_path": "assets/audio/fur_elise_inspired_soft_piano.wav",
    "bgm_volume_db": -15.0,
    "narration_volume_db": 0.0,
    "ducking": True,
    "ducking_threshold": 0.025,
    "ducking_ratio": 16,
    "ducking_attack_ms": 80,
    "ducking_release_ms": 900,
    "fade_in_s": 4.0,
    "fade_out_s": 5.0,
    "audio_codec": "aac",
    "audio_bitrate_kbps": 192,
    "sample_rate_hz": 44100,
}
