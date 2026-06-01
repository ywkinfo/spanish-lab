"""A2 entry story-card episode: Jin declines Diego's running invitation because he is sick."""

from __future__ import annotations

IMAGE_PATH = "images/ep37-llamada-gripe-rechazo-source.png"
DESCRIP_PATH = "a2-llamada-gripe-rechazo/descrip.md"
OUTPUT_NAME = "llamada-gripe-rechazo"
PUBLIC_SLUG = "a2-llamada-gripe-rechazo"
YOUTUBE_URL = ""
SERIES = "frases-a2"
SERIES_TITLE = "Español A2 -- Frases útiles"
EPISODE = 37
LEVEL = "A2 입문"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a2-ep37-llamada-gripe-rechazo.jpg"
YOUTUBE_TITLE = "No puedo ir porque estoy enfermo 📞 전화로 약속 거절하기 | Español A2 · Ep.37"
DESCRIPTION_INTRO = (
    "Diego llama a Jin para correr, pero Jin no puede ir porque tiene gripe. "
    "En este episodio Jin aprende a rechazar una invitación y a explicar sus síntomas por teléfono: No puedo ir, Tengo gripe y Me duele todo el cuerpo."
)
DESCRIPTION_OUTRO = (
    "Escucha primero, repite en voz alta y practica las expresiones: "
    "No puedo ir, Tengo gripe, Me duele todo el cuerpo y Que te mejores pronto."
)
KOREAN_TEASER = (
    "한국어 티저: EP.37 전화 약속 거절 편입니다. "
    "디에고의 러닝 제안 전화에 대해 아파서 거절하는 상황에서 쓰는 'No puedo ir(갈 수 없어)', 'Tengo gripe(독감에 걸렸어)', 'Me duele todo el cuerpo(온몸이 아파)' 표현을 배웁니다. "
    "아픈 친구에게 건네는 따뜻한 덕담 'Que te mejores pronto(빨리 나아)'까지 함께 익혀보세요!"
)
BASE_TAGS = ["스페인어", "스페인어 입문", "스페인어 A2", "Spanish A2", "aprender español", "español para coreanos"]
EXTRA_TAGS = ["no puedo ir", "tengo gripe", "me duele todo el cuerpo", "que te mejores pronto", "스페인어 회화", "스페인어 전화 표현"]
BASE_HASHTAGS = ["#EspañolA2", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#NoPuedoIr", "#TengoGripe", "#SpanishLab"]

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
    {"block_id": 1, "title_es": "La invitación", "title_ko": "전화와 약속 제안", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "El rechazo y los síntomas", "title_ko": "거절과 독감 증상", "color_block": "teal", "start": 5},
    {"block_id": 3, "title_es": "El alivio y los deseos", "title_ko": "안도와 건강 기원", "color_block": "amber", "start": 12},
    {"block_id": 4, "title_es": "Mini prueba", "title_ko": "미니 퀴즈", "color_block": "blue", "start": 20},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Diego", "Hoy aprendemos a proponer planes por teléfono y a rechazar invitaciones si estamos enfermos.", "오늘은 전화로 약속을 제안하고, 아플 때 거절하는 방법을 배워요.", "A2", 1, "coral", 8.5),
    (2, "Lucía", "Diego llama a Jin para ir a correr. Pero Jin no se siente bien.", "Diego가 러닝하러 가자고 Jin에게 전화를 해요. 하지만 Jin은 몸 상태가 좋지 않습니다.", "contexto", 1, "coral", 8.0),
    (3, "Diego", "En la conversación, Jin explica sus síntomas a Diego.", "대화 속에서 Jin은 Diego에게 자신의 증상을 설명해요.", "explicar", 1, "coral", 8.0),
    (4, "Diego", "¡Hola, Jin! ¿Qué tal? Hace muy buen tiempo para correr hoy.", "안녕 Jin! 어떻게 지내? 오늘 러닝하기 정말 좋은 날씨야.", "modelo", 1, "coral", 7.5),
    (5, "Jin", "Hola, Diego. Me encantaría, pero hoy no puedo ir.", "안녕 Diego. 가고 싶지만 오늘은 갈 수가 없어.", "modelo", 2, "teal", 6.5),
    (6, "Lucía", "Me encantaría expresa un deseo fuerte de aceptar, pero va seguido de un pero.", "Me encantaría는 수락하고 싶은 강한 의지를 표현하지만, 뒤이어 pero(하지만)가 따라와요.", "uso", 2, "teal", 8.5),
    (7, "Diego", "¿Qué te pasa? ¿Te encuentras mal?", "무슨 일 있어? 몸이 안 좋아?", "modelo", 2, "teal", 6.5),
    (8, "Jin", "Sí, no me encuentro bien. Tengo gripe.", "응, 몸이 안 좋아. 독감에 걸렸어.", "modelo", 2, "teal", 6.5),
    (9, "Diego", "Gripe es una enfermedad vírica que produce fiebre y dolor de cuerpo.", "독감(gripe)은 열과 몸살을 동반하는 바이러스성 질환이에요.", "significado", 2, "teal", 8.5),
    (10, "Jin", "Me duele todo el cuerpo y tengo mucha fiebre.", "온몸이 아프고 열이 많이 나.", "modelo", 2, "teal", 7.0),
    (11, "Lucía", "Me duele todo el cuerpo significa que sientes dolor en general.", "Me duele todo el cuerpo는 전반적으로 통증을 느낀다는 뜻이에요.", "explicación", 2, "teal", 8.0),
    (12, "Diego", "¡Qué lástima! ¿Has ido al médico o has tomado algo?", "안타깝다! 병원에 갔거나 약은 좀 먹었어?", "modelo", 3, "amber", 7.5),
    (13, "Jin", "Fui ayer. El médico me dijo que tengo que descansar.", "어제 갔다 왔어. 의사 선생님이 쉬어야 한대.", "modelo", 3, "amber", 6.5),
    (14, "Diego", "Menos mal que fuiste. Tómate la medicina y descansa mucho.", "병원에 갔다니 다행이다. 약 먹고 푹 쉬어.", "modelo", 3, "amber", 7.5),
    (15, "Lucía", "Menos mal expresa alivio por algo bueno que ha ocurrido.", "Menos mal은 다행스러운 일에 대해 안도감을 표현해요.", "uso", 3, "amber", 8.0),
    (16, "Jin", "Gracias, Diego. Disfruta de la carrera.", "고마워 Diego. 러닝 잘 해.", "modelo", 3, "amber", 6.5),
    (17, "Diego", "De nada. ¡Que te mejores pronto!", "천만에. 빨리 낫기를 바랄게!", "modelo", 3, "amber", 6.5),
    (18, "Lucía", "Que te mejores pronto es un deseo común para alguien enfermo.", "Que te mejores pronto는 아픈 사람에게 건내는 흔한 덕담이에요.", "uso", 3, "amber", 8.0),
    (19, "Diego", "Excelente. Ahora Jin sabe cómo disculparse y explicar que está enfermo.", "훌륭해요. 이제 Jin은 아파서 약속을 거절하는 방법을 알아요.", "cierre_llamada", 3, "amber", 8.0),
    (20, "Diego", "Mini prueba: ¿cómo dices '가고 싶지만, 오늘 못 가요'?", "미니 퀴즈: '가고 싶지만, 오늘 못 가요'를 어떻게 말할까요?", "quiz", 4, "blue", 8.0),
    (21, "Lucía", "Dices: Me encantaría, pero hoy no puedo ir.", "Me encantaría, pero hoy no puedo ir라고 해요.", "respuesta", 4, "blue", 7.0),
    (22, "Diego", "¿Cómo dices '독감에 걸렸어' en español?", "스페인어로 '독감에 걸렸어'를 어떻게 말할까요?", "pregunta", 4, "blue", 7.5),
    (23, "Lucía", "Dices: Tengo gripe.", "Tengo gripe라고 해요.", "respuesta", 4, "blue", 7.0),
    (24, "Diego", "¿Cómo dices '빨리 나아'?", "'빨리 나아'는 어떻게 말할까요?", "pregunta", 4, "blue", 7.0),
    (25, "Jin", "Que te mejores pronto.", "Que te mejores pronto라고 해요.", "respuesta", 4, "blue", 6.5),
    (26, "Diego", "Muy bien. Ya sabes hablar de tu salud por teléfono.", "좋아요. 이제 전화로 건강 상태에 대해 이야기할 수 있어요.", "cierre", 4, "blue", 8.0),
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
    "intro_subtitle": "Español A2 · Ep.37",
    "intro_ko": "아파서 못 가요",
    "intro_scene_image_path": "images/ep37-llamada-gripe-rechazo-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "No puedo ir",
    "thumbnail_subtitle": "Español A2 · Ep.37",
    "thumbnail_ko": "아파서 못 가요",
    "outro_ko": "이제 전화로 건강 상태를 말하고 약속을 거절할 수 있어요",
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
            "text_es": "Hoy Jin aprende a rechazar una invitación y a explicar sus síntomas por teléfono diciendo No puedo ir, Tengo gripe y Me duele todo el cuerpo.",
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
                "Muy bien. Ahora puedes rechazar invitaciones y hablar de tu salud por teléfono en español: "
                "No puedo ir, Tengo gripe, Me duele todo el cuerpo y Que te mejores pronto."
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
    {"segment": 7, "title": "El rechazo y los síntomas"},
    {"segment": 15, "title": "El alivio y los deseos"},
    {"segment": 24, "title": "Mini prueba"},
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
