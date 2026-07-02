"""Español en el Camino · Ep.1: "La idea" (PILOT).

Dialogue drama, A2+/B1-low. Three friends — Lucía, Diego, Jin — receive the
pilgrim's credential by post. Grammar focus: querer/me gustaría + infinitivo.
31 spoken lines, ~5 min finished length.

RENDER_TYPE = "diary"  (multi-scene stills + Ken Burns + per-speaker TTS)
STATUS: draft — awaiting 8 scene images in assets/images/camino_a2_ep01_la_idea/
"""

from __future__ import annotations

IMAGE_PATH = ""
DESCRIP_PATH = "camino-a2-ep01-la-idea/descrip.md"
OUTPUT_NAME = "la-idea"
PUBLIC_SLUG = "camino-a2-ep01-la-idea"
YOUTUBE_URL = ""
SERIES = "camino-a2"
SERIES_TITLE = "Español en el Camino"
EPISODE = 1
LEVEL = "A2+/B1-low"
LANGUAGE = "es"
RENDER_VERSION = 2
RENDER_TYPE = "diary"
THUMBNAIL_PATH = "thumbs/camino-a2-ep01-la-idea-draft.jpg"
YOUTUBE_TITLE = (
    "La idea — Ep.01 | Español en el Camino "
    "🐚 순례길을 걷고 싶어 | querer + infinitivo · A2+"
)
DESCRIPTION_INTRO = (
    "Tres amigos reciben la credencial del peregrino por correo y tienen que decidir, "
    "de verdad, si quieren hacer el Camino de Santiago. Lucía, Diego y Jin expresan "
    "sus deseos con la estructura querer + infinitivo y me gustaría + infinitivo. "
    "Episodio piloto de la serie 'Español en el Camino'."
)
DESCRIPTION_OUTRO = (
    "¿Quieres hacer el Camino? Practica en voz alta: 'Quiero hacer el Camino. "
    "Me gustaría hacerlo con mis amigos.' Repasa las palabras clave: "
    "la credencial, el peregrino, la vieira, el albergue. ¡Buen Camino!"
)
KOREAN_TEASER = (
    "루시아, 디에고, 진 — 세 친구가 우편으로 순례자 여권(크레덴시알)을 받습니다. "
    "산티아고 순례길을 정말 걸을 수 있을까요? "
    "'Quiero + 동사원형'(~하고 싶어)과 'Me gustaría + 동사원형'(~하면 좋겠어) 표현을 "
    "자연스러운 대화 속에서 익혀 보세요. 'Español en el Camino' 시리즈 1화."
)

BASE_TAGS = [
    "스페인어",
    "스페인어 A2",
    "스페인어 듣기 연습",
]
EXTRA_TAGS = [
    "querer 동사",
    "산티아고 순례길",
    "스페인어 드라마",
    "스페인어 이야기",
    "Camino de Santiago",
]
BASE_HASHTAGS = ["#EspañolA2", "#스페인어"]
EXTRA_HASHTAGS = ["#CaminoDeSantiago", "#순례길스페인어", "#EspañolEnElCamino"]

# Exactly 5 items (validated by checks/validate_segments.py). Focus: querer/me gustaría
# + infinitivo and the episode's Camino vocabulary.
MINI_QUIZ = [
    ("¿Cómo dices '순례자 여권'?", "La credencial"),
    ("¿Cómo dices '가리비 (순례길의 상징)'?", "La vieira"),
    ("¿Cómo dices '나는 순례길을 걷고 싶어'?", "Quiero hacer el Camino"),
    ("¿Cómo dices '~하면 좋겠다 (부드러운 바람)'?", "Me gustaría"),
    ("¿Cómo dices '좋은 순례길 되세요 (순례자 인사)'?", "Buen Camino"),
]

