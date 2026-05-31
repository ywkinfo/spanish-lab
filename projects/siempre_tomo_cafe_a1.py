"""A1+ story-card episode: Jin talks about fixed morning routine with siempre."""

from __future__ import annotations

IMAGE_PATH = "images/ep22-siempre-tomo-cafe-source.png"
DESCRIP_PATH = "a1-siempre-tomo-cafe/descrip.md"
OUTPUT_NAME = "siempre-tomo-cafe"
PUBLIC_SLUG = "a1-siempre-tomo-cafe"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 22
LEVEL = "A1+"
LANGUAGE = "es"
RENDER_VERSION = 3
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a1-ep22-siempre-tomo-cafe.jpg"
YOUTUBE_TITLE = "Siempre tomo café por la mañana ☕ 항상 커피 마셔요 | Español A1+ · Ep.22"
DESCRIPTION_INTRO = (
    "Jin continúa con palabras de frecuencia después de a veces y aprende una rutina fija: "
    "siempre tomo café por la mañana. Practicamos siempre con café, estudiar español y llevar un cuaderno."
)
DESCRIPTION_OUTRO = (
    "Escucha primero, repite en voz alta y después cambia la acción: "
    "siempre tomo café, siempre estudio español, siempre llevo mi cuaderno."
)
KOREAN_TEASER = (
    "한국어 티저: EP.22에서는 Ep.21의 a veces 다음 단계로 '항상 ~해요'를 말합니다. "
    "핵심 표현은 하나, siempre + 현재형입니다. Siempre tomo café por la mañana처럼 따라 말해 보세요."
)
BASE_TAGS = ["스페인어", "스페인어 입문", "스페인어 A1", "Spanish A1", "aprender español", "español para principiantes"]
EXTRA_TAGS = ["siempre", "siempre en español", "Spanish frequency", "Spanish A1+", "스페인어 회화", "스페인어 루틴"]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#Siempre", "#SpanishLab"]

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
    {"block_id": 2, "title_es": "Siempre", "title_ko": "항상", "color_block": "teal", "start": 10},
    {"block_id": 3, "title_es": "Mi rutina", "title_ko": "나의 루틴", "color_block": "amber", "start": 19},
    {"block_id": 4, "title_es": "Mini prueba", "title_ko": "미니 퀴즈", "color_block": "blue", "start": 25},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Diego", "Hoy seguimos con palabras de frecuencia.", "오늘은 빈도를 말하는 단어를 계속 배워요.", "frecuencia", 1, "coral", 8.5),
    (2, "Lucía", "Jin está en la cocina por la mañana.", "Jin은 아침에 주방에 있어요.", "contexto", 1, "coral", 8.0),
    (3, "Diego", "Tiene una taza de café.", "커피 한 잔이 있어요.", "café", 1, "coral", 7.0),
    (4, "Lucía", "Jin, ¿qué haces por la mañana?", "Jin, 아침에 무엇을 해요?", "pregunta", 1, "coral", 7.5),
    (5, "Jin", "Tomo café por la mañana.", "저는 아침에 커피를 마셔요.", "repaso", 1, "coral", 7.5),
    (6, "Diego", "Muy bien. Ahora añadimos una palabra.", "좋아요. 이제 단어 하나를 추가해요.", "añadir", 1, "coral", 8.5),
    (7, "Lucía", "La palabra es: siempre.", "그 단어는 siempre예요.", "siempre", 1, "coral", 7.0),
    (8, "Diego", "Siempre habla de frecuencia.", "siempre는 빈도를 말해요.", "frecuencia", 1, "coral", 8.0),
    (9, "Lucía", "En coreano, suena como: 항상.", "한국어로는 '항상'이에요.", "significado", 1, "coral", 7.5),
    (10, "Diego", "Escucha la frase completa.", "완전한 문장을 들어 보세요.", "modelo", 2, "teal", 7.0),
    (11, "Jin", "Siempre tomo café por la mañana.", "저는 항상 아침에 커피를 마셔요.", "modelo", 2, "teal", 8.5),
    (12, "Lucía", "Repite: siempre.", "따라 하세요: siempre.", "repetición", 2, "teal", 7.0),
    (13, "Jin", "Siempre.", "항상.", "repetición", 2, "teal", 6.0),
    (14, "Lucía", "Repite: tomo café.", "따라 하세요: 커피를 마셔요.", "repetición", 2, "teal", 7.0),
    (15, "Jin", "Tomo café.", "저는 커피를 마셔요.", "repetición", 2, "teal", 6.5),
    (16, "Diego", "Ahora todo junto.", "이제 함께 말해요.", "unir", 2, "teal", 6.5),
    (17, "Jin", "Siempre tomo café por la mañana.", "항상 아침에 커피를 마셔요.", "frase completa", 2, "teal", 8.5),
    (18, "Lucía", "Perfecto. Es una rutina fija.", "완벽해요. 고정된 루틴이에요.", "rutina", 2, "teal", 8.0),
    (19, "Diego", "Ahora usamos siempre con más rutinas.", "이제 siempre를 다른 루틴과 써 봐요.", "rutina", 3, "amber", 8.5),
    (20, "Jin", "Siempre estudio español por la noche.", "저는 항상 밤에 스페인어를 공부해요.", "estudio", 3, "amber", 9.0),
    (21, "Lucía", "Literalmente: siempre estudio español.", "직역하면: 나는 항상 스페인어를 공부해요.", "literal", 3, "amber", 8.5),
    (22, "Jin", "Siempre voy al trabajo en metro.", "저는 항상 지하철로 출근해요.", "trabajo", 3, "amber", 8.5),
    (23, "Diego", "Muy bien. Siempre más una acción.", "좋아요. siempre 뒤에 행동을 붙여요.", "acción", 3, "amber", 8.0),
    (24, "Jin", "Siempre llevo mi cuaderno.", "저는 항상 제 공책을 가지고 다녀요.", "cuaderno", 3, "amber", 8.0),
    (25, "Diego", "Mini prueba: ¿qué significa siempre?", "미니 퀴즈: siempre는 무슨 뜻일까요?", "quiz", 4, "blue", 8.5),
    (26, "Lucía", "Significa: 항상.", "뜻은 '항상'이에요.", "respuesta", 4, "blue", 7.0),
    (27, "Diego", "Pregunta: ¿cómo dices 항상 커피를 마셔요?", "질문: '항상 커피를 마셔요'를 어떻게 말할까요?", "pregunta", 4, "blue", 9.0),
    (28, "Jin", "Siempre tomo café.", "항상 커피를 마셔요.", "respuesta", 4, "blue", 7.5),
    (29, "Diego", "Otra frase: siempre estudio español.", "다른 문장: 항상 스페인어를 공부해요.", "otra frase", 4, "blue", 8.0),
    (30, "Lucía", "Excelente. Ya puedes hablar de una rutina fija.", "훌륭해요. 이제 고정된 루틴을 말할 수 있어요.", "cierre", 4, "blue", 9.0),
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
    "intro_title": "Siempre",
    "intro_subtitle": "Español A1+ · Ep.22",
    "intro_ko": "항상 아침에 커피를 마셔요",
    "intro_scene_image_path": "images/ep22-siempre-tomo-cafe-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "Siempre tomo café por la mañana",
    "thumbnail_subtitle": "Español A1+ · Ep.22",
    "thumbnail_ko": "항상 커피 마셔요",
    "outro_ko": "이제 스페인어로 고정된 루틴을 말할 수 있어요",
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
            "text_es": "Hoy Jin aprende a hablar de una rutina fija: siempre tomo café por la mañana.",
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
                "Muy bien. Ahora puedes hablar de una rutina fija: "
                "siempre tomo café, siempre estudio español, siempre llevo mi cuaderno."
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
    {"segment": 12, "title": "Siempre"},
    {"segment": 22, "title": "Mi rutina"},
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
