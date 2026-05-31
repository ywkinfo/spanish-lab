"""A1 story-card episode: Jin makes a simple Spanish practice plan."""

from __future__ import annotations

IMAGE_PATH = "assets/generated/ep14-voy-a-practicar-source.png"
DESCRIP_PATH = "a1-voy-a-practicar/descrip.md"
OUTPUT_NAME = "voy-a-practicar"
PUBLIC_SLUG = "a1-voy-a-practicar"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 14
LEVEL = "A1"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a1-voy-a-practicar.jpg"
YOUTUBE_TITLE = "Voy a practicar mañana 📚 내일 연습할 거야 | Español A1 · Ep.14"
DESCRIPTION_INTRO = (
    "Después de decir que quiere aprender más, Jin hace un plan sencillo con Lucía y Diego. "
    "En este episodio practicamos una frase A1 muy útil: Voy a + infinitivo. "
    "Aprende a decir: Voy a practicar mañana, Voy a escuchar y repetir, "
    "Voy a hablar un poco y Voy a aprender más."
)
DESCRIPTION_OUTRO = (
    "Escucha primero, repite en voz alta y después crea tu propio plan: "
    "voy a practicar, voy a escuchar, voy a repetir, voy a hablar o voy a aprender más."
)
KOREAN_TEASER = (
    "한국어 티저: EP.14에서는 EP.13의 ‘더 배우고 싶어’에서 이어져, 내일 할 일을 말하는 "
    "Voy a + 동사원형을 연습합니다. 연습할 거야, 듣고 따라 할 거야, 조금 말할 거야, "
    "더 배울 거야를 A1 문장으로 말해 보세요."
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
    "Voy a practicar",
    "Voy a infinitivo",
    "futuro próximo español",
    "practicar español",
    "conversacion español A1",
    "스페인어 회화",
    "스페인어 동사원형",
    "스페인어 미래 표현",
]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#frasesenespañol", "#VoyAPracticar"]

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
    {"block_id": 1, "title_es": "Voy a practicar mañana", "title_ko": "내일 연습할 거야", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "Voy a escuchar y repetir", "title_ko": "듣고 따라 할 거야", "color_block": "amber", "start": 9},
    {"block_id": 3, "title_es": "Voy a hablar un poco", "title_ko": "조금 말할 거야", "color_block": "teal", "start": 16},
    {"block_id": 4, "title_es": "Voy a aprender más", "title_ko": "더 배울 거야", "color_block": "blue", "start": 24},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Jin", "Mañana voy a practicar español.", "내일 스페인어를 연습할 거야.", "voy a practicar", 1, "coral", 9.0),
    (2, "Lucía", "¡Muy bien! ¿Vas a practicar mañana?", "아주 좋아! 내일 연습할 거야?", "¿vas a practicar?", 1, "coral", 8.5),
    (3, "Jin", "Sí, voy a practicar mañana.", "응, 내일 연습할 거야.", "voy a practicar mañana", 1, "coral", 8.5),
    (4, "Diego", "Perfecto. Hoy practicamos: voy a practicar.", "완벽해요. 오늘은 voy a practicar를 연습해요.", "voy a practicar", 1, "coral", 9.5),
    (5, "Diego", "Jin, repite: voy a practicar.", "Jin, 따라 해 봐: voy a practicar.", "repite", 1, "coral", 8.5),
    (6, "Jin", "Voy a practicar.", "연습할 거야.", "voy a practicar", 1, "coral", 7.5),
    (7, "Lucía", "¿Vas a practicar en casa?", "집에서 연습할 거야?", "en casa", 1, "coral", 8.5),
    (8, "Jin", "Sí, voy a practicar en casa.", "응, 집에서 연습할 거야.", "voy a practicar en casa", 1, "coral", 9.0),
    (9, "Jin", "Primero, voy a escuchar.", "먼저, 들을 거야.", "voy a escuchar", 2, "amber", 8.0),
    (10, "Diego", "Muy bien: voy a escuchar.", "아주 좋아: voy a escuchar.", "voy a escuchar", 2, "amber", 8.0),
    (11, "Jin", "Después, voy a repetir.", "그다음, 따라 할 거야.", "voy a repetir", 2, "amber", 8.0),
    (12, "Lucía", "Escuchar y repetir. Muy buena idea.", "듣고 따라 하기. 아주 좋은 생각이야.", "escuchar y repetir", 2, "amber", 8.5),
    (13, "Jin", "Voy a escuchar y repetir.", "듣고 따라 할 거야.", "voy a escuchar y repetir", 2, "amber", 8.5),
    (14, "Diego", "Despacio, Jin: voy a escuchar y repetir.", "천천히, Jin: voy a escuchar y repetir.", "despacio", 2, "amber", 9.5),
    (15, "Jin", "Voy a escuchar y repetir.", "듣고 따라 할 거야.", "voy a escuchar y repetir", 2, "amber", 8.5),
    (16, "Jin", "Luego, voy a hablar un poco.", "그다음, 조금 말할 거야.", "voy a hablar", 3, "teal", 8.5),
    (17, "Lucía", "¡Eso es! Hablar un poco es importante.", "바로 그거야! 조금 말하는 것이 중요해.", "hablar un poco", 3, "teal", 9.0),
    (18, "Jin", "Voy a hablar un poco con Lucía.", "Lucía와 조금 말할 거야.", "con Lucía", 3, "teal", 9.0),
    (19, "Lucía", "Claro, vamos a hablar juntos.", "물론이지, 같이 말해 보자.", "juntos", 3, "teal", 8.5),
    (20, "Jin", "Diego, ¿está bien mi frase?", "Diego, 내 문장 괜찮아요?", "mi frase", 3, "teal", 8.5),
    (21, "Diego", "Sí. Voy a hablar un poco. Muy natural.", "네. Voy a hablar un poco. 아주 자연스러워요.", "muy natural", 3, "teal", 9.5),
    (22, "Jin", "Voy a hablar un poco.", "조금 말할 거야.", "voy a hablar un poco", 3, "teal", 8.0),
    (23, "Diego", "Muy bien, Jin. Poco a poco.", "아주 좋아, Jin. 조금씩.", "poco a poco", 3, "teal", 8.0),
    (24, "Jin", "Y mañana, voy a aprender más.", "그리고 내일, 더 배울 거야.", "voy a aprender", 4, "blue", 8.5),
    (25, "Diego", "Excelente. Voy a aprender más.", "훌륭해요. Voy a aprender más.", "aprender más", 4, "blue", 8.5),
    (26, "Lucía", "¿Qué vas a aprender?", "무엇을 배울 거야?", "¿qué vas a aprender?", 4, "blue", 8.0),
    (27, "Jin", "Voy a aprender frases útiles.", "유용한 표현을 배울 거야.", "frases útiles", 4, "blue", 8.5),
    (28, "Diego", "Primero escuchar, repetir y hablar.", "먼저 듣고, 따라 하고, 말하기.", "recap", 4, "blue", 8.5),
    (29, "Jin", "Sí. Voy a practicar y voy a aprender más.", "응. 연습하고 더 배울 거야.", "voy a practicar", 4, "blue", 9.5),
    (30, "Lucía", "Perfecto. Mañana seguimos juntos.", "완벽해. 내일 같이 계속하자.", "mañana seguimos", 4, "blue", 8.5),
]