# ---------------------------------------------------------------------------
# Visual design
# ---------------------------------------------------------------------------
DESIGN = {
    "output_size": (1920, 1080),
    "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
    "font_index": 0,
    "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
    "font_index_ko": 0,
    "font_size_title": 82,
    "font_size_es": 84,
    "min_font_size_es": 52,
    "font_size_ko": 36,
    "font_size_example": 34,
    "background_color": (248, 247, 242),
    "text_color": (31, 35, 40),
    "muted_text_color": (96, 101, 109),
    "intro_title": "La idea",
    "intro_subtitle": "Español en el Camino · Ep.1",
    "intro_ko": "세 친구에게 순례자 여권이 도착했어요. 산티아고 순례길, 정말 떠날까요?",
    "outro_title": "Muy bien",
    "outro_subtitle": "Fin de la lección",
    "outro_ko": "2화에서는 세 친구가 여행 계획을 세워요. 댓글로 여러분의 대답도 들려주세요!",
    "diary_intro_background_path": "assets/images/camino_a2_ep01_la_idea/scene_02_three_backs.png",
    "diary_outro_background_path": "assets/images/camino_a2_ep01_la_idea/scene_08_cuaderno_closeup.png",
    # --- Intro/outro big center card (diary_intro_layout = "center_card") ---
    "diary_intro_layout": "center_card",
    "diary_intro_image_blend_alpha": 0.24,
    "diary_intro_title_font_size": 106,
    "diary_intro_subtitle_font_size": 48,
    # Camino intro/outro narrations run ~240 chars — larger card, smaller body
    # than the diario ep51 golden so the text stays inside the card.
    "diary_intro_body_font_size": 48,
    "diary_intro_ko_font_size": 44,
    "diary_intro_card_w": 1560,
    "diary_intro_card_h": 900,
    "diary_intro_card_pad_top": 74,
    "diary_intro_card_fill": (255, 250, 239, 140),
    "diary_intro_card_outline": (255, 255, 255, 120),
    "diary_intro_body_line_step": 60,
    "diary_intro_ko_line_step": 52,
    # --- Enlarged caption panel (diario ep51 values) ---
    "diary_caption_speaker_font_size": 38,
    "diary_caption_es_font_size": 82,
    "diary_caption_ko_font_size": 52,
    "diary_caption_es_line_step": 92,
    "diary_caption_ko_line_step": 62,
    "diary_caption_interline_gap": 18,
    "diary_caption_panel_w": 1720,
    "diary_caption_panel_min_h": 280,
    "diary_caption_panel_bottom": 34,
    "diary_caption_panel_alpha": 185,
    # --- Fixed per-character badge colors (matched to wardrobe/assets) ---
    "speaker_colors": {
        "Lucía": (47, 95, 143),
        "Diego": (92, 111, 53),
        "Jin": (179, 106, 46),
        "Narrador": (42, 48, 57),
    },
    "montage_title": "La idea",
    "montage_subtitle": "el episodio completo",
    "montage_ko": "에피소드 전체 다시 보기",
    "montage_order_text": "La idea  →  La credencial  →  La decisión  →  ¡Buen Camino!",
    "thumbnail_title": "La idea",
    "thumbnail_subtitle": "Español en el Camino · A2+",
    "thumbnail_ko": "Quiero hacer el Camino",
    "color_blocks": {
        "coral": (224, 91, 76),
        "amber": (230, 158, 62),
        "teal": (44, 150, 142),
        "blue": (70, 120, 196),
        "green": (92, 148, 86),
        "neutral": (42, 48, 57),
    },
}

# ---------------------------------------------------------------------------
# v2 diary: STORY_SCENES
# ---------------------------------------------------------------------------
_BASE = "assets/images/camino_a2_ep01_la_idea"

