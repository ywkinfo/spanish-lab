# GitHub Workflow for Spanish Lab / Hermes Español Studio

This repository is a production pipeline and content factory. Hermes may prepare content packages, but public publishing follows a review gate.

## Operating model

- Hermes generates lesson/content packages, metadata, subtitles, scripts, and export files.
- Hermes may push only to content/staging branches such as `hermes/content-*`.
- `main` is protected and is not for direct Hermes pushes.
- GitHub Pages publishes from `main` + `/docs`, so anything merged to `main` can become public.
- Human review is required before merge.

## Allowed for Hermes

- Create or edit content-package files
- Create a review checklist
- Commit changes locally
- Push a staging/content branch
- Open a PR or prepare a merge-ready patch if GitHub auth is available
- Send a review request message with the exact branch and checklist

## Not allowed for Hermes

- Direct push to `main`
- Direct GitHub Pages publication without review
- Automatic YouTube publishing
- Social posting or comment automation

## Recommended branch flow

1. Fetch latest `main`.
2. Create a branch named like `hermes/content-a1-YYYYMMDD-HHMM`.
3. Generate the content package.
4. Run validation / lint / preview checks.
5. Commit the package.
6. Push the branch.
7. Ask for human review.
8. Merge only after approval.

## Human review checklist

Before merging to `main`, confirm:

- Spanish sounds natural and matches the intended level
- Korean explanations are accurate and concise
- Metadata, titles, and slugs are correct
- Subtitle timing / text is clean
- No secrets, tokens, or private data are included
- GitHub Pages paths are correct and safe to publish
- The page represents the intended public lesson, not an unfinished draft

## GitHub auth options

Preferred options for this environment:

1. SSH deploy key for repo-scoped branch pushes
2. Fine-grained PAT for PR / API workflows
3. gh auth login only if the token is intentionally managed in this session

See `GITHUB_DEPLOY_KEY_SETUP.md` for the exact SSH deploy-key setup and branch-push flow.

## Content package outputs

A reusable content package may include:

- lesson markdown
- JSON data
- Shorts script
- long-form outline
- quiz
- subtitles
- metadata

## Publishing note

If GitHub Pages is sourced from `main` and `/docs`, do not merge until the page is review-ready. A branch push is safe; a `main` merge is a public release.
