---
description: Start a new Spanish Lab episode from a slug/topic idea, route editorial and linguist work, and prepare for producer handoff once an image exists.
argument-hint: "<slug> <topic>"
---

# Episode New

Use this skill to start a new Spanish Lab `Descripción de imagen B2` episode.

Arguments:

`$ARGUMENTS`

## Current Publish Metadata

!`for f in output/meta/*.json; do jq -r '[.episode,.slug,.video.duration_s,.youtube.title] | @tsv' "$f"; done 2>/dev/null | sort -n || true`

## Workflow

1. Resolve the requested slug and topic from `$ARGUMENTS`.
2. Detect the next episode number from `output/meta/*.json`.
3. Dispatch `episode-planner` first:
   - If `images/candidates/` contains unused images, ask for 1-3 shortlist briefs under `output/planning/`.
   - If no unused candidate image exists, ask for `output/planning/_pending-image.md`, stop at `ready for image`, and tell the user to add a source image under `images/candidates/`.
   - The planner may only shortlist; it must not write scripts or project modules.
4. After showrunner greenlight, append a `greenlight` event to `~/.claude/projects/<workspace-slug>/memory/episode-decisions/epNN-<slug>.jsonl`.
5. Create a 5-line showrunner brief:
   - topic
   - grammar focus
   - image cue
   - target duration
   - target chapter count
6. Dispatch `editorial-strategist` to draft the source script and instructor notes.
7. Dispatch `linguist` for Spanish B2 register approval.
8. If no source image exists at `images/<slug>.png`, stop at `ready for image` and tell the user the exact expected path.
9. After the image exists, dispatch `producer` to create `projects/<module>.py` from the closest existing episode pattern.

## Rules

- Manual upload only.
- Do not create cron or scheduled tasks.
- Do not edit shared infra.
- Do not run TTS before linguist approval.
- New project modules use underscore module names; `OUTPUT_NAME` stays hyphenated.
- Planner output is advisory; showrunner greenlight remains required.
- Decision logs under memory are canonical; `output/meta/*-decisions.json` is only a publish snapshot.
