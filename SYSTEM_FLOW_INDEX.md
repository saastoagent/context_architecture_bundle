# System Flow Index - [PROJECT_NAME]

Last updated: [YYYY-MM-DD HH:MM TZ]

This file is the compact source of truth for currently implemented runtime and
UX flows. Use `context.md` for restart state and `architecture/components/` for
implementation detail.

## Active Architecture

```text
[SYSTEM_TRUTH_OWNER]
  -> [SERVICE_OR_RUNTIME_LAYER]
    -> [UI_OR_AGENT_CONSUMER]
      -> [VALIDATED_OPERATION_OR_OUTPUT]
```

Current anchors:

- Project setup: `README.md`
- Current context: `context.md`
- Code ownership map: `architecture/code-map.md`
- Component docs: `architecture/components/`
- Validation index: `test_index/README.md`

## Primary Routes, Commands, Or Interfaces

- `[INTERFACE_1]`
- `[INTERFACE_2]`
- `[INTERFACE_3]`

## Main Flow

```text
[USER_OR_CALLER]
  -> [ENTRYPOINT]
  -> [STATE_OR_SERVICE_LAYER]
  -> [DECISION_OR_OPERATION]
  -> [COMMIT_OR_RESPONSE]
```

Rules:

- [FLOW_RULE_1]
- [FLOW_RULE_2]
- [FLOW_RULE_3]

## Secondary / Diagnostic Flow

```text
[DIAGNOSTIC_ENTRY]
  -> [READ_MODEL_OR_TRACE]
  -> [SAFE_INSPECTION_OUTPUT]
```

Rules:

- Diagnostics are read-only unless explicitly designed otherwise.
- Diagnostics may expose internals that public/user-facing surfaces must hide.

## Known Compatibility Debt

- [COMPAT_DEBT_1]
- [COMPAT_DEBT_2]

## Validation Index

Fast checks:

```powershell
[FAST_CHECK_COMMAND]
```

Focused checks:

```powershell
[FOCUSED_CHECK_COMMAND]
```

Full checks:

```powershell
[FULL_CHECK_COMMAND]
```
