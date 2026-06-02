# Tiny Task Tracker Code Map

Last updated: 2026-06-01

This is the canonical subsystem-to-code map for the example project.

## Coverage Table

| Subsystem | Purpose | Source globs | Interfaces | Architecture anchors | Test anchors | Update triggers |
| --- | --- | --- | --- | --- | --- | --- |
| Task API | Validates task input and exposes task CRUD routes. | `app/api/**/*.py`, `app/services/tasks.py` | `GET /tasks`, `POST /tasks`, `PATCH /tasks/{id}` | `SYSTEM_FLOW_INDEX.md` | `tests/test_tasks_api.py`, `test_index/README.md` | Route shape, validation, status rules, or response order changes. |
| Persistence | Stores task records and status transitions. | `app/db/**/*.py`, `migrations/**/*.sql` | SQLite task table | `SYSTEM_FLOW_INDEX.md` | `tests/test_task_persistence.py` | Schema, migration, ordering, or transaction behavior changes. |
| Browser UI | Renders task board and sends API updates. | `web/**/*.ts`, `web/**/*.tsx`, `web/**/*.css` | Task board UI | `SYSTEM_FLOW_INDEX.md` | `tests/e2e/**/*.spec.ts` | Board workflow, API client, or visible task state changes. |
| Tests and validation harness | Proves task behavior and guards regressions. | `tests/**/*.py`, `tests/e2e/**/*.ts`, `test_index/*.md` | pytest and browser checks | `architecture/code-map.md`, `test_index/README.md` | `pytest`, `npx playwright test` | Test command, fixture, or acceptance criteria changes. |
