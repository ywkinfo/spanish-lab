"""A1+ story-card episode: Jin gives a short reason with porque."""

from __future__ import annotations

IMAGE_PATH = "images/ep20-porque-tengo-sueno-source.png"
DESCRIP_PATH = "a1-porque-tengo-sueno/descrip.md"
OUTPUT_NAME = "porque-tengo-sueno"
PUBLIC_SLUG = "a1-porque-tengo-sueno"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 20
LEVEL = "A1+"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a1-ep20-porque-tengo-sueno.jpg"
YOUTUBE_TITLE = "Porque tengo sueño 😴 졸려서요 | Español A1+ · Ep.20"
DESCRIPTION_INTRO = (
    "Jin sigue en la cafetería con Lucía y Diego. Después de decir prefiero café, "
    "aprende a responder a ¿por qué? con una razón corta: porque tengo sueño. "
    "Practicamos porque tengo sueño, prefiero café porque tengo sueño y quiero agua porque tengo sed."
)
DESCRIPTION_OUTRO = (
    "Escucha primero, repite en voz alta y después di tu propia razón: "
    "porque tengo sueño, porque tengo sed o porque hace calor."
)
KOREAN_TEASER = (
    "한국어 티저: EP.20에서는 '왜요?'라는 질문에 짧게 이유를 말하는 A1+ 표현을 연습합니다. "
    "핵심 표현은 하나, porque + 이유입니다. Porque tengo sueño, Quiero agua porque tengo sed처럼 바로 따라 말해 보세요."
)
BASE_TAGS = ["스페인어", "스페인어 입문", "스페인어 A1", "Spanish A1", "aprender español", "español para principiantes"]
EXTRA_TAGS = ["porque", "porque en español", "Spanish reasons", "Spanish A1+", "스페인어 회화", "스페인어 이유 말하기"]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#Madrid", "#Porque"]

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
    {"block_id": 1, "title_es": "Hace calor", "title_ko": "더워요", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "¿Por qué?", "title_ko": "왜요?", "color_block": "teal", "start": 8},
    {"block_id": 3, "title_es": "Porque tengo sueño", "title_ko": "졸려서요", "color_block": "amber", "start": 18},
    {"block_id": 4, "title_es": "Mini prueba", "title_ko": "미니 퀴즈", "color_block": "blue", "start": 25},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Diego", "Hoy Jin aprende a responder con una razón: porque tengo sueño.", "오늘 Jin은 이유를 대답하는 표현을 배워요: 졸려서요.", "porque", 1, "coral", 10.0),
    (2, "Lucía", "Seguimos en la cafetería.", "우리는 계속 카페에 있어요.", "cafetería", 1, "coral", 7.5),
    (3, "Lucía", "Hace calor en Madrid.", "마드리드는 더워요.", "contexto", 1, "coral", 7.5),
    (4, "Diego", "Jin está un poco cansado.", "Jin은 조금 피곤해요.", "contexto", 1, "coral", 7.5),
    (5, "Lucía", "Jin, ¿quieres café o té?", "Jin, 커피 원해요, 아니면 차 원해요?", "opciones", 1, "coral", 8.0),
    (6, "Jin", "Prefiero café.", "저는 커피가 더 좋아요.", "repaso", 1, "coral", 7.0),
    (7, "Diego", "Muy bien. Ahora vamos a decir la razón.", "좋아요. 이제 이유를 말해 볼 거예요.", "razón", 1, "coral", 9.0),
    (8, "Diego", "Diego pregunta: ¿por qué?", "Diego가 물어요: 왜요?", "pregunta", 2, "teal", 8.0),
    (9, "Diego", "¿Por qué?", "왜요?", "por qué", 2, "teal", 6.0),
    (10, "Jin", "Porque tengo sueño.", "졸려서요.", "modelo", 2, "teal", 7.5),
    (11, "Lucía", "Repite: porque tengo sueño.", "따라 하세요: 졸려서요.", "repetición", 2, "teal", 8.0),
    (12, "Diego", "Porque significa: 이유를 말해요.", "porque는 이유를 말한다는 뜻이에요.", "significado", 2, "teal", 8.5),
    (13, "Diego", "En español: porque.", "스페인어로는 porque예요.", "porque", 2, "teal", 7.0),
    (14, "Lucía", "En coreano: 왜냐하면, 또는 ~해서.", "한국어로는 왜냐하면, 또는 ~해서예요.", "traducción", 2, "teal", 8.5),
    (15, "Diego", "Una frase corta es suficiente.", "짧은 문장이면 충분해요.", "simple", 2, "teal", 8.0),
    (16, "Lucía", "¿Por qué prefieres café?", "왜 커피가 더 좋아요?", "pregunta", 2, "teal", 8.0),
    (17, "Jin", "Porque tengo sueño.", "졸려서요.", "respuesta", 2, "teal", 7.5),
    (18, "Diego", "Ahora una frase completa.", "이제 완전한 문장이에요.", "frase completa", 3, "amber", 7.5),
    (19, "Jin", "Prefiero café porque tengo sueño.", "졸려서 커피가 더 좋아요.", "frase completa", 3, "amber", 8.5),
    (20, "Diego", "Perfecto. Es una preferencia y una razón.", "완벽해요. 선호와 이유예요.", "preferencia", 3, "amber", 9.0),
    (21, "Lucía", "Otra situación: tengo sed.", "다른 상황: 목말라요.", "tengo sed", 3, "amber", 7.5),
    (22, "Jin", "Quiero agua porque tengo sed.", "목말라서 물을 원해요.", "tengo sed", 3, "amber", 8.5),
    (23, "Diego", "Muy natural. Porque tengo sed.", "아주 자연스러워요. 목말라서요.", "razón", 3, "amber", 8.0),
    (24, "Jin", "Me quedo aquí porque hace calor.", "더워서 여기 있을래요.", "hace calor", 3, "amber", 8.5),
    (25, "Diego", "Mini prueba: ¿qué significa porque tengo sueño?", "미니 퀴즈: porque tengo sueño는 무슨 뜻일까요?", "quiz", 4, "blue", 9.5),
    (26, "Lucía", "Significa: 졸려서요.", "뜻은 졸려서요예요.", "respuesta", 4, "blue", 7.5),
    (27, "Diego", "Pregunta: ¿por qué prefieres café?", "질문: 왜 커피가 더 좋아요?", "pregunta", 4, "blue", 8.5),
    (28, "Jin", "Respuesta: porque tengo sueño.", "대답: 졸려서요.", "respuesta", 4, "blue", 7.5),
    (29, "Diego", "Otra frase: quiero agua porque tengo sed.", "다른 문장: 목말라서 물을 원해요.", "otra frase", 4, "blue", 9.0),
    (30, "Diego", "Excelente. Ya puedes dar una razón corta.", "훌륭해요. 이제 짧은 이유를 말할 수 있어요.", "cierre", 4, "blue", 9.0),
]

