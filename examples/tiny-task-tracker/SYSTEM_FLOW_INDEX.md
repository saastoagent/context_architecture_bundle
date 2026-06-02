# System Flow Index - Tiny Task Tracker

Last updated: 2026-06-01 11:30 IST

## Active Architecture

```text
SQLite
  -> FastAPI task service
    -> HTTP JSON API
      -> browser task board
```

## Primary Routes, Commands, Or Interfaces

- `GET /tasks`
- `POST /tasks`
- `PATCH /tasks/{id}`
- `pytest`

## Main Flow

```text
user
  -> browser task board
  -> HTTP JSON API
  -> task service validation
  -> SQLite persistence
  -> refreshed board response
```

Rules:

- API validates task status.
- UI renders server-returned task state.
- Tests prove persistence and route behavior before UI-only changes.

## Validation Index

Fast checks:

```powershell
pytest tests/test_tasks_api.py
```

Full checks:

```powershell
pytest
```
