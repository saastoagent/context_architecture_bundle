# [PROJECT_NAME] Context

Last updated: [YYYY-MM-DD HH:MM TZ]
Project: [PROJECT_NAME]
Status: [CURRENT_STATUS]
Repository: `[REPO_OR_PACKAGE_PATH]`
Current branch: `[BRANCH_NAME]`
Recent baseline commit: `[SHORT_SHA AND MESSAGE]`

## Start Here

- North star: `critical_prompt.md`
- Setup and usage: `README.md`
- Code ownership map: `architecture/code-map.md`
- Component docs: `architecture/components/`
- Flow source of truth: `SYSTEM_FLOW_INDEX.md`
- Latest checkpoint: `context_checkpoints/[LATEST_CHECKPOINT].md`
- Latest closeout log: `logs/[LATEST_LOG].md`
- Active plan: `plans/[ACTIVE_PLAN].md`

## Current Runtime Model

```text
[STATE_OWNER]
  -> [PROJECTION_OR_SERVICE_LAYER]
    -> [UI_OR_AGENT_CONSUMER]
      -> [VALIDATED_OPERATION]
        -> [COMMIT_OR_RESULT]
```

## Current App / Package Setup

- Main local command: `[RUN_COMMAND]`
- Primary local URL, if any: `[LOCAL_URL]`
- Health/check command: `[HEALTH_OR_SMOKE_COMMAND]`
- Main validation command: `[VALIDATION_COMMAND]`

## Current Contracts To Preserve

- [CONTRACT_1]
- [CONTRACT_2]
- [CONTRACT_3]

## Recently Completed

- [RECENT_COMPLETION_1]
- [RECENT_COMPLETION_2]
- [RECENT_COMPLETION_3]

## Known Debt / Next Work

- [KNOWN_DEBT_1]
- [KNOWN_DEBT_2]
- [NEXT_CONCRETE_STEP]

## Validation Evidence

Latest verified commands:

```powershell
[COMMAND_1]
[RESULT_1]

[COMMAND_2]
[RESULT_2]
```

## Documentation Rule

When source files change, map them through `architecture/code-map.md`, update
the related component/test docs or explicitly record why they are unchanged,
then refresh this file as the concise restart snapshot.
