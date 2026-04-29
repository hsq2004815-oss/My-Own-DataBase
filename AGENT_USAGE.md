# Agent Usage

Use this local knowledge base before starting a task that may benefit from UI/design, workflow, or automation context.

## Default Rule

Do not read the whole `E:\DataBase` directory. Call the local API or brief CLI first, then use only the returned chunks.

GitHub is not the default runtime source. GitHub is only for remote backup, human inspection, ChatGPT structure review, and version synchronization.

Default local API:

```text
http://127.0.0.1:8765
```

When the user says "根据我的数据库", "用我的数据库", "按我的数据库规则", "调用我的数据库", "based on my database", or "use my database", automatically call:

```http
GET http://127.0.0.1:8765/health
POST http://127.0.0.1:8765/brief
```

For ordinary frontend/design tasks, use UI and workflow context only:

```powershell
python E:\DataBase\scripts\brief.py "<task>" --ui 8 --workflow 2 --automation 0 --assets 10
```

Use automation context only when the user explicitly asks for browser automation, upload/download, CDP, selectors, screenshots, or verification:

```powershell
python E:\DataBase\scripts\brief.py "<task>" --ui 2 --workflow 4 --automation 8 --assets 0
```

For backend/API/database/auth/deployment/RAG tasks, backend is currently maintained as curated files, not as a `/brief` indexed runtime domain. Read:

```text
E:\DataBase\domains\backend\README.md
```

Then follow that README to the relevant `rules/`, `wiki/`, `references/`, or processed GitHub project metadata/chunks. Do not read `domains/backend/raw/github_projects` for normal generation tasks, and do not run projects, install dependencies, start the API, build indexes, or modify `runtime/db/sqlite`.

For general coding or agent workflow tasks:

```powershell
python E:\DataBase\scripts\brief.py "<task>" --ui 2 --workflow 6 --automation 2 --assets 0
```

## Motion Asset Bootstrap

For UI / frontend / portfolio / landing page tasks, if the user asks for "高级", "动效", "动画", "小动画", "motion", "Lottie", "视觉效果", or "交互高级", do not only call `/brief`.

After `/brief`, call `/assets/search` for:

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

Final output must list retrieved `asset_id` / `chunk_id`, `usage_policy`, whether each asset was directly used or only used as inspiration, and the implementation method: CSS, SVG, Canvas, Lottie, or video.

If no suitable `direct_use` animation asset is found, say: "未检索到可用 direct_use 动画素材，因此使用 CSS/SVG/Canvas 复刻动效。"

## Premium UI Execution Requirement

For UI / frontend / portfolio / landing page / dashboard / app UI tasks, after retrieving `/brief`, the agent must also perform a design execution self-check.

Before coding, state:

1. selected visual direction
2. selected hero pattern
3. selected material system
4. selected visual anchor
5. selected component system
6. record_id / rules used

After coding, state:

1. which rules were applied
2. whether ui_assets were used or only referenced
3. whether any metrics are placeholders
4. whether the result avoids generic template layout

If the generated page lacks a visual anchor or looks like a generic template, revise before final answer.

## If The API Is Not Running

Start it in a separate terminal:

```powershell
cd E:\DataBase\backend_api
python -m uvicorn app.main:app --host 127.0.0.1 --port 8765 --reload
```

Clearly tell the user the local database API is not running. Do not silently fall back to GitHub unless the user explicitly asks.

## Required Final Report

Include:

- `ui_queries`, `workflow_queries`, `automation_queries`, and `asset_queries`
- chunk ids actually used
- asset ids actually used, if any
- which returned guidance affected the implementation

Do not modify `E:\DataBase` unless the user explicitly asks you to maintain the database.

## Direct HTTP Form

```http
POST http://127.0.0.1:8765/brief
```

UI / frontend / portfolio / landing page / dashboard / app UI:

```json
{
  "task": "<task>",
  "ui_limit": 8,
  "workflow_limit": 2,
  "automation_limit": 0,
  "asset_limit": 10
}
```

Browser automation / RPA / upload tools:

```json
{
  "task": "<task>",
  "ui_limit": 2,
  "workflow_limit": 4,
  "automation_limit": 8,
  "asset_limit": 0
}
```

General coding / agent workflow:

```json
{
  "task": "<task>",
  "ui_limit": 2,
  "workflow_limit": 6,
  "automation_limit": 2,
  "asset_limit": 0
}
```

`asset_suggestions` are not automatically direct-use assets. Follow `usage_policy`: `inspiration_only` means borrow the visual idea only; `review_required` means inspect the license before using files directly.

Before doing the task, briefly state that local database context was retrieved. After the task, briefly state which database areas influenced the result.
