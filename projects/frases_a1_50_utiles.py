"""Card-based A1 phrase trainer episode: 50 useful phrases."""

from __future__ import annotations

IMAGE_PATH = ""
DESCRIP_PATH = "aea1/descrip.md"
OUTPUT_NAME = "50-utiles"
PUBLIC_SLUG = "a1-50-frases-utiles"
YOUTUBE_URL = "https://www.youtube.com/watch?v=2WrERE9LOyE"
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 1
LEVEL = "A1"
LANGUAGE = "es"
RENDER_VERSION = 6
RENDER_TYPE = "cards"
THUMBNAIL_PATH = None
YOUTUBE_TITLE = "50 frases útiles para hablar español desde hoy | Español A1 · Ep.1"
DESCRIPTION_INTRO = (
    "Aprende 50 frases útiles de español A1 para la vida diaria. "
    "Escucha cada frase, lee la traducción en coreano y repite en voz alta."
)
DESCRIPTION_OUTRO = (
    "Vuelve a practicar este video hasta que puedas decir las frases sin mirar. "
    "En el próximo episodio podemos practicar restaurante, mercado o presentaciones."
)
KOREAN_TEASER = (
    "한국어 티저: 스페인어 A1 초급자를 위한 실전 표현 50개를 듣고, 읽고, "
    "따라 말하면서 바로 입에 붙이는 반복 훈련 영상입니다."
)
BASE_TAGS = [
    "스페인어",
    "스페인어 입문",
    "스페인어 A1",
    "Spanish A1",
    "aprender español",
    "español para principiantes",
    "frases utiles español",
]
EXTRA_TAGS = [
    "50 frases español",
    "frases para la vida diaria",
    "español básico",
    "Spanish phrases for beginners",
    "스페인어 기초 표현",
]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#frasesenespañol"]

