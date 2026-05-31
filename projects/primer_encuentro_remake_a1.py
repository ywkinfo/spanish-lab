"""A1 story-card remake of Ep.2: asking and answering names."""

from __future__ import annotations

IMAGE_PATH = "images/ep02-primer-encuentro-remake-source.png"
DESCRIP_PATH = "a1-primer-encuentro-remake/descrip.md"
OUTPUT_NAME = "primer-encuentro-remake"
PUBLIC_SLUG = "a1-primer-encuentro-remake"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 2
LEVEL = "A1"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a1-ep02-primer-encuentro-remake.jpg"
YOUTUBE_TITLE = "¿Cómo te llamas? 이름 묻고 답하기 | Español A1 · Ep.2 remake"
DESCRIPTION_INTRO = (
    "Remake de Ep.2 al estilo actual de Spanish Lab. "
    "Jin, Lucía y Diego practican una sola función A1: preguntar el nombre con "
    "¿Cómo te llamas? y responder con Me llamo..."
)
DESCRIPTION_OUTRO = (
    "Escucha primero, repite en voz alta y después cambia el nombre: "
    "¿Cómo te llamas? Me llamo Jin. Me llamo Lucía."
)
KOREAN_TEASER = (
    "한국어 티저: EP.2 리메이크는 첫 만남에서 이름을 묻고 답하는 A1 상황극입니다. "
    "핵심 표현은 하나, ¿Cómo te llamas? / Me llamo... 입니다."
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
    "como te llamas",
    "me llamo",
    "primer encuentro español",
    "conversacion español A1",
    "스페인어 자기소개",
    "스페인어 이름 묻기",
]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#MeLlamo", "#SpanishLab"]

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
    {"block_id": 1, "title_es": "Primer encuentro", "title_ko": "첫 만남", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "¿Cómo te llamas?", "title_ko": "이름 묻기", "color_block": "teal", "start": 11},
    {"block_id": 3, "title_es": "Me llamo...", "title_ko": "이름 답하기", "color_block": "amber", "start": 16},
    {"block_id": 4, "title_es": "Mini conversación", "title_ko": "짧은 대화", "color_block": "blue", "start": 20},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Diego", "Hoy practicamos una frase para empezar.", "오늘은 시작할 때 쓰는 표현 하나를 연습해요.", "A1", 1, "coral", 8.5),
    (2, "Diego", "Jin conoce a Lucía por primera vez.", "Jin이 Lucía를 처음 만나요.", "contexto", 1, "coral", 8.5),
    (3, "Diego", "Primero escucha: ¿Cómo te llamas?", "먼저 들어 보세요: 이름이 뭐예요?", "escucha", 1, "coral", 8.5),
    (4, "Lucía", "Hola.", "안녕하세요.", "Hola", 1, "coral", 6.5),
    (5, "Jin", "Hola.", "안녕하세요.", "Hola", 1, "coral", 6.5),
    (6, "Lucía", "Me llamo Lucía.", "저는 Lucía예요.", "Me llamo", 1, "coral", 7.5),
    (7, "Lucía", "¿Cómo te llamas?", "이름이 뭐예요?", "pregunta", 1, "coral", 7.5),
    (8, "Jin", "Me llamo Jin.", "저는 Jin이에요.", "respuesta", 1, "coral", 7.5),
    (9, "Lucía", "Mucho gusto.", "만나서 반가워요.", "saludo", 1, "coral", 7.0),
    (10, "Jin", "Igualmente.", "저도 반가워요.", "saludo", 1, "coral", 7.0),
    (11, "Diego", "La pregunta es: ¿Cómo te llamas?", "질문은 ¿Cómo te llamas?예요.", "pregunta", 2, "teal", 8.5),
    (12, "Diego", "Literalmente: ¿cómo te llamas?", "직역하면 ‘너는 어떻게 불리니?’예요.", "literal", 2, "teal", 8.5),
    (13, "Diego", "En coreano natural: 이름이 뭐예요?", "자연스러운 한국어로는 ‘이름이 뭐예요?’예요.", "natural", 2, "teal", 9.0),
    (14, "Diego", "Repite despacio: ¿Cómo te llamas?", "천천히 따라 해요: 이름이 뭐예요?", "shadowing", 2, "teal", 8.5),
    (15, "Jin", "¿Cómo te llamas?", "이름이 뭐예요?", "repetición", 2, "teal", 7.5),
    (16, "Diego", "La respuesta es: Me llamo Jin.", "대답은 Me llamo Jin이에요.", "respuesta", 3, "amber", 8.5),
    (17, "Diego", "Me llamo significa: 저는 ...예요.", "Me llamo는 ‘저는 ...예요’라는 뜻이에요.", "significado", 3, "amber", 9.0),
    (18, "Lucía", "Cambia el nombre: Me llamo Lucía.", "이름만 바꿔요: 저는 Lucía예요.", "cambia", 3, "amber", 8.5),
    (19, "Jin", "Me llamo Jin.", "저는 Jin이에요.", "modelo", 3, "amber", 7.5),
    (20, "Diego", "Muy bien. Ahora una mini conversación.", "좋아요. 이제 짧은 대화예요.", "diálogo", 4, "blue", 8.5),
    (21, "Lucía", "Hola, me llamo Lucía.", "안녕하세요, 저는 Lucía예요.", "modelo", 4, "blue", 8.0),
    (22, "Jin", "Hola, me llamo Jin.", "안녕하세요, 저는 Jin이에요.", "modelo", 4, "blue", 8.0),
    (23, "Lucía", "Jin, ¿cómo te llamas?", "Jin, 이름이 뭐예요?", "pregunta", 4, "blue", 8.0),
    (24, "Jin", "Me llamo Jin. ¿Y tú?", "저는 Jin이에요. 당신은요?", "¿Y tú?", 4, "blue", 8.5),
    (25, "Lucía", "Me llamo Lucía.", "저는 Lucía예요.", "respuesta", 4, "blue", 7.5),
    (26, "Jin", "Mucho gusto.", "만나서 반가워요.", "saludo", 4, "blue", 7.0),
    (27, "Lucía", "Igualmente.", "저도 반가워요.", "saludo", 4, "blue", 7.0),
    (28, "Diego", "Mini prueba: 이름이 뭐예요?", "미니 퀴즈: 이름이 뭐예요?", "quiz", 4, "blue", 8.0),
    (29, "Jin", "¿Cómo te llamas?", "이름이 뭐예요?", "respuesta", 4, "blue", 7.5),
    (30, "Diego", "Perfecto. Ahora puedes presentarte.", "완벽해요. 이제 자기소개를 할 수 있어요.", "cierre", 4, "blue", 8.5),
]

