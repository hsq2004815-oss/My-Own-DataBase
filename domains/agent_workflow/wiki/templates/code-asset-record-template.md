# Code Asset Record Template

Use this template when creating a new `processed/code_assets/*.asset.json` record. Fill all required fields; leave optional fields empty or omit them.

## Required Fields

| Field | Description |
|-------|-------------|
| `asset_id` | Stable unique identifier, kebab-case (e.g. `launch-control-readiness-pattern`) |
| `title` | Human-readable title |
| `domain` | Primary domain from the code asset taxonomy |
| `capability` | Specific capability from the code asset taxonomy |
| `source_project` | Name of the source project (e.g. `xiaohuang`, `FastAPI`, `openWakeWord`) |
| `source_url` | URL or local path to the source |
| `source_path` | Relative path within the source project |
| `license` | SPDX identifier or description |
| `reuse_level` | `direct_dependency` / `implementation_pattern` / `extractable_module` / `research_only` |
| `reuse_policy` | `direct_use_allowed` / `adapter_required` / `inspiration_only` / `license_review_required` / `do_not_copy_code` |
| `summary` | One paragraph describing what this asset provides |
| `why_reusable` | Why this capability generalizes beyond its source project |
| `adapter_target` | Suggested target service, adapter layer, or project |
| `implementation_notes` | Array of key implementation notes |
| `tests_required` | Array of tests to write when reusing |
| `risks` | Array of risks and caveats |

## Optional Fields

| Field | Description |
|-------|-------------|
| `language` | Primary programming language |
| `dependencies` | Required dependencies (array) |
| `windows_compatibility` | `full` / `partial` / `none` / `unknown` |
| `packaging_impact` | Impact on packaging (PyInstaller, MSIX, etc.) |
| `related_files` | Related source files |
| `related_patterns` | Related pattern asset IDs |
| `related_snippets` | Related wiki snippet paths |
| `related_adapters` | Related wiki adapter paths |
| `prompt_tags` | Tags for agent retrieval (array) |
| `do_not_do` | Common mistakes to avoid (array) |
| `notes` | Additional notes |

## Example Structure

```json
{
  "asset_id": "example-pattern",
  "title": "Example Reusable Pattern",
  "domain": "desktop_app",
  "capability": "launch_control",
  "source_project": "example-project",
  "source_url": "E:/Projects/example",
  "source_path": "src/example/module.py",
  "license": "MIT",
  "reuse_level": "implementation_pattern",
  "reuse_policy": "adapter_required",
  "summary": "Describes a reusable pattern for...",
  "why_reusable": "The pattern generalizes to any desktop app that needs...",
  "adapter_target": "Future desktop assistant / Windows tool",
  "implementation_notes": [
    "Use a single-file adapter to avoid polluting the main pipeline",
    "Wrap platform-specific calls behind a protocol/interface"
  ],
  "tests_required": [
    "Unit test for the adapter with mocked subprocess",
    "Integration test on Windows with real PowerShell"
  ],
  "risks": [
    "PowerShell execution policy may block scripts",
    "Operation lock file must be cleaned up on crash"
  ],
  "do_not_do": [
    "Do not call PowerShell without a timeout",
    "Do not hardcode paths"
  ]
}
```
