"""Español en el Camino · Ep.2: "La ruta".

Dialogue drama, A2+/B1-low. Three friends — Lucía, Diego, Jin — have decided
to walk the Camino; now they must choose the route. Grammar focus:
comparatives más… que / menos… que, culminating in the superlative el más….
29 spoken lines, ~5 min finished length.

RENDER_TYPE = "diary"  (multi-scene stills + Ken Burns + per-speaker TTS)
STATUS: draft — awaiting 8 scene images in assets/images/camino_a2_ep02_la_ruta/
"""

from __future__ import annotations

IMAGE_PATH = "assets/images/camino_a2_ep02_la_ruta/scene_01_map_on_table.png"
DESCRIP_PATH = "camino-a2-ep02-la-ruta/descrip.md"
OUTPUT_NAME = "la-ruta"
PUBLIC_SLUG = "camino-a2-ep02-la-ruta"
YOUTUBE_URL = ""
SERIES = "camino-a2"
SERIES_TITLE = "Español en el Camino"
EPISODE = 2
LEVEL = "A2+/B1-low"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "diary"
THUMBNAIL_PATH = "thumbs/camino-a2-ep02-la-ruta-draft.jpg"
YOUTUBE_TITLE = (
    "[스페인어 듣기 A2+] 어느 길로 갈까? | La ruta Camino Ep.02"
)
DESCRIPTION_INTRO = (
    "Tres amigos ya han decidido hacer el Camino de Santiago; ahora tienen que elegir "
    "la ruta. Una tarde en el piso de Lucía, con un gran mapa sobre la mesa, Diego "
    "presenta las opciones: el Francés, el del Norte y el Portugués. Lucía, Diego y "
    "Jin comparan las rutas con la estructura 'más… que' / 'menos… que' y llegan al "
    "superlativo 'el más…'. Episodio 2 de la serie 'Español en el Camino'."
)
DESCRIPTION_OUTRO = (
    "Practica en voz alta: 'El Francés es el más largo, pero el más bonito.' Y tú, "
    "¿qué camino prefieres? Escríbelo en los comentarios. Repasa las palabras clave: "
    "la ruta, el mapa, la guía, el albergue. En el próximo episodio, los tres eligen "
    "la fecha de salida. ¡Buen Camino!"
)
KOREAN_TEASER = (
    "루시아, 디에고, 진 — 이제 순례길을 걷기로 한 세 친구가 어느 길로 갈지 정합니다. "
    "프랑세스, 노르테, 포르투게스 중 어떤 길이 좋을까요? "
    "비교급 'más… que'(~보다 더) / 'menos… que'(~보다 덜)와 "
    "최상급 'el más…'(가장 ~한) 표현을 자연스러운 대화 속에서 익혀 보세요. "
    "'Español en el Camino' 시리즈 2화."
)

BASE_TAGS = [
    "스페인어",
    "스페인어 A2",
    "스페인어 듣기 연습",
]
EXTRA_TAGS = [
    "스페인어 비교급",
    "산티아고 순례길",
    "스페인어 드라마",
    "스페인어 이야기",
    "Camino de Santiago",
]
BASE_HASHTAGS = ["#EspañolA2", "#스페인어"]
EXTRA_HASHTAGS = ["#CaminoDeSantiago", "#순례길스페인어", "#EspañolEnElCamino"]

