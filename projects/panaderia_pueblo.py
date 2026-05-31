"""Segment data for the Panaderia Pueblo Spanish-learning video."""

from __future__ import annotations

IMAGE_PATH = "images/panaderia-pueblo.png"
DESCRIP_PATH = "5thsc/descrip.md"
OUTPUT_NAME = "panaderia-pueblo"
SERIES = "descripcion"
SERIES_TITLE = "Descripción de imagen B2"
EPISODE = 5
LEVEL = "B2"
LANGUAGE = "es"
RENDER_VERSION = 1
YOUTUBE_TITLE = "Charla en la panadería | Descripción de imagen B2 · Ep.5"
DESCRIPTION_INTRO = (
    "Práctica de descripción de imagen para estudiantes de español B2. "
    "Observa una panadería de pueblo y aprende a expresar probabilidad "
    "con deber de + infinitivo y puede que + subjuntivo."
)
DESCRIPTION_OUTRO = (
    "Vuelve a ver el video y describe la escena con tus propias palabras. "
    "Después, reformula dos hipótesis con deber de + infinitivo "
    "y puede que + subjuntivo."
)
KOREAN_TEASER = (
    "한국어 티저: 스페인 마을 빵집 앞에서 벌어지는 짧은 대화를 보며 "
    "가능성과 추측을 자연스럽게 말하는 B2 표현을 연습합니다."
)
CHAPTERS = [
    {"segment": 1, "title": "Vocabulario clave"},
    {"segment": 3, "title": "La calle del pueblo"},
    {"segment": 4, "title": "El panadero y el cliente"},
    {"segment": 11, "title": "La señora del banco"},
    {"segment": 14, "title": "El escaparate"},
    {"segment": 16, "title": "La vida de barrio"},
    {"segment": 19, "title": "Cierre y repaso (probabilidad)"},
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
        "text": "Antes de empezar, observa la panadería: una calle estrecha, dos vecinos charlando y el olor a pan recién hecho.",
        "frame": {"x": 0, "y": 0, "w": 1280, "h": 720},
        "zoom": {"start": 1.00, "end": 1.00},
    },
    {
        "text": "La escena tiene lugar en una calle estrecha de un pueblo o barrio antiguo de España, con esos edificios de piedra dorada típicos del Mediterráneo.",
        "frame": {"x": 0, "y": 0, "w": 1280, "h": 720},
        "zoom": {"start": 1.00, "end": 1.03},
    },
    {
        "text": "Es una mañana tranquila — probablemente de fin de semana — cuando la luz del sol se cuela suavemente entre las casas y los vecinos salen a hacer sus recados.",
        "frame": {"x": 0, "y": 0, "w": 800, "h": 450},
        "zoom": {"start": 1.00, "end": 1.04},
    },
    {
        "text": "En primer plano, dos hombres están manteniendo una conversación animada en la entrada de una panadería de toda la vida.",
        "frame": {"x": 340, "y": 0, "w": 840, "h": 473},
        "zoom": {"start": 1.00, "end": 1.04},
    },
    {
        "text": "El de la derecha es el panadero. Lleva una camisa blanca arremangada y un delantal de lino color crudo.",
        "frame": {"x": 665, "y": 25, "w": 540, "h": 304},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "Sostiene en las manos una hogaza de pan recién horneada, todavía dorada y crujiente.",
        "frame": {"x": 650, "y": 215, "w": 540, "h": 304},
        "zoom": {"start": 1.00, "end": 1.06},
    },
    {
        "text": "Está sonriendo abiertamente, con una risa franca, lo que sugiere que conoce muy bien al cliente.",
        "frame": {"x": 670, "y": 25, "w": 540, "h": 304},
        "zoom": {"start": 1.05, "end": 1.00},
    },
    {
        "text": "Frente a él, apoyado contra la pared de piedra, está un hombre de pelo rizado y barba corta, con una chaqueta verde oliva y vaqueros azules.",
        "frame": {"x": 320, "y": 20, "w": 580, "h": 326},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "Lleva una bolsa de tela colgada del hombro y parece haber pasado por la panadería como parte de su rutina mañanera.",
        "frame": {"x": 250, "y": 195, "w": 560, "h": 315},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "Por la postura relajada y la sonrisa cómplice, se nota que no es la primera vez que charlan así — quizás se conozcan desde hace años.",
        "frame": {"x": 340, "y": 20, "w": 760, "h": 428},
        "zoom": {"start": 1.04, "end": 1.00},
    },
    {
        "text": "A lo lejos, sentada en un banco de madera, una señora mayor lee tranquilamente el periódico mientras espera a alguien o simplemente disfruta del solecito.",
        "frame": {"x": 0, "y": 190, "w": 600, "h": 338},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "Lleva una chaqueta beige y pantalones oscuros.",
        "frame": {"x": 20, "y": 255, "w": 520, "h": 293},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "Su presencia añade ternura a la escena, como si formara parte del paisaje cotidiano del barrio.",
        "frame": {"x": 0, "y": 140, "w": 720, "h": 405},
        "zoom": {"start": 1.05, "end": 1.00},
    },
    {
        "text": "En el escaparate de la panadería, a la derecha, se ven todo tipo de panes artesanos:",
        "frame": {"x": 800, "y": 30, "w": 480, "h": 270},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "chapatas, hogazas, panes de centeno y algunos panecillos. El olorcito a pan fresco debe de impregnar toda la calle.",
        "frame": {"x": 800, "y": 165, "w": 480, "h": 270},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "Es una escena cotidiana, pero llena de calidez — ese tipo de momento que define la vida de un pueblo español,",
        "frame": {"x": 0, "y": 0, "w": 1280, "h": 720},
        "zoom": {"start": 1.00, "end": 1.03},
    },
    {
        "text": "donde el panadero conoce a sus clientes por el nombre",
        "frame": {"x": 625, "y": 25, "w": 600, "h": 338},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "y donde una pequeña charla matutina puede convertirse en una tertulia de media hora.",
        "frame": {"x": 340, "y": 40, "w": 760, "h": 428},
        "zoom": {"start": 1.04, "end": 1.00},
    },
    {
        "text": "Recuerda: deber de + infinitivo expresa probabilidad. El pan fresco debe de impregnar toda la calle.",
        "frame": {"x": 650, "y": 215, "w": 540, "h": 304},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "También puedes usar puede que + subjuntivo: puede que se conozcan desde hace años. Y ordena la imagen con en primer plano, a lo lejos y a la derecha.",
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