DESIGN = {
    "output_size": (1280, 720),
    "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
    "font_index": 0,
    "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
    "font_index_ko": 0,
    "font_size_title": 66,
    "font_size_es": 68,
    "min_font_size_es": 38,
    "font_size_ko": 32,
    "font_size_example": 30,
    "background_color": (248, 247, 242),
    "text_color": (31, 35, 40),
    "muted_text_color": (96, 101, 109),
    "intro_title": "Voy a practicar",
    "intro_subtitle": "Español A1 · Ep.14",
    "intro_ko": "연습할 거야",
    "intro_scene_image_path": "assets/generated/ep14-voy-a-practicar-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "Voy a practicar",
    "thumbnail_subtitle": "Español A1 · Ep.14",
    "thumbnail_ko": "연습할 거야",
    "outro_ko": "이제 스페인어로 내일 할 일을 말할 수 있어요",
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
            "text_es": (
                "Hoy Jin hace un plan para mañana. Practicamos una frase muy útil: "
                "voy a seguido de un verbo."
            ),
            "duration_s": 14.0,
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
                "Muy bien. Ahora puedes hacer un plan sencillo en español: voy a practicar, "
                "voy a escuchar, voy a repetir, voy a hablar y voy a aprender más."
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
    {"segment": 2, "title": "Voy a practicar"},
    {"segment": 11, "title": "Escuchar y repetir"},
    {"segment": 19, "title": "Hablar un poco"},
    {"segment": 28, "title": "Aprender más"},
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
