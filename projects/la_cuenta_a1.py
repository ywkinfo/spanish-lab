"""A1 café story episode: Lucía asks for the bill and pays."""

from __future__ import annotations

IMAGE_PATH = "assets/generated/lucia-cafe-bill-thumbnail-source.png"
DESCRIP_PATH = "a1-la-cuenta/descrip.md"
OUTPUT_NAME = "la-cuenta"
PUBLIC_SLUG = "a1-la-cuenta"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 8
LEVEL = "A1"
LANGUAGE = "es"
RENDER_VERSION = 3
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a1-la-cuenta.jpg"
YOUTUBE_TITLE = "La cuenta, por favor 💶 카페에서 계산하기 | Español A1 · Ep.8"
DESCRIPTION_INTRO = (
    "Después del café de Ep.7, Lucía está lista para pedir la cuenta. "
    "Jin, Lucía y Diego practican una escena muy útil de cafetería: pedir la cuenta, preguntar el precio y pagar con tarjeta."
)
DESCRIPTION_OUTRO = (
    "Escucha primero, repite en voz alta y después haz toda la escena tú: "
    "La cuenta, por favor. ¿Cuánto es? Pago con tarjeta. Gracias."
)
KOREAN_TEASER = (
    "한국어 티저: EP.8은 카페에서 계산서를 요청하고 가격을 확인한 뒤 카드로 결제하는 A1 상황극입니다. "
    "이번 편부터 한국인 학습자 이름은 Jin으로 사용합니다."
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
    "la cuenta por favor",
    "cafeteria español",
    "pagar en español",
    "cuanto es español",
    "pago con tarjeta",
    "conversacion español A1",
    "스페인어 카페 표현",
    "스페인어 계산하기",
]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#frasesenespañol", "#Cafetería"]

CHARACTERS = {
    "Jin": "assets/characters/peter-profile.png",
    "Lucía": "assets/generated/lucia-cafe-bill-lucia-centered-portrait.png",
    "Diego": "assets/characters/diego-profile.png",
}
CHARACTER_VOICES = {
    "Lucía": "es-ES-ElviraNeural",
    "Jin": "es-ES-AlvaroNeural",
    "Diego": "es-MX-JorgeNeural",
}

