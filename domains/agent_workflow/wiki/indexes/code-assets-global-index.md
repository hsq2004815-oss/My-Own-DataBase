# Code Assets Global Index

Global entry point for discovering reusable code assets. Organized by capability category. Agents should check this index first before scanning `raw/` or reading individual asset records.

## How to Use

1. Find the capability category below that matches your task.
2. Follow the link to the relevant code asset record(s).
3. Read the asset record for reuse level, license, risks, and adapter guidance.
4. Check related snippets and adapters for implementation details.

---

## desktop_tray

System tray icon, menu, and notification patterns for Windows desktop apps.

| Asset ID | Source | Reuse Level | Record |
|----------|--------|-------------|--------|
| *(pending)* | — | — | — |

## launch_control

Application launch, subprocess management, readiness polling, and operation lock patterns.

| Asset ID | Source | Reuse Level | Record |
|----------|--------|-------------|--------|
| `launch-control-readiness-pattern` | xiaohuang | implementation_pattern | [.asset.json](../../processed/code_assets/launch-control-readiness-pattern.asset.json) |

### Related Snippets
- [launch-control-readiness-operation-lock.md](../../wiki/snippets/launch-control-readiness-operation-lock.md)

### Related Adapters
- [adapt-launch-control-to-desktop-assistant.md](../../wiki/adapters/adapt-launch-control-to-desktop-assistant.md)

## settings_ui

Settings UI patterns: config editor, validation, save-reload, and unknown fields preservation.

| Asset ID | Source | Reuse Level | Record |
|----------|--------|-------------|--------|
| `settings-ui-config-validation-pattern` | xiaohuang | implementation_pattern | [.asset.json](../../processed/code_assets/settings-ui-config-validation-pattern.asset.json) |

## config_validation

Configuration validation, schema enforcement, and safe save/reload patterns.

| Asset ID | Source | Reuse Level | Record |
|----------|--------|-------------|--------|
| `settings-ui-config-validation-pattern` | xiaohuang | implementation_pattern | *(see settings_ui)* |

## llm_provider_router

OpenAI-compatible provider abstraction, API key resolution, and no-key fallback patterns.

| Asset ID | Source | Reuse Level | Record |
|----------|--------|-------------|--------|
| `llm-provider-router-pattern` | xiaohuang | implementation_pattern | [.asset.json](../../processed/code_assets/llm-provider-router-pattern.asset.json) |

## voice_assistant

Wake word detection, STT, TTS, and conversation session patterns.

| Asset ID | Source | Reuse Level | Record |
|----------|--------|-------------|--------|
| *(pending)* | — | — | — |

## wake_word

Wake word / hotword detection engine selection and integration patterns.

| Asset ID | Source | Reuse Level | Record |
|----------|--------|-------------|--------|
| *(pending — see voice_assistant domain)* | — | — | — |

## stt

Speech-to-text engine selection, VAD integration, and streaming patterns.

| Asset ID | Source | Reuse Level | Record |
|----------|--------|-------------|--------|
| *(pending — see voice_assistant domain)* | — | — | — |

## tts

Text-to-speech engine selection, streaming, and caching patterns.

| Asset ID | Source | Reuse Level | Record |
|----------|--------|-------------|--------|
| *(pending — see voice_assistant domain)* | — | — | — |

## conversation_session

Conversation state management, turn tracking, and session lifecycle patterns.

| Asset ID | Source | Reuse Level | Record |
|----------|--------|-------------|--------|
| *(pending)* | — | — | — |

## browser_automation

Playwright/CDP browser automation, uploads, iframes, and screenshot patterns.

| Asset ID | Source | Reuse Level | Record |
|----------|--------|-------------|--------|
| *(pending — see automation domain)* | — | — | — |

## backend_api

REST API design, routing, middleware, endpoint, knowledge retrieval, and index building patterns.

