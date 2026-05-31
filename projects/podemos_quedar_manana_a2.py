"""A2 entry story-card episode: Jin reschedules a plan politely."""

from __future__ import annotations

IMAGE_PATH = "images/ep25-podemos-quedar-manana-source.png"
DESCRIP_PATH = "a2-podemos-quedar-manana/descrip.md"
OUTPUT_NAME = "podemos-quedar-manana"
PUBLIC_SLUG = "a2-podemos-quedar-manana"
YOUTUBE_URL = ""
SERIES = "frases-a2"
SERIES_TITLE = "Español A2 -- Frases útiles"
EPISODE = 25
LEVEL = "A2 입문"
LANGUAGE = "es"
RENDER_VERSION = 2
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a2-ep25-podemos-quedar-manana.jpg"
YOUTUBE_TITLE = "¿Podemos quedar mañana? ☕ 내일 만날 수 있을까요? | Español A2 · Ep.25"
DESCRIPTION_INTRO = (
    "Jin sigue practicando respuestas naturales de nivel A2. "
    "Después de decir que hoy no puede, aprende a proponer otra opción: "
    "¿podemos quedar mañana?"
)
DESCRIPTION_OUTRO = (
    "Escucha primero, repite en voz alta y después cambia el plan: "
    "¿podemos quedar mañana?, ¿podemos hablar más tarde?, ¿podemos tomar café el viernes?"
)
KOREAN_TEASER = (
    "한국어 티저: EP.25는 A2 입문 표현입니다. "
    "핵심 표현은 하나, ¿Podemos + 동사원형 + 시간표현? 입니다. "
    "¿Podemos quedar mañana?처럼 오늘이 어려울 때 다른 시간을 제안해 보세요."
)
BASE_TAGS = ["스페인어", "스페인어 입문", "스페인어 A2", "Spanish A2", "aprender español", "español para coreanos"]
EXTRA_TAGS = ["podemos quedar", "quedar mañana", "Spanish plans", "Spanish conversation", "스페인어 회화", "스페인어 A2 입문", "약속 스페인어"]
BASE_HASHTAGS = ["#EspañolA2", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA2", "#PodemosQuedar", "#SpanishLab"]

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
    {"block_id": 1, "title_es": "Hoy no puedo", "title_ko": "오늘은 어려워요", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "¿Podemos quedar?", "title_ko": "만날 수 있을까요?", "color_block": "teal", "start": 8},
    {"block_id": 3, "title_es": "Mañana o más tarde", "title_ko": "내일 또는 나중에", "color_block": "amber", "start": 17},
    {"block_id": 4, "title_es": "Mini prueba", "title_ko": "미니 퀴즈", "color_block": "blue", "start": 25},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Diego", "Hoy seguimos con una situación muy real.", "오늘은 정말 자주 있는 상황을 이어 가요.", "A2", 1, "coral", 8.5),
    (2, "Lucía", "Jin quiere tomar café con una amiga.", "Jin은 친구와 커피를 마시고 싶어요.", "contexto", 1, "coral", 8.5),
    (3, "Diego", "Pero hoy tiene mucho trabajo.", "하지만 오늘은 일이 많아요.", "hoy", 1, "coral", 7.5),
    (4, "Lucía", "Jin, ¿quieres tomar café esta tarde?", "Jin, 오늘 오후에 커피 마실래요?", "invitación", 1, "coral", 8.5),
    (5, "Jin", "Quiero, pero hoy no puedo.", "가고 싶지만 오늘은 못 가요.", "contraste", 1, "coral", 8.5),
    (6, "Diego", "Muy bien. Ahora proponemos otra opción.", "좋아요. 이제 다른 선택지를 제안해요.", "opción", 1, "coral", 8.5),
    (7, "Lucía", "Una frase útil es: ¿podemos quedar mañana?", "유용한 표현은 ¿podemos quedar mañana?예요.", "modelo", 1, "coral", 9.0),
    (8, "Diego", "Escucha la primera parte: podemos.", "첫 부분을 들어 보세요: podemos.", "podemos", 2, "teal", 7.5),
    (9, "Jin", "Podemos.", "우리는 할 수 있어요.", "modelo", 2, "teal", 6.5),
    (10, "Lucía", "Podemos significa: nosotros podemos.", "podemos는 ‘우리는 할 수 있어요’라는 뜻이에요.", "significado", 2, "teal", 8.5),
    (11, "Diego", "Ahora añadimos un verbo: quedar.", "이제 동사를 붙여요: quedar.", "quedar", 2, "teal", 8.0),
    (12, "Jin", "Podemos quedar.", "우리는 만날 수 있어요.", "modelo", 2, "teal", 7.0),
    (13, "Lucía", "Como pregunta: ¿podemos quedar?", "질문으로는 ¿podemos quedar?예요.", "pregunta", 2, "teal", 8.0),
    (14, "Jin", "¿Podemos quedar?", "우리 만날 수 있을까요?", "repetición", 2, "teal", 7.5),
    (15, "Diego", "Suena amable y natural.", "정중하고 자연스럽게 들려요.", "natural", 2, "teal", 7.5),
    (16, "Lucía", "Pero necesitamos decir cuándo.", "하지만 언제인지 말해야 해요.", "cuándo", 2, "teal", 8.0),
    (17, "Diego", "Escucha la frase completa.", "완전한 문장을 들어 보세요.", "completa", 3, "amber", 7.0),
    (18, "Jin", "¿Podemos quedar mañana?", "내일 만날 수 있을까요?", "mañana", 3, "amber", 8.0),
    (19, "Lucía", "Literalmente: ¿podemos quedar mañana?", "직역하면: 우리는 내일 만날 수 있나요?", "literal", 3, "amber", 8.5),
    (20, "Diego", "Naturalmente, suena como una propuesta amable.", "자연스럽게는 ‘내일 만날 수 있을까요?’예요.", "natural", 3, "amber", 8.5),
    (21, "Jin", "Lo siento, hoy no puedo. ¿Podemos quedar mañana?", "미안해요, 오늘은 안 돼요. 내일 만날 수 있을까요?", "frase completa", 3, "amber", 10.0),
    (22, "Lucía", "También puedes decir: ¿podemos hablar más tarde?", "또 이렇게 말할 수 있어요: 나중에 이야기할 수 있을까요?", "más tarde", 3, "amber", 9.5),
    (23, "Jin", "¿Podemos hablar más tarde?", "나중에 이야기할 수 있을까요?", "modelo", 3, "amber", 8.0),
    (24, "Diego", "Excelente. Cambias el plan sin sonar brusco.", "훌륭해요. 딱딱하지 않게 계획을 바꿔요.", "A2", 3, "amber", 9.0),
    (25, "Diego", "Mini prueba: ¿qué significa mañana?", "미니 퀴즈: mañana는 무슨 뜻일까요?", "quiz", 4, "blue", 8.5),
    (26, "Lucía", "Mañana es el día después de hoy.", "mañana는 ‘내일’이라는 뜻이에요.", "respuesta", 4, "blue", 7.5),
    (27, "Diego", "¿Cómo dices esta frase en español?", "‘내일 만날 수 있을까요?’를 스페인어로 어떻게 말할까요?", "pregunta", 4, "blue", 8.5),
    (28, "Jin", "¿Podemos quedar mañana?", "내일 만날 수 있을까요?", "respuesta", 4, "blue", 8.0),
    (29, "Lucía", "Otra opción: ¿podemos hablar más tarde?", "다른 선택지: 나중에 이야기할 수 있을까요?", "opción", 4, "blue", 8.5),
    (30, "Diego", "Muy bien. Ya puedes proponer otra hora.", "좋아요. 이제 다른 시간을 제안할 수 있어요.", "cierre", 4, "blue", 8.5),
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
    "intro_title": "¿Podemos quedar mañana?",
    "intro_subtitle": "Español A2 · Ep.25",
    "intro_ko": "내일 만날 수 있을까요?",
    "intro_scene_image_path": "images/ep25-podemos-quedar-manana-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "¿Podemos quedar mañana?",
    "thumbnail_subtitle": "Español A2 · Ep.25",
    "thumbnail_ko": "내일 만날 수 있을까요?",
    "outro_ko": "이제 스페인어로 다른 시간을 자연스럽게 제안할 수 있어요",
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
            "text_es": "Hoy Jin aprende a proponer otra opción: ¿podemos quedar mañana?",
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
                "Muy bien. Ahora puedes proponer otra opción de forma amable: "
                "¿podemos quedar mañana?, ¿podemos hablar más tarde?"
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
    {"segment": 2, "title": "Hoy no puedo"},
    {"segment": 10, "title": "¿Podemos quedar?"},
    {"segment": 20, "title": "Mañana o más tarde"},
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
