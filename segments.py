"""Project segment loader."""

from __future__ import annotations

import importlib
import os

PROJECT = os.environ.get("PROJECT", "reunion_madrid")
_project = importlib.import_module(f"projects.{PROJECT}")

IMAGE_PATH = _project.IMAGE_PATH
DESCRIP_PATH = _project.DESCRIP_PATH
OUTPUT_NAME = _project.OUTPUT_NAME
SERIES = getattr(_project, "SERIES", "descripcion")
SERIES_TITLE = getattr(_project, "SERIES_TITLE", "Descripción de imagen B2")
EPISODE = getattr(_project, "EPISODE", 1)
LEVEL = getattr(_project, "LEVEL", "B2")
LANGUAGE = getattr(_project, "LANGUAGE", "es")
RENDER_VERSION = getattr(_project, "RENDER_VERSION", 1)
RENDER_TYPE = getattr(_project, "RENDER_TYPE", "kenburns")
THUMBNAIL_PATH = getattr(_project, "THUMBNAIL_PATH", None)
YOUTUBE_TITLE = getattr(_project, "YOUTUBE_TITLE", None)
DESCRIPTION_INTRO = getattr(_project, "DESCRIPTION_INTRO", "")
DESCRIPTION_OUTRO = getattr(_project, "DESCRIPTION_OUTRO", "")
CHAPTERS = getattr(_project, "CHAPTERS", None)
SEGMENTS = _project.SEGMENTS
DESIGN = _project.DESIGN
AUDIO = getattr(_project, "AUDIO", None)
PUBLIC_SLUG = getattr(_project, "PUBLIC_SLUG", "")
KOREAN_TEASER = getattr(_project, "KOREAN_TEASER", "")
PHRASES = getattr(_project, "PHRASES", None)
BLOCKS = getattr(_project, "BLOCKS", None)
MINI_QUIZ = getattr(_project, "MINI_QUIZ", None)
BASE_TAGS = getattr(_project, "BASE_TAGS", None)
EXTRA_TAGS = getattr(_project, "EXTRA_TAGS", None)
BASE_HASHTAGS = getattr(_project, "BASE_HASHTAGS", None)
EXTRA_HASHTAGS = getattr(_project, "EXTRA_HASHTAGS", None)
STORY_SCENES = getattr(_project, "STORY_SCENES", None)
SFX_MANIFEST = getattr(_project, "SFX_MANIFEST", None)
SEGMENT_SFX = getattr(_project, "SEGMENT_SFX", None)

