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
| `launch-control-readiness-pattern` | xiaohuang | implementation_pattern | [launch-control-readiness-pattern.asset.json](../../processed/code_assets/launch-control-readiness-pattern.asset.json) |

### Related Snippets
- [launch-control-readiness-operation-lock.md](../../wiki/snippets/launch-control-readiness-operation-lock.md)

### Related Adapters
- [adapt-launch-control-to-desktop-assistant.md](../../wiki/adapters/adapt-launch-control-to-desktop-assistant.md)

## settings_ui

Settings UI patterns: config editor, validation, save-reload, and unknown fields preservation.

| Asset ID | Source | Reuse Level | Record |
|----------|--------|-------------|--------|
| `settings-ui-config-validation-pattern` | xiaohuang | implementation_pattern | [settings-ui-config-validation-pattern.asset.json](../../processed/code_assets/settings-ui-config-validation-pattern.asset.json) |

## config_validation

Configuration validation, schema enforcement, and safe save/reload patterns.

| Asset ID | Source | Reuse Level | Record |
|----------|--------|-------------|--------|
| `settings-ui-config-validation-pattern` | xiaohuang | implementation_pattern | *(see settings_ui)* |

## llm_provider_router

OpenAI-compatible provider abstraction, API key resolution, and no-key fallback patterns.

| Asset ID | Source | Reuse Level | Record |
|----------|--------|-------------|--------|
| `llm-provider-router-pattern` | xiaohuang | implementation_pattern | [llm-provider-router-pattern.asset.json](../../processed/code_assets/llm-provider-router-pattern.asset.json) |

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

REST API design, routing, middleware, and endpoint patterns.

| Asset ID | Source | Reuse Level | Record |
|----------|--------|-------------|--------|
| `backend-healthcheck-error-envelope-pattern` | backend (curated) | extractable_module | [backend-healthcheck-error-envelope-pattern.asset.json](../../processed/code_assets/backend-healthcheck-error-envelope-pattern.asset.json) |

## logging

Structured logging, request ID propagation, and log level management patterns.

| Asset ID | Source | Reuse Level | Record |
|----------|--------|-------------|--------|
| *(pending — see backend domain)* | — | — | — |

## healthcheck

Readiness/liveness healthcheck endpoint patterns.

| Asset ID | Source | Reuse Level | Record |
|----------|--------|-------------|--------|
| `backend-healthcheck-error-envelope-pattern` | backend (curated) | extractable_module | *(see backend_api)* |
| `launch-control-readiness-pattern` | xiaohuang | implementation_pattern | *(see launch_control)* |

## error_handling

Error envelope, structured error responses, and error code taxonomy patterns.

| Asset ID | Source | Reuse Level | Record |
|----------|--------|-------------|--------|
| `backend-healthcheck-error-envelope-pattern` | backend (curated) | extractable_module | *(see backend_api)* |

---

## Pending Capabilities

The following capabilities have no code asset records yet. They will be populated as relevant patterns are identified and reviewed:

- `subprocess` — subprocess management and lifecycle
- `powershell` — PowerShell invocation patterns for Windows tools
- `readiness_healthcheck` — standalone readiness/liveness checks
- `operation_lock` — single-instance lock and crash recovery
- `config_schema` — configuration schema design and versioning
- `crawler` — web crawling and scraping patterns
- `deployment` — deployment and CI/CD patterns
- `ui_pattern` — UI implementation patterns

---

*Last updated: 2026-05-02*
