# Agent Instructions

This repository is a local knowledge base for AI-assisted UI/design, workflow, asset, and automation tasks. Use it as a retrieval system, not as a blob of text to dump into context.

## First Rule

Do not read the entire repository for a normal task. Start with the brief CLI or API, then inspect only the returned chunks/assets and the files directly relevant to the task.

Default CLI:

```powershell
python E:\DataBase\scripts\brief.py "<task>" --ui 8 --workflow 4 --automation 0 --assets 6
```

Start the API if the CLI cannot connect:

```powershell
cd E:\DataBase\backend_api
python -m uvicorn app.main:app --host 127.0.0.1 --port 8765 --reload
```

## Domain Routing

- UI/frontend/design work: use `ui_design` plus `agent_workflow`; keep `automation_limit=0`.
- Dynamic backgrounds, screenshots, fonts, icons, or UI kits: include `ui_assets` suggestions and follow `usage_policy`.
- Browser automation, uploads, CDP, selectors, screenshots, iframe/modal handling, or verification: explicitly request automation chunks with `--automation > 0`.
- API or retrieval maintenance: inspect `backend_api/app/main.py`, `scripts/brief.py`, and the relevant domain scripts.
- Schema/taxonomy changes: inspect `common/schemas`, `common/templates`, and `common/taxonomy` first.

## Asset Safety

`asset_suggestions` are not automatically safe to copy.

- `inspiration_only`: borrow ideas only.
- `review_required`: inspect license and source before direct use.
- Do not treat unknown web downloads as reusable product assets.

## Repository Hygiene

- Keep Python caches, `.pyc`, runtime logs, and temporary brief artifacts out of git.
- Keep useful SQLite indexes under `runtime/db/sqlite/*` because they are the runtime retrieval artifacts.
- Root `runtime/db/*.db` files may be empty compatibility leftovers; usable DBs are under `runtime/db/sqlite/*`.
- Use PowerShell carefully with Windows paths. In Bash/Git Bash, convert Windows paths to forward slashes.
- Prefer targeted `rg`, file slices, and CLI/API retrieval over broad file dumps.

## Verification

For maintenance changes, run the smallest command that proves the edited path still works. Common checks:

```powershell
python -m py_compile E:\DataBase\backend_api\app\main.py E:\DataBase\scripts\brief.py
```

If the API is running:

```powershell
Invoke-RestMethod "http://127.0.0.1:8765/health"
python E:\DataBase\scripts\brief.py "做一个高级玻璃生态 AI dashboard，带动态背景和字体" --ui 8 --workflow 4 --automation 0 --assets 6
```

## Final Handoff

When using this database for a task, report:

- `ui_queries`, `workflow_queries`, `automation_queries`, and `asset_queries`
- chunk ids actually used
- asset ids actually used, if any
- which returned guidance affected the implementation
- verification performed and remaining gaps
