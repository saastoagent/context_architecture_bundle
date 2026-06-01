# Test Index - Tiny Task Tracker

## Suite Index

| Suite | Command | Protects | Source owner |
| --- | --- | --- | --- |
| API tests | `pytest tests/test_tasks_api.py` | Task route validation and response shape | Task API |
| Persistence tests | `pytest tests/test_task_persistence.py` | SQLite persistence and ordering | Persistence |
| Full suite | `pytest` | Backend behavior | Tests and validation harness |
| Browser flow | `npx playwright test` | Task board workflow | Browser UI |

## Validation Rule

Any change to task status rules, route shape, or persistence ordering must update
the matching `architecture/code-map.md` row and record validation evidence in
`context.md` or a checkpoint.
