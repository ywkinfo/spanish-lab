"""A1+ story-card episode: Jin talks about occasional morning routine with a veces."""

from __future__ import annotations

IMAGE_PATH = "images/ep21-a-veces-me-levanto-temprano-source.png"
DESCRIP_PATH = "a1-a-veces-me-levanto-temprano/descrip.md"
OUTPUT_NAME = "a-veces-me-levanto-temprano"
PUBLIC_SLUG = "a1-a-veces-me-levanto-temprano"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 21
LEVEL = "A1+"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a1-ep21-a-veces-me-levanto-temprano.jpg"
YOUTUBE_TITLE = "A veces me levanto temprano 🌅 가끔 일찍 일어나요 | Español A1+ · Ep.21"
DESCRIPTION_INTRO = (
    "Jin retoma frases de rutina de Ep.1 y aprende a decir frecuencia con una frase simple: "
    "a veces me levanto temprano. Practicamos a veces con tengo tiempo, voy al trabajo y estudio español."
)
DESCRIPTION_OUTRO = (
    "Escucha primero, repite en voz alta y después cambia el verbo: "
    "a veces tengo tiempo, a veces voy al trabajo, a veces estudio español."
)
KOREAN_TEASER = (
    "한국어 티저: EP.21에서는 Ep.1의 루틴 표현을 A1+로 확장합니다. "
    "핵심 표현은 하나, a veces + 현재형입니다. A veces me levanto temprano처럼 '가끔 ~해요'를 말해 보세요."
)
BASE_TAGS = ["스페인어", "스페인어 입문", "스페인어 A1", "Spanish A1", "aprender español", "español para principiantes"]
EXTRA_TAGS = ["a veces", "a veces en español", "Spanish frequency", "Spanish A1+", "스페인어 회화", "스페인어 루틴"]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#AVeces", "#SpanishLab"]

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
    {"block_id": 1, "title_es": "Por la mañana", "title_ko": "아침에", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "A veces", "title_ko": "가끔", "color_block": "teal", "start": 8},
    {"block_id": 3, "title_es": "Mi rutina", "title_ko": "나의 루틴", "color_block": "amber", "start": 18},
    {"block_id": 4, "title_es": "Mini prueba", "title_ko": "미니 퀴즈", "color_block": "blue", "start": 25},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Diego", "Hoy volvemos a una frase de Ep.1: me levanto temprano.", "오늘은 Ep.1의 표현으로 돌아가요: 일찍 일어나요.", "Ep.1", 1, "coral", 9.5),
    (2, "Lucía", "Jin está en casa por la mañana.", "Jin은 아침에 집에 있어요.", "contexto", 1, "coral", 7.5),
    (3, "Jin", "Me levanto temprano.", "저는 일찍 일어나요.", "repaso", 1, "coral", 7.0),
    (4, "Diego", "Muy bien. Ahora añadimos una palabra.", "좋아요. 이제 단어 하나를 추가해요.", "añadir", 1, "coral", 8.5),
    (5, "Lucía", "La palabra es: a veces.", "그 단어는 a veces예요.", "a veces", 1, "coral", 7.0),
    (6, "Diego", "A veces habla de frecuencia.", "a veces는 빈도를 말해요.", "frecuencia", 1, "coral", 8.0),
    (7, "Lucía", "En coreano, suena como: 가끔.", "한국어로는 '가끔'이에요.", "significado", 1, "coral", 7.5),
    (8, "Diego", "Escucha la frase completa.", "완전한 문장을 들어 보세요.", "modelo", 2, "teal", 7.0),
    (9, "Jin", "A veces me levanto temprano.", "저는 가끔 일찍 일어나요.", "modelo", 2, "teal", 8.0),
    (10, "Lucía", "Repite: a veces.", "따라 하세요: a veces.", "repetición", 2, "teal", 7.0),
    (11, "Jin", "A veces.", "가끔.", "repetición", 2, "teal", 6.0),
    (12, "Lucía", "Repite: me levanto temprano.", "따라 하세요: 일찍 일어나요.", "repetición", 2, "teal", 7.5),
    (13, "Jin", "Me levanto temprano.", "저는 일찍 일어나요.", "repetición", 2, "teal", 7.0),
    (14, "Diego", "Ahora todo junto.", "이제 함께 말해요.", "unir", 2, "teal", 6.5),
    (15, "Jin", "A veces me levanto temprano.", "가끔 일찍 일어나요.", "frase completa", 2, "teal", 8.0),
    (16, "Lucía", "Muy natural. Una frase simple y útil.", "아주 자연스러워요. 쉽고 유용한 문장이에요.", "natural", 2, "teal", 8.5),
    (17, "Diego", "No necesitamos una explicación larga.", "긴 설명은 필요 없어요.", "simple", 2, "teal", 8.0),
    (18, "Diego", "Ahora usamos más frases de Ep.1.", "이제 Ep.1의 표현을 더 써 봐요.", "Ep.1", 3, "amber", 8.0),
    (19, "Jin", "A veces tengo tiempo.", "저는 가끔 시간이 있어요.", "tengo tiempo", 3, "amber", 7.5),
    (20, "Lucía", "Literalmente: a veces tengo tiempo.", "직역하면: 나는 가끔 시간이 있어요.", "literal", 3, "amber", 8.5),
    (21, "Jin", "A veces voy al trabajo en metro.", "저는 가끔 지하철로 출근해요.", "trabajo", 3, "amber", 8.5),
    (22, "Diego", "Muy bien. A veces más una acción.", "좋아요. a veces 뒤에 행동을 붙여요.", "acción", 3, "amber", 8.0),
    (23, "Jin", "A veces estudio español por la noche.", "저는 가끔 밤에 스페인어를 공부해요.", "estudio", 3, "amber", 9.0),
    (24, "Lucía", "Perfecto. Es tu rutina, pero no todos los días.", "완벽해요. 루틴이지만 매일은 아니에요.", "rutina", 3, "amber", 9.0),
    (25, "Diego", "Mini prueba: ¿qué significa a veces?", "미니 퀴즈: a veces는 무슨 뜻일까요?", "quiz", 4, "blue", 8.5),
    (26, "Lucía", "Significa: 가끔.", "뜻은 '가끔'이에요.", "respuesta", 4, "blue", 7.0),
    (27, "Diego", "Pregunta: ¿cómo dices 가끔 일찍 일어나요?", "질문: '가끔 일찍 일어나요'를 어떻게 말할까요?", "pregunta", 4, "blue", 9.0),
    (28, "Jin", "A veces me levanto temprano.", "가끔 일찍 일어나요.", "respuesta", 4, "blue", 8.0),
    (29, "Diego", "Otra frase: a veces tengo tiempo.", "다른 문장: 가끔 시간이 있어요.", "otra frase", 4, "blue", 8.0),
    (30, "Lucía", "Excelente. Ya puedes hablar de una rutina ocasional.", "훌륭해요. 이제 가끔 하는 루틴을 말할 수 있어요.", "cierre", 4, "blue", 9.0),
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
    "intro_title": "A veces me levanto temprano",
    "intro_subtitle": "Español A1+ · Ep.21",
    "intro_ko": "가끔 일찍 일어나요",
    "intro_scene_image_path": "images/ep21-a-veces-me-levanto-temprano-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "A veces me levanto temprano",
    "thumbnail_subtitle": "Español A1+ · Ep.21",
    "thumbnail_ko": "가끔 일찍 일어나요",
    "outro_ko": "이제 스페인어로 가끔 하는 루틴을 말할 수 있어요",
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
            "text_es": "Hoy Jin aprende a hablar de una rutina ocasional: a veces me levanto temprano.",
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
                "Muy bien. Ahora puedes hablar de una rutina ocasional: "
                "a veces me levanto temprano, a veces tengo tiempo, a veces estudio español."
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
    {"segment": 2, "title": "Por la mañana"},
    {"segment": 10, "title": "A veces"},
    {"segment": 21, "title": "Mi rutina"},
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