# Exactly 5 items (validated by checks/validate_segments.py). Focus: comparatives
# más… que / menos… que + superlative el más… and the episode's Camino vocabulary.
MINI_QUIZ = [
    ("¿Cómo dices '길 / 경로'?", "La ruta"),
    ("¿Cómo dices '지도'?", "El mapa"),
    ("¿Cómo dices '프랑세스가 포르투게스보다 더 길어'?", "El Francés es más largo que el Portugués"),
    ("¿Cómo dices '(그중) 제일 아름다운'?", "El más bonito"),
    ("¿Cómo dices '순례자 숙소'?", "El albergue"),
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
    "intro_title": "La ruta",
    "intro_subtitle": "Español en el Camino · Ep.2",
    "intro_ko": "순례길은 정했어요. 이제 어느 길로 갈까요? 프랑세스, 노르테, 포르투게스.",
    "outro_title": "Muy bien",
    "outro_subtitle": "Fin de la lección",
    "outro_ko": "3화에서는 세 친구가 출발 날짜를 정해요. 여러분은 어느 길이 좋나요? 댓글로 알려 주세요!",
    "diary_intro_background_path": "assets/images/camino_a2_ep02_la_ruta/scene_02_three_backs_over_map.png",
    "diary_outro_background_path": "assets/images/camino_a2_ep02_la_ruta/scene_08_cuaderno_closeup.png",
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
    "montage_title": "La ruta",
    "montage_subtitle": "el episodio completo",
    "montage_ko": "에피소드 전체 다시 보기",
    "montage_order_text": "El mapa  →  Las opciones  →  ¿Demasiado largo?  →  El Francés  →  ¡Buen Camino!",
    "thumbnail_title": "La ruta",
    "thumbnail_subtitle": "Español en el Camino · A2+",
    "thumbnail_ko": "El más largo, pero el más bonito",
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
_BASE = "assets/images/camino_a2_ep02_la_ruta"

STORY_SCENES = [
    # ------------------------------------------------------------------
    # Scene 1 — Cold-open  "El mapa sobre la mesa"  (atmosphere, no dialogue)
    # ------------------------------------------------------------------
    {
        "scene_id": 1,
        "title_es": "El mapa sobre la mesa",
        "title_ko": "테이블 위의 지도",
        "image_path": f"{_BASE}/scene_01_map_on_table.png",
        "ambient_sfx": "",
        "ambient_sfx_license": "CC0",
        "pause_s": 2.5,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Esa noche, en casa de Lucía, hay un gran mapa sobre la mesa.",
                "text_ko": "그날 밤, 루시아네 집, 테이블 위에 커다란 지도가 펼쳐져 있습니다.",
            },
        ],
    },
    # ------------------------------------------------------------------
    # Scene 2 — Title beat  "La ruta"
    # ------------------------------------------------------------------
    {
        "scene_id": 2,
        "title_es": "La ruta",
        "title_ko": "그 길",
        "image_path": f"{_BASE}/scene_02_three_backs_over_map.png",
        "ambient_sfx": "",
        "ambient_sfx_license": "CC0",
        "pause_s": 2.5,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Episodio dos: \"La ruta\". Otra vez están Lucía, Diego y Jin.",
                "text_ko": "2화 \"그 길\". 다시 루시아, 디에고, 진이 모였습니다.",
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Muy bien, ya lo decidimos. Ahora, ¿por dónde vamos?",
                "text_ko": "좋아, 이제 결정했잖아. 그럼 어느 길로 가지?",
            },
        ],
    },
    # ------------------------------------------------------------------
    # Scene 3 — Diego performs the expert  "Hay muchos caminos"
    # ------------------------------------------------------------------
    {
        "scene_id": 3,
        "title_es": "Hay muchos caminos",
        "title_ko": "길은 많아",
        "image_path": f"{_BASE}/scene_03_diego_points_at_routes.png",
        "ambient_sfx": "",
        "ambient_sfx_license": "CC0",
        "pause_s": 2.5,
        "lines": [
            {
                "kind": "dialogue",
                "speaker": "Diego",
                "text_es": "Mirad el mapa. Hay muchos caminos a Santiago.",
                "text_ko": "지도 좀 봐. 산티아고로 가는 길이 많아.",
            },
            {
                "kind": "dialogue",
                "speaker": "Diego",
                "text_es": "El Francés, el del Norte y el Portugués. Lo he leído en la guía.",
                "text_ko": "프랑세스, 노르테, 그리고 포르투게스. 가이드북에서 읽었어.",
            },
            {
                "kind": "dialogue",
                "speaker": "Diego",
                "text_es": "El Camino Francés es más largo que el Portugués.",
                "text_ko": "카미노 프랑세스가 포르투게스보다 더 길어.",
            },
            {
                "kind": "dialogue",
                "speaker": "Jin",
                "text_es": "¿Más largo que el Portugués? Entonces son más días.",
                "text_ko": "포르투게스보다 더 길다고? 그럼 날이 더 걸리잖아.",
            },
        ],
    },
    # ------------------------------------------------------------------
    # Scene 4 — Jin worries + the Norte is set aside  "¿Demasiado largo?"
    # ------------------------------------------------------------------
    {
        "scene_id": 4,
        "title_es": "¿Demasiado largo?",
        "title_ko": "너무 길지 않아?",
        "image_path": f"{_BASE}/scene_04_jin_worried_over_map.png",
        "ambient_sfx": "",
        "ambient_sfx_license": "CC0",
        "pause_s": 2.5,
        "lines": [
            {
                "kind": "dialogue",
                "speaker": "Jin",
                "text_es": "Más días… ¿y más caro también?",
                "text_ko": "날이 더 걸리면… 돈도 더 드는 거 아냐?",
            },
            {
                "kind": "dialogue",
                "speaker": "Jin",
                "text_es": "¿Y el del Norte? ¿No es más fácil?",
                "text_ko": "그럼 노르테는? 더 쉽지 않아?",
            },
            {
                "kind": "dialogue",
                "speaker": "Diego",
                "text_es": "El Norte es más duro que el Francés. Hay más subidas.",
                "text_ko": "노르테가 프랑세스보다 더 고돼. 오르막이 더 많거든.",
            },
            {
                "kind": "dialogue",
                "speaker": "Diego",
                "text_es": "Y en el Norte hay menos albergues que en el Francés.",
                "text_ko": "그리고 노르테에는 프랑세스보다 알베르게가 더 적어.",
            },
        ],
    },
    # ------------------------------------------------------------------
    # Scene 5 — Lucía's quiet pull  "Yo quiero el más largo"
    # ------------------------------------------------------------------
    {
        "scene_id": 5,
        "title_es": "Yo quiero el más largo",
        "title_ko": "난 제일 긴 길이 좋아",
        "image_path": f"{_BASE}/scene_05_lucia_over_map.png",
        "ambient_sfx": "",
        "ambient_sfx_license": "CC0",
        "pause_s": 2.5,
        "lines": [
            {
                "kind": "dialogue",
                "speaker": "Jin",
                "text_es": "Vale, el Norte no. ¿Entonces el Francés o el Portugués?",
                "text_ko": "좋아, 노르테는 아니고. 그럼 프랑세스 아니면 포르투게스야?",
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Para mí, el Francés es el más bonito de los dos.",
                "text_ko": "나한테는 둘 중에 프랑세스가 제일 예뻐.",
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Y quiero el más largo. Necesito más tiempo… para pensar.",
                "text_ko": "그리고 제일 긴 길로 가고 싶어. 생각할 시간이 더 필요하거든.",
            },
            {
                "kind": "dialogue",
                "speaker": "Diego",
                "text_es": "¿El más largo? Pues el Francés es más largo que el Portugués.",
                "text_ko": "제일 긴 거? 그럼 프랑세스가 포르투게스보다 더 길어.",
            },
        ],
    },
    # ------------------------------------------------------------------
    # Scene 6 — The route takes shape  "El más largo, pero el más bonito"
    # ------------------------------------------------------------------
    {
        "scene_id": 6,
        "title_es": "El más bonito",
        "title_ko": "제일 예뻐",
        "image_path": f"{_BASE}/scene_06_three_closer_over_map.png",
        "ambient_sfx": "",
        "ambient_sfx_license": "CC0",
        "pause_s": 2.5,
        "lines": [
            {
                "kind": "dialogue",
                "speaker": "Diego",
                "text_es": "El Francés es el más largo, pero el más bonito.",
                "text_ko": "프랑세스가 제일 길지만, 제일 아름다워.",
            },
            {
                "kind": "dialogue",
                "speaker": "Diego",
                "text_es": "Y es el más popular. Hay más peregrinos que en las otras rutas.",
                "text_ko": "그리고 제일 인기 많아. 다른 길보다 순례자가 더 많거든.",
            },
            {
                "kind": "dialogue",
                "speaker": "Jin",
                "text_es": "¿Más peregrinos? Entonces conocemos a más gente.",
                "text_ko": "순례자가 더 많다고? 그럼 사람도 더 많이 만나겠네.",
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Sí. Solos, da un poco de miedo. Con más gente, menos.",
                "text_ko": "응. 우리끼리만 가면 좀 무섭잖아. 사람이 많으면 덜하고.",
            },
        ],
    },
    # ------------------------------------------------------------------
    # Scene 7 — The decision  "Vamos por el Francés"
    # ------------------------------------------------------------------
    {
        "scene_id": 7,
        "title_es": "Vamos por el Francés",
        "title_ko": "프랑세스로 가자",
        "image_path": f"{_BASE}/scene_07_marking_route_decision.png",
        "ambient_sfx": "",
        "ambient_sfx_license": "CC0",
        "pause_s": 2.5,
        "lines": [
            {
                "kind": "dialogue",
                "speaker": "Diego",
                "text_es": "Entonces, ¿vamos por el Francés?",
                "text_ko": "그럼, 프랑세스로 가는 거야?",
            },
            {
                "kind": "dialogue",
                "speaker": "Jin",
                "text_es": "Por el Francés.",
                "text_ko": "프랑세스로.",
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Por el Francés. Es el más largo, pero también el más bonito.",
                "text_ko": "프랑세스로. 제일 길지만, 그래도 제일 아름다우니까.",
            },
            {
                "kind": "dialogue",
                "speaker": "Diego",
                "text_es": "Perfecto. Mañana marcamos la ruta en el mapa.",
                "text_ko": "좋아. 내일 지도에 길을 표시하자.",
            },
            {
                "kind": "dialogue",
                "speaker": "Jin",
                "text_es": "Vale… pero ¿cuándo salimos? Yo tengo pocos días libres.",
                "text_ko": "좋아… 근데 우리 언제 출발해? 나 휴가가 별로 없는데.",
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
                "text_es": "Esa noche, Jin escribe otra vez en su cuaderno.",
                "text_ko": "그날 밤, 진은 또 공책에 씁니다.",
            },
            {
                "kind": "dialogue",
                "speaker": "Jin",
                "text_es": "La frase del día es \"El Francés es el más largo, pero el más bonito\".",
                "text_ko": "오늘의 문장: \"프랑세스가 제일 길지만, 제일 아름다워\".",
            },
            {
                "kind": "dialogue",
                "speaker": "Jin",
                "text_es": "Con \"más… que\" y \"menos… que\", comparo cosas.",
                "text_ko": "\"más… que\"와 \"menos… que\"로 비교한다.",
            },
            {
                "kind": "dialogue",
                "speaker": "Jin",
                "text_es": "Y \"el más…\" es el superlativo: el más largo, el más bonito.",
                "text_ko": "그리고 \"el más…\"는 최상급이다: 제일 긴, 제일 아름다운.",
            },
            {
                "kind": "dialogue",
                "speaker": "Jin",
                "text_es": "Palabras nuevas: la ruta, el mapa, la guía, el albergue. ¡Buen Camino!",
                "text_ko": "새 단어: 길, 지도, 가이드북, 알베르게. 부엔 카미노!",
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
    debug_frame = {"x": 0, "y": 0, "w": 1920, "h": 1080}
    segments: list[dict] = [
        {
            "type": "intro",
            "text_es": (
                "Ya está decidido: van a hacer el Camino. Esta noche, con un mapa sobre "
                "la mesa, tienen que elegir la ruta. ¿El Francés, el del Norte o el "
                "Portugués? Fíjate en las comparaciones: \"más… que\", \"menos… que\" y "
                "\"el más…\"."
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
                "Muy bien. Practica en voz alta: \"El Francés es el más largo, pero el "
                "más bonito.\" Y tú, ¿qué camino prefieres? Escríbelo en los comentarios. "
                "En el próximo episodio, los tres eligen la fecha de salida. ¡Buen Camino!"
            ),
            "duration_s": 19.0,
        }
    )
    for seg in segments:
        seg.setdefault("frame", dict(debug_frame))
        if "text" not in seg:
            if seg.get("type") == "scene_header":
                seg["text"] = seg.get("title_es", "")
            elif seg.get("type") == "diary_line":
                speaker = seg.get("speaker", "")
                prefix = f"{speaker}: " if speaker else ""
                seg["text"] = f"{prefix}{seg.get('text_es', '')}"
            else:
                seg["text"] = seg.get("text_es", "")
    return segments


SEGMENTS = _build_diary_segments()


def _find_chapter_segment(scene_id: int) -> int:
    for idx, seg in enumerate(SEGMENTS):
        if seg.get("type") == "scene_header" and seg.get("scene_id") == scene_id:
            return idx + 1
    raise ValueError(f"missing scene_header for scene_id={scene_id}")


# Order (v1): the diary builder places the INTRO card first, so segment 1 is the
# title card at 0:00 ("La ruta") — NOT a bug. The map cold-open is Scene 1, which
# follows the title card; true cold-open-before-title would need a builder reorder and
# is a deferred enhancement. Chapters below are honest to the actual segment order.
CHAPTERS = [
    {"segment": 1,                         "title": "La ruta"},
    {"segment": _find_chapter_segment(1),  "title": "El mapa sobre la mesa"},
    {"segment": _find_chapter_segment(2),  "title": "Los tres, otra vez"},
    {"segment": _find_chapter_segment(3),  "title": "Hay muchos caminos"},
    {"segment": _find_chapter_segment(4),  "title": "¿Demasiado largo?"},
    {"segment": _find_chapter_segment(5),  "title": "El más largo"},
    {"segment": _find_chapter_segment(6),  "title": "El más bonito"},
    {"segment": _find_chapter_segment(7),  "title": "Vamos por el Francés"},
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