DESIGN = {
    "output_size": (1280, 720),
    "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
    "font_index": 0,
    "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
    "font_index_ko": 0,
    "font_size_title": 68,
    "font_size_es": 66,
    "min_font_size_es": 34,
    "font_size_ko": 32,
    "font_size_example": 30,
    "background_color": (248, 247, 242),
    "text_color": (31, 35, 40),
    "muted_text_color": (96, 101, 109),
    "intro_title": "¿Cómo te llamas?",
    "intro_subtitle": "Español A1 · Ep.2 remake",
    "intro_ko": "첫 만남에서 이름 묻고 답하기",
    "intro_scene_image_path": "images/ep02-primer-encuentro-remake-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "¿Cómo te llamas?",
    "thumbnail_subtitle": "Español A1 · Ep.2",
    "thumbnail_ko": "이름 묻고 답하기",
    "outro_ko": "이제 스페인어로 이름을 묻고 답해 보세요",
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
                "Hoy Jin aprende una frase esencial para un primer encuentro: "
                "¿cómo te llamas?"
            ),
            "duration_s": 13.0,
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
                "Muy bien. Ahora haz la escena tú: Hola, me llamo Jin. "
                "¿Cómo te llamas? Mucho gusto."
            ),
            "duration_s": 22.0,
            "color_block": "neutral",
            "characters": ["Jin", "Lucía", "Diego"],
        }
    )
    return segments


SEGMENTS = _build_segments()
CHAPTERS = [
    {"segment": 1, "title": "Introducción"},
    {"segment": 2, "title": "Primer encuentro"},
    {"segment": 13, "title": "¿Cómo te llamas?"},
    {"segment": 19, "title": "Me llamo..."},
    {"segment": 24, "title": "Mini conversación"},
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
