"""A1 phrase-trainer episode for a first encounter in Spanish."""

from __future__ import annotations

IMAGE_PATH = ""
DESCRIP_PATH = ""
OUTPUT_NAME = "primer-encuentro"
PUBLIC_SLUG = "a1-primer-encuentro"
YOUTUBE_URL = "https://www.youtube.com/watch?v=tkNs4tJunaU"
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 2
LEVEL = "A1"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "cards"
THUMBNAIL_PATH = None
YOUTUBE_TITLE = "Frases útiles para un primer encuentro en español | Español A1 · Ep.2"
DESCRIPTION_INTRO = (
    "Practica frases útiles para un primer encuentro en español A1. "
    "Escucha un diálogo sencillo con Peter, Lucía y Diego, lee la traducción en coreano y repite en voz alta."
)
DESCRIPTION_OUTRO = (
    "Vuelve a practicar este video hasta que puedas presentarte con naturalidad. "
    "En el próximo episodio podemos ampliar la conversación con más preguntas y respuestas básicas."
)
KOREAN_TEASER = (
    "한국어 티저: 첫 만남에서 바로 쓸 수 있는 인사, 자기소개, 가벼운 질문 표현을 "
    "Peter, Lucía y Diego의 짧은 대화로 익히는 A1 입문 영상입니다."
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
    "primer encuentro en español",
    "frases de presentación",
    "diálogo español A1",
    "Spanish dialogue for beginners",
    "스페인어 자기소개",
]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#frasesenespañol"]
PHRASES = [
    (1, "Hola.", "안녕하세요.", "Hola, Peter."),
    (2, "Me llamo Lucía.", "저는 루시아예요.", "Hola, me llamo Lucía."),
    (3, "Me llamo Peter.", "저는 피터예요.", "Me llamo Peter y estudio español."),
    (4, "¿Cómo te llamas?", "이름이 뭐예요?", "Hola, ¿cómo te llamas?"),
    (5, "Mucho gusto.", "만나서 반갑습니다.", "Mucho gusto, Lucía."),
    (6, "Igualmente.", "저도요.", "Mucho gusto. — Igualmente."),
    (7, "¿Y tú?", "당신은요?", "Yo soy de Corea. ¿Y tú?"),
    (8, "Soy de Corea.", "저는 한국에서 왔어요.", "Soy de Corea."),
    (9, "Soy de Madrid.", "저는 마드리드에서 왔어요.", "Soy de Madrid."),
    (10, "Encantado / Encantada.", "만나서 반갑습니다.", "Encantado. / Encantada."),
]
BLOCKS = [
    {"block_id": 1, "title_es": "Saludo inicial", "title_ko": "첫 인사", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "Presentarte", "title_ko": "자기소개", "color_block": "amber", "start": 2},
    {"block_id": 3, "title_es": "Preguntar el nombre", "title_ko": "이름 묻기", "color_block": "teal", "start": 4},
    {"block_id": 4, "title_es": "Responder con naturalidad", "title_ko": "자연스럽게 답하기", "color_block": "blue", "start": 6},
    {"block_id": 5, "title_es": "Origen y cierre", "title_ko": "출신과 마무리", "color_block": "green", "start": 8},
]
CHAPTERS = [
    {"segment": 1, "title": "Saludo y entrada"},
    {"segment": 2, "title": "Me llamo..."},
    {"segment": 4, "title": "¿Cómo te llamas?"},
    {"segment": 6, "title": "Mucho gusto / Igualmente"},
    {"segment": 8, "title": "Soy de Corea / Soy de Madrid"},
    {"segment": 10, "title": "Repaso final"},
]
DESIGN = {
    "output_size": (1280, 720),
    "font_path": "/System/Library/Fonts/Optima.ttc",
    "font_index": 0,
    "font_path_ko": "/System/Library/Fonts/AppleSDGothicNeo.ttc",
    "font_index_ko": 0,
    "font_size": 38,
    "min_font_size": 26,
    "letter_spacing": 0.5,
    "bar_style": "gradient",
    "bar_top_color": (24, 18, 12, 200),
    "bar_bottom_color": (8, 6, 4, 220),
    "bar_corner_radius": 0,
    "bar_accent_color": (244, 162, 97, 255),
    "bar_accent_height": 2,
    "bar_padding_x": 36,
    "bar_padding_y": 22,
    "bar_bottom_margin_ratio": 0.07,
    "text_color": (255, 252, 246, 255),
    "text_shadow_color": (0, 0, 0, 200),
    "text_shadow_offset": (0, 2),
    "text_shadow_blur": 3,
    "easing": "ease_in_out_cubic",
    "transition_s": 0.8,
    "fade_s": 0.4,
    "idle_zoom_drift": 0.012,
    "grade": {
        "saturation": 1.08,
        "contrast": 1.04,
        "warmth": 5,
    },
}
SEGMENTS = []
AUDIO = []
