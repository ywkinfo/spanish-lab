"""A1 story-card episode: needs and simple café requests."""

from __future__ import annotations

IMAGE_PATH = ""
DESCRIP_PATH = "a1-tengo-hambre/descrip.md"
OUTPUT_NAME = "tengo-hambre"
PUBLIC_SLUG = "a1-tengo-hambre"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 4
LEVEL = "A1"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "cards"
THUMBNAIL_PATH = None
YOUTUBE_TITLE = "Tengo hambre 배고파요, 물 주세요 말하기 | Español A1 · Ep.4"
DESCRIPTION_INTRO = (
    "Practica cómo decir que tienes hambre o sed en español A1. "
    "Aprende a pedir agua, café o un bocadillo con por favor y gracias, "
    "y repite una escena corta en una cafetería con Peter, Lucía y Diego."
)
DESCRIPTION_OUTRO = (
    "Vuelve a practicar este episodio hasta que puedas decir qué necesitas de forma natural. "
    "En el próximo episodio podemos entrar más en la cafetería: pedir, pagar y preguntar el precio."
)
KOREAN_TEASER = (
    "한국어 티저: 배고프거나 목마를 때 바로 쓸 수 있는 스페인어 A1 표현입니다. "
    "Tengo hambre, Tengo sed, Quiero agua, Quiero un café를 "
    "Peter, Lucía y Diego의 카페 장면으로 연습합니다."
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
    "tengo hambre español",
    "tengo sed español",
    "quiero cafe español",
    "frases cafeteria español",
    "스페인어 카페 주문",
    "스페인어 배고파요",
]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#frasesenespañol", "#TengoHambre"]

CHARACTERS = {
    "Peter": "assets/characters/peter-profile.png",
    "Lucía": "assets/characters/lucia-profile.png",
    "Diego": "assets/characters/diego-profile.png",
}

PHRASES = [
    (1, "Tengo hambre.", "배고파요.", "Peter: Tengo hambre.", "Peter"),
    (2, "Tengo sed.", "목말라요.", "Peter: Tengo sed.", "Peter"),
    (3, "Quiero agua.", "물을 원해요.", "Quiero agua, por favor.", "Peter"),
    (4, "Quiero café.", "커피를 원해요.", "Diego: Quiero café.", "Diego"),
    (5, "Quiero un café.", "커피 한 잔 원해요.", "Quiero un café, por favor.", "Diego"),
    (6, "Quiero un bocadillo.", "보카디요 하나 원해요.", "Quiero un bocadillo, por favor.", "Peter"),
    (7, "Por favor.", "부탁합니다 / 주세요.", "Un café, por favor.", "Lucía"),
    (8, "Gracias.", "감사합니다.", "Gracias, Lucía.", "Peter"),
    (9, "¿Quieres algo?", "뭐 좀 원해?", "Lucía: ¿Quieres algo?", "Lucía"),
    (10, "Sí, quiero agua, por favor.", "네, 물 주세요.", "Sí, quiero agua, por favor.", "Peter"),
]
BLOCKS = [
    {"block_id": 1, "title_es": "Necesidades", "title_ko": "필요 말하기", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "Quiero...", "title_ko": "원하는 것 말하기", "color_block": "amber", "start": 3},
    {"block_id": 3, "title_es": "Pedir con educación", "title_ko": "정중하게 부탁하기", "color_block": "teal", "start": 7},
    {"block_id": 4, "title_es": "Mini diálogo", "title_ko": "짧은 카페 대화", "color_block": "blue", "start": 9},
]
DIALOGUE = [
    ("Peter", "Estoy cansado... y tengo hambre.", "피곤해… 그리고 배고파."),
    ("Lucía", "Entonces, vamos a una cafetería.", "그럼 카페에 가자."),
    ("Lucía", "Peter, ¿quieres algo?", "Peter, 뭐 좀 원해?"),
    ("Peter", "Sí, quiero agua, por favor.", "응, 물 주세요."),
    ("Diego", "Yo quiero un café.", "나는 커피 한 잔 원해."),
    ("Lucía", "Muy bien.", "아주 좋아."),
]
MINI_QUIZ = [
    ("¿Cómo dices “배고파요”?", "Tengo hambre."),
    ("¿Cómo dices “목말라요”?", "Tengo sed."),
    ("¿Cómo pides agua?", "Quiero agua, por favor."),
    ("¿Cómo dices “커피 한 잔 원해요”?", "Quiero un café."),
    ("¿Cómo dices “감사합니다”?", "Gracias."),
]
DESIGN = {
    "output_size": (1280, 720),
    "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
    "font_index": 0,
    "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
    "font_index_ko": 0,
    "font_size_title": 82,
    "font_size_es": 78,
    "min_font_size_es": 48,
    "font_size_ko": 34,
    "font_size_example": 32,
    "background_color": (248, 247, 242),
    "text_color": (31, 35, 40),
    "muted_text_color": (96, 101, 109),
    "intro_title": "Tengo hambre",
    "intro_subtitle": "Español A1 · Ep.4",
    "intro_ko": "배고파요, 물 주세요 말하기",
    "thumbnail_title": "Tengo hambre",
    "thumbnail_subtitle": "Español A1 · Ep.4",
    "thumbnail_ko": "배고파요 / 목말라요 / 물 주세요",
    "outro_ko": "다음 영상: 카페에서 주문하기",
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


def _dialogue_text() -> str:
    return " ".join(f"{speaker}: {text_es}" for speaker, text_es, _ in DIALOGUE)


def _build_segments() -> list[dict]:
    segments: list[dict] = [
        {
            "type": "intro",
            "text_es": (
                "Hoy Peter tiene hambre y sed. Practicamos frases simples "
                "para pedir agua, café y comida en una cafetería."
            ),
            "duration_s": 11.0,
            "color_block": "neutral",
            "characters": ["Peter", "Lucía", "Diego"],
        }
    ]
    block_ranges = {
        1: [1, 2],
        2: [3, 4, 5, 6],
        3: [7, 8],
        4: [9, 10],
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
                "Muy bien. Ahora puedes decir tengo hambre, tengo sed, "
                "y pedir algo con por favor y gracias."
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
    {"segment": 2, "title": "Tengo hambre / Tengo sed"},
    {"segment": 5, "title": "Quiero agua"},
    {"segment": 9, "title": "Por favor y gracias"},
    {"segment": 12, "title": "Mini diálogo"},
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
