# Tiny Task Tracker Context

Last updated: 2026-06-01 11:30 IST
Project: Tiny Task Tracker
Status: Example context architecture, not a runnable app
Repository: `examples/tiny-task-tracker`
Current branch: `main`
Recent baseline commit: example only

## Start Here

- North star: `critical_prompt.md`
- Code ownership map: `architecture/code-map.md`
- Flow source of truth: `SYSTEM_FLOW_INDEX.md`
- Validation index: `test_index/README.md`

## Current Runtime Model

```text
SQLite tasks table
  -> FastAPI task service
    -> HTTP JSON routes
      -> browser task board
```

## Current App / Package Setup

- Main local command: `uvicorn app.main:app --reload`
- Primary local URL: `http://localhost:8000`
- Health/check command: `curl http://localhost:8000/health`
- Main validation command: `pytest`

## Current Contracts To Preserve

- Task status is one of `todo`, `doing`, or `done`.
- `GET /tasks` returns tasks sorted by newest first.
- `PATCH /tasks/{id}` validates status before persistence.

## Recently Completed

- Example context architecture populated.
- API, UI, and validation ownership rows defined.
- Example validation commands documented.

## Known Debt / Next Work

- Add real source files if this example becomes executable.
- Add a component doc for the task API once routes exist.
- Add a checkpoint after the first real implementation session.

## Validation Evidence

Latest verified commands:

```powershell
python scripts/check_doc_coverage.py --files examples/tiny-task-tracker/context.md
Result: maps to the example/docs ownership row in the parent repo.
```