PHRASES = [
    (1, "Hola.", "안녕하세요.", "Hola, ¿cómo estás?"),
    (2, "Buenos días.", "좋은 아침입니다.", "Buenos días, ¿qué tal?"),
    (3, "Buenas tardes.", "좋은 오후입니다.", "Buenas tardes, señor García."),
    (4, "Buenas noches.", "안녕히 주무세요.", "Buenas noches, hasta mañana."),
    (5, "¿Cómo estás?", "어떻게 지내요?", "Hola, ¿cómo estás hoy?"),
    (6, "Me llamo Peter.", "제 이름은 Peter입니다.", "Hola, me llamo Peter."),
    (7, "Soy de Corea.", "저는 한국에서 왔습니다.", "Soy de Corea y estudio español."),
    (8, "Mucho gusto.", "만나서 반갑습니다.", "Mucho gusto, encantado."),
    (9, "Soy estudiante.", "저는 학생입니다.", "Soy estudiante de español."),
    (10, "Hablo un poco de español.", "저는 스페인어를 조금 합니다.", "Hablo un poco de español, pero quiero practicar."),
    (11, "¿Qué significa esto?", "이것은 무슨 뜻인가요?", "Perdón, ¿qué significa esto?"),
    (12, "¿Cómo se dice en español?", "스페인어로 어떻게 말하나요?", "¿Cómo se dice café en español?"),
    (13, "¿Puedes repetir, por favor?", "다시 말해 줄 수 있나요?", "¿Puedes repetir, por favor? No entiendo."),
    (14, "¿Hablas inglés?", "영어를 할 수 있나요?", "Perdón, ¿hablas inglés?"),
    (15, "No entiendo.", "이해하지 못했습니다.", "Lo siento, no entiendo."),
    (16, "Tengo hambre.", "배가 고파요.", "Tengo hambre, quiero comer algo."),
    (17, "Tengo sed.", "목이 말라요.", "Tengo sed, necesito agua."),
    (18, "Estoy cansado.", "피곤해요.", "Estoy cansado después del trabajo."),
    (19, "Tengo tiempo.", "시간이 있어요.", "Hoy tengo tiempo para estudiar."),
    (20, "No tengo tiempo.", "시간이 없어요.", "Ahora no tengo tiempo."),
    (21, "Me levanto temprano.", "저는 일찍 일어납니다.", "Me levanto temprano todos los días."),
    (22, "Voy al trabajo.", "저는 일하러 갑니다.", "Voy al trabajo por la mañana."),
    (23, "Voy a estudiar español.", "저는 스페인어를 공부할 거예요.", "Esta noche voy a estudiar español."),
    (24, "Me gusta leer.", "저는 읽는 것을 좋아합니다.", "Me gusta leer libros sencillos."),
    (25, "Me gusta aprender idiomas.", "저는 언어 배우는 것을 좋아합니다.", "Me gusta aprender idiomas nuevos."),
    (26, "Quiero agua.", "물을 원합니다.", "Quiero agua, por favor."),
    (27, "Quiero café.", "커피를 원합니다.", "Quiero café con leche."),
    (28, "Quiero pagar.", "계산하고 싶습니다.", "Quiero pagar, por favor."),
    (29, "¿Cuánto cuesta?", "얼마인가요?", "¿Cuánto cuesta esta botella?"),
    (30, "Es demasiado caro.", "너무 비쌉니다.", "Lo siento, es demasiado caro."),
    (31, "La cuenta, por favor.", "계산서 주세요.", "La cuenta, por favor."),
    (32, "Quisiera esto.", "이것을 원합니다.", "Quisiera esto, por favor."),
    (33, "Está muy rico.", "아주 맛있어요.", "Este plato está muy rico."),
    (34, "No me gusta.", "마음에 들지 않아요.", "No me gusta mucho este sabor."),
    (35, "¿Hay menú en inglés?", "영어 메뉴가 있나요?", "Perdón, ¿hay menú en inglés?"),
    (36, "¿Dónde está la estación?", "역은 어디에 있나요?", "Disculpe, ¿dónde está la estación?"),
    (37, "¿Dónde está el baño?", "화장실은 어디에 있나요?", "Perdón, ¿dónde está el baño?"),
    (38, "Voy al centro.", "저는 시내로 갑니다.", "Voy al centro en metro."),
    (39, "¿Cuánto cuesta el billete?", "표는 얼마인가요?", "¿Cuánto cuesta el billete de autobús?"),
    (40, "Necesito un taxi.", "택시가 필요합니다.", "Necesito un taxi para ir al hotel."),
    (41, "Necesito ayuda.", "도움이 필요합니다.", "Por favor, necesito ayuda."),
    (42, "Estoy perdido.", "길을 잃었어요.", "Estoy perdido, ¿puede ayudarme?"),
    (43, "Llame a la policía, por favor.", "경찰을 불러 주세요.", "Llame a la policía, por favor."),
    (44, "Llame a un médico, por favor.", "의사를 불러 주세요.", "Llame a un médico, por favor."),
    (45, "Me duele aquí.", "여기가 아파요.", "Me duele aquí, en el brazo."),
    (46, "Está bien.", "괜찮습니다.", "Está bien, no hay problema."),
    (47, "Perfecto.", "완벽합니다.", "Perfecto, muchas gracias."),
    (48, "Gracias.", "감사합니다.", "Gracias por tu ayuda."),
    (49, "De nada.", "천만에요.", "De nada, hasta luego."),
    (50, "Hasta luego.", "나중에 봐요.", "Hasta luego, nos vemos mañana."),
]

