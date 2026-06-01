# Critical Prompt - Tiny Task Tracker

Use this file as the stable north star for Tiny Task Tracker.

## Product / System Goal

Tiny Task Tracker exists to help a solo developer capture, update, and complete
small project tasks without leaving the browser.

The primary users are:

- solo developers
- small project maintainers
- AI coding agents working on the repo

The core workflow is:

```text
user opens task board
  -> creates or edits a task
  -> task is persisted through the API
  -> board refreshes with the updated task state
```

## Non-Negotiable Boundaries

- The backend API owns task validation and persistence.
- The UI may cache task lists but must not be the source of truth.
- No credentials or private task content belongs in repo docs.
- Tests must cover API behavior before UI polish work is merged.

## Current Architecture Posture

- Runtime owner: `FastAPI app`
- UI owner: `browser client`
- Persistence owner: `SQLite`
- Integration owner: `HTTP JSON API`
- Validation owner: `test_index/` plus pytest

## Design Defaults

- Prefer small API contracts over broad narrative docs.
- Keep `context.md` concise; put durable architecture in `architecture/`.
- Update docs and tests when API contracts move.

## Stop Conditions

Stop and re-plan if:

- task ownership between API and UI becomes unclear
- persistence behavior cannot be verified by tests
- a change requires storing secrets or private production data in docs
