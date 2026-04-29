# Backend Phase 2D Index Build Report

## 1. 本次读取文件

读取了全局说明、backend README、Phase 2A/2B/2C 报告、Phase 2C manifest/chunk/routing/search target，以及现有 `runtime/db/sqlite`、`backend_api`、`scripts` 结构。`backend-doc-sync-after-phase-2b-report.md` 未找到；Phase 2C 报告已记录该缺失，不影响本阶段。

## 2. Runtime 预检结果

发现现有 SQLite 文件：

- `runtime/db/sqlite/ui_design/ui_design_references.db`
- `runtime/db/sqlite/automation/automation_references.db`
- `runtime/db/sqlite/agent_workflow/agent_workflow_references.db`

现有库按领域分目录、分 DB，均有 `chunks` 与 `chunks_fts` FTS5 表。`backend_api` 当前只连接 UI、workflow、automation 与 assets，未接入 backend。现有 scripts 也按领域提供 `build_sqlite_index.py` 和 search 脚本。

预检结论：

- `safe_to_write_runtime`: true
- `target_db_path`: `runtime/db/sqlite/backend/backend_references.db`
- `target_tables`: `backend_chunks`, `backend_chunks_fts`
- `required_schema_changes`: 新建 backend 专用 DB 和 backend 专用表，不修改其他领域库
- `backup_required`: true when replacing an existing backend DB; 本次目标 DB 不存在，无原 backend DB 可预先复制
- `dry_run_required`: true

## 3. 新增/修改文件

- `scripts/backend/build_backend_index.py`
- `scripts/backend/validate_backend_search.py`
- `domains/backend/processed/manifest/backend-index-manifest.json`
- `domains/backend/output/reports/backend-phase-2d-dry-run-report.json`
- `domains/backend/output/reports/backend-phase-2d-write-report.json`
- `domains/backend/output/search_tests/backend-search-test-results.json`
- `domains/backend/output/reports/backend-phase-2d-index-build-report.md`
- `runtime/db/sqlite/backend/backend_references.db`
- `TASK_MEMORY.md`

## 4. Dry-run 结果

- 输入 chunks 数量：338
- JSONL 解析结果：通过
- chunk_id 重复检查：无重复
- 空 content 检查：未发现
- secret-like 检查：未发现
- source_type 分布：`{'checklist': 24, 'github_project_analysis': 26, 'github_project_chunk': 39, 'pattern': 28, 'reference': 28, 'rule': 76, 'template': 81, 'topic': 36}`
- priority 分布：`{'high': 227, 'low': 17, 'medium': 94}`
- trust_level 分布：`{'core_reference': 30, 'good_reference': 25, 'not_applicable': 266, 'sample_only': 17}`

## 5. SQLite 写入结果

已写入 runtime SQLite。

- backup 路径：空。原因是 `runtime/db/sqlite/backend/backend_references.db` 在写入前不存在，没有原 backend DB 可复制；未触碰其他领域 DB。
- 写入表：`backend_chunks`, `backend_chunks_fts`
- 写入/更新数量：338
- FTS 是否启用：true
- BM25 是否可用：true，SQLite FTS5 `bm25()` 用于验证脚本排序
- 是否没有删除其他 domain 数据：是，只新建 backend 领域 DB 和表

## 6. 搜索验证结果

已执行 16 条搜索测试：

- pass：3
- partial：13
- fail：0

没有 fail。partial 的主要原因是当前验证脚本按 expected source_type / expected file 精确命中计分，FTS 召回有结果但并非每条都在 top 10 同时命中所有期望文件。后续 Phase 2E/API 集成时可调高规则类 chunk 权重，并优化 Phase 2C 的 tags，使 rules/wiki 在宽泛查询中优先于 GitHub 项目 chunk。

## 7. 安全检查结果

- 未发现 secret 原文。
- 未复制 raw 项目源码。
- 未运行 GitHub 项目。
- 未安装依赖。
- 未启动 API。
- 未调用 embedding。
- 未修改 `domains/backend/raw/github_projects`。
- 未删除或清空其他 domain 数据。

## 8. 当前未完成事项

- 尚未接入 `backend_api`。
- 尚未接入 `/brief`。
- 尚未做 embedding/vector index。
- 尚未做 API 级召回测试。

## 9. 下一步建议

建议进入 Phase 2E：

- backend API / brief 集成。
- 增加 backend domain 检索入口。
- 使用 16 条 search expected targets 做 API 召回测试。
- 更新 AGENT_USAGE 中的 backend 检索调用方式。
