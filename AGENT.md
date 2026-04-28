# Agent Instructions

This repository is a local knowledge base for AI-assisted UI/design, workflow, asset, and automation tasks. Use it through the local API first, not as a blob of text to dump into context.

## First Rule

Do not read the entire repository for a normal task. Start with the local API, then inspect only the returned chunks/assets and the files directly relevant to the task.

## Local Database API First Protocol

My-Own-DataBase is primarily accessed through the local FastAPI service.

Default local API:

```text
http://127.0.0.1:8765
```

GitHub is not the default runtime source. GitHub is only for remote backup, human inspection, ChatGPT structure review, and version synchronization.

When the user says “根据我的数据库”, “用我的数据库”, “按我的数据库规则”, “调用我的数据库”, “based on my database”, or “use my database”, the agent must automatically call the local database API.

Required sequence:

```http
GET http://127.0.0.1:8765/health
POST http://127.0.0.1:8765/brief
```

For UI / frontend / portfolio / landing page / dashboard / app UI tasks:

```json
{
  "task": "<user task>",
  "ui_limit": 8,
  "workflow_limit": 2,
  "automation_limit": 0,
  "asset_limit": 10
}
```

When the task is UI generation, do not only retrieve rules. Apply the premium UI execution self-check:
- choose pattern
- choose material system
- choose visual anchor
- choose component system
- avoid generic templates
- report record_id used

For browser automation / RPA / upload tool tasks:

```json
{
  "task": "<user task>",
  "ui_limit": 2,
  "workflow_limit": 4,
  "automation_limit": 8,
  "asset_limit": 0
}
```

For general coding / agent workflow tasks:

```json
{
  "task": "<user task>",
  "ui_limit": 2,
  "workflow_limit": 6,
  "automation_limit": 2,
  "asset_limit": 0
}
```

If the local API is not reachable:

- Clearly tell the user the local database API is not running.
- Suggest starting it with:

```powershell
cd E:\DataBase\backend_api
python -m uvicorn app.main:app --host 127.0.0.1 --port 8765 --reload
```

- Do not silently fall back to GitHub unless the user explicitly asks.

Required behavior:

- Before doing the task, briefly state that local database context was retrieved.
- After the task, briefly state which database areas influenced the result.
- Do not scan the whole repository unless API retrieval is unavailable and the user allows file reading.

## Motion Asset Bootstrap Protocol

For UI / frontend / portfolio / landing page tasks, if the user asks for "高级", "动效", "动画", "小动画", "motion", "Lottie", "视觉效果", or "交互高级", do not stop after `/brief`.

After the required `/brief` call, also call `/assets/search` with each query below:

```text
小动画
微交互
loading animation
hover motion
button animation
animated icon
lottie animation
motion reference
hero background motion
```

In the final output, list:

- retrieved `asset_id` / `chunk_id`
- `usage_policy`
- whether the asset was directly used or only used as inspiration
- implementation method: CSS, SVG, Canvas, Lottie, or video

If no suitable `direct_use` animation asset is found, explicitly say: "未检索到可用 direct_use 动画素材，因此使用 CSS/SVG/Canvas 复刻动效。"

Do not imply that an inspiration-only or review-required asset was copied into the project.

Default CLI:

```powershell
python E:\DataBase\scripts\brief.py "<task>" --ui 8 --workflow 2 --automation 0 --assets 10
```

Start the API if the CLI cannot connect:

```powershell
cd E:\DataBase\backend_api
python -m uvicorn app.main:app --host 127.0.0.1 --port 8765 --reload
```

## Domain Routing

- UI/frontend/design work: use `ui_design` plus `agent_workflow`; keep `automation_limit=0`.
- For ordinary Web UI, landing page, SaaS homepage, product page, dashboard, and portfolio tasks, treat the `ui_design` premium rules as the default aesthetic layer before brand `design-*.md` topics.
- Dynamic backgrounds, screenshots, fonts, icons, or UI kits: include `ui_assets` suggestions and follow `usage_policy`.
- Browser automation, uploads, CDP, selectors, screenshots, iframe/modal handling, or verification: explicitly request automation chunks with `--automation > 0`.
- API or retrieval maintenance: inspect `backend_api/app/main.py`, `scripts/brief.py`, and the relevant domain scripts.
- Schema/taxonomy changes: inspect `common/schemas`, `common/templates`, and `common/taxonomy` first.

## Asset Safety

`asset_suggestions` are not automatically safe to copy.

- `inspiration_only`: borrow ideas only.
- `review_required`: inspect license and source before direct use.
- Do not treat unknown web downloads as reusable product assets.

## UI Aesthetic Defaults

For premium Web UI generation, prefer these `ui_design` wiki topics and their processed references first:

1. `domains/ui_design/wiki/topics/premium-web-ui-initial-aesthetic-rules.md`
2. `domains/ui_design/wiki/topics/liquid-glass-design-system.md`
3. `domains/ui_design/wiki/topics/cinematic-video-hero-rules.md`
4. `domains/ui_design/wiki/topics/video-hero-layout-patterns.md`
5. `domains/ui_design/wiki/topics/premium-typography-and-layout-rules.md`
6. `domains/ui_design/wiki/topics/motion-interaction-premium-rules.md`
7. `domains/ui_design/wiki/topics/landing-page-section-patterns.md`

Use brand `design-*.md` topics as secondary flavor references. If a brand topic is information-insufficient, do not let it override the premium rules.

For Hero / Landing Page / SaaS Homepage / Portfolio First Screen tasks, prioritize video hero layout patterns and cinematic video hero rules. For Web App / Dashboard / Workspace tasks, prioritize `liquid-glass-web-app-ui-kit.md` instead; do not apply hero rules blindly to forms, dashboards, or complex consoles.

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
python E:\DataBase\scripts\brief.py "做一个高级玻璃生态 AI dashboard，带动态背景和字体" --ui 8 --workflow 2 --automation 0 --assets 10
```

## Final Handoff

When using this database for a task, report:

- `ui_queries`, `workflow_queries`, `automation_queries`, and `asset_queries`
- chunk ids actually used
- asset ids actually used, if any
- which returned guidance affected the implementation
- verification performed and remaining gaps
