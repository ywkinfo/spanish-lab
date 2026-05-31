"""A1+ story-card episode: Jin learns to ask to speak slowly."""

from __future__ import annotations

IMAGE_PATH = "images/ep31-mas-despacio-por-favor-source.png"
DESCRIP_PATH = "a1-mas-despacio-por-favor/descrip.md"
OUTPUT_NAME = "mas-despacio-por-favor"
PUBLIC_SLUG = "a1-mas-despacio-por-favor"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 31
LEVEL = "A1+"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a1-ep31-mas-despacio-por-favor.jpg"
YOUTUBE_TITLE = "Más despacio, por favor 🗣️ 천천히 말해주세요 | Español A1+ · Ep.31"
DESCRIPTION_INTRO = (
    "Jin aprende una frase crucial para cuando los nativos hablan rápido: "
    "Más despacio, por favor."
)
DESCRIPTION_OUTRO = (
    "Usa esta frase cuando necesites que alguien repita o hable más despacio: "
    "¡Más despacio, por favor!"
)
KOREAN_TEASER = (
    "한국어 티저: EP.31은 원어민이 너무 빠르게 말할 때 쓸 수 있는 생존 표현입니다. "
    "핵심은 하나, Más despacio, por favor.입니다. "
    "정중하게 천천히 말해달라고 부탁해 보세요."
)
BASE_TAGS = ["스페인어", "스페인어 입문", "스페인어 A1", "Spanish A1", "aprender español", "español para coreanos"]
EXTRA_TAGS = ["Más despacio, por favor", "스페인어 회화", "스페인어 여행", "스페인어 듣기", "Spanish Lab", "천천히 말해주세요"]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#MasDespacio", "#SpanishLab"]

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
    {"block_id": 1, "title_es": "Más despacio, por favor", "title_ko": "천천히 말해주세요", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "Una frase crucial", "title_ko": "소통의 생존 표현", "color_block": "teal", "start": 8},
    {"block_id": 3, "title_es": "En la cafetería", "title_ko": "카페에서 연습하기", "color_block": "amber", "start": 16},
    {"block_id": 4, "title_es": "Mini prueba", "title_ko": "미니 퀴즈", "color_block": "blue", "start": 24},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Diego", "¡Hola a todos! Hoy tenemos una lección de conversación.", "안녕하세요 모두들! 오늘은 회화 수업이 있어요.", "contexto", 1, "coral", 7.5),
    (2, "Jin", "Hola, Diego. Estoy listo para aprender.", "안녕하세요, Diego. 배울 준비가 됐어요.", "preparación", 1, "coral", 7.0),
    (3, "Diego", "Estupendo. Hablaremos de una pregunta muy importante que es básica para...", "좋아요. 아주 중요하고 기본적인 질문에 대해 이야기할 건데...", "rapidez", 1, "coral", 8.5),
    (4, "Jin", "Perdón, Diego. Hablas muy rápido.", "죄송해요, Diego. 말을 너무 빠르게 해요.", "problema", 1, "coral", 7.0),
    (5, "Diego", "¡Ah, lo siento! Hoy aprendemos a pedir que hablen más despacio.", "아, 미안해요! 오늘은 천천히 말해달라고 부탁하는 법을 배워요.", "función", 1, "coral", 8.0),
    (6, "Lucía", "La frase clave es: Más despacio, por favor.", "핵심 표현은: Más despacio, por favor. 예요.", "clave", 1, "coral", 7.5),
    (7, "Jin", "Más despacio, por favor.", "천천히 말해주세요.", "modelo", 1, "coral", 6.5),
    (8, "Diego", "Perfecto. Ahora explicamos la frase.", "완벽해요. 이제 표현을 설명할게요.", "explicación", 2, "teal", 7.0),
    (9, "Diego", "Literalmente: más despacio, por favor.", "직역하면: 더 천천히, 부탁합니다 예요.", "literal", 2, "teal", 7.5),
    (10, "Lucía", "Significa: por favor, habla más despacio.", "의미는 “천천히 말씀해 주세요”예요.", "natural", 2, "teal", 7.0),
    (11, "Diego", "Es una frase muy educada y útil.", "아주 예의 바르고 유용한 표현이에요.", "consejo", 2, "teal", 7.5),
    (12, "Jin", "Más despacio, por favor.", "천천히 말해주세요.", "repetición", 2, "teal", 6.5),
    (13, "Diego", "Puedes complementarla con otra pregunta.", "다른 질문과 함께 쓸 수도 있어요.", "opción", 2, "teal", 7.5),
    (14, "Lucía", "¿Puedes hablar más despacio?", "더 천천히 말해줄 수 있어요?", "variación", 2, "teal", 7.0),
    (15, "Jin", "¿Puedes hablar más despacio?", "더 천천히 말해줄 수 있어요?", "repetición", 2, "teal", 7.0),
    (16, "Diego", "¡Excelente! Ahora practicamos con Lucía.", "훌륭해요! 이제 Lucía와 연습해 봐요.", "diálogo", 3, "amber", 7.5),
    (17, "Lucía", "Hola Jin, ¿quieres comprar este libro de español?", "안녕 Jin, 이 스페인어 책을 사고 싶니?", "diálogo", 3, "amber", 7.5),
    (18, "Jin", "Sí, pero...", "네, 하지만...", "duda", 3, "amber", 5.5),
    (19, "Lucía", "Es que este libro es muy bueno porque tiene ejercicios y...", "이 책은 연습문제도 있고 아주 좋아서...", "rapidez", 3, "amber", 8.5),
    (20, "Jin", "Más despacio, por favor.", "천천히 말해주세요.", "reacción", 3, "amber", 6.5),
    (21, "Lucía", "Ah, disculpa. ¿Quieres comprar este libro?", "아, 미안해. 이 책을 사고 싶니?", "diálogo", 3, "amber", 7.5),
    (22, "Jin", "Sí, gracias. Ahora entiendo.", "네, 고마워요. 이제 이해했어요.", "comprensión", 3, "amber", 7.0),
    (23, "Diego", "Muy bien Jin. Reaccionaste perfectamente.", "아주 잘했어요 Jin. 완벽하게 반응했어요.", "feedback", 3, "amber", 7.5),
    (24, "Diego", "Mini prueba. ¿Cómo pides que hablen más despacio?", "미니 퀴즈. 천천히 말해달라고 어떻게 부탁할까요?", "quiz", 4, "blue", 7.8),
    (25, "Jin", "Más despacio, por favor.", "천천히 말해주세요.", "respuesta", 4, "blue", 6.5),
    (26, "Lucía", "Muy bien. ¿Y la pregunta más larga?", "아주 좋아요. 그럼 더 긴 질문은요?", "quiz", 4, "blue", 7.0),
    (27, "Jin", "¿Puedes hablar más despacio?", "더 천천히 말해줄 수 있어요?", "respuesta", 4, "blue", 7.0),
    (28, "Diego", "¿Qué significa 'despacio'?", "despacio는 무슨 뜻일까요?", "quiz", 4, "blue", 7.5),
    (29, "Lucía", "Significa: con lentitud o despacio.", "“천천히” 또는 “느리게”라는 뜻이에요.", "respuesta", 4, "blue", 7.5),
]

