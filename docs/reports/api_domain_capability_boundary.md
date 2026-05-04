# API / Domain Capability Boundary

Prevent agents from assuming database API capabilities that don't exist yet.

## Current `/brief` API (exact capabilities)

| Parameter | Domain | Description |
|-----------|--------|-------------|
| `ui_limit` | ui_design + ui_assets | UI chunks + asset suggestions |
| `workflow_limit` | agent_workflow | Agent workflow chunks |
| `automation_limit` | automation | Browser automation chunks |
| `backend_limit` | backend | Backend engineering chunks |
| `asset_limit` | ui_assets | Asset metadata suggestions |

## Not yet available as `/brief` parameters

**Do NOT pass these parameters** — they will be ignored or cause errors:
- `voice_limit` — voice_assistant is NOT wired to `/brief`
- `dev_tools_limit` — dev_tools is NOT wired to `/brief`

## How to use voice_assistant / dev_tools

These domains must be accessed manually:
1. Read `domains/<domain>/AGENT_USAGE.md`
2. Read the domain wiki index
3. Read relevant rules/topics/patterns directly
4. Do NOT call `/brief` expecting chunks from these domains

## API fallback (if `http://127.0.0.1:8765` is not running)

1. State clearly that the local API is not running
2. Follow fallback order: `CLAUDE.md` → `AGENT_USAGE.md` → domain `AGENT_USAGE.md` → playbook → rules/wiki
3. Do NOT default to scanning the entire repository
4. Do NOT default to reading `raw/`