DESIGN = {
    "output_size": (1280, 720),
    "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
    "font_index": 0,
    "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
    "font_index_ko": 0,
    "font_size_title": 66,
    "font_size_es": 62,
    "min_font_size_es": 34,
    "font_size_ko": 32,
    "font_size_example": 30,
    "background_color": (248, 247, 242),
    "text_color": (31, 35, 40),
    "muted_text_color": (96, 101, 109),
    "intro_title": "Porque tengo sueño",
    "intro_subtitle": "Español A1+ · Ep.20",
    "intro_ko": "졸려서요",
    "intro_scene_image_path": "images/ep20-porque-tengo-sueno-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "Porque tengo sueño",
    "thumbnail_subtitle": "Español A1+ · Ep.20",
    "thumbnail_ko": "졸려서요",
    "outro_ko": "이제 스페인어로 짧은 이유를 말할 수 있어요",
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
            "text_es": "Hoy Jin aprende a dar una razón corta: porque tengo sueño.",
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
                "Muy bien. Ahora puedes responder a por qué con una razón corta: "
                "porque tengo sueño, porque tengo sed o porque hace calor."
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
    {"segment": 2, "title": "Hace calor"},
    {"segment": 10, "title": "¿Por qué?"},
    {"segment": 21, "title": "Porque tengo sueño"},
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