BLOCKS = [
    {"block_id": 1, "title_es": "Saludos", "title_ko": "인사", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "Presentarte", "title_ko": "자기소개", "color_block": "amber", "start": 6},
    {"block_id": 3, "title_es": "Preguntas básicas", "title_ko": "기본 질문", "color_block": "teal", "start": 11},
    {"block_id": 4, "title_es": "Vida diaria", "title_ko": "일상생활", "color_block": "blue", "start": 16},
    {"block_id": 5, "title_es": "Casa y rutina", "title_ko": "집과 루틴", "color_block": "green", "start": 21},
    {"block_id": 6, "title_es": "Comida y compras", "title_ko": "음식과 쇼핑", "color_block": "violet", "start": 26},
    {"block_id": 7, "title_es": "Restaurante", "title_ko": "식당", "color_block": "rose", "start": 31},
    {"block_id": 8, "title_es": "Transporte", "title_ko": "교통", "color_block": "indigo", "start": 36},
    {"block_id": 9, "title_es": "Emergencias", "title_ko": "긴급 상황", "color_block": "red", "start": 41},
    {"block_id": 10, "title_es": "Cierre útil", "title_ko": "마무리 표현", "color_block": "slate", "start": 46},
]

DESIGN = {
    "output_size": (1280, 720),
    "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
    "font_index": 0,
    "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
    "font_index_ko": 0,
    "font_size_title": 82,
    "font_size_es": 88,
    "min_font_size_es": 54,
    "font_size_ko": 36,
    "font_size_example": 34,
    "background_color": (248, 247, 242),
    "text_color": (31, 35, 40),
    "muted_text_color": (96, 101, 109),
    "fade_s": 0.18,
    "color_blocks": {
        "coral": (224, 91, 76),
        "amber": (230, 158, 62),
        "teal": (44, 150, 142),
        "blue": (70, 120, 196),
        "green": (92, 148, 86),
        "violet": (138, 104, 190),
        "rose": (199, 90, 126),
        "indigo": (87, 98, 174),
        "red": (207, 72, 72),
        "slate": (87, 99, 115),
        "neutral": (42, 48, 57),
    },
}


def _phrases_for_block(start: int) -> list[tuple[int, str, str, str]]:
    return [phrase for phrase in PHRASES if start <= phrase[0] <= start + 4]


def _build_segments() -> list[dict]:
    segments: list[dict] = [
        {
            "type": "intro",
            "text_es": (
                "Hoy vamos a aprender 50 frases útiles de español A1 para la vida diaria. "
                "Lee, escucha y repite conmigo."
            ),
            "duration_s": 12.0,
            "color_block": "neutral",
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
        for number, text_es, text_ko, example_es in _phrases_for_block(block["start"]):
            segments.append(
                {
                    "type": "phrase",
                    "frase_num": number,
                    "text_es": text_es,
                    "text_ko": text_ko,
                    "example_es": example_es,
                    "block_id": block["block_id"],
                    "color_block": block["color_block"],
                    "duration_s": 11.5,
                    "repeat_pause_s": 2.0,
                }
            )
    segments.append(
        {
            "type": "outro",
            "text_es": (
                "Muy bien. Ya tienes 50 frases útiles para empezar a hablar español. "
                "Vuelve a practicar y repite las frases en voz alta."
            ),
            "duration_s": 12.0,
            "color_block": "neutral",
        }
    )
    return segments


SEGMENTS = _build_segments()

CHAPTERS = [{"segment": 1, "title": "Introducción"}]
for block_index, block in enumerate(BLOCKS):
    CHAPTERS.append({"segment": 2 + block_index * 6, "title": block["title_es"]})
CHAPTERS.append({"segment": len(SEGMENTS), "title": "Cierre"})

AUDIO = {
    "tts_engine": "edge",
    "voice": "es-ES-ElviraNeural",
    "edge_voice": "es-ES-ElviraNeural",
    "edge_rate": "+12%",
    "edge_pitch": "+0Hz",
    "edge_volume": "+0%",
    "rate_wpm": 160,
    "lead_padding_s": 0.25,
    "tail_padding_s": 0.4,
    "min_duration_s": 3.0,
    "readability_floor_ratio": 0.0,
    "bgm_path": "assets/audio/frases_a1_guitar_tremolo.mp3",
    "bgm_volume_db": -14.0,
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
