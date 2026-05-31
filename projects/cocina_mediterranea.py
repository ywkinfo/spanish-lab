"""Segment data for the Cocina Mediterranea Spanish-learning video."""

from __future__ import annotations

IMAGE_PATH = "images/cocina-mediterranea.png"
DESCRIP_PATH = "4thsc/descrip.md"
OUTPUT_NAME = "cocina-mediterranea"
SERIES = "descripcion"
SERIES_TITLE = "Descripción de imagen B2"
EPISODE = 4
LEVEL = "B2"
LANGUAGE = "es"
RENDER_VERSION = 1
YOUTUBE_TITLE = "En la cocina mediterránea | Descripción de imagen B2 · Ep.4"
DESCRIPTION_INTRO = (
    "Práctica de descripción de imagen para estudiantes de español B2. "
    "Observa una cocina andaluza en una mañana de sábado y aprende a describir "
    "acciones en curso con estar + gerundio."
)
DESCRIPTION_OUTRO = (
    "Vuelve a ver el video y describe la escena con tus propias palabras. "
    "Después, intenta reformular cada acción con estar + gerundio "
    "(está picando, está removiendo, están preparando…)."
)
CHAPTERS = [
    {"segment": 1, "title": "Vocabulario clave"},
    {"segment": 2, "title": "La cocina mediterránea"},
    {"segment": 6, "title": "Los dos hermanos"},
    {"segment": 9, "title": "El chico picando zanahorias"},
    {"segment": 12, "title": "La chica removiendo la olla"},
    {"segment": 14, "title": "Los ingredientes"},
    {"segment": 19, "title": "Cierre y repaso (estar + gerundio)"},
]

DESIGN = {
    "output_size": (1280, 720),
    "font_path": "/System/Library/Fonts/Optima.ttc",
    "font_index": 0,
    "font_path_emph": "/System/Library/Fonts/Optima.ttc",
    "font_index_emph": 3,
    "font_size": 36,
    "min_font_size": 26,
    "letter_spacing": 0.5,
    "bar_style": "gradient",
    "bar_top_color": (24, 18, 12, 200),
    "bar_bottom_color": (8, 6, 4, 220),
    "bar_corner_radius": 0,
    "bar_accent_color": (244, 162, 97, 255),
    "bar_accent_height": 2,
    "bar_padding_x": 36,
    "bar_padding_y": 22,
    "bar_bottom_margin_ratio": 0.07,
    "text_color": (255, 252, 246, 255),
    "text_shadow_color": (0, 0, 0, 200),
    "text_shadow_offset": (0, 2),
    "text_shadow_blur": 3,
    "easing": "ease_in_out_cubic",
    "transition_s": 0.8,
    "fade_s": 0.4,
    "idle_zoom_drift": 0.012,
    "grade": {
        "saturation": 1.10,
        "contrast": 1.05,
        "warmth": 6,
    },
}

