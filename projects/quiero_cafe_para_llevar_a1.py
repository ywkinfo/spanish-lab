
"""A1+ story-card episode: Jin orders takeaway coffee using Quiero + noun + para llevar."""

from __future__ import annotations

IMAGE_PATH = "images/ep28-quiero-cafe-para-llevar-source.png"
DESCRIP_PATH = "a1-quiero-cafe-para-llevar/descrip.md"
OUTPUT_NAME = "quiero-cafe-para-llevar"
PUBLIC_SLUG = "a1-quiero-cafe-para-llevar"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 28
LEVEL = "A1+"
LANGUAGE = "es"
RENDER_VERSION = 4
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a1-ep28-quiero-cafe-para-llevar.jpg"
YOUTUBE_TITLE = "Quiero un café para llevar ☕ 포장해 주세요 | Español A1+ · Ep.28"
DESCRIPTION_INTRO = (
    "Jin aprende una frase muy práctica para cafeterías y viajes: "
    "quiero un café para llevar."
)
DESCRIPTION_OUTRO = (
    "Escucha, repite en voz alta y cambia solo el producto: "
    "quiero un café para llevar, quiero un té para llevar, quiero un bocadillo para llevar."
)
KOREAN_TEASER = (
    "한국어 티저: EP.28은 카페와 여행에서 바로 쓰는 A1+ 표현입니다. "
    "핵심은 하나, Quiero + 명사 + para llevar입니다. "
    "Quiero un café para llevar처럼 포장 주문을 짧고 자연스럽게 말해 보세요."
)
BASE_TAGS = ["스페인어", "스페인어 입문", "스페인어 A1", "Spanish A1", "aprender español", "español para coreanos"]
EXTRA_TAGS = ["para llevar", "Quiero un café", "Spanish cafe", "스페인어 회화", "스페인어 여행", "스페인어 카페", "포장 스페인어"]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#ParaLlevar", "#SpanishLab"]

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
    {"block_id": 1, "title_es": "Para llevar", "title_ko": "포장 / 가져가기", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "Quiero un café", "title_ko": "커피 하나 원해요", "color_block": "teal", "start": 9},
    {"block_id": 3, "title_es": "Cambia el producto", "title_ko": "메뉴만 바꾸기", "color_block": "amber", "start": 17},
    {"block_id": 4, "title_es": "Mini prueba", "title_ko": "미니 퀴즈", "color_block": "blue", "start": 25},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [(1, 'Diego', 'Hoy estamos en una cafetería cerca de la estación.', '오늘은 역 근처 카페에 있어요.', 'contexto', 1, 'coral', 8.0), (2, 'Lucía', 'Jin quiere un café, pero no tiene mucho tiempo.', 'Jin은 커피를 원하지만 시간이 많지 않아요.', 'situación', 1, 'coral', 8.5), (3, 'Jin', 'Tengo que tomar el tren pronto.', '저는 곧 기차를 타야 해요.', 'contexto', 1, 'coral', 8.0), (4, 'Diego', 'Entonces la frase clave es: para llevar.', '그래서 오늘의 핵심 표현은 para llevar예요.', 'clave', 1, 'coral', 8.0), (5, 'Lucía', 'Para llevar significa que no comes aquí.', 'para llevar는 여기서 먹지 않는다는 뜻이에요.', 'significado', 1, 'coral', 8.5), (6, 'Diego', 'En coreano natural, es una petición para llevar.', '한국어로 자연스럽게는 포장해 주세요, 또는 가져갈게요예요.', 'natural', 1, 'coral', 8.5), (7, 'Jin', 'Quiero un café para llevar.', '커피 하나 포장해 주세요.', 'modelo', 1, 'coral', 8.0), (8, 'Lucía', 'Muy bien. Esa frase suena natural en una cafetería.', '아주 좋아요. 카페에서 자연스럽게 들리는 문장이에요.', 'feedback', 1, 'coral', 9.0), (9, 'Diego', 'Primero, escucha la estructura completa.', '먼저 전체 구조를 들어 보세요.', 'estructura', 2, 'teal', 7.5), (10, 'Diego', 'La estructura es: quiero, un producto, y para llevar.', '구조는 quiero, 메뉴 하나, 그리고 para llevar예요.', 'estructura', 2, 'teal', 8.5), (11, 'Lucía', 'Quiero un café para llevar.', '커피 하나 포장해 주세요.', 'café', 2, 'teal', 7.5), (12, 'Jin', 'Quiero un café para llevar.', '커피 하나 포장해 주세요.', 'repetición', 2, 'teal', 7.5), (13, 'Diego', 'Literalmente: quiero un café para llevar.', '직역하면: 가져가기 위한 커피 하나를 원해요.', 'literal', 2, 'teal', 8.5), (14, 'Lucía', 'Naturalmente: un café para llevar.', '자연스럽게는 “커피 하나 포장해 주세요”예요.', 'natural', 2, 'teal', 8.0), (15, 'Jin', 'Para llevar, por favor.', '포장으로 부탁해요.', 'corto', 2, 'teal', 7.0), (16, 'Diego', 'También puedes decir solo: para llevar, por favor.', '짧게 para llevar, por favor만 말해도 좋아요.', 'corto', 2, 'teal', 8.5), (17, 'Lucía', 'Ahora cambiamos solo la bebida o la comida.', '이제 음료나 음식만 바꿔 볼게요.', 'cambiar', 3, 'amber', 8.0), (18, 'Lucía', 'Quiero un té para llevar.', '차 하나 포장해 주세요.', 'té', 3, 'amber', 7.5), (19, 'Jin', 'Quiero un té para llevar.', '차 하나 포장해 주세요.', 'repetición', 3, 'amber', 7.5), (20, 'Diego', 'Quiero un bocadillo para llevar.', '샌드위치 하나 포장해 주세요.', 'bocadillo', 3, 'amber', 8.0), (21, 'Jin', 'Quiero un bocadillo para llevar.', '샌드위치 하나 포장해 주세요.', 'repetición', 3, 'amber', 8.0), (22, 'Lucía', 'Si ya tienes el café, puedes añadir: para llevar.', '이미 커피를 말했으면 para llevar를 덧붙이면 돼요.', 'añadir', 3, 'amber', 8.5), (23, 'Jin', 'Un café, para llevar, por favor.', '커피 하나, 포장으로 부탁해요.', 'natural', 3, 'amber', 8.0), (24, 'Diego', 'Perfecto. Corto, claro y útil para viajar.', '완벽해요. 짧고 분명하고 여행에 유용해요.', 'feedback', 3, 'amber', 8.0), (25, 'Diego', 'Mini prueba. ¿Cómo pides un café para llevar?', '미니 퀴즈예요. 커피 포장은 어떻게 주문할까요?', 'quiz', 4, 'blue', 8.0), (26, 'Jin', 'Quiero un café para llevar.', '커피 하나 포장해 주세요.', 'respuesta', 4, 'blue', 7.5), (27, 'Lucía', 'Muy bien. ¿Y un té para llevar?', '아주 좋아요. 그럼 차 포장은요?', 'quiz', 4, 'blue', 7.5), (28, 'Jin', 'Quiero un té para llevar.', '차 하나 포장해 주세요.', 'respuesta', 4, 'blue', 7.5), (29, 'Diego', 'Última frase: para llevar, por favor.', '마지막 문장: 포장으로 부탁해요.', 'shadowing', 4, 'blue', 8.0), (30, 'Jin', 'Para llevar, por favor.', '포장으로 부탁해요.', 'shadowing', 4, 'blue', 7.0)]

