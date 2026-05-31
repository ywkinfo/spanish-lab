"""A2 entry story-card episode: Jin declines an invitation and gives a reason."""

from __future__ import annotations

IMAGE_PATH = "images/ep24-no-puedo-ir-source.png"
DESCRIP_PATH = "a2-no-puedo-ir/descrip.md"
OUTPUT_NAME = "no-puedo-ir"
PUBLIC_SLUG = "a2-no-puedo-ir"
YOUTUBE_URL = ""
SERIES = "frases-a2"
SERIES_TITLE = "Español A2 -- Frases útiles"
EPISODE = 24
LEVEL = "A2 입문"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a2-ep24-no-puedo-ir.jpg"
YOUTUBE_TITLE = "No puedo ir porque tengo que trabajar 💻 일해야 해서 못 가요 | Español A2 · Ep.24"
DESCRIPTION_INTRO = (
    "Jin empieza a pasar de frases A1 a respuestas más naturales de nivel A2. "
    "En este episodio aprende a rechazar una invitación con una razón: "
    "no puedo ir porque tengo que trabajar."
)
DESCRIPTION_OUTRO = (
    "Escucha primero, repite en voz alta y después cambia la razón: "
    "no puedo ir porque tengo que trabajar, estudiar o descansar."
)
KOREAN_TEASER = (
    "한국어 티저: EP.24부터 A2 입문으로 올라갑니다. "
    "핵심 표현은 하나, No puedo + 동사원형 + porque tengo que + 동사원형입니다. "
    "No puedo ir porque tengo que trabajar처럼 거절과 이유를 한 문장으로 말해 보세요."
)
BASE_TAGS = ["스페인어", "스페인어 입문", "스페인어 A2", "Spanish A2", "aprender español", "español para coreanos"]
EXTRA_TAGS = ["no puedo", "tengo que", "porque", "Spanish excuses", "Spanish conversation", "스페인어 회화", "스페인어 A2 입문"]
BASE_HASHTAGS = ["#EspañolA2", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA2", "#NoPuedo", "#SpanishLab"]

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
    {"block_id": 1, "title_es": "La invitación", "title_ko": "초대", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "No puedo ir", "title_ko": "갈 수 없어요", "color_block": "teal", "start": 8},
    {"block_id": 3, "title_es": "Porque tengo que trabajar", "title_ko": "일해야 해서요", "color_block": "amber", "start": 17},
    {"block_id": 4, "title_es": "Mini prueba", "title_ko": "미니 퀴즈", "color_block": "blue", "start": 25},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Diego", "Hoy subimos un paso: una respuesta más completa.", "오늘은 한 단계 올라가서 더 완전한 대답을 해요.", "A2", 1, "coral", 9.0),
    (2, "Lucía", "Jin está trabajando por la tarde.", "Jin은 오후에 일하고 있어요.", "contexto", 1, "coral", 8.0),
    (3, "Diego", "Tiene una reunión y muchos mensajes.", "회의도 있고 메시지도 많아요.", "trabajo", 1, "coral", 8.0),
    (4, "Lucía", "Jin, ¿quieres tomar café esta tarde?", "Jin, 오늘 오후에 커피 마실래요?", "invitación", 1, "coral", 8.5),
    (5, "Jin", "Quiero, pero hoy no puedo.", "가고 싶지만 오늘은 못 가요.", "contraste", 1, "coral", 8.5),
    (6, "Diego", "Muy bien. Primero decimos: no puedo.", "좋아요. 먼저 no puedo라고 말해요.", "no puedo", 1, "coral", 8.5),
    (7, "Lucía", "No puedo significa: no es posible para mí.", "no puedo는 ‘할 수 없어요, 못 해요’라는 뜻이에요.", "significado", 1, "coral", 9.0),
    (8, "Diego", "Escucha la primera parte.", "첫 부분을 들어 보세요.", "modelo", 2, "teal", 7.0),
    (9, "Jin", "No puedo ir.", "저는 갈 수 없어요.", "modelo", 2, "teal", 7.0),
    (10, "Lucía", "Repite: no puedo ir.", "따라 하세요: no puedo ir.", "repetición", 2, "teal", 7.5),
    (11, "Jin", "No puedo ir.", "갈 수 없어요.", "repetición", 2, "teal", 6.5),
    (12, "Diego", "Ahora lo hacemos más amable.", "이제 더 정중하게 만들어요.", "amable", 2, "teal", 8.0),
    (13, "Jin", "Lo siento, no puedo ir.", "미안해요, 저는 갈 수 없어요.", "lo siento", 2, "teal", 8.0),
    (14, "Lucía", "Muy natural. Lo siento suaviza la frase.", "아주 자연스러워요. Lo siento는 문장을 부드럽게 해요.", "natural", 2, "teal", 9.0),
    (15, "Diego", "Pero en A2 damos una razón.", "하지만 A2에서는 이유를 붙여요.", "razón", 2, "teal", 8.0),
    (16, "Lucía", "La razón de Jin es el trabajo.", "Jin의 이유는 일이에요.", "trabajo", 2, "teal", 7.5),
    (17, "Diego", "Escucha: tengo que trabajar.", "들어 보세요: 일해야 해요.", "tengo que", 3, "amber", 7.5),
    (18, "Jin", "Tengo que trabajar.", "저는 일해야 해요.", "modelo", 3, "amber", 7.0),
    (19, "Lucía", "Tengo que expresa una obligación.", "tengo que는 ‘해야 해요’라는 뜻이에요.", "significado", 3, "amber", 8.0),
    (20, "Diego", "Ahora unimos las dos partes con porque.", "이제 porque로 두 부분을 연결해요.", "unir", 3, "amber", 8.5),
    (21, "Jin", "No puedo ir porque tengo que trabajar.", "일해야 해서 갈 수 없어요.", "frase completa", 3, "amber", 9.0),
    (22, "Lucía", "Literalmente: no puedo ir porque tengo que trabajar.", "직역하면: 저는 갈 수 없어요, 왜냐하면 일해야 해요.", "literal", 3, "amber", 9.5),
    (23, "Jin", "Lo siento, no puedo ir porque tengo que trabajar.", "미안해요, 일해야 해서 못 가요.", "natural", 3, "amber", 10.0),
    (24, "Diego", "Excelente. Es una respuesta completa y amable.", "훌륭해요. 완전하고 정중한 대답이에요.", "A2", 3, "amber", 9.0),
    (25, "Diego", "Mini prueba: ¿qué significa no puedo ir?", "미니 퀴즈: no puedo ir는 무슨 뜻일까요?", "quiz", 4, "blue", 9.0),
    (26, "Lucía", "Significa: no puedo ir.", "뜻은 ‘갈 수 없어요’예요.", "respuesta", 4, "blue", 7.5),
    (27, "Diego", "¿Cómo dices esta frase en español?", "‘일해야 해서 못 가요’를 어떻게 말할까요?", "pregunta", 4, "blue", 8.5),
    (28, "Jin", "No puedo ir porque tengo que trabajar.", "일해야 해서 못 가요.", "respuesta", 4, "blue", 9.0),
    (29, "Lucía", "Otra razón: tengo que estudiar.", "다른 이유: 공부해야 해요.", "otra razón", 4, "blue", 7.5),
    (30, "Diego", "Muy bien. Ya puedes rechazar con una razón.", "좋아요. 이제 이유를 붙여 거절할 수 있어요.", "cierre", 4, "blue", 9.0),
]