SEGMENTS = [
    {
        "text": "Antes de empezar, observa la escena: una cocina mediterránea, dos hermanos cocinando juntos y muchos ingredientes frescos sobre la encimera.",
        "frame": {"x": 0, "y": 0, "w": 1280, "h": 720},
        "zoom": {"start": 1.00, "end": 1.00},
    },
    {
        "text": "La imagen nos transporta a una cocina mediterránea tradicional, posiblemente de una casa de pueblo en Andalucía o Valencia.",
        "frame": {"x": 0, "y": 0, "w": 1280, "h": 720},
        "zoom": {"start": 1.00, "end": 1.03},
    },
    {
        "text": "Los azulejos azules, blancos y amarillos cubren las paredes con motivos geométricos típicos de la cerámica española,",
        "frame": {"x": 130, "y": 0, "w": 720, "h": 405},
        "zoom": {"start": 1.00, "end": 1.04},
    },
    {
        "text": "y el suelo está cubierto de baldosas de terracota que dan al espacio un aire cálido y rústico.",
        "frame": {"x": 160, "y": 180, "w": 960, "h": 540},
        "zoom": {"start": 1.04, "end": 1.00},
    },
    {
        "text": "La luz suave que entra por la ventana sugiere que es media mañana de un sábado tranquilo en familia.",
        "frame": {"x": 830, "y": 0, "w": 450, "h": 253},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "En el centro de la escena, dos hermanos adolescentes — un chico y una chica — están preparando la comida juntos.",
        "frame": {"x": 0, "y": 0, "w": 1280, "h": 720},
        "zoom": {"start": 1.00, "end": 1.03},
    },
    {
        "text": "Parece que se están divirtiendo trabajando en equipo.",
        "frame": {"x": 0, "y": 0, "w": 1280, "h": 720},
        "zoom": {"start": 1.03, "end": 1.00},
    },
    {
        "text": "El chico, a la izquierda, lleva una camiseta azul marino",
        "frame": {"x": 160, "y": 30, "w": 540, "h": 304},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "y está concentrado picando zanahorias sobre una tabla de cortar de madera.",
        "frame": {"x": 350, "y": 416, "w": 540, "h": 304},
        "zoom": {"start": 1.00, "end": 1.06},
    },
    {
        "text": "Sostiene un cuchillo con cuidado y, por su expresión seria pero serena, se nota que es un chico responsable y aplicado.",
        "frame": {"x": 160, "y": 30, "w": 540, "h": 304},
        "zoom": {"start": 1.05, "end": 1.00},
    },
    {
        "text": "A su lado, la chica, con el pelo recogido en un moño alto y una blusa blanca de aire vintage,",
        "frame": {"x": 580, "y": 50, "w": 540, "h": 304},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "está removiendo algo dentro de una olla de acero.",
        "frame": {"x": 670, "y": 360, "w": 480, "h": 270},
        "zoom": {"start": 1.00, "end": 1.06},
    },
    {
        "text": "Sonríe ligeramente — quizás esté oliendo el aroma de un guiso casero, o tal vez esté pensando en cómo va a quedar el plato.",
        "frame": {"x": 580, "y": 50, "w": 540, "h": 304},
        "zoom": {"start": 1.05, "end": 1.00},
    },
    {
        "text": "Sobre la encimera hay un festín de ingredientes: pimientos rojos y verdes, patatas sin pelar, pepinos,",
        "frame": {"x": 0, "y": 416, "w": 540, "h": 304},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "un manojo de perejil fresco, una cesta con cebollas y tomates, y un cuenco de barro lleno de sal gruesa.",
        "frame": {"x": 740, "y": 400, "w": 540, "h": 304},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "Todo sugiere que están preparando algo muy casero — tal vez un sofrito, una menestra de verduras, o incluso un puchero.",
        "frame": {"x": 160, "y": 180, "w": 960, "h": 540},
        "zoom": {"start": 1.04, "end": 1.00},
    },
    {
        "text": "El ambiente es acogedor y familiar.",
        "frame": {"x": 0, "y": 0, "w": 1280, "h": 720},
        "zoom": {"start": 1.00, "end": 1.02},
    },
    {
        "text": "Cocinar juntos, en silencio cómplice, en una cocina llena de tradición — eso es la esencia de la vida mediterránea.",
        "frame": {"x": 0, "y": 0, "w": 1280, "h": 720},
        "zoom": {"start": 1.02, "end": 1.00},
    },
    {
        "text": "Recuerda: estar + gerundio expresa una acción en curso, algo que está ocurriendo en este momento —",
        "frame": {"x": 0, "y": 0, "w": 1280, "h": 720},
        "zoom": {"start": 1.00, "end": 1.02},
    },
    {
        "text": "está picando, está removiendo, están preparando.",
        "frame": {"x": 0, "y": 0, "w": 1280, "h": 720},
        "zoom": {"start": 1.02, "end": 1.00},
    },
]

AUDIO = {
    "voice": "Mónica",
    "rate_wpm": 175,
    "lead_padding_s": 0.35,
    "tail_padding_s": 0.55,
    "min_duration_s": 4.0,
    "readability_floor_ratio": 0.9,
    "bgm_path": "assets/audio/bgm.mp3",
    "bgm_volume_db": -16.0,
    "narration_volume_db": 0.0,
    "ducking": True,
    "ducking_threshold": 0.05,
    "ducking_ratio": 8,
    "ducking_attack_ms": 120,
    "ducking_release_ms": 600,
    "fade_in_s": 1.5,
    "fade_out_s": 2.0,
    "audio_codec": "aac",
    "audio_bitrate_kbps": 192,
    "sample_rate_hz": 44100,
}