DESIGN = {
    "output_size": (1280, 720),
    "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
    "font_index": 0,
    "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
    "font_index_ko": 0,
    "font_size_title": 58,
    "font_size_es": 58,
    "min_font_size_es": 30,
    "font_size_ko": 32,
    "font_size_example": 30,
    "background_color": (248, 247, 242),
    "text_color": (31, 35, 40),
    "muted_text_color": (96, 101, 109),
    "intro_title": "Quiero un café para llevar",
    "intro_subtitle": "Español A1+ · Ep.28",
    "intro_ko": "커피 하나 포장해 주세요",
    "intro_scene_image_path": "images/ep28-quiero-cafe-para-llevar-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "Para llevar",
    "thumbnail_subtitle": "Español A1+ · Ep.28",
    "thumbnail_ko": "포장해 주세요",
    "outro_ko": "이제 스페인어로 카페 포장 주문을 말할 수 있어요",
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
            "text_es": "Hoy Jin aprende a pedir algo para llevar: quiero un café para llevar.",
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
                "Muy bien. Ahora puedes pedir algo para llevar: "
                "quiero un café para llevar, quiero un té para llevar, para llevar, por favor."
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
    {"segment": 2, "title": "Para llevar"},
    {"segment": 11, "title": "Quiero un café"},
    {"segment": 20, "title": "Cambia el producto"},
    {"segment": 29, "title": "Mini prueba"},
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