STORY_SCENES = [
    # ------------------------------------------------------------------
    # Scene 1 — Cold-open  "Una tarde en el café"  (atmosphere, no dialogue)
    # ------------------------------------------------------------------
    {
        "scene_id": 1,
        "title_es": "Una tarde en el café",
        "title_ko": "카페에서의 오후",
        "image_path": f"{_BASE}/scene_01_cafe_terrace.png",
        "ambient_sfx": "",
        "ambient_sfx_license": "CC0",
        "pause_s": 2.5,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Una tarde de primavera en un café de España.",
                "text_ko": "스페인의 어느 봄날 오후, 카페입니다.",
            },
        ],
    },
    # ------------------------------------------------------------------
    # Scene 2 — Intro / title beat  "La idea"
    # ------------------------------------------------------------------
    {
        "scene_id": 2,
        "title_es": "La idea",
        "title_ko": "그 아이디어",
        "image_path": f"{_BASE}/scene_02_three_backs.png",
        "ambient_sfx": "",
        "ambient_sfx_license": "CC0",
        "pause_s": 2.5,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": 'Episodio uno: "La idea". Estos son Lucía, Diego y Jin.',
                "text_ko": '1화 "그 아이디어". 이쪽은 루시아, 디에고, 진입니다.',
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "¡Por fin estamos los tres juntos!",
                "text_ko": "드디어 우리 셋이 다 모였네!",
            },
        ],
    },
    # ------------------------------------------------------------------
    # Scene 3 — The credencial arrives  "El sobre"
    # ------------------------------------------------------------------
    {
        "scene_id": 3,
        "title_es": "El sobre",
        "title_ko": "봉투",
        "image_path": f"{_BASE}/scene_03_envelope_arrival.png",
        "ambient_sfx": "",
        "ambient_sfx_license": "CC0",
        "pause_s": 2.5,
        "lines": [
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Mirad, ha llegado algo por correo. Es la credencial del peregrino.",
                "text_ko": "봐, 우편으로 뭔가 왔어. 순례자 여권이야.",
            },
            {
                "kind": "dialogue",
                "speaker": "Diego",
                "text_es": "¿La credencial? ¿La del Camino de Santiago?",
                "text_ko": "크레덴시알? 산티아고 순례길 거?",
            },
            {
                "kind": "dialogue",
                "speaker": "Jin",
                "text_es": '¿Cómo se dice "concha"? ¿Esta de aquí?',
                "text_ko": '"concha"가 뭐였지? 이거 말이야?',
            },
            {
                "kind": "dialogue",
                "speaker": "Diego",
                "text_es": "Es la vieira, el símbolo del Camino. Y la credencial todavía está vacía.",
                "text_ko": "가리비(vieira)야, 순례길의 상징이지. 그리고 크레덴시알은 아직 비어 있어.",
            },
        ],
    },
    # ------------------------------------------------------------------
    # Scene 4 — Hesitation + Lucía's seed  "¿Estamos locos?"
    # ------------------------------------------------------------------
    {
        "scene_id": 4,
        "title_es": "¿Estamos locos?",
        "title_ko": "우리 미친 거 아냐?",
        "image_path": f"{_BASE}/scene_04_credencial_closeup.png",
        "ambient_sfx": "",
        "ambient_sfx_license": "CC0",
        "pause_s": 2.5,
        "lines": [
            {
                "kind": "dialogue",
                "speaker": "Diego",
                "text_es": "¿Ochocientos kilómetros a pie? ¿Estamos locos?",
                "text_ko": "800킬로미터를 걸어서? 우리 미친 거 아냐?",
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Quizá. Pero quiero hacer el Camino.",
                "text_ko": "아마도. 하지만 나는 순례길을 걷고 싶어.",
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Quiero empezar algo nuevo. Necesito tiempo para pensar.",
                "text_ko": "새로운 걸 시작하고 싶어. 생각할 시간이 필요해.",
            },
            {
                "kind": "dialogue",
                "speaker": "Diego",
                "text_es": "¿De verdad quieres hacerlo?",
                "text_ko": "정말 하고 싶어?",
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Sí, de verdad. No quiero esperar más.",
                "text_ko": "응, 정말로. 더는 미루고 싶지 않아.",
            },
        ],
    },
    # ------------------------------------------------------------------
    # Scene 5 — Each reason surfaces  "Cada uno tiene su razón"
    # ------------------------------------------------------------------
    {
        "scene_id": 5,
        "title_es": "Cada uno tiene su razón",
        "title_ko": "각자의 이유",
        "image_path": f"{_BASE}/scene_05_reasons_table.png",
        "ambient_sfx": "",
        "ambient_sfx_license": "CC0",
        "pause_s": 2.5,
        "lines": [
            {
                "kind": "dialogue",
                "speaker": "Diego",
                "text_es": "Soy mexicano y nunca he hecho el Camino. Yo también quiero hacerlo.",
                "text_ko": "나 멕시코 사람인데 순례길을 한 번도 안 해 봤어. 나도 하고 싶어.",
            },
            {
                "kind": "dialogue",
                "speaker": "Diego",
                "text_es": "Quiero ver España a pie, despacio.",
                "text_ko": "스페인을 두 발로, 천천히 보고 싶어.",
            },
            {
                "kind": "dialogue",
                "speaker": "Jin",
                "text_es": "¿Y el dinero? ¿Y los días libres?",
                "text_ko": "돈은? 그리고 휴가는?",
            },
            {
                "kind": "dialogue",
                "speaker": "Diego",
                "text_es": "Con poco dinero se puede. Los albergues son baratos.",
                "text_ko": "적은 돈으로도 돼. 알베르게는 싸거든.",
            },
            {
                "kind": "dialogue",
                "speaker": "Jin",
                "text_es": "Entonces… me gustaría hacer el Camino con vosotros.",
                "text_ko": "그럼… 나도 너희랑 순례길을 걷고 싶어.",
            },
            {
                "kind": "dialogue",
                "speaker": "Jin",
                "text_es": "Quiero hablar español de verdad, no solo estudiarlo.",
                "text_ko": "스페인어를 진짜로 말하고 싶어. 공부만 하는 게 아니라.",
            },
        ],
    },
    # ------------------------------------------------------------------
    # Scene 6 — The doubt softens  "Juntos da menos miedo"
    # ------------------------------------------------------------------
    {
        "scene_id": 6,
        "title_es": "Juntos da menos miedo",
        "title_ko": "같이 가면 덜 무서워",
        "image_path": f"{_BASE}/scene_06_together.png",
        "ambient_sfx": "",
        "ambient_sfx_license": "CC0",
        "pause_s": 2.5,
        "lines": [
            {
                "kind": "dialogue",
                "speaker": "Jin",
                "text_es": "Solo, me da un poco de miedo.",
                "text_ko": "혼자라면 좀 무서워.",
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Yo no quiero hacerlo sola. Quiero hacer el Camino con vosotros.",
                "text_ko": "나 혼자 하고 싶지 않아. 너희랑 함께 순례길을 걷고 싶어.",
            },
            {
                "kind": "dialogue",
                "speaker": "Diego",
                "text_es": "Juntos da menos miedo. Pues lo hacemos, los tres.",
                "text_ko": "같이 가면 덜 무섭지. 그럼 하는 거야, 우리 셋이서.",
            },
            {
                "kind": "dialogue",
                "speaker": "Jin",
                "text_es": "¿De verdad? ¿Los tres juntos?",
                "text_ko": "정말? 우리 셋이 다 같이?",
            },
        ],
    },
    # ------------------------------------------------------------------
    # Scene 7 — The decision  "Lo hacemos"
    # ------------------------------------------------------------------
    {
        "scene_id": 7,
        "title_es": "Lo hacemos",
        "title_ko": "하는 거야",
        "image_path": f"{_BASE}/scene_07_decision.png",
        "ambient_sfx": "",
        "ambient_sfx_license": "CC0",
        "pause_s": 2.5,
        "lines": [
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Entonces, ¿lo hacemos?",
                "text_ko": "그래서, 우리 하는 거지?",
            },
            {
                "kind": "dialogue",
                "speaker": "Diego",
                "text_es": "¡Lo hacemos!",
                "text_ko": "하자!",
            },
            {
                "kind": "dialogue",
                "speaker": "Jin",
                "text_es": "¡Lo hacemos!",
                "text_ko": "하자!",
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Queremos hacer el Camino juntos.",
                "text_ko": "우리는 함께 순례길을 걷고 싶어.",
            },
            {
                "kind": "dialogue",
                "speaker": "Diego",
                "text_es": 'Hay una frase para esto. Se dice "Buen Camino".',
                "text_ko": '이럴 때 쓰는 말이 있어. "부엔 카미노"라고 해.',
            },
        ],
    },
    # ------------------------------------------------------------------
    # Scene 8 — Cuaderno del peregrino  "El cuaderno de Jin"
    # ------------------------------------------------------------------
    {
        "scene_id": 8,
        "title_es": "El cuaderno de Jin",
        "title_ko": "진의 공책",
        "image_path": f"{_BASE}/scene_08_cuaderno_closeup.png",
        "ambient_sfx": "",
        "ambient_sfx_license": "CC0",
        "pause_s": 3.0,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Esa noche, Jin escribe en su cuaderno.",
                "text_ko": "그날 밤, 진은 공책에 씁니다.",
            },
            {
                "kind": "dialogue",
                "speaker": "Jin",
                "text_es": 'La frase del día es "Quiero hacer el Camino".',
                "text_ko": '오늘의 문장: "나는 순례길을 걷고 싶어".',
            },
            {
                "kind": "dialogue",
                "speaker": "Jin",
                "text_es": 'Con "querer" más infinitivo, digo lo que deseo.',
                "text_ko": '"querer + 동사원형"으로 바라는 걸 말한다.',
            },
            {
                "kind": "dialogue",
                "speaker": "Jin",
                "text_es": 'También, "Me gustaría hacerlo".',
                "text_ko": '"Me gustaría hacerlo"라고도 한다.',
            },
            {
                "kind": "dialogue",
                "speaker": "Jin",
                "text_es": "Palabras nuevas: la credencial, el peregrino, la vieira. ¡Buen Camino!",
                "text_ko": "새 단어: 크레덴시알, 순례자, 가리비. 부엔 카미노!",
            },
        ],
    },
]