| Asset ID | Source | Reuse Level | Record |
|----------|--------|-------------|--------|
| `multi-domain-knowledge-retrieval-api` | DataBase | extractable_module | [.asset.json](../../processed/code_assets/multi-domain-knowledge-retrieval-api.asset.json) |
| `sqlite-fts5-index-builder-pipeline` | DataBase | extractable_module | [.asset.json](../../processed/code_assets/sqlite-fts5-index-builder-pipeline.asset.json) |
| `ranked-search-multi-strategy-fallback` | DataBase | extractable_module | [.asset.json](../../processed/code_assets/ranked-search-multi-strategy-fallback.asset.json) |
| `reference-to-chunk-pipeline` | DataBase | extractable_module | [.asset.json](../../processed/code_assets/reference-to-chunk-pipeline.asset.json) |
| `agent-friendly-cli-bridge` | DataBase | implementation_pattern | [.asset.json](../../processed/code_assets/agent-friendly-cli-bridge.asset.json) |
| `query-derivation-engine` | DataBase | extractable_module | [.asset.json](../../processed/code_assets/query-derivation-engine.asset.json) |
| `sse-streaming-response-pattern` | DataBase (curated) | implementation_pattern | [.asset.json](../../processed/code_assets/sse-streaming-response-pattern.asset.json) |
| `backend-healthcheck-error-envelope-pattern` | backend (curated) | extractable_module | [.asset.json](../../processed/code_assets/backend-healthcheck-error-envelope-pattern.asset.json) |

### Related Snippets
- [query-derivation-engine-interface.md](../../wiki/snippets/query-derivation-engine-interface.md)

### Related Adapters
- [adapt-knowledge-retrieval-to-new-domain.md](../../wiki/adapters/adapt-knowledge-retrieval-to-new-domain.md)

## logging

Structured logging, request ID propagation, and log level management patterns.

| Asset ID | Source | Reuse Level | Record |
|----------|--------|-------------|--------|
| `structured-api-request-logging` | DataBase | extractable_module | [.asset.json](../../processed/code_assets/structured-api-request-logging.asset.json) |

## healthcheck

Readiness/liveness healthcheck endpoint patterns.

| Asset ID | Source | Reuse Level | Record |
|----------|--------|-------------|--------|
| `backend-healthcheck-error-envelope-pattern` | backend (curated) | extractable_module | *(see backend_api)* |
| `launch-control-readiness-pattern` | xiaohuang | implementation_pattern | *(see launch_control)* |

## error_handling

Error envelope, structured error responses, error code taxonomy, and request ID propagation patterns.

| Asset ID | Source | Reuse Level | Record |
|----------|--------|-------------|--------|
| `unified-error-envelope-request-id` | DataBase (curated) | extractable_module | [.asset.json](../../processed/code_assets/unified-error-envelope-request-id.asset.json) |
| `backend-healthcheck-error-envelope-pattern` | backend (curated) | extractable_module | *(see backend_api)* |

## search_validation

Search quality regression testing and validation harness patterns.

| Asset ID | Source | Reuse Level | Record |
|----------|--------|-------------|--------|
| `search-validation-test-harness` | DataBase | extractable_module | [.asset.json](../../processed/code_assets/search-validation-test-harness.asset.json) |

---

## Pending Capabilities

The following capabilities have no code asset records yet:

- `subprocess` — subprocess management and lifecycle
- `powershell` — PowerShell invocation patterns for Windows tools
- `readiness_healthcheck` — standalone readiness/liveness checks
- `operation_lock` — single-instance lock and crash recovery
- `config_schema` — configuration schema design and versioning
- `crawler` — web crawling and scraping patterns
- `deployment` — deployment and CI/CD patterns
- `ui_pattern` — UI implementation patterns

---

## Asset Summary

Total code asset records: **14**

| Domain | Count | Records |
|--------|-------|---------|
| desktop_app | 2 | launch-control, settings-ui |
| agent_workflow | 3 | llm-provider-router, query-derivation-engine, agent-friendly-cli-bridge |
| backend | 9 | multi-domain-retrieval-api, sqlite-index-builder, ranked-search-fallback, structured-logging, search-validation, reference-to-chunk, error-envelope-request-id, sse-streaming, healthcheck-error-envelope |

| Reuse Level | Count |
|-------------|-------|
| extractable_module | 10 |
| implementation_pattern | 4 |

| Source | Count |
|--------|-------|
| My-Own-DataBase | 9 |
| xiaohuang | 3 |
| backend curated rules | 2 |

---

*Last updated: 2026-05-02*