DESIGN = {
    "output_size": (1280, 720),
    "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
    "font_index": 0,
    "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
    "font_index_ko": 0,
    "font_size_title": 56,
    "font_size_es": 58,
    "min_font_size_es": 30,
    "font_size_ko": 32,
    "font_size_example": 30,
    "background_color": (248, 247, 242),
    "text_color": (31, 35, 40),
    "muted_text_color": (96, 101, 109),
    "intro_title": "Más despacio, por favor",
    "intro_subtitle": "Español A1+ · Ep.31",
    "intro_ko": "천천히 말해주세요",
    "intro_scene_image_path": "images/ep31-mas-despacio-por-favor-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "Más despacio, por favor",
    "thumbnail_subtitle": "Español A1+ · Ep.31",
    "thumbnail_ko": "천천히 말해주세요",
    "outro_ko": "이제 스페인어가 너무 빠를 때 '천천히 말해주세요'라고 할 수 있어요",
    "conversation_label": "Conversación A1+",
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
            "text_es": "Hoy Jin aprende una frase de supervivencia para cuando los nativos hablan muy rápido: Más despacio, por favor.",
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
                "Muy bien. Cuando un nativo hable demasiado rápido, recuerda usar esta frase con calma: "
                "¡Más despacio, por favor! o también ¿Puedes hablar más despacio?"
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
    {"segment": 2, "title": "Más despacio, por favor"},
    {"segment": 10, "title": "Una frase crucial"},
    {"segment": 19, "title": "En la cafetería"},
    {"segment": 28, "title": "Mini prueba"},
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
