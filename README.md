# screenplan-contracts

Cross-project type contracts for the ScreenPlan repos: the JSON schemas in this
folder are the **source of truth** for any data shape that crosses a project
boundary. The TypeScript and Python packages alongside it are derived views.

```
packages/
  screenplan-contracts/         <- schemas + examples + this README (source of truth)
  screenplan-contracts-ts/      <- TS types + AJV validators        (npm: @screenplan/contracts)
  screenplan-contracts-py/      <- Pydantic models + jsonschema     (pip: screenplan-contracts, import screenplan_contracts)
```

## What is covered

| Schema                                  | Used by                                                | Notes |
|-----------------------------------------|--------------------------------------------------------|------|
| `script.schema.json`                    | script-studio (author) ↔ ScriptEngine (execute)        | `Script` document with action rows. |
| `script-action.schema.json`             | script-studio ↔ ScriptEngine                           | Common envelope for the 41 action subtypes. Per-subtype `actionData` is open today (TODO). |
| `script-status.schema.json`             | Script-Engine-Controller ↔ script-studio               | Entry shape of `running_scripts.json` / `completed_scripts.json`. |
| `event-status.schema.json`              | Script-Engine-Controller ↔ script-studio               | Entry shape of `running_events.json` / `completed_events.json`. Each event is a `sequence` tree. |
| `script-action-log.schema.json`         | ScriptEngine (write) → script-studio (read)            | Per-action `action-log.json` produced by `ScriptActionLog._flush`. |
| `script-action-artifacts.schema.json`   | both                                                   | Schema for the per-action artifact spec. |
| `script-action-artifacts.json`          | both                                                   | Canonical mapping `actionName → { pre_file, post_file, supporting_files, attributes }`. |
| `common.schema.json`                    | -                                                      | Enums and small `$defs` (`SystemName`, `RunStatus`, `FileType`, …). |

## Conventions

- JSON Schema **draft 2020-12**.
- Required fields reflect what code today actually requires; optional otherwise.
- `additionalProperties: false` only where the existing code is closed-shape
  (e.g. `Script` and `ScriptActionRow`). Loose envelopes
  (`ScriptStatus`, `EventStatus`, `ScriptAction`, `ScriptActionLog`) keep
  `additionalProperties: true` so callers can attach fields without breaking
  consumers.
- Enums are used wherever the code clearly has a finite set of strings.

## TypeScript usage

```ts
import type { ScriptAction, ScriptActionLog, ScriptStatus } from "@screenplan/contracts";
import { validateScriptAction, validateScriptStatus } from "@screenplan/contracts";

const status: ScriptStatus = validateScriptStatus.assert(JSON.parse(buf));
```

Wired up in `Script-Engine-Controller/package.json` and
`script-studio/package.json` as a `file:` dependency. After cloning:

```sh
(cd packages/screenplan-contracts-ts && npm install && npm run build)
```

## Python usage

```python
from screenplan_contracts.models import ScriptAction
from screenplan_contracts.validation import validate_script_action_log
log = validate_script_action_log(json.loads(buf))
```

Listed in `components/ScriptEngine/setup.py`. Local install:

```sh
pip install -e packages/screenplan-contracts-py
```

Schema JSON files are shipped as package data and loaded via
`importlib.resources`, so PyInstaller/cx_Freeze frozen builds don't need any
filesystem path tricks (they're inside the wheel).

## Adding a new shared type

1. Create `packages/screenplan-contracts/schemas/<name>.schema.json` (draft 2020-12).
2. Add an example under `packages/screenplan-contracts/examples/<name>.example.json`.
3. Register it in:
   - `packages/screenplan-contracts-ts/src/validators.ts` (`ajv.addSchema(...)` + a
     `makeValidator` line).
   - `packages/screenplan-contracts-py/screenplan_contracts/validation.py` (one
     `validate_<thing>` helper + add to `_store()`).
   - `packages/screenplan-contracts-ts/src/types.ts` and
     `packages/screenplan-contracts-py/screenplan_contracts/models.py` (mirror types).
4. Re-build both packages and run validation:
   ```sh
   (cd packages/screenplan-contracts-ts && npm run build && npm test)
   (cd packages/screenplan-contracts-py && pytest -q)
   node packages/screenplan-contracts/validate-known-files.mjs
   ```

## Validation scripts

- `packages/screenplan-contracts-ts/test/validate-examples.mjs` — every
  `examples/*.json` validates against its schema (`npm test`).
- `packages/screenplan-contracts-py/tests/test_examples.py` — same on the Python
  side (`pytest`).
- `packages/screenplan-contracts/validate-known-files.mjs` — validate real
  `running_*.json` / `completed_*.json` queue files in
  `Script-Engine-Controller/tmp/`. Pass an optional log dir to also walk every
  `*-action-log.json` under it.

## How projects are wired

| Project                    | Integration                                                                                                |
|----------------------------|-------------------------------------------------------------------------------------------------------------|
| Script-Engine-Controller   | `@screenplan/contracts` in `package.json`. `QueueManager` accepts an optional `itemValidator`; wired in `index.mjs`. Validation is opt-in via `SHARED_CONTRACTS_VALIDATE=1`. |
| script-studio              | `@screenplan/contracts` in `package.json`. Re-export shim at `src/app/shared/contracts.ts`. Existing `editor/interfaces/*.ts` types kept as-is with mirror-warning comments. |
| ScriptEngine               | `screenplan-contracts` in `setup.py`. `ScriptActionLog._flush` validates the payload against `ScriptActionLog` schema when `SHARED_CONTRACTS_VALIDATE=1`. |

## Per-action artifact contract (Group C)

`schemas/script-action-artifacts.json` declares, for each of the 41 action
subtypes, the predictable set of files ScriptEngine attaches to the
`ScriptActionLog`:

```jsonc
"detectObject": {
  "pre_file":  { "file_type": "image", "presence": "always", "name_suffix": "screenshot-pre.png" },
  "post_file": { "file_type": "image", "presence": "optional", "name_suffix": "detection-matches.png" },
  "supporting_files": [{ "file_type": "text", "presence": "optional", "name_suffix": "detection-confidence.txt" }],
  "attributes": { "detectActionType": { "presence": "always", "enum": ["floatingObject", "fixedObject"] } }
}
```

`presence` is one of `always | optional | never`. script-studio uses this to
drive the Action Details viewer; ScriptEngine should treat `always`/`never` as
authoring requirements when adding new action types. **TODO:** add a
ScriptEngine-side test that runs each action and asserts that emitted files
match the spec.

## Known gaps / TODOs

- `actionData` per-subtype shapes are not yet schema'd — the `ScriptAction`
  envelope is open. Capturing them is the next obvious step (~41 sub-schemas).
- Artifacts spec is **best-effort** — it was inferred from current code but has
  not been exhaustively cross-validated against every executor. Treat
  `optional` as the default until verified.
- `device_details` accepts both `object | string | null` to match historical
  data — newer code should write objects only.
- Python validation uses `jsonschema.RefResolver`, which is deprecated. Migrate
  to `referencing` when convenient.