# ---------------------------------------------------------------------------
# SFX manifest — empty until audio-engineer sources Camino ambience
# (non-empty paths with silent WAVs block the gate; leave empty for now)
# ---------------------------------------------------------------------------
SFX_MANIFEST: list[dict] = []

# ---------------------------------------------------------------------------
# Structural segment SFX — paths left empty; audio-engineer fills these later
# ---------------------------------------------------------------------------
SEGMENT_SFX: list[dict] = []

# ---------------------------------------------------------------------------
# Segment builder (v2 diary)
# ---------------------------------------------------------------------------

def _build_diary_segments() -> list[dict]:
    """Generate SEGMENTS from STORY_SCENES for the diary render pipeline."""
    segments: list[dict] = [
        {
            "type": "intro",
            "text_es": (
                "Hoy empieza una nueva historia. Lucía, Diego y Jin son tres amigos. "
                "Reciben la credencial del peregrino por correo y tienen que decidir: "
                "¿quieren hacer el Camino de Santiago? "
                "Fíjate en la frase 'Quiero hacer el Camino' y sus variaciones."
            ),
            "duration_s": 16.0,
        }
    ]
    for scene in STORY_SCENES:
        # Scene header
        segments.append(
            {
                "type": "scene_header",
                "scene_id": scene["scene_id"],
                "title_es": scene["title_es"],
                "title_ko": scene["title_ko"],
                "duration_s": 3.0,
            }
        )
        # Lines
        for line in scene["lines"]:
            resolved_img = line.get("image_path") or scene.get("image_path", "")
            seg = {
                "type": "diary_line",
                "scene_id": scene["scene_id"],
                "kind": line["kind"],
                "speaker": line["speaker"],
                "text_es": line["text_es"],
                "text_ko": line["text_ko"],
                "image_path": resolved_img,
            }
            if "duration_s" in line:
                seg["duration_s"] = line["duration_s"]
            if "min_hold_s" in line:
                seg["min_hold_s"] = line["min_hold_s"]
            if "processing_pause_s" in line:
                seg["processing_pause_s"] = line["processing_pause_s"]
            segments.append(seg)
        # Pause after scene
        last_line_img = (
            scene["lines"][-1].get("image_path") or scene.get("image_path", "")
            if scene["lines"]
            else scene.get("image_path", "")
        )
        segments.append(
            {
                "type": "pause",
                "scene_id": scene["scene_id"],
                "duration_s": scene["pause_s"],
                "image_path": last_line_img,
            }
        )
    # Montage
    segments.append(
        {
            "type": "montage",
            "duration_s": 6.0,
        }
    )
    # Outro
    segments.append(
        {
            "type": "outro",
            "text_es": (
                "Muy bien. Practica en voz alta: 'Quiero hacer el Camino. "
                "Me gustaría hacerlo con mis amigos.' "
                "Y tú, ¿quieres hacer el Camino? Escríbelo en los comentarios. "
                "En el próximo episodio, los tres empiezan a planificar el viaje. ¡Buen Camino!"
            ),
            "duration_s": 15.0,
        }
    )
    return segments


