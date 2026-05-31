"""A1 phrase-trainer episode: asking and answering "¿Cómo estás?"."""

from __future__ import annotations

IMAGE_PATH = ""
DESCRIP_PATH = "a1-como-estas/descrip.md"
OUTPUT_NAME = "como-estas"
PUBLIC_SLUG = "a1-como-estas"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 3
LEVEL = "A1"
LANGUAGE = "es"
RENDER_VERSION = 4
RENDER_TYPE = "cards"
THUMBNAIL_PATH = None
YOUTUBE_TITLE = "¿Cómo estás? 피곤해요, 괜찮아요 말하기 | Español A1 · Ep.3"
DESCRIPTION_INTRO = (
    "Practica cómo preguntar y responder ¿Cómo estás? en español A1. "
    "Aprende a decir que estás bien, más o menos, cansado o con sueño, "
    "y repite una conversación corta con Peter, Lucía y Diego."
)
DESCRIPTION_OUTRO = (
    "Vuelve a practicar este episodio hasta que puedas responder ¿Cómo estás? sin pensar. "
    "En el próximo episodio podemos pasar a necesidades básicas como tengo hambre, tengo sed y necesito ayuda."
)
KOREAN_TEASER = (
    "한국어 티저: 월요일 아침처럼 피곤한 날에도 바로 쓸 수 있는 스페인어 A1 표현입니다. "
    "¿Cómo estás?, Estoy cansado, Tengo sueño, Me voy a dormir temprano를 "
    "Peter, Lucía y Diego의 짧은 대화로 연습합니다."
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
    "como estas español",
    "estoy cansado español",
    "frases de estado español",
    "Spanish feelings for beginners",
    "스페인어 기분 표현",
    "스페인어 피곤해요",
]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#frasesenespañol", "#CómoEstás"]
PHRASES = [
    (1, "¿Cómo estás?", "어떻게 지내?", "Hola, Peter. ¿Cómo estás?"),
    (2, "Estoy bien.", "잘 지내.", "Estoy bien, gracias."),
    (3, "Estoy muy bien.", "아주 잘 지내.", "Hoy estoy muy bien."),
    (4, "Estoy más o menos.", "그럭저럭이야.", "Estoy más o menos. Es lunes."),
    (5, "Estoy un poco cansado.", "조금 피곤해. 남성 화자", "Estoy un poco cansado esta mañana."),
    (6, "Estoy cansada.", "피곤해. 여성 화자", "Hoy estoy cansada."),
    (7, "Tengo sueño.", "졸려.", "Tengo sueño. Necesito café."),
    (8, "Estoy ocupado.", "바빠.", "Hoy estoy ocupado."),
    (9, "Necesito descansar.", "쉬어야 해.", "Necesito descansar un poco."),
    (10, "Me voy a dormir temprano.", "일찍 잘 거야.", "Esta noche me voy a dormir temprano."),
]
BLOCKS = [
    {"block_id": 1, "title_es": "Preguntar", "title_ko": "상태 묻기", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "Responder bien", "title_ko": "괜찮다고 답하기", "color_block": "amber", "start": 2},
    {"block_id": 3, "title_es": "Responder regular", "title_ko": "그럭저럭 답하기", "color_block": "teal", "start": 4},
    {"block_id": 4, "title_es": "Cansancio", "title_ko": "피곤함 말하기", "color_block": "blue", "start": 5},
    {"block_id": 5, "title_es": "Descansar", "title_ko": "쉬기와 잠", "color_block": "green", "start": 9},
]
DIALOGUE = [
    ("Lucía", "Hola, Peter. ¿Cómo estás?", "안녕, Peter. 어떻게 지내?"),
    ("Peter", "Estoy más o menos. Es lunes.", "그럭저럭이야. 월요일이야."),
    ("Lucía", "Te entiendo. ¿Estás cansado?", "이해해. 피곤해?"),
    ("Peter", "Sí, estoy un poco cansado.", "응, 조금 피곤해."),
    ("Diego", "Entonces esta noche, a dormir temprano.", "그럼 오늘 밤은 일찍 자기."),
    ("Peter", "Sí, me voy a dormir temprano.", "응, 일찍 잘 거야."),
]
MINI_QUIZ = [
    ("¿Cómo preguntas “어떻게 지내?”", "¿Cómo estás?"),
    ("¿Cómo dices “그럭저럭이야”?", "Estoy más o menos."),
    ("¿Cómo dices “조금 피곤해”?", "Estoy un poco cansado / cansada."),
    ("¿Cómo dices “졸려”?", "Tengo sueño."),
    ("¿Cómo dices “일찍 잘 거야”?", "Me voy a dormir temprano."),
]
DESIGN = {
    "output_size": (1280, 720),
    "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
    "font_index": 0,
    "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
    "font_index_ko": 0,
    "font_size_title": 82,
    "font_size_es": 84,
    "min_font_size_es": 52,
    "font_size_ko": 36,
    "font_size_example": 34,
    "background_color": (248, 247, 242),
    "text_color": (31, 35, 40),
    "muted_text_color": (96, 101, 109),
    "intro_title": "¿Cómo estás?",
    "intro_subtitle": "Español A1 · Ep.3",
    "intro_ko": "피곤해요, 괜찮아요 말하기",
    "thumbnail_title": "¿Cómo estás?",
    "thumbnail_subtitle": "Español A1 · Ep.3",
    "thumbnail_ko": "피곤해요 / 괜찮아요 / 졸려요",
    "outro_ko": "다음 영상에서 또 연습해요",
    "color_blocks": {
        "coral": (224, 91, 76),
        "amber": (230, 158, 62),
        "teal": (44, 150, 142),
        "blue": (70, 120, 196),
        "green": (92, 148, 86),
        "neutral": (42, 48, 57),
    },
}


def _phrase_for_number(number: int) -> tuple[int, str, str, str]:
    for phrase in PHRASES:
        if phrase[0] == number:
            return phrase
    raise ValueError(f"Unknown phrase number: {number}")


def _build_segments() -> list[dict]:
    segments: list[dict] = [
        {
            "type": "intro",
            "text_es": (
                "Hoy practicamos una pregunta muy básica: ¿Cómo estás? "
                "Vas a responder bien, más o menos, cansado o con sueño."
            ),
            "duration_s": 11.0,
            "color_block": "neutral",
        }
    ]
    block_ranges = {
        1: [1],
        2: [2, 3],
        3: [4],
        4: [5, 6, 7, 8],
        5: [9, 10],
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
            phrase_number, text_es, text_ko, example_es = _phrase_for_number(number)
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
                }
            )
    segments.append(
        {
            "type": "outro",
            "text_es": (
                "Muy bien. Ahora puedes preguntar ¿Cómo estás? y responder de forma natural. "
                "Practica otra vez y usa estas frases hoy."
            ),
            "duration_s": 11.0,
            "color_block": "neutral",
        }
    )
    return segments


SEGMENTS = _build_segments()
CHAPTERS = [
    {"segment": 1, "title": "Introducción"},
    {"segment": 2, "title": "¿Cómo estás?"},
    {"segment": 4, "title": "Estoy bien"},
    {"segment": 7, "title": "Estoy más o menos"},
    {"segment": 9, "title": "Estoy cansado / Tengo sueño"},
    {"segment": 14, "title": "Descansar y dormir temprano"},
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
