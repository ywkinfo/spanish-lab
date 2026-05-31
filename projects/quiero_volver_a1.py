"""A1 travel follow-up story episode: Jin says what he wants to do after Toledo."""

from __future__ import annotations

IMAGE_PATH = "assets/generated/ep13-quiero-volver-source.png"
DESCRIP_PATH = "a1-quiero-volver/descrip.md"
OUTPUT_NAME = "quiero-volver"
PUBLIC_SLUG = "a1-quiero-volver"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 13
LEVEL = "A1"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a1-quiero-volver.jpg"
YOUTUBE_TITLE = "Quiero volver 😊 다시 가고 싶어 | Español A1 · Ep.13"
DESCRIPTION_INTRO = (
    "Después del viaje a Toledo, Jin mira sus fotos con Lucía y Diego. "
    "En este episodio practicamos una frase A1 muy útil: Quiero + infinitivo. "
    "Aprende a decir: Quiero volver, Quiero descansar, Quiero ver las fotos "
    "y Quiero practicar español."
)
DESCRIPTION_OUTRO = (
    "Escucha primero, repite en voz alta y después crea tu propia frase: "
    "Quiero volver, quiero descansar, quiero ver las fotos o quiero practicar español."
)
KOREAN_TEASER = (
    "한국어 티저: EP.13에서는 EP.12의 여행 후 대화를 이어서 ‘~하고 싶어’를 말하는 "
    "Quiero + 동사원형을 연습합니다. 다시 가고 싶어, 쉬고 싶어, 사진 보고 싶어, "
    "스페인어 연습하고 싶어를 A1 문장으로 말해 보세요."
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
    "Quiero volver",
    "Quiero infinitivo",
    "querer en español",
    "viaje en español",
    "Toledo en español",
    "conversacion español A1",
    "스페인어 여행",
    "스페인어 회화",
    "스페인어 동사원형",
]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#frasesenespañol", "#QuieroVolver"]

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
    {"block_id": 1, "title_es": "Quiero volver", "title_ko": "다시 가고 싶어", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "Quiero descansar", "title_ko": "쉬고 싶어", "color_block": "amber", "start": 10},
    {"block_id": 3, "title_es": "Quiero ver las fotos", "title_ko": "사진을 보고 싶어", "color_block": "teal", "start": 16},
    {"block_id": 4, "title_es": "Quiero practicar español", "title_ko": "스페인어를 연습하고 싶어", "color_block": "blue", "start": 24},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Jin", "Mira, Lucía. Tengo fotos de Toledo.", "봐, Lucía. 톨레도 사진이 있어.", "tengo fotos", 1, "coral", 9.0),
    (2, "Lucía", "¡Qué bonitas! ¿Quieres volver?", "정말 예쁘다! 다시 가고 싶어?", "¿Quieres volver?", 1, "coral", 8.5),
    (3, "Jin", "Sí, quiero volver.", "응, 다시 가고 싶어.", "quiero volver", 1, "coral", 8.0),
    (4, "Diego", "Muy bien. Hoy practicamos: quiero volver.", "좋아. 오늘은 quiero volver를 연습해요.", "quiero volver", 1, "coral", 9.5),
    (5, "Diego", "Jin, repite: quiero volver.", "Jin, 따라 해 봐: quiero volver.", "repite", 1, "coral", 8.5),
    (6, "Jin", "Quiero volver.", "다시 가고 싶어.", "quiero volver", 1, "coral", 7.5),
    (7, "Lucía", "¿Quieres volver a Toledo?", "톨레도에 다시 가고 싶어?", "volver a Toledo", 1, "coral", 8.5),
    (8, "Jin", "Sí, quiero volver a Toledo.", "응, 톨레도에 다시 가고 싶어.", "quiero volver a Toledo", 1, "coral", 9.0),
    (9, "Diego", "Perfecto. Después de quiero, usamos un verbo.", "완벽해요. quiero 뒤에는 동사를 써요.", "quiero + verbo", 1, "coral", 10.0),
    (10, "Lucía", "Después del viaje, ¿qué quieres hacer?", "여행 후에 뭘 하고 싶어?", "¿qué quieres hacer?", 2, "amber", 9.0),
    (11, "Jin", "Quiero descansar.", "쉬고 싶어.", "quiero descansar", 2, "amber", 8.0),
    (12, "Lucía", "Claro. El viaje fue bonito, pero largo.", "그렇지. 여행은 좋았지만 길었어.", "bonito, pero largo", 2, "amber", 9.0),
    (13, "Jin", "Quiero descansar un poco.", "조금 쉬고 싶어.", "un poco", 2, "amber", 8.5),
    (14, "Diego", "Muy natural: quiero descansar un poco.", "아주 자연스러워요: quiero descansar un poco.", "muy natural", 2, "amber", 9.5),
    (15, "Lucía", "Yo también quiero descansar.", "나도 쉬고 싶어.", "yo también", 2, "amber", 8.0),
    (16, "Jin", "Pero primero, quiero ver las fotos.", "하지만 먼저, 사진을 보고 싶어.", "quiero ver", 3, "teal", 9.0),
    (17, "Diego", "Buena frase: quiero ver las fotos.", "좋은 문장이에요: quiero ver las fotos.", "quiero ver las fotos", 3, "teal", 9.0),
    (18, "Jin", "¿Quieres ver esta foto?", "이 사진을 보고 싶어?", "esta foto", 3, "teal", 8.5),
    (19, "Lucía", "Sí, quiero ver la foto.", "응, 그 사진을 보고 싶어.", "quiero ver la foto", 3, "teal", 8.5),
    (20, "Jin", "Es la catedral de Toledo.", "톨레도 대성당이야.", "catedral", 3, "teal", 8.0),
    (21, "Lucía", "¡Muy bonita! Quiero visitar Toledo.", "정말 예쁘다! 톨레도를 방문하고 싶어.", "quiero visitar", 3, "teal", 9.0),
    (22, "Diego", "Yo quiero sacar fotos allí.", "나는 거기서 사진을 찍고 싶어.", "quiero sacar fotos", 3, "teal", 8.5),
    (23, "Jin", "Y yo quiero comer tortilla otra vez.", "그리고 나는 토르티야를 또 먹고 싶어.", "otra vez", 3, "teal", 9.0),
    (24, "Diego", "Muy bien. Ahora, español.", "좋아요. 이제 스페인어예요.", "ahora español", 4, "blue", 8.0),
    (25, "Jin", "Quiero practicar español.", "스페인어를 연습하고 싶어.", "quiero practicar", 4, "blue", 8.5),
    (26, "Diego", "Excelente. Quiero practicar español.", "훌륭해요. Quiero practicar español.", "practicar español", 4, "blue", 9.0),
    (27, "Lucía", "Jin, una frase completa.", "Jin, 완전한 문장 하나.", "frase completa", 4, "blue", 8.0),
    (28, "Jin", "Hoy quiero descansar y practicar español.", "오늘은 쉬고 스페인어를 연습하고 싶어.", "hoy quiero", 4, "blue", 9.5),
    (29, "Diego", "Perfecto. Viaje, fotos y español.", "완벽해. 여행, 사진, 그리고 스페인어.", "viaje y español", 4, "blue", 8.5),
    (30, "Jin", "Sí. Quiero volver y quiero aprender más.", "응. 다시 가고 싶고 더 배우고 싶어.", "aprender más", 4, "blue", 9.5),
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
    "intro_title": "Quiero volver",
    "intro_subtitle": "Español A1 · Ep.13",
    "intro_ko": "다시 가고 싶어",
    "intro_scene_image_path": "assets/generated/ep13-quiero-volver-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "Quiero volver",
    "thumbnail_subtitle": "Español A1 · Ep.13",
    "thumbnail_ko": "다시 가고 싶어",
    "outro_ko": "이제 스페인어로 하고 싶은 일을 말할 수 있어요",
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
                "Hoy seguimos después del viaje de Jin. Mira las fotos de Toledo "
                "con Lucía y Diego. Practicamos una frase muy útil: quiero más un verbo."
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
                "Muy bien. Ahora puedes decir lo que quieres hacer: quiero volver, "
                "quiero descansar, quiero ver las fotos y quiero practicar español."
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
    {"segment": 2, "title": "Quiero volver"},
    {"segment": 12, "title": "Quiero descansar"},
    {"segment": 19, "title": "Quiero ver las fotos"},
    {"segment": 28, "title": "Quiero practicar español"},
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