SEGMENTS = _build_diary_segments()


def _find_chapter_segment(scene_id: int) -> int:
    for idx, seg in enumerate(SEGMENTS):
        if seg.get("type") == "scene_header" and seg.get("scene_id") == scene_id:
            return idx + 1
    raise ValueError(f"missing scene_header for scene_id={scene_id}")


# Order (v1): the diary builder places the INTRO card first, so segment 1 is the
# title card at 0:00 ("La idea") — NOT a bug. The café "cold-open" is Scene 1, which
# follows the title card; true cold-open-before-title would need a builder reorder and
# is a deferred enhancement. Chapters below are honest to the actual segment order.
CHAPTERS = [
    {"segment": 1,                         "title": "La idea"},
    {"segment": _find_chapter_segment(1),  "title": "La tarde en el café"},
    {"segment": _find_chapter_segment(2),  "title": "Los tres amigos"},
    {"segment": _find_chapter_segment(3),  "title": "El sobre"},
    {"segment": _find_chapter_segment(4),  "title": "¿Estamos locos?"},
    {"segment": _find_chapter_segment(5),  "title": "Cada uno tiene su razón"},
    {"segment": _find_chapter_segment(6),  "title": "Juntos da menos miedo"},
    {"segment": _find_chapter_segment(7),  "title": "Lo hacemos"},
    {"segment": _find_chapter_segment(8),  "title": "El cuaderno de Jin"},
    {"segment": len(SEGMENTS),             "title": "Cuaderno del peregrino"},
]