BLOCKS = [
    {"block_id": 1, "title_es": "La escena termina", "title_ko": "카페 장면 마무리", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "La cuenta, por favor", "title_ko": "계산서 요청하기", "color_block": "amber", "start": 8},
    {"block_id": 3, "title_es": "¿Cuánto es?", "title_ko": "얼마인지 묻기", "color_block": "teal", "start": 16},
    {"block_id": 4, "title_es": "Pago con tarjeta", "title_ko": "결제하고 인사하기", "color_block": "blue", "start": 24},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Diego", "Mira la imagen, Jin.", "Jin, 그림을 봐.", "Mira la imagen", 1, "coral", 8.0),
    (2, "Jin", "Veo a Lucía en la cafetería.", "카페에 있는 루시아가 보여.", "Veo a Lucía", 1, "coral", 8.5),
    (3, "Diego", "Muy bien. ¿Qué hay en la mesa?", "좋아. 테이블 위에 뭐가 있어?", "¿Qué hay?", 1, "coral", 8.5),
    (4, "Jin", "Hay una taza y una tapa.", "컵과 타파스가 있어.", "Hay una taza", 1, "coral", 8.5),
    (5, "Diego", "También hay una cuenta pequeña.", "작은 계산서도 있어.", "una cuenta", 1, "coral", 8.5),
    (6, "Lucía", "Ya terminé el café.", "나는 커피를 다 마셨어.", "Ya terminé", 1, "coral", 8.5),
    (7, "Diego", "Perfecto. Ahora pedimos la cuenta.", "좋아. 이제 계산서를 요청해 보자.", "pedimos la cuenta", 1, "coral", 9.0),
    (8, "Diego", "Repite despacio: la cuenta.", "천천히 반복해: 계산서.", "la cuenta", 2, "amber", 8.0),
    (9, "Jin", "La cuenta.", "계산서.", "La cuenta", 2, "amber", 8.0),
    (10, "Diego", "Ahora completo: La cuenta, por favor.", "이제 전체 문장: 계산서 주세요.", "por favor", 2, "amber", 9.0),
    (11, "Jin", "La cuenta, por favor.", "계산서 주세요.", "frase central", 2, "amber", 8.5),
    (12, "Lucía", "Perdón, la cuenta, por favor.", "실례합니다, 계산서 주세요.", "Perdón", 2, "amber", 9.0),
    (13, "Diego", "Muy natural. Usa por favor.", "아주 자연스러워. por favor를 써.", "cortesía", 2, "amber", 8.5),
    (14, "Jin", "Por favor.", "부탁합니다.", "Por favor", 2, "amber", 8.0),
    (15, "Jin", "La cuenta, por favor.", "계산서 주세요.", "repetición", 2, "amber", 8.5),
    (16, "Diego", "Ahora pregunta el precio.", "이제 가격을 물어봐.", "pregunta", 3, "teal", 8.5),
    (17, "Jin", "¿Cuánto es?", "얼마예요?", "¿Cuánto es?", 3, "teal", 8.0),
    (18, "Lucía", "Son cinco euros.", "5유로입니다.", "cinco euros", 3, "teal", 8.0),
    (19, "Jin", "Cinco euros.", "5유로.", "número", 3, "teal", 8.0),
    (20, "Diego", "Muy bien. Escucha y repite.", "좋아. 듣고 반복해.", "repite", 3, "teal", 8.5),
    (21, "Lucía", "Son cinco euros, por favor.", "5유로입니다.", "precio", 3, "teal", 8.5),
    (22, "Jin", "Son cinco euros.", "5유로입니다.", "Son cinco euros", 3, "teal", 8.0),
    (23, "Diego", "En una cafetería, es una frase muy útil.", "카페에서 아주 유용한 표현이야.", "frase útil", 3, "teal", 9.0),
    (24, "Diego", "Ahora pagamos.", "이제 계산해.", "pagamos", 4, "blue", 8.0),
    (25, "Jin", "Pago con tarjeta.", "카드로 낼게요.", "con tarjeta", 4, "blue", 8.5),
    (26, "Lucía", "Aquí tiene.", "여기 있습니다.", "Aquí tiene", 4, "blue", 8.0),
    (27, "Jin", "Gracias.", "감사합니다.", "Gracias", 4, "blue", 8.0),
    (28, "Lucía", "De nada.", "천만에요.", "De nada", 4, "blue", 8.0),
    (29, "Diego", "Muy bien. Ahora toda la escena.", "좋아. 이제 전체 장면.", "escena completa", 4, "blue", 8.5),
    (30, "Jin", "La cuenta, por favor. ¿Cuánto es? Pago con tarjeta. Gracias.", "계산서 주세요. 얼마예요? 카드로 낼게요. 감사합니다.", "escena completa", 4, "blue", 10.0),
]

DESIGN = {
    "output_size": (1280, 720),
    "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
    "font_index": 0,
    "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
    "font_index_ko": 0,
    "font_size_title": 70,
    "font_size_es": 68,
    "min_font_size_es": 38,
    "font_size_ko": 32,
    "font_size_example": 30,
    "background_color": (248, 247, 242),
    "text_color": (31, 35, 40),
    "muted_text_color": (96, 101, 109),
    "intro_title": "La cuenta, por favor",
    "intro_subtitle": "Español A1 · Ep.8",
    "intro_ko": "카페에서 계산서 요청하고 결제하기",
    "intro_scene_image_path": "assets/generated/lucia-cafe-bill-thumbnail-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "La cuenta, por favor",
    "thumbnail_subtitle": "Español A1 · Ep.8",
    "thumbnail_ko": "카페에서 계산하기",
    "outro_ko": "이제 카페에서 직접 계산해 보세요",
    "outro_font_size_es": 27,
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
            "text_es": (
                "Hoy seguimos en la cafetería. Lucía ya terminó el café y ahora practica una frase muy útil: "
                "la cuenta, por favor."
            ),
            "duration_s": 12.0,
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
                    "character": speaker,
                }
            )
    segments.append(
        {
            "type": "outro",
            "text_es": (
                "Muy bien. Ahora haz toda la escena tú: La cuenta, por favor. ¿Cuánto es? "
                "Pago con tarjeta. Gracias. En el próximo episodio salimos de la cafetería y preguntamos por un lugar."
            ),
            "duration_s": 23.0,
            "color_block": "neutral",
            "characters": ["Jin", "Lucía", "Diego"],
        }
    )
    return segments


SEGMENTS = _build_segments()
CHAPTERS = [
    {"segment": 1, "title": "Introducción"},
    {"segment": 2, "title": "La escena termina"},
    {"segment": 10, "title": "La cuenta, por favor"},
    {"segment": 19, "title": "¿Cuánto es?"},
    {"segment": 27, "title": "Pago con tarjeta"},
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
