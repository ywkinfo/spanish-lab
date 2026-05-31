"""A2 entry story-card episode: Jin explains symptoms at a clinic."""

from __future__ import annotations

IMAGE_PATH = "images/ep36-en-el-medico-sintomas-source.png"
DESCRIP_PATH = "a2-en-el-medico-sintomas/descrip.md"
OUTPUT_NAME = "en-el-medico-sintomas"
PUBLIC_SLUG = "a2-en-el-medico-sintomas"
YOUTUBE_URL = ""
SERIES = "frases-a2"
SERIES_TITLE = "Español A2 -- Frases útiles"
EPISODE = 36
LEVEL = "A2 입문"
LANGUAGE = "es"
RENDER_VERSION = 2
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a2-ep36-en-el-medico-sintomas.jpg"
YOUTUBE_TITLE = "Me duele la cabeza 🤕 머리가 아파요 | Español A2 · Ep.36"
DESCRIPTION_INTRO = (
    "Jin no se siente bien y visita una clínica. "
    "En este episodio Jin aprende a explicar sus síntomas al médico diciendo Me duele la cabeza, Tengo fiebre y Tengo tos."
)
DESCRIPTION_OUTRO = (
    "Escucha primero, repite en voz alta y practica las expresiones: "
    "Me duele la cabeza, Tengo fiebre y Tengo tos."
)
KOREAN_TEASER = (
    "한국어 티저: EP.36 병원·증상 편입니다. "
    "아픈 부위를 표현하는 'Me duele la cabeza(머리가 아파요)'와 'Tengo fiebre(열이 나요)', 'Tengo tos(기침이 나요)' 표현을 배웁니다. "
    "의사 선생님의 정중한 처방 표현까지 스페인어로 익혀 보세요!"
)
BASE_TAGS = ["스페인어", "스페인어 입문", "스페인어 A2", "Spanish A2", "aprender español", "español para coreanos"]
EXTRA_TAGS = ["me duele la cabeza", "tengo fiebre", "tengo tos", "Spanish clinic symptoms", "스페인어 회화", "스페인어 병원 표현"]
BASE_HASHTAGS = ["#EspañolA2", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#MeDueleLaCabeza", "#TengoFiebre", "#SpanishLab"]

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
    {"block_id": 1, "title_es": "Los síntomas", "title_ko": "증상 설명", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "El verbo doler", "title_ko": "doler 동사", "color_block": "teal", "start": 4},
    {"block_id": 3, "title_es": "Tener y la receta", "title_ko": "tener와 약 처방", "color_block": "amber", "start": 8},
    {"block_id": 4, "title_es": "Mini prueba", "title_ko": "미니 퀴즈", "color_block": "blue", "start": 17},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Diego", "Hoy aprendemos a hablar de los síntomas en el médico.", "오늘은 병원에서 증상을 말하는 방법을 배워요.", "A2", 1, "coral", 8.0),
    (2, "Lucía", "Jin no se siente bien. Tiene fiebre y dolor de cabeza.", "Jin은 몸이 좋지 않아요. 열이 나고 머리가 아픕니다.", "contexto", 1, "coral", 8.0),
    (3, "Diego", "En la consulta, Jin le explica sus síntomas al médico.", "진료실에서 Jin은 의사에게 자신의 증상을 설명해요.", "consulta", 1, "coral", 8.0),
    (4, "Lucía", "Para decir que te duele una parte del cuerpo, usas el verbo doler: Me duele la cabeza.", "몸의 한 부분이 아프다고 말할 때 doler 동사를 사용해요: 머리가 아파요.", "doler", 2, "teal", 8.5),
    (5, "Jin", "Me duele la cabeza.", "머리가 아파요.", "modelo", 2, "teal", 6.0),
    (6, "Diego", "Muy bien. Y si tienes fiebre, dices: Tengo fiebre.", "좋아요. 그리고 열이 나면 'Tengo fiebre'라고 해요.", "fiebre", 2, "teal", 8.0),
    (7, "Jin", "Tengo fiebre.", "열이 나요.", "modelo", 2, "teal", 6.0),
    (8, "Lucía", "Tengo significa 'yo tengo', del verbo tener.", "Tengo는 tener 동사에서 온 '나는 가지고 있다'라는 뜻이에요.", "tener", 3, "amber", 7.5),
    (9, "Diego", "Si tienes tos, dices: Tengo tos.", "기침이 나면 'Tengo tos'라고 해요.", "tos", 3, "amber", 8.0),
    (10, "Jin", "Tengo tos.", "기침이 나요.", "modelo", 3, "amber", 6.0),
    (11, "Lucía", "Tengo tos significa: 기침이 난다는 뜻이에요.", "Tengo tos는 기침이 난다는 뜻이에요.", "significado", 3, "amber", 7.5),
    (12, "Diego", "El médico examina a Jin y le receta un medicamento.", "의사가 Jin을 진찰하고 약을 처방해 줘요.", "médico", 3, "amber", 8.0),
    (13, "Lucía", "El médico dice: Tome esta medicina.", "의사가 말해요: 이 약을 드세요.", "medicina", 3, "amber", 7.5),
    (14, "Diego", "Tome es una forma del imperativo para usted.", "Tome는 usted에 대한 명령형 형태예요.", "imperativo", 3, "amber", 8.0),
    (15, "Lucía", "Es una expresión muy formal y educada.", "매우 정중하고 예의 바른 표현이에요.", "formal", 3, "amber", 7.5),
    (16, "Diego", "Excelente. Ahora Jin sabe cómo explicar sus síntomas.", "훌륭해요. 이제 Jin은 자신의 증상을 설명할 수 있어요.", "cierre_consulta", 3, "amber", 8.0),
    (17, "Diego", "Mini prueba: ¿cómo dices '머리가 아파요'?", "미니 퀴즈: '머리가 아파요'를 어떻게 말할까요?", "quiz", 4, "blue", 8.0),
    (18, "Lucía", "Dices: Me duele la cabeza.", "Me duele la cabeza라고 해요.", "respuesta", 4, "blue", 7.0),
    (19, "Diego", "¿Cómo dices '열이 나요' en español?", "스페인어로 '열이 나요'를 어떻게 말할까요?", "pregunta", 4, "blue", 7.5),
    (20, "Lucía", "Dices: Tengo fiebre.", "Tengo fiebre라고 해요.", "respuesta", 4, "blue", 7.0),
    (21, "Diego", "¿Cómo dices '기침이 나요'?", "'기침이 나요'는 어떻게 말할까요?", "pregunta", 4, "blue", 7.5),
    (22, "Jin", "Tengo tos.", "Tengo tos라고 해요.", "respuesta", 4, "blue", 7.0),
    (23, "Diego", "Muy bien. Ya sabes hablar de tus síntomas en español.", "좋아요. 이제 스페인어로 증상을 설명할 수 있어요.", "cierre", 4, "blue", 8.5),
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
    "intro_title": "En el médico",
    "intro_subtitle": "Español A2 · Ep.36",
    "intro_ko": "의사 선생님, 아파요",
    "intro_scene_image_path": "images/ep36-en-el-medico-sintomas-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "En el médico",
    "thumbnail_subtitle": "Español A2 · Ep.36",
    "thumbnail_ko": "의사 선생님, 아파요",
    "outro_ko": "이제 스페인어로 자신의 증상을 설명할 수 있어요",
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
            "text_es": "Hoy Jin aprende a explicar sus síntomas al médico diciendo Me duele la cabeza, Tengo fiebre y Tengo tos.",
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
                "Muy bien. Ahora puedes explicar tus síntomas al médico en español: "
                "Me duele la cabeza, Tengo fiebre y Tengo tos."
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
    {"segment": 2, "title": "Los síntomas"},
    {"segment": 6, "title": "El verbo doler"},
    {"segment": 11, "title": "Tener y la receta"},
    {"segment": 21, "title": "Mini prueba"},
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