# ---------------------------------------------------------------------------
# Audio — 4-voice: Lucía / Diego / Jin / narrator (Ximena)
# ---------------------------------------------------------------------------
AUDIO = {
    "tts_engine": "edge",
    "edge_voice": "es-ES-XimenaNeural",   # narrator voice
    "edge_rate": "+8%",
    "edge_pitch": "+0Hz",
    "edge_volume": "+0%",
    "voice": "es-ES-XimenaNeural",        # narrator voice (legacy alias)
    "character_voices": {
        "Lucía": "es-ES-ElviraNeural",
        "Diego": "es-MX-JorgeNeural",
        "Jin":   "es-US-AlonsoNeural",
    },
    "rate_wpm": 160,
    "lead_padding_s": 0.25,
    "tail_padding_s": 0.4,
    "min_duration_s": 3.0,
    "readability_floor_ratio": 0.0,
    "processing_pause_s": 2.5,            # A2+ comprehension time — do not shorten
    "min_hold_s": 2.5,
    "ambient_bed_db": -11.9,
    "bgm_path": "assets/audio/spanish-lab-brand-bgm.mp3",
    "bgm_volume_db": -4.0,
    "narration_volume_db": 0.0,
    "ducking": True,
    "ducking_threshold": 0.05,
    "ducking_ratio": 4,
    "ducking_attack_ms": 80,
    "ducking_release_ms": 550,
    "fade_in_s": 4.0,
    "fade_out_s": 5.0,
    "audio_codec": "aac",
    "audio_bitrate_kbps": 192,
    "sample_rate_hz": 44100,
}
