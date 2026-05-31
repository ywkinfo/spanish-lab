"""A2 entry story-card episode: Jin confirms a restaurant reservation with Lucía via message."""

from __future__ import annotations

IMAGE_PATH = "images/ep33-confirmar-reserva-source.png"
DESCRIP_PATH = "a2-confirmar-reserva/descrip.md"
OUTPUT_NAME = "confirmar-reserva"
PUBLIC_SLUG = "a2-confirmar-reserva"
YOUTUBE_URL = ""
SERIES = "frases-a2"
SERIES_TITLE = "Español A2 -- Frases útiles"
EPISODE = 33
LEVEL = "A2 입문"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a2-ep33-confirmar-reserva.jpg"
YOUTUBE_TITLE = "He reservado la mesa 💬 예약 완료했어 | Español A2 · Ep.33"
DESCRIPTION_INTRO = (
    "Jin confirma la reserva del restaurante enviándole un mensaje de texto a Lucía. "
    "En este episodio aprende a usar el pretérito perfecto para confirmar planes y la expresión nos vemos allí."
)
DESCRIPTION_OUTRO = (
    "Escucha primero, repite en voz alta y practica el pretérito perfecto: "
    "he reservado, ya he reservado la mesa, y he visto el menú."
)
KOREAN_TEASER = (
    "한국어 티저: EP.33 예약 확인 편입니다. "
    "식당 예약 결과를 루시아에게 메시지로 전하고 약속을 확정하는 실전 A2 회화를 연습합니다. "
    "현재완료형인 'He reservado(예약했어)', 'He visto(봤어)'와 약속 조율 표현인 'Nos vemos allí(거기서 보자)'를 마스터해 보세요!"
)
BASE_TAGS = ["스페인어", "스페인어 입문", "스페인어 A2", "Spanish A2", "aprender español", "español para coreanos"]
EXTRA_TAGS = ["he reservado", "nos vemos", "pretérito perfecto", "Spanish text message", "스페인어 회화", "식당 예약 완료 스페인어"]
BASE_HASHTAGS = ["#EspañolA2", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#Confirmación", "#NosVemos", "#SpanishLab"]

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
    {"block_id": 1, "title_es": "La confirmación", "title_ko": "예약 결과 공유", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "El mensaje de Lucía", "title_ko": "루시아의 답장", "color_block": "teal", "start": 10},
    {"block_id": 3, "title_es": "El menú", "title_ko": "메뉴와 기대", "color_block": "amber", "start": 15},
    {"block_id": 4, "title_es": "Mini prueba", "title_ko": "미니 퀴즈", "color_block": "blue", "start": 24},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Diego", "Hoy aprendemos a confirmar una cita en español.", "오늘은 스페인어로 약속을 확정하는 방법을 배워요.", "A2", 1, "coral", 8.0),
    (2, "Lucía", "Jin ha hecho la reserva y le envía un mensaje a Lucía.", "Jin은 예약을 마쳤고 루시아에게 메시지를 보냅니다.", "contexto", 1, "coral", 9.0),
    (3, "Diego", "Quiere decirle que la mesa está lista.", "테이블이 준비되었다고 말하고 싶어 해요.", "mensaje", 1, "coral", 7.5),
    (4, "Lucía", "Primero dice: He reservado la mesa.", "먼저 '테이블을 예약했어'라고 말해요.", "he reservado", 1, "coral", 7.5),
    (5, "Jin", "He reservado la mesa.", "테이블을 예약했어.", "modelo", 1, "coral", 6.5),
    (6, "Diego", "Muy bien. He reservado es el pretérito perfecto de reservar.", "좋아요. He reservado는 reservar의 현재완료형이에요.", "gramática", 1, "coral", 9.0),
    (7, "Lucía", "Significa: yo he hecho la reserva.", "내가 예약을 했다는 뜻이에요.", "significado", 1, "coral", 7.5),
    (8, "Jin", "Ya he reservado la mesa.", "이미 테이블을 예약했어.", "modelo", 1, "coral", 7.0),
    (9, "Diego", "Muy bien. Ya significa: en este momento, antes de lo esperado.", "좋아요. Ya는 '이미'라는 뜻이에요.", "ya", 1, "coral", 8.5),
    (10, "Lucía", "Escucha la respuesta de Lucía: ¡Genial! Nos vemos allí.", "루시아의 답장을 들어보세요: 좋아! 거기서 봐.", "respuesta", 2, "teal", 8.5),
    (11, "Lucía", "¡Genial! Nos vemos allí.", "좋아! 거기서 봐.", "modelo", 2, "teal", 6.5),
    (12, "Diego", "Nos vemos significa: nos encontramos.", "Nos vemos는 '우리 만나자'라는 뜻이에요.", "nos vemos", 2, "teal", 7.5),
    (13, "Lucía", "Allí se refiere al restaurante.", "Allí는 그 레스토랑을 가리켜요.", "allí", 2, "teal", 7.5),
    (14, "Jin", "Nos vemos allí a las ocho.", "8시에 거기서 만나자.", "modelo", 2, "teal", 7.5),
    (15, "Diego", "Ahora hablan de la comida. Lucía tiene hambre.", "이제 음식에 대해 이야기해요. 루시아는 배가 고파요.", "hambre", 3, "amber", 8.5),
    (16, "Lucía", "¿Viste el menú? Hay tortilla y croquetas.", "메뉴 봤어? 또르띠야랑 크로케타가 있어.", "menú", 3, "amber", 8.0),
    (17, "Jin", "Sí, ya lo he visto.", "응, 이미 봤어.", "modelo", 3, "amber", 6.5),
    (18, "Diego", "Muy bien. He visto es el participio irregular de ver.", "좋아요. He visto는 ver의 불규칙 과거분사예요.", "gramática", 3, "amber", 8.5),
    (19, "Lucía", "Ella dice: ¡Qué rico! ¡Hasta ahora!", "그녀가 말해요: 맛있겠다! 곧 봐!", "modelo", 3, "amber", 7.5),
    (20, "Lucía", "¡Qué rico! ¡Hasta ahora!", "맛있겠다! 곧 봐!", "modelo", 3, "amber", 6.5),
    (21, "Diego", "¡Hasta ahora! se usa cuando te vas a ver muy pronto.", "¡Hasta ahora!는 아주 곧 만날 때 사용하는 인사예요.", "hasta ahora", 3, "amber", 9.0),
    (22, "Jin", "Sí, ¡hasta ahora!", "응, 곧 봐!", "modelo", 3, "amber", 6.0),
    (23, "Diego", "Excelente. Una conversación muy natural por mensaje de texto.", "훌륭해요. 문자 메시지로 나누는 아주 자연스러운 대화예요.", "natural", 3, "amber", 8.5),
    (24, "Diego", "Mini prueba: ¿qué significa he reservado?", "미니 퀴즈: he reservado는 무슨 뜻일까요?", "quiz", 4, "blue", 8.0),
    (25, "Lucía", "Significa: 예약했어.", "뜻은 ‘예약했어’예요.", "respuesta", 4, "blue", 7.0),
    (26, "Diego", "¿Cómo dices esta frase en español?", "이 문장을 스페인어로 어떻게 말할까요?", "pregunta", 4, "blue", 8.0),
    (27, "Jin", "Ya he reservado la mesa.", "이미 테이블을 예약했어.", "respuesta", 4, "blue", 7.0),
    (28, "Lucía", "¿Cómo dices ‘8시에 거기서 만나자’?", "‘8시에 거기서 만나자’를 어떻게 말할까요?", "pregunta", 4, "blue", 8.5),
    (29, "Jin", "Nos vemos allí a las ocho.", "8시에 거기서 만나자.", "respuesta", 4, "blue", 7.5),
    (30, "Diego", "Perfecto. Ya puedes confirmar tus planes en español.", "완벽해요. 이제 스페인어로 약속을 확정할 수 있어요.", "cierre", 4, "blue", 8.5),
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
    "intro_title": "He reservado la mesa",
    "intro_subtitle": "Español A2 · Ep.33",
    "intro_ko": "예약 완료했어",
    "intro_scene_image_path": "images/ep33-confirmar-reserva-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "He reservado la mesa",
    "thumbnail_subtitle": "Español A2 · Ep.33",
    "thumbnail_ko": "예약 완료했어",
    "outro_ko": "이제 스페인어로 약속 결과를 알리고 확정할 수 있어요",
    "conversation_label": "Conversación A2",
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
            "text_es": "Hoy Jin aprende a confirmar un plan por mensaje de texto usando el pretérito perfecto y expresiones de cita.",
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
                "Muy bien. Ahora puedes confirmar tus planes con Lucía y Diego: "
                "he reservado la mesa, ya he visto el menú y nos vemos allí a las ocho."
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
    {"segment": 2, "title": "La confirmación"},
    {"segment": 12, "title": "El mensaje de Lucía"},
    {"segment": 18, "title": "El menú"},
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
