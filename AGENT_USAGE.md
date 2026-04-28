# Agent Usage

Use this local knowledge base before starting a task that may benefit from UI/design, workflow, or automation context.

## Default Rule

Do not read the whole `E:\DataBase` directory. Call the brief API or CLI first, then use only the returned chunks.

For ordinary frontend/design tasks, use UI and workflow context only:

```powershell
python E:\DataBase\scripts\brief.py "<task>" --ui 8 --workflow 4 --automation 0 --assets 6
```

Use automation context only when the user explicitly asks for browser automation, upload/download, CDP, selectors, screenshots, or verification:

```powershell
python E:\DataBase\scripts\brief.py "<task>" --ui 1 --workflow 4 --automation 6
```

## If The API Is Not Running

Start it in a separate terminal:

```powershell
cd E:\DataBase\backend_api
python -m uvicorn app.main:app --host 127.0.0.1 --port 8765 --reload
```

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

```json
{
  "task": "<task>",
  "ui_limit": 8,
  "workflow_limit": 4,
  "automation_limit": 0,
  "asset_limit": 6
}
```

`asset_suggestions` are not automatically direct-use assets. Follow `usage_policy`: `inspiration_only` means borrow the visual idea only; `review_required` means inspect the license before using files directly.
