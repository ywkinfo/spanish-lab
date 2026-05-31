"""A1+ story-card episode: Jin says what he never does with nunca."""

from __future__ import annotations

IMAGE_PATH = "images/ep23-nunca-tomo-cafe-source.png"
DESCRIP_PATH = "a1-nunca-tomo-cafe/descrip.md"
OUTPUT_NAME = "nunca-tomo-cafe"
PUBLIC_SLUG = "a1-nunca-tomo-cafe"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 23
LEVEL = "A1+"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a1-ep23-nunca-tomo-cafe.jpg"
YOUTUBE_TITLE = "Nunca tomo café por la noche ☕ 밤에는 커피 안 마셔요 | Español A1+ · Ep.23"
DESCRIPTION_INTRO = (
    "Jin completa una pequeña serie de palabras de frecuencia después de a veces y siempre. "
    "En este episodio aprende a decir lo que no hace: nunca tomo café por la noche."
)
DESCRIPTION_OUTRO = (
    "Escucha primero, repite en voz alta y después cambia la acción: "
    "nunca tomo café, nunca estudio sin mi cuaderno, nunca como tarde."
)
KOREAN_TEASER = (
    "한국어 티저: EP.23에서는 Ep.21 a veces, Ep.22 siempre 다음 단계로 '절대/전혀 ~하지 않아요'를 말합니다. "
    "핵심 표현은 하나, nunca + 현재형입니다. Nunca tomo café por la noche처럼 따라 말해 보세요."
)
BASE_TAGS = ["스페인어", "스페인어 입문", "스페인어 A1", "Spanish A1", "aprender español", "español para principiantes"]
EXTRA_TAGS = ["nunca", "nunca en español", "Spanish negative", "Spanish frequency", "Spanish A1+", "스페인어 회화"]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#Nunca", "#SpanishLab"]

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
    {"block_id": 1, "title_es": "Por la noche", "title_ko": "밤에", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "Nunca", "title_ko": "절대 안", "color_block": "teal", "start": 10},
    {"block_id": 3, "title_es": "Mi frase negativa", "title_ko": "나의 부정문", "color_block": "amber", "start": 19},
    {"block_id": 4, "title_es": "Mini prueba", "title_ko": "미니 퀴즈", "color_block": "blue", "start": 25},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Diego", "Hoy seguimos con palabras de frecuencia.", "오늘은 빈도 표현을 계속 배워요.", "frecuencia", 1, "coral", 8.5),
    (2, "Lucía", "Ya vimos a veces y siempre.", "우리는 이미 a veces와 siempre를 봤어요.", "repaso", 1, "coral", 8.0),
    (3, "Diego", "Hoy aprendemos una palabra nueva: nunca.", "오늘은 새 단어 nunca를 배워요.", "nunca", 1, "coral", 8.5),
    (4, "Lucía", "Jin está estudiando por la noche.", "Jin은 밤에 공부하고 있어요.", "contexto", 1, "coral", 8.0),
    (5, "Diego", "Tiene una taza de café en la mesa.", "책상 위에 커피 한 잔이 있어요.", "café", 1, "coral", 8.0),
    (6, "Lucía", "Jin, ¿tomas café por la noche?", "Jin, 밤에 커피를 마셔요?", "pregunta", 1, "coral", 7.5),
    (7, "Jin", "No. Tomo café por la mañana.", "아니요. 저는 아침에 커피를 마셔요.", "contraste", 1, "coral", 8.0),
    (8, "Diego", "Muy bien. Ahora usamos nunca.", "좋아요. 이제 nunca를 써요.", "añadir", 1, "coral", 8.0),
    (9, "Lucía", "Nunca significa: 절대 안, 전혀 안.", "nunca는 ‘절대 안, 전혀 안’이라는 뜻이에요.", "significado", 1, "coral", 8.5),
    (10, "Diego", "Escucha la frase completa.", "완전한 문장을 들어 보세요.", "modelo", 2, "teal", 7.0),
    (11, "Jin", "Nunca tomo café por la noche.", "저는 밤에는 절대 커피를 마시지 않아요.", "modelo", 2, "teal", 8.5),
    (12, "Lucía", "Repite: nunca.", "따라 하세요: nunca.", "repetición", 2, "teal", 7.0),
    (13, "Jin", "Nunca.", "절대 안 해요.", "repetición", 2, "teal", 6.0),
    (14, "Lucía", "Repite: tomo café.", "따라 하세요: 커피를 마셔요.", "repetición", 2, "teal", 7.0),
    (15, "Jin", "Tomo café.", "저는 커피를 마셔요.", "repetición", 2, "teal", 6.5),
    (16, "Diego", "Ahora todo junto.", "이제 함께 말해요.", "unir", 2, "teal", 6.5),
    (17, "Jin", "Nunca tomo café por la noche.", "밤에는 절대 커피를 마시지 않아요.", "frase completa", 2, "teal", 8.5),
    (18, "Lucía", "Perfecto. Es una frase negativa.", "완벽해요. 부정문이에요.", "negativa", 2, "teal", 8.0),
    (19, "Diego", "Ahora cambiamos la acción.", "이제 행동을 바꿔 봐요.", "acción", 3, "amber", 8.0),
    (20, "Jin", "Nunca estudio sin mi cuaderno.", "저는 공책 없이 공부하지 않아요.", "cuaderno", 3, "amber", 8.5),
    (21, "Lucía", "Literalmente: nunca estudio sin mi cuaderno.", "직역하면: 나는 내 공책 없이 절대 공부하지 않아요.", "literal", 3, "amber", 9.0),
    (22, "Jin", "Nunca voy al trabajo en coche.", "저는 차로 출근하지 않아요.", "trabajo", 3, "amber", 8.5),
    (23, "Diego", "Muy bien. Nunca más una acción.", "좋아요. nunca 뒤에 행동을 붙여요.", "acción", 3, "amber", 8.0),
    (24, "Jin", "Nunca como tarde por la noche.", "저는 밤늦게 먹지 않아요.", "noche", 3, "amber", 8.5),
    (25, "Diego", "Mini prueba: ¿qué significa nunca?", "미니 퀴즈: nunca는 무슨 뜻일까요?", "quiz", 4, "blue", 8.5),
    (26, "Lucía", "Significa: 절대 안, 전혀 안.", "뜻은 ‘절대 안, 전혀 안’이에요.", "respuesta", 4, "blue", 7.5),
    (27, "Diego", "Pregunta: ¿cómo dices 밤에는 커피를 안 마셔요?", "질문: ‘밤에는 커피를 안 마셔요’를 어떻게 말할까요?", "pregunta", 4, "blue", 9.0),
    (28, "Jin", "Nunca tomo café por la noche.", "밤에는 커피를 안 마셔요.", "respuesta", 4, "blue", 8.0),
    (29, "Diego", "Otra frase: nunca estudio sin mi cuaderno.", "다른 문장: 공책 없이 공부하지 않아요.", "otra frase", 4, "blue", 8.5),
    (30, "Lucía", "Excelente. Ya puedes decir lo que no haces.", "훌륭해요. 이제 하지 않는 일을 말할 수 있어요.", "cierre", 4, "blue", 9.0),
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
    # Keep the intro title short and the intro sentence compact so the top three text divisions
    # (title / subtitle / episode sentence) stay visually separate, per Peter's Ep.23 note.
    "intro_title": "Nunca",
    "intro_subtitle": "Español A1+ · Ep.23",
    "intro_ko": "밤에는 커피 안 마셔요",
    "intro_scene_image_path": "images/ep23-nunca-tomo-cafe-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "Nunca tomo café por la noche",
    "thumbnail_subtitle": "Español A1+ · Ep.23",
    "thumbnail_ko": "밤에는 커피 안 마셔요",
    "outro_ko": "이제 스페인어로 하지 않는 일을 말할 수 있어요",
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
            "text_es": "Hoy Jin aprende a decir lo que no hace: nunca tomo café por la noche.",
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
                "Muy bien. Ahora puedes decir lo que no haces: "
                "nunca tomo café, nunca estudio sin mi cuaderno, nunca como tarde."
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
    {"segment": 2, "title": "Por la noche"},
    {"segment": 12, "title": "Nunca"},
    {"segment": 22, "title": "Mi frase negativa"},
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
