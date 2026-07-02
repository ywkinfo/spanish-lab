"""Orchestrator for the diary render pipeline."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

from build.camera import output_size_for_design
from build.audio import build_narration_wav, mix_with_bgm, mux_into_video, synthesize_segments, write_manifest, mix_sfx_layer
from build.diary_timeline import build_diary_timings, DiaryTiming
from build.segment_adapter import RENDER_TYPE_DIARY, narration_text
from segments import AUDIO, DESIGN, OUTPUT_NAME, SEGMENTS, STORY_SCENES, SFX_MANIFEST, SEGMENT_SFX

OUTPUT_DIR = Path("output")
ROOT = Path(__file__).resolve().parents[1]

COLOR_BLOCKS = DESIGN.get("color_blocks", {
    "coral": (224, 91, 76),
    "amber": (230, 158, 62),
    "teal": (44, 150, 142),
    "blue": (70, 120, 196),
    "green": (92, 148, 86),
    "neutral": (42, 48, 57),
})


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render the Spanish-learning diary video.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--preview", action="store_true", help="Render a fast 12 fps preview.")
    mode.add_argument("--final", action="store_true", help="Render the final 30 fps MP4.")
    return parser.parse_args()


def get_scene_by_id(scene_id: int | None) -> dict | None:
    if scene_id is None or STORY_SCENES is None:
        return None
    for scene in STORY_SCENES:
        if scene.get("scene_id") == scene_id:
            return scene
    return None


def get_scene_color(scene_id: int | None) -> tuple[int, int, int]:
    if not scene_id:
        return COLOR_BLOCKS["neutral"]
    colors = ["coral", "amber", "teal", "blue", "green"]
    color_name = colors[(scene_id - 1) % len(colors)]
    return COLOR_BLOCKS.get(color_name, COLOR_BLOCKS["neutral"])


def _load_font(font_path: str, size: int, index: int = 0) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    from build.subtitles import find_font_path
    path = find_font_path(font_path)
    if path:
        return ImageFont.truetype(path, size=size, index=index)
    try:
        return ImageFont.load_default(size=size)
    except TypeError:
        return ImageFont.load_default()


def wrap_text(text: str, font: ImageFont.ImageFont, max_width: int, draw: ImageDraw.ImageDraw) -> list[str]:
    from build.subtitles import wrap_text_pixels
    return wrap_text_pixels(text, font, max_width, draw, stroke_width=0)


def render_diary_montage(scenes: list[dict], design: dict) -> Image.Image:
    """Render a 4x2 grid montage of all 8 scene illustrations."""
    width, height = output_size_for_design(design)
    bg_color = design.get("background_color", (248, 247, 242))
    text_color = design.get("text_color", (31, 35, 40))
    muted_text_color = design.get("muted_text_color", (96, 101, 109))
    scene_color = COLOR_BLOCKS.get("teal", (44, 150, 142))
    
    font_bold_path = design.get("font_path", "assets/fonts/NotoSansKR-Bold.ttf")
    font_regular_path = design.get("font_path_ko", "assets/fonts/NotoSansKR-Regular.ttf")
    font_index = int(design.get("font_index", 0))
    font_index_ko = int(design.get("font_index_ko", 0))
    
    image = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(image)
    
    # 1. Header
    title_font = _load_font(font_bold_path, 48, font_index)
    sub_font = _load_font(font_regular_path, 24, font_index_ko)
    
    title_text = str(design.get("montage_title", design.get("intro_title", "Un día de Lucía")))
    subtitle_text = str(design.get("montage_subtitle", "el día entero"))
    ko_text = str(design.get("montage_ko", design.get("intro_ko", "")))
    order_text = str(
        design.get(
            "montage_order_text",
            "Primero (먼저)  ➔  Luego (그다음)  ➔  Después (그 후)  ➔  Al final (마지막에)",
        )
    )
    heading_text = f"{title_text} — {subtitle_text}" if subtitle_text else title_text

    draw.text((120, 76), heading_text, font=title_font, fill=text_color)
    header_y = 142
    if ko_text:
        draw.text((120, header_y), ko_text, font=sub_font, fill=muted_text_color)
        header_y += 34
    draw.text((120, header_y), order_text, font=sub_font, fill=scene_color)
    draw.line((120, header_y + 50, width - 120, header_y + 50), fill=(220, 218, 210), width=2)
    
    # 2. Grid Constants for 1080p
    col_width = 370
    col_height = 208 # 16:9
    gap_x = 50
    gap_y = 110
    start_x = 120
    start_y = header_y + 95
    
    card_font_num = _load_font(font_bold_path, 22, font_index)
    card_font_title = _load_font(font_regular_path, 18, font_index_ko)
    
    for i, scene in enumerate(scenes[:8]):
        col = i % 4
        row = i // 4
        x = start_x + col * (col_width + gap_x)
        y = start_y + row * (col_height + gap_y)
        
        # Load and crop scene illustration
        img_path = ROOT / scene.get("image_path", "")
        if img_path.exists():
            with Image.open(img_path) as s_img:
                sw, sh = s_img.size
                aspect = 16.0 / 9.0
                if sw / sh > aspect:
                    cw = sh * aspect
                    ch = sh
                    cx = (sw - cw) / 2
                    cy = 0
                else:
                    cw = sw
                    ch = cw / aspect
                    cx = 0
                    y_ratio = design.get("diary_crop_y_ratio", 0.5) if design else 0.5
                    cy = (sh - ch) * y_ratio
                
                cropped = s_img.crop((int(cx), int(cy), int(cx + cw), int(cy + ch)))
                resized = cropped.resize((col_width, col_height), Image.Resampling.LANCZOS)
                
                mask = Image.new("L", (col_width, col_height), 0)
                m_draw = ImageDraw.Draw(mask)
                m_draw.rounded_rectangle((0, 0, col_width, col_height), radius=14, fill=255)
                
                image.paste(resized, (x, y), mask)
                draw.rounded_rectangle((x, y, x + col_width, y + col_height), radius=14, outline=(210, 208, 198), width=2)
        else:
            draw.rounded_rectangle((x, y, x + col_width, y + col_height), radius=14, fill=(235, 233, 225), outline=(210, 208, 198), width=2)
            ph_text = f"[Escena {i+1}]"
            ph_w = draw.textbbox((0, 0), ph_text, font=card_font_num)[2]
            draw.text((x + (col_width - ph_w) // 2, y + (col_height - 30) // 2), ph_text, font=card_font_num, fill=muted_text_color)
            
        num_str = f"Escena {i+1}"
        title_str = scene.get("title_ko", "")
        
        draw.text((x + 10, y + col_height + 12), num_str, font=card_font_num, fill=text_color)
        draw.text((x + 10, y + col_height + 42), title_str, font=card_font_title, fill=muted_text_color)
        
    return image


def render_diary_background(segment: dict, timing: DiaryTiming, design: dict) -> Image.Image:
    """Render background (source resolution if it is a photo, viewport size if fallback/card)."""
    width, height = output_size_for_design(design)
    seg_type = timing.type
    scene_id = timing.scene_id
    scene_color = get_scene_color(scene_id)
    bg_color = design.get("background_color", (248, 247, 242))
    text_color = design.get("text_color", (31, 35, 40))
    muted_text_color = design.get("muted_text_color", (96, 101, 109))
    
    font_bold_path = design.get("font_path", "assets/fonts/NotoSansKR-Bold.ttf")
    font_regular_path = design.get("font_path_ko", "assets/fonts/NotoSansKR-Regular.ttf")
    font_index = int(design.get("font_index", 0))
    font_index_ko = int(design.get("font_index_ko", 0))

    if seg_type == "montage":
        return render_diary_montage(STORY_SCENES, design)

    elif seg_type == "intro" or seg_type == "outro":
        default_illustration_path = "assets/story/lucia_scene_01_morning.png" if seg_type == "intro" else "assets/story/lucia_scene_08_diary.png"
        illustration_path = design.get("diary_intro_background_path", default_illustration_path) if seg_type == "intro" else design.get("diary_outro_background_path", default_illustration_path)
        img_path = Path(illustration_path)
        
        if img_path.exists():
            with Image.open(img_path) as s_img:
                sw, sh = s_img.size
                aspect = 16.0 / 9.0
                if sw / sh > aspect:
                    cw = sh * aspect
                    ch = sh
                    cx = (sw - cw) / 2
                    cy = 0
                else:
                    cw = sw
                    ch = cw / aspect
                    cx = 0
                    y_ratio = design.get("diary_crop_y_ratio", 0.5) if design else 0.5
                    cy = (sh - ch) * y_ratio
                cropped = s_img.crop((int(cx), int(cy), int(cx + cw), int(cy + ch)))
                resized = cropped.resize((width, height), Image.Resampling.LANCZOS)
                # Keep the episode image visible. Previous intro/outro frames blended
                # the art into the paper background too strongly, so the approved
                # image direction looked almost unreflected in the rendered video.
                image_alpha = float(design.get("diary_intro_image_blend_alpha", 0.38))
                image = Image.blend(resized, Image.new("RGB", (width, height), bg_color), alpha=image_alpha)
        else:
            image = Image.new("RGB", (width, height), bg_color)
            
        draw = ImageDraw.Draw(image)
        title_font = _load_font(font_bold_path, int(design.get("diary_intro_title_font_size", 72)), font_index)
        sub_font = _load_font(font_regular_path, int(design.get("diary_intro_subtitle_font_size", 36)), font_index_ko)
        body_font = _load_font(font_regular_path, int(design.get("diary_intro_body_font_size", 42)), font_index_ko)
        ko_font = _load_font(font_regular_path, int(design.get("diary_intro_ko_font_size", 44)), font_index_ko)
        
        title_text = design.get("intro_title", "Un día de Lucía") if seg_type == "intro" else design.get("outro_title", "Muy bien")
        sub_text = design.get("intro_subtitle", "Español A1 · Historia") if seg_type == "intro" else design.get("outro_subtitle", "Fin de la lección")
        body_text = timing.text_es
        ko_text = design.get("intro_ko", "") if seg_type == "intro" else design.get("outro_ko", "")
        layout = str(design.get("diary_intro_layout", "left"))

        if layout == "center_card":
            card_w = int(design.get("diary_intro_card_w", width * 0.74))
            card_h = int(design.get("diary_intro_card_h", height * 0.66))
            card_x = (width - card_w) // 2
            card_y = (height - card_h) // 2
            overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
            odraw = ImageDraw.Draw(overlay)
            odraw.rounded_rectangle(
                (card_x, card_y, card_x + card_w, card_y + card_h),
                radius=44,
                fill=tuple(design.get("diary_intro_card_fill", (255, 250, 239, 140))),
                outline=tuple(design.get("diary_intro_card_outline", (255, 255, 255, 120))),
                width=3,
            )
            image = Image.alpha_composite(image.convert("RGBA"), overlay).convert("RGB")
            draw = ImageDraw.Draw(image)

            center_x = width // 2
            y = card_y + int(design.get("diary_intro_card_pad_top", 72))
            for text, font, fill, gap in [
                (title_text, title_font, text_color, int(design.get("diary_intro_title_gap", 34))),
                (sub_text, sub_font, COLOR_BLOCKS["neutral"], int(design.get("diary_intro_subtitle_gap", 44))),
            ]:
                bbox = draw.textbbox((0, 0), text, font=font)
                draw.text((center_x - (bbox[2] - bbox[0]) // 2, y), text, font=font, fill=fill)
                y += (bbox[3] - bbox[1]) + gap

            line_y = y - 14
            draw.line((card_x + 150, line_y, card_x + card_w - 150, line_y), fill=(200, 195, 184), width=3)
            y += int(design.get("diary_intro_body_top_gap", 34))

            lines = wrap_text(body_text, body_font, card_w - 250, draw)
            body_step = int(design.get("diary_intro_body_line_step", 70))
            for line in lines:
                bbox = draw.textbbox((0, 0), line, font=body_font)
                draw.text((center_x - (bbox[2] - bbox[0]) // 2, y), line, font=body_font, fill=text_color)
                y += body_step

            if ko_text:
                y += int(design.get("diary_intro_ko_top_gap", 24))
                ko_lines = wrap_text(str(ko_text), ko_font, card_w - 250, draw)
                ko_step = int(design.get("diary_intro_ko_line_step", 56))
                for line in ko_lines:
                    bbox = draw.textbbox((0, 0), line, font=ko_font)
                    draw.text((center_x - (bbox[2] - bbox[0]) // 2, y), line, font=ko_font, fill=muted_text_color)
                    y += ko_step
        else:
            draw.rectangle((0, 0, 36, height), fill=COLOR_BLOCKS["neutral"])
            draw.text((120, 150), title_text, font=title_font, fill=text_color)
            draw.text((120, 248), sub_text, font=sub_font, fill=COLOR_BLOCKS["neutral"])
            draw.line((120, 315, width - 120, 315), fill=(220, 218, 210), width=3)
            lines = wrap_text(body_text, body_font, width - 240, draw)
            y = 375
            for line in lines:
                draw.text((120, y), line, font=body_font, fill=text_color)
                y += 68
        return image
        
    elif seg_type == "scene_header":
        scene = get_scene_by_id(scene_id)
        illustration_path = scene.get("image_path", "") if scene else ""
        img_path = Path(illustration_path) if illustration_path else None
        
        if img_path and img_path.exists():
            with Image.open(img_path) as s_img:
                sw, sh = s_img.size
                aspect = 16.0 / 9.0
                if sw / sh > aspect:
                    cw = sh * aspect
                    ch = sh
                    cx = (sw - cw) / 2
                    cy = 0
                else:
                    cw = sw
                    ch = cw / aspect
                    cx = 0
                    y_ratio = design.get("diary_crop_y_ratio", 0.5) if design else 0.5
                    cy = (sh - ch) * y_ratio
                cropped = s_img.crop((int(cx), int(cy), int(cx + cw), int(cy + ch)))
                resized = cropped.resize((width, height), Image.Resampling.LANCZOS)
                blurred = resized.filter(ImageFilter.GaussianBlur(15))
                image = Image.blend(blurred, Image.new("RGB", (width, height), scene_color), alpha=0.72)
        else:
            image = Image.new("RGB", (width, height), scene_color)
            
        draw = ImageDraw.Draw(image)
        
        large_font = _load_font(font_bold_path, 54, font_index)
        huge_font = _load_font(font_bold_path, 96, font_index)
        ko_title_font = _load_font(font_regular_path, 54, font_index_ko)
        
        scene_num_str = f"Escena {scene_id}"
        title_es = timing.title_es or ""
        title_ko = timing.title_ko or ""
        
        num_w = draw.textbbox((0, 0), scene_num_str, font=large_font)[2]
        title_es_w = draw.textbbox((0, 0), title_es, font=huge_font)[2]
        title_ko_w = draw.textbbox((0, 0), title_ko, font=ko_title_font)[2]
        
        draw.text(((width - num_w) // 2, 300), scene_num_str, font=large_font, fill=(255, 255, 255, 200))
        draw.text(((width - title_es_w) // 2, 420), title_es, font=huge_font, fill=(255, 255, 255))
        draw.line(((width - 300) // 2, 600, (width + 300) // 2, 600), fill=(255, 255, 255, 120), width=4)
        draw.text(((width - title_ko_w) // 2, 645), title_ko, font=ko_title_font, fill=(255, 255, 255, 220))
        return image

    elif seg_type in ("diary_line", "pause"):
        image_path = segment.get("image_path", "")
        if image_path:
            img_path = Path(image_path)
            if img_path.exists():
                return Image.open(img_path).convert("RGB")
        
        # Fallback background: warm page with vertical band
        image = Image.new("RGB", (width, height), bg_color)
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, 36, height), fill=scene_color)
        
        wm_font = _load_font(font_bold_path, 30, font_index)
        wm_text = f"Escena {scene_id}: {timing.title_es or ''}"
        draw.text((90, 60), wm_text, font=wm_font, fill=scene_color)
        draw.line((90, 112, width - 90, 112), fill=(220, 218, 210), width=2)
        
        ph_font = _load_font(font_regular_path, 42, font_index_ko)
        ph_text = f"[장면 {scene_id} 이미지 위치]"
        ph_w = draw.textbbox((0, 0), ph_text, font=ph_font)[2]
        draw.text(((width - ph_w) // 2, 390), ph_text, font=ph_font, fill=muted_text_color)
        return image

    return Image.new("RGB", (width, height), bg_color)


def render_diary_caption(timing: DiaryTiming, design: dict) -> Image.Image | None:
    """Render the translucent subtitle overlay panel as a standalone RGBA frame."""
    if timing.type != "diary_line":
        return None
        
    width, height = output_size_for_design(design)
    font_bold_path = design.get("font_path", "assets/fonts/NotoSansKR-Bold.ttf")
    font_regular_path = design.get("font_path_ko", "assets/fonts/NotoSansKR-Regular.ttf")
    font_index = int(design.get("font_index", 0))
    font_index_ko = int(design.get("font_index_ko", 0))
    
    text_color = design.get("text_color", (31, 35, 40))
    muted_text_color = (60, 64, 70) # Darken Korean text for legibility
    scene_id = timing.scene_id
    scene_color = get_scene_color(scene_id)
    
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    
    # 1. Draw a bottom gradient scrim (full-width)
    scrim_h = 320
    scrim_top = height - scrim_h
    pixels = overlay.load()
    bg_r, bg_g, bg_b = design.get("background_color", (248, 247, 242))
    
    for y_offset in range(scrim_h):
        y = scrim_top + y_offset
        alpha = int(220 * (y_offset / max(1, scrim_h - 1)))
        for x in range(width):
            pixels[x, y] = (bg_r, bg_g, bg_b, alpha)
            
    draw = ImageDraw.Draw(overlay)
    
    # 2. Compute dynamic heights to prevent overlapping. Default values preserve
    # older diary renders; newer projects can opt into larger captions via DESIGN.
    speaker_font_size = int(design.get("diary_caption_speaker_font_size", 33))
    es_font_size = int(design.get("diary_caption_es_font_size", 51))
    ko_font_size = int(design.get("diary_caption_ko_font_size", 36))
    es_line_step = int(design.get("diary_caption_es_line_step", max(58, es_font_size + 7)))
    ko_line_step = int(design.get("diary_caption_ko_line_step", max(42, ko_font_size + 6)))
    speaker_step = int(design.get("diary_caption_speaker_step", max(58, speaker_font_size + 25)))
    interline_gap = int(design.get("diary_caption_interline_gap", 18))
    panel_w = int(design.get("diary_caption_panel_w", 1650))
    panel_margin_x = int(design.get("diary_caption_margin_x", 60))
    panel_pad_y = int(design.get("diary_caption_pad_y", 24))
    panel_min_h = int(design.get("diary_caption_panel_min_h", 230))
    panel_bottom = int(design.get("diary_caption_panel_bottom", 40))
    panel_alpha = int(design.get("diary_caption_panel_alpha", 130))

    speaker_font = _load_font(font_bold_path, speaker_font_size, font_index)
    es_font = _load_font(font_bold_path, es_font_size, font_index)
    ko_font = _load_font(font_bold_path, ko_font_size, font_index_ko)
    
    es_lines = wrap_text(timing.text_es, es_font, panel_w - (panel_margin_x * 2), draw)
    ko_lines = wrap_text(timing.text_ko or "", ko_font, panel_w - (panel_margin_x * 2), draw)
    
    needed_h = panel_pad_y * 2
    if timing.speaker:
        needed_h += speaker_step
    needed_h += len(es_lines) * es_line_step
    needed_h += interline_gap
    needed_h += len(ko_lines) * ko_line_step
    
    panel_h = max(panel_min_h, needed_h)
    panel_x = (width - panel_w) // 2
    panel_y = height - panel_h - panel_bottom
    
    # 3. Draw a shorter translucent panel (rounded rectangle)
    draw.rounded_rectangle(
        (panel_x, panel_y, panel_x + panel_w, panel_y + panel_h),
        radius=24,
        fill=(250, 249, 245, panel_alpha),
        outline=(210, 208, 198, 160),
        width=2
    )
    
    text_x = panel_x + panel_margin_x
    current_y = panel_y + panel_pad_y
    
    # Draw speaker badge if present
    if timing.speaker:
        sp_text = timing.speaker
        sp_w = draw.textbbox((0, 0), sp_text, font=speaker_font)[2]
        badge_color = design.get("speaker_colors", {}).get(timing.speaker, scene_color)
        draw.rounded_rectangle(
            (text_x, current_y, text_x + sp_w + 30, current_y + 42),
            radius=8,
            fill=badge_color,
        )
        draw.text((text_x + 15, current_y + 3), sp_text, font=speaker_font, fill=(255, 255, 255))
        current_y += speaker_step
    
    # Spanish text
    for line in es_lines:
        draw.text((text_x, current_y), line, font=es_font, fill=text_color)
        current_y += es_line_step
        
    # Korean text
    current_y += interline_gap
    for line in ko_lines:
        draw.text((text_x, current_y), line, font=ko_font, fill=muted_text_color)
        current_y += ko_line_step
        
    return overlay


def render_diary_segment_image(segment: dict, timing: DiaryTiming, design: dict) -> Image.Image:
    """Render a single merged image, combining background and caption overlay (backward compatibility)."""
    bg = render_diary_background(segment, timing, design)
    cap = render_diary_caption(timing, design)
    if cap:
        bg.paste(cap, (0, 0), cap)
    return bg


def build_diary_video_clip(segments: list[dict], design: dict | None, timings: list[DiaryTiming]):
    from moviepy import CompositeVideoClip, ImageClip, VideoClip
    from build.easing import ease_in_out_quad, lerp
    from build.camera import crop_and_resize, clamp
    import numpy as np
    
    output_size = output_size_for_design(design)
    width, height = output_size
    
    # 1. Group timings into beats based on same non-empty resolved image_path
    beats = []
    current_beat_timings = []
    current_img = None
    current_sid = None
    
    for segment, timing in zip(segments, timings):
        img_path = segment.get("image_path", "")
        sid = timing.scene_id
        exists = img_path and Path(img_path).exists()
        
        if exists:
            if img_path == current_img and sid == current_sid:
                current_beat_timings.append(timing)
            else:
                if current_beat_timings:
                    beats.append({
                        "image_path": current_img,
                        "scene_id": current_sid,
                        "timings": current_beat_timings,
                        "start_s": current_beat_timings[0].start_s,
                        "end_s": current_beat_timings[-1].end_s,
                        "duration": current_beat_timings[-1].end_s - current_beat_timings[0].start_s
                    })
                current_beat_timings = [timing]
                current_img = img_path
                current_sid = sid
        else:
            if current_beat_timings:
                beats.append({
                    "image_path": current_img,
                    "scene_id": current_sid,
                    "timings": current_beat_timings,
                    "start_s": current_beat_timings[0].start_s,
                    "end_s": current_beat_timings[-1].end_s,
                    "duration": current_beat_timings[-1].end_s - current_beat_timings[0].start_s
                })
                current_beat_timings = []
                current_img = None
                current_sid = None
                
    if current_beat_timings:
        beats.append({
            "image_path": current_img,
            "scene_id": current_sid,
            "timings": current_beat_timings,
            "start_s": current_beat_timings[0].start_s,
            "end_s": current_beat_timings[-1].end_s,
            "duration": current_beat_timings[-1].end_s - current_beat_timings[0].start_s
        })
        
    beat_map = {}
    for beat in beats:
        for timing in beat["timings"]:
            beat_map[timing.index] = beat
            
    # 2. Pre-load beat images to cache them
    beat_images = {}
    for beat in beats:
        img_path = beat["image_path"]
        if img_path not in beat_images:
            beat_images[img_path] = Image.open(ROOT / img_path).convert("RGB")
            
    # 3. Create clips for each segment
    clips = []
    for idx, (segment, timing) in enumerate(zip(segments, timings)):
        timing_index = timing.index
        seg_duration = timing.duration_s
        if seg_duration <= 0:
            continue
            
        beat = beat_map.get(timing_index)
        is_last = (idx == len(timings) - 1)
        is_first = (idx == 0)
        
        # Extend duration for crossfade overlap (T4)
        clip_dur = seg_duration if is_last else (seg_duration + 0.4)
        
        # Background clip
        if beat:
            beat_img = beat_images[beat["image_path"]]
            # Determine base crop frame centered on the source image with aspect ratio 16:9
            source_w, source_h = beat_img.size
            aspect = 16.0 / 9.0
            if source_w / source_h > aspect:
                w_f = source_h * aspect
                h_f = source_h
                x_f = (source_w - w_f) / 2.0
                y_f = 0.0
            else:
                w_f = source_w
                h_f = w_f / aspect
                x_f = 0.0
                y_ratio = design.get("diary_crop_y_ratio", 0.5) if design else 0.5
                y_f = (source_h - h_f) * y_ratio
            base_frame = {"x": x_f, "y": y_f, "w": w_f, "h": h_f}
            
            # Closure for frame generator capturing beat_img and base_frame
            def make_bg_frame(local_t: float, t_timing=timing, t_beat=beat, t_base_frame=base_frame, t_img=beat_img) -> np.ndarray:
                abs_t = t_timing.start_s + local_t
                beat_dur = t_beat["duration"]
                p = (abs_t - t_beat["start_s"]) / beat_dur if beat_dur > 0 else 0.0
                progress = ease_in_out_quad(clamp(p, 0.0, 1.0))
                
                # T7: Vary pan/zoom by scene_id for variety
                sid = t_beat.get("scene_id", 1) or 1
                if sid % 3 == 0:
                    zoom = lerp(1.0, 1.08, progress)
                elif sid % 3 == 1:
                    zoom = lerp(1.08, 1.0, progress)
                else:
                    zoom = 1.04
                
                max_slack_w = t_base_frame["w"] * 0.05
                max_slack_h = t_base_frame["h"] * 0.05
                
                dx = 0.0
                dy = 0.0
                mode = sid % 4
                if mode == 0:
                    dx = lerp(-max_slack_w, max_slack_w, progress)
                elif mode == 1:
                    dx = lerp(max_slack_w, -max_slack_w, progress)
                elif mode == 2:
                    dy = lerp(max_slack_h, -max_slack_h, progress)
                elif mode == 3:
                    dy = lerp(-max_slack_h, max_slack_h, progress)
                
                shifted_frame = {
                    "x": t_base_frame["x"] + dx,
                    "y": t_base_frame["y"] + dy,
                    "w": t_base_frame["w"],
                    "h": t_base_frame["h"]
                }
                return crop_and_resize(t_img, shifted_frame, zoom, output_size=output_size)
                
            bg_clip = VideoClip(frame_function=make_bg_frame, duration=clip_dur).with_start(timing.start_s)
        else:
            # Fallback/static background
            bg_img = render_diary_background(segment, timing, design)
            bg_clip = ImageClip(np.asarray(bg_img)).with_start(timing.start_s).with_duration(clip_dur)
            
        # Apply crossfade if not first clip
        if not is_first:
            from moviepy.video.fx import CrossFadeIn
            bg_clip = bg_clip.with_effects([CrossFadeIn(duration=0.4)])
            
        clips.append(bg_clip)
        
        # Caption overlay clip (diary_line only - no extension to keep sync exact)
        if timing.type == "diary_line":
            caption_img = render_diary_caption(timing, design)
            if caption_img:
                # Build transparent overlay
                arr = np.asarray(caption_img)
                rgb = arr[:, :, :3]
                alpha = arr[:, :, 3].astype("float32") / 255.0
                
                caption_rgb_clip = ImageClip(rgb).with_start(timing.start_s).with_duration(seg_duration)
                mask = ImageClip(alpha, is_mask=True).with_start(timing.start_s).with_duration(seg_duration)
                caption_clip = caption_rgb_clip.with_mask(mask)
                clips.append(caption_clip)
                
    total_duration = timings[-1].end_s if timings else 0.0
    return CompositeVideoClip(clips, size=output_size).with_duration(total_duration)


def main() -> int:
    args = parse_args()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    audio_dir = OUTPUT_DIR / "audio"
    seg_audios = None
    tts_durations = None

    if AUDIO:
        seg_audios = synthesize_segments(SEGMENTS, AUDIO, audio_dir / "tts", render_type=RENDER_TYPE_DIARY)
        tts_durations = {int(seg_audio["index"]): float(seg_audio["duration_s"]) for seg_audio in seg_audios}

    timings = build_diary_timings(SEGMENTS, design=DESIGN, tts_durations=tts_durations, audio_cfg=AUDIO)
    total_duration_s = timings[-1].end_s if timings else 0.0
    clip = build_diary_video_clip(SEGMENTS, design=DESIGN, timings=timings)

    if args.preview:
        silent_path = OUTPUT_DIR / "preview-silent.mp4"
        output_path = OUTPUT_DIR / "preview.mp4"
        fps = 12
        preset = "ultrafast"
        crf = "26"
    else:
        silent_path = OUTPUT_DIR / f"{OUTPUT_NAME}-silent.mp4"
        output_path = OUTPUT_DIR / f"{OUTPUT_NAME}.mp4"
        fps = 30
        preset = "medium"
        crf = "18"

    clip.write_videofile(
        str(silent_path),
        codec="libx264",
        audio=False,
        fps=fps,
        preset=preset,
        ffmpeg_params=["-pix_fmt", "yuv420p", "-movflags", "+faststart", "-crf", crf],
    )
    clip.close()

    if AUDIO and seg_audios is not None:
        narration_wav = build_narration_wav(seg_audios, timings, AUDIO, total_duration_s, audio_dir / "narration.wav")
        narration_sfx_wav = mix_sfx_layer(
            narration_wav,
            SFX_MANIFEST,
            timings,
            total_duration_s,
            audio_dir / "narration_sfx.wav",
            story_scenes=STORY_SCENES,
            audio_cfg=AUDIO,
            segment_sfx=SEGMENT_SFX,
        )
        mix_wav = mix_with_bgm(narration_sfx_wav, AUDIO.get("bgm_path"), AUDIO, total_duration_s, audio_dir / "mix.wav")
        write_manifest(seg_audios, timings, AUDIO, total_duration_s, audio_dir / "tts" / "manifest.json")
        mux_into_video(silent_path, mix_wav, AUDIO, output_path)
        silent_path.unlink(missing_ok=True)
    else:
        silent_path.rename(output_path)

    print(
        json.dumps(
            {
                "ok": True,
                "output": str(output_path),
                "fps": fps,
                "duration_s": round(total_duration_s, 3),
                "audio": bool(AUDIO),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
