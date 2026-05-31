# Human Review Checklist

Use this checklist before merging a Hermes content branch into `main`.

## Content

- [ ] Spanish sounds natural for the target level
- [ ] Korean explanations are accurate and concise
- [ ] The teaching point is clear and consistent across files
- [ ] No accidental English leakage appears in public-facing copy

## Metadata

- [ ] Title matches the actual lesson content
- [ ] Slug is correct and stable
- [ ] Tags / hashtags / labels are appropriate
- [ ] Description and summary are not misleading

## Learning package

- [ ] Lesson markdown is complete
- [ ] JSON data matches the markdown
- [ ] Shorts script is consistent with the lesson
- [ ] Long-form outline is aligned with the lesson goal
- [ ] Quiz answers are correct
- [ ] Subtitles are clean and readable

## Public safety

- [ ] No secrets, tokens, private keys, or internal-only notes are included
- [ ] GitHub Pages paths are correct
- [ ] The page is ready for public viewing
- [ ] The branch is the intended review branch, not `main`

## Merge gate

- [ ] Human reviewer approved
- [ ] Any requested edits were applied
- [ ] Merge to `main` is intentional
- [ ] If `main` feeds GitHub Pages, publication is acceptable now
