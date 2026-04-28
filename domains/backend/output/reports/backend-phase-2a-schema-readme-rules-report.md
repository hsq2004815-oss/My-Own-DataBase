# Backend Phase 2A Schema README Rules Report

## 1. 本次读取的输入文件

- `E:\DataBase\README.md`
- `E:\DataBase\AGENT.md`
- `E:\DataBase\AGENTS.md`
- `E:\DataBase\AGENT_USAGE.md`
- `E:\DataBase\TASK_MEMORY.md`
- `E:\DataBase\common\schemas\ui_reference.schema.json`
- `E:\DataBase\common\schemas\ui_asset.schema.json`
- `E:\DataBase\common\schemas\automation_reference.schema.json`
- `E:\DataBase\common\schemas\agent_workflow_reference.schema.json`
- `E:\DataBase\domains\backend\output\reports\github-projects-analysis-report.md`
- `E:\DataBase\domains\backend\processed\cleaned_text\github_projects\*.analysis.md`
- `E:\DataBase\domains\backend\processed\metadata\github_projects\*.metadata.json`
- `E:\DataBase\domains\backend\processed\chunks\github_projects\*.chunks.json`

## 2. 新增/更新的文件

- `E:\DataBase\common\schemas\backend_reference.schema.json`
- `E:\DataBase\domains\backend\README.md`
- `E:\DataBase\domains\backend\rules\backend-engineering-map.md`
- `E:\DataBase\domains\backend\rules\backend-agent-usage-rules.md`
- `E:\DataBase\domains\backend\rules\api-design-rules.md`
- `E:\DataBase\domains\backend\rules\database-modeling-rules.md`
- `E:\DataBase\domains\backend\rules\auth-and-permission-rules.md`
- `E:\DataBase\domains\backend\rules\backend-layered-architecture-rules.md`
- `E:\DataBase\domains\backend\rules\error-handling-and-logging-rules.md`
- `E:\DataBase\domains\backend\rules\backend-security-checklist.md`
- `E:\DataBase\domains\backend\rules\deployment-and-env-rules.md`
- `E:\DataBase\domains\backend\rules\performance-and-stability-rules.md`
- `E:\DataBase\domains\backend\rules\ai-backend-design-rules.md`
- `E:\DataBase\domains\backend\rules\github-backend-project-selection-rules.md`
- `E:\DataBase\domains\backend\rules\backend-project-template-rules.md`
- `E:\DataBase\domains\backend\output\reports\backend-phase-2a-schema-readme-rules-report.md`

如同名文件已存在，写入前已按 `.bak_YYYYMMDD_HHMMSS` 规则备份。

## 3. backend_reference.schema.json

- 已创建 `E:\DataBase\common\schemas\backend_reference.schema.json`。
- schema 采用 JSON Schema draft 2020-12。
- 支持 backend 领域的 category、source_type、agent_usage、retrieval、related_rules、related_topics。
- JSON 解析校验已通过：`backend_reference.schema.json` 可被 `json.loads` 正常解析。

## 4. README 优先级规则

- README 已包含 backend 领域定义。
- README 已包含 Agent 使用场景。
- README 已包含 API、数据库、登录权限、安全、部署、AI backend、GitHub 项目分析的优先读取文件。
- README 已说明纯前端任务不应使用 backend 规则。
- README 已说明普通个人项目不要默认微服务、K8s、DDD、服务网格。
- README 已说明 raw GitHub 项目源码只是原始资料，Agent 使用 rules/wiki/references/processed chunks。

## 5. 13 个 rules 文件检查

本阶段应生成的 13 个 rules 文件均已写入 `E:\DataBase\domains\backend\rules`。每个文件均包含：文件用途、适用场景、优先读取条件、适合项目类型、不适合项目类型、推荐做法、禁止做法、Agent 生成代码时必须遵守的规则、常见失败案例、检查清单、推荐参考来源、关联文件。

## 6. 空文件检查

最终验证脚本已检查 schema、README、13 个 rules 和本报告，未发现空文件。

## 7. secret 复制风险检查

本阶段规则只记录 secret 风险和占位符要求，没有复制第一阶段发现的示例 RSA private key、JWT secret 或 DB password 原文。规则明确要求：

- 模板 secret 必须使用 `CHANGE_ME`、`REPLACE_WITH_RANDOM_SECRET`、`your_postgres_password` 等明显占位符。
- 不允许把示例 RSA private key、JWT secret、DB password 当成可复用模板内容。
- 不允许在 README、template、rules、references 中沉淀真实或疑似真实 secret。
- 发现 secret-looking 内容只能写“存在风险，需要替换”，不要复制原文。
- `.env.example` 用于说明变量名，不用于提供真实值。

## 8. 越界行为检查

本阶段未运行 GitHub 项目，未安装依赖，未执行 npm/pnpm/pip/docker/alembic/prisma 命令，未修改 raw/github_projects，未修改 runtime/db/sqlite，未启动 backend_api，未 git commit，未生成 wiki topics/patterns/checklists/templates 文件，未生成 references JSON。

最终验证结果：

- schema JSON：通过。
- README 优先级规则：通过。
- 13 个 rules 文件：全部存在。
- rules 必需章节：全部存在。
- 空文件检查：未发现空文件。
- hardcoded secret 原文复制检查：未发现。
- runtime/db/sqlite 越界检查：未发现。
- wiki 文件生成检查：未发现本阶段禁止生成的 wiki 文件。

## 9. 下一步建议

下一阶段建议生成 wiki topics / patterns / checklists / templates / references JSON。仍然不要运行项目，不要改 raw 源码，不要改 runtime SQLite；先让用户确认本阶段 schema、README 和 rules。