DESIGN = {
    "output_size": (1280, 720),
    "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
    "font_index": 0,
    "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
    "font_index_ko": 0,
    "font_size_title": 64,
    "font_size_es": 60,
    "min_font_size_es": 30,
    "font_size_ko": 32,
    "font_size_example": 30,
    "background_color": (248, 247, 242),
    "text_color": (31, 35, 40),
    "muted_text_color": (96, 101, 109),
    "intro_title": "No puedo ir",
    "intro_subtitle": "Español A2 · Ep.24",
    "intro_ko": "일해야 해서 못 가요",
    "intro_scene_image_path": "images/ep24-no-puedo-ir-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "No puedo ir porque tengo que trabajar",
    "thumbnail_subtitle": "Español A2 · Ep.24",
    "thumbnail_ko": "일해야 해서 못 가요",
    "outro_ko": "이제 스페인어로 이유를 붙여 정중하게 거절할 수 있어요",
    "conversation_label": "Conversación A2",
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
            "text_es": "Hoy Jin aprende a rechazar una invitación con una razón: no puedo ir porque tengo que trabajar.",
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
                "Muy bien. Ahora puedes rechazar una invitación con una razón: "
                "no puedo ir porque tengo que trabajar, estudiar o descansar."
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
    {"segment": 2, "title": "La invitación"},
    {"segment": 10, "title": "No puedo ir"},
    {"segment": 20, "title": "Porque tengo que trabajar"},
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
