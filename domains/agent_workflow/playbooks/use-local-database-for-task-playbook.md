# Use Local Database for Task Playbook

How an agent decides whether to use this database, which domain, and what to report after.

## 1. When to use

- User says "根据我的数据库" / "用我的数据库" / "按我的数据库规则" / "use my database" / "based on my database"
- Task involves UI / backend / automation / agent workflow / assets / voice assistant / dev tools
- Task needs my preferences, past pitfalls, project patterns, reusable code assets

## 2. When NOT to use the database

- General coding questions unrelated to the 7 domains
- Pure algorithm/data structure questions
- Reading third-party documentation
- Tasks where the agent's training data is sufficient

## 3. Do NOT do these

- Do not read the entire repository
- Do not start from `raw/`
- Do not scan `processed/chunks/` as task context
- Do not use GitHub as the runtime source
- Do not open automation tools or raw projects for ordinary tasks

## 4. Routing decision

| Task type | Domains to use |
|-----------|---------------|
| UI / frontend / landing / portfolio / dashboard | `ui_design` + `ui_assets` + `agent_workflow` |
| Backend / API / DB / auth / deployment / RAG | `backend` + `agent_workflow` |
| Browser automation / upload / iframe / CDP | `automation` + `agent_workflow` |
| Windows desktop tool / tray / launcher / config | `agent_workflow` + `backend` (if needed) |
| Voice assistant / wake word / STT / TTS / 小黄 | `voice_assistant` + `agent_workflow` |
| GitHub import / download acceleration | `dev_tools` + `agent_workflow` + target domain |
| Raw-to-rules curation | `agent_workflow` + target domain |

## 5. API usage

`/brief` currently supports: `ui_limit`, `workflow_limit`, `automation_limit`, `backend_limit`, `asset_limit`.

Example calls:
```powershell
# UI task
python E:\DataBase\scripts\brief.py "landing page design" --ui 8 --workflow 2 --assets 10

# Backend task
python E:\DataBase\scripts\brief.py "design JWT auth API" --backend 8 --workflow 2

# Browser automation task
python E:\DataBase\scripts\brief.py "file upload automation" --automation 8 --workflow 4 --ui 2
```

For `voice_assistant` / `dev_tools`: read domain `AGENT_USAGE.md` + wiki index + rules manually. Do NOT pass `voice_limit` or `dev_tools_limit`.

## 6. Required output after task

Agent must report:
- Which domains were used
- Which playbooks were followed
- Which rules / patterns / templates were applied
- Retrieved query / chunk IDs / asset IDs (if API was used)
- How database guidance affected the implementation
- Remaining uncertainties

## 7. Feedback loop

After task completion, judge whether to persist:
- New pitfall → add to rules / playbook / checklist
- New reusable capability → add code asset / snippet / adapter
- New external source → raw → processed → rules/wiki/references
- Eval failure → record in eval report; do NOT blindly rewrite the database
