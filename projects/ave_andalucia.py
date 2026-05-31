"""Segment data for the AVE Andalucia Spanish-learning video."""

from __future__ import annotations

IMAGE_PATH = "images/ave-andalucia.png"
DESCRIP_PATH = "3rdsc/descrip.md"
OUTPUT_NAME = "ave-andalucia"
SERIES = "descripcion"
SERIES_TITLE = "Descripción de imagen B2"
EPISODE = 3
LEVEL = "B2"
LANGUAGE = "es"
RENDER_VERSION = 1
YOUTUBE_TITLE = "En el AVE por Andalucía | Descripción de imagen B2 · Ep.3"
DESCRIPTION_INTRO = (
    "Práctica de descripción de imagen para estudiantes de español B2. "
    "Escucha la escena del AVE, repite las hipótesis con quizás y observa cómo se describen tres viajeros."
)
DESCRIPTION_OUTRO = (
    "Vuelve a ver el video y describe la escena con tus propias palabras. "
    "Después, intenta reformular cada quizás + subjuntivo con tal vez o parecer + infinitivo."
)
CHAPTERS = [
    {"segment": 1, "title": "Vocabulario clave"},
    {"segment": 3, "title": "El paisaje andaluz"},
    {"segment": 7, "title": "La mujer de la izquierda"},
    {"segment": 11, "title": "La mujer del pañuelo"},
    {"segment": 15, "title": "El hombre de la chaqueta verde"},
    {"segment": 19, "title": "Cierre y repaso"},
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
        "text": "Antes de empezar, observa el AVE: un vagón luminoso, una ventanilla enorme y tres amigos conversando durante el viaje.",
        "frame": {"x": 0, "y": 0, "w": 1280, "h": 720},
        "zoom": {"start": 1.00, "end": 1.00},
    },
    {
        "text": "Mira también el paisaje andaluz: colinas doradas, olivares, sierra azulada y mucha luz de final de verano.",
        "frame": {"x": 140, "y": 0, "w": 640, "h": 360},
        "zoom": {"start": 1.00, "end": 1.04},
    },
    {
        "text": "La escena tiene lugar dentro de un vagón del AVE, el tren de alta velocidad español,",
        "frame": {"x": 0, "y": 0, "w": 1280, "h": 720},
        "zoom": {"start": 1.00, "end": 1.03},
    },
    {
        "text": "que parece estar atravesando el campo andaluz.",
        "frame": {"x": 140, "y": 0, "w": 640, "h": 360},
        "zoom": {"start": 1.03, "end": 1.00},
    },
    {
        "text": "A través de la ventanilla se ve un paisaje espectacular: colinas doradas,",
        "frame": {"x": 120, "y": 20, "w": 640, "h": 360},
        "zoom": {"start": 1.00, "end": 1.04},
    },
    {
        "text": "olivares que se extienden hasta el horizonte, y al fondo, una sierra azulada bajo un cielo despejado.",
        "frame": {"x": 120, "y": 0, "w": 720, "h": 405},
        "zoom": {"start": 1.04, "end": 1.00},
    },
    {
        "text": "Es un día de finales de verano, soleado y luminoso.",
        "frame": {"x": 120, "y": 0, "w": 720, "h": 405},
        "zoom": {"start": 1.00, "end": 1.03},
    },
    {
        "text": "En el compartimento están viajando tres pasajeros, dos mujeres y un hombre, que parecen ser amigos de toda la vida.",
        "frame": {"x": 0, "y": 0, "w": 1280, "h": 720},
        "zoom": {"start": 1.00, "end": 1.03},
    },
    {
        "text": "Están manteniendo una conversación animada y se nota que se llevan muy bien.",
        "frame": {"x": 410, "y": 90, "w": 870, "h": 489},
        "zoom": {"start": 1.00, "end": 1.04},
    },
    {
        "text": "A la izquierda, de espaldas a la cámara, está una mujer joven de pelo largo y oscuro.",
        "frame": {"x": 0, "y": 80, "w": 480, "h": 270},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "Está gesticulando con las manos mientras cuenta algo —",
        "frame": {"x": 180, "y": 390, "w": 540, "h": 304},
        "zoom": {"start": 1.00, "end": 1.06},
    },
    {
        "text": "quizás esté narrando una anécdota divertida del viaje, o tal vez esté contando un chisme.",
        "frame": {"x": 180, "y": 390, "w": 540, "h": 304},
        "zoom": {"start": 1.06, "end": 1.02},
    },
    {
        "text": "Por su postura, se ve que es una persona expresiva y comunicativa.",
        "frame": {"x": 0, "y": 80, "w": 520, "h": 293},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "Frente a ella, están sentados sus dos compañeros.",
        "frame": {"x": 520, "y": 90, "w": 760, "h": 428},
        "zoom": {"start": 1.00, "end": 1.04},
    },
    {
        "text": "La mujer del medio lleva una camiseta blanca y un pañuelo de colores cálidos — naranja, rojo y marrón — que le da un toque bohemio.",
        "frame": {"x": 500, "y": 190, "w": 540, "h": 304},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "Está sonriendo abiertamente, con los ojos entornados, lo que sugiere que la historia es realmente graciosa o entrañable. Es una sonrisa genuina.",
        "frame": {"x": 520, "y": 110, "w": 520, "h": 293},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "A su lado, el hombre, de pelo castaño ondulado y barba de pocos días, lleva una chaqueta verde militar sobre una camiseta gris.",
        "frame": {"x": 740, "y": 90, "w": 540, "h": 304},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "También sonríe, aunque de forma más contenida, mirando con afecto a sus compañeras.",
        "frame": {"x": 780, "y": 60, "w": 500, "h": 281},
        "zoom": {"start": 1.05, "end": 1.00},
    },
    {
        "text": "Parece estar muy cómodo en su asiento.",
        "frame": {"x": 760, "y": 120, "w": 520, "h": 293},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "El ambiente del vagón es acogedor: la luz natural entra por la ventanilla, hace buen tiempo fuera, y los tres viajeros están disfrutando del trayecto tanto como del paisaje.",
        "frame": {"x": 0, "y": 0, "w": 1280, "h": 720},
        "zoom": {"start": 1.00, "end": 1.03},
    },
    {
        "text": "Aunque el viaje en AVE de Madrid a Sevilla es largo — unas dos horas y media — para ellos parece estar pasando volando.",
        "frame": {"x": 0, "y": 0, "w": 1280, "h": 720},
        "zoom": {"start": 1.03, "end": 1.00},
    },
    {
        "text": "Recuerda: quizás y tal vez con subjuntivo expresan hipótesis; parecer + infinitivo sirve para describir una impresión.",
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
