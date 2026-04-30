# Agentic Software Delivery Pipeline — Backend 项目如何接入

> 来源：`garrytan/gstack` (MIT) — ship/land-and-deploy/canary/document-release 交付管线
> 生成时间：2026-04-30
> 适用范围：后端/API 项目的 agentic 交付流程

## 一、后端项目的 Agentic Delivery 适配

gstack 的 7 阶段流程（Think→Plan→Build→Review→Test→Ship→Reflect）完全适用于后端/API 项目。以下是针对后端的各阶段适配：

### Think 阶段 — 需求重定义

```
输入：用户的功能需求
输出：明确的 API 功能边界 + 约束 + 成功标准
检查：是否可以通过配置/现有服务完成？是否需要新的 API endpoint？
```

### Plan 阶段 — 架构设计

```
输出：
- API endpoint 设计 (RESTful / gRPC)
- 数据库 schema 变更 (migration)
- 数据流图
- 测试策略 (unit + integration + E2E)
- 安全考虑 (认证/授权/输入校验)

审查 Gate：
- Eng Gate：数据流是否清晰？边界条件是否完整？
- DX Gate：API 命名一致？错误消息可理解？分页/排序/过滤规范？
- Security Gate：(高风险) OWASP + STRIDE
```

### Build 阶段 — 实现

```
- 先写 migration
- 再写 model/schema
- 再写 repository
- 再写 service
- 最后写 controller
- 同步写测试
```

### Review 阶段 — 代码审查

```
- PR review：backend rules 合规
- Security review：SQL 注入/XSS/CSRF/JWT 安全
- DX review：API 文档 + 错误响应
- 跨模型审查 (可选)：Claude + Codex 独立审查
```

### Test 阶段 — 测试

```
- Unit test：service/repository 覆盖
- Integration test：API endpoint + DB
- Security scan：(如适用)
- Performance test：(如性能敏感)
```

### Ship 阶段 — 发布

```
1. 同步 main 分支
2. 运行完整测试套件
3. Push + 打开 PR
4. Merge (CI 通过)
5. 运行 database migration
6. 部署
7. 健康检查 + 金丝雀监控
8. 更新 API 文档
```

### Reflect 阶段 — 复盘

```
- API 设计决策回顾
- 性能问题记录
- 安全漏洞教训
- 写入 backend rules/checklists
```

## 二、Backend Review Gates

| Gate | 检查内容 | 强制？ |
|------|---------|:-----:|
| **API Design** | RESTful 规范、分页、错误码、版本管理 | 必须 |
| **Database** | Migration 可回滚、索引合理、无 N+1 | 必须 |
| **Security** | SQL 注入、XSS、CSRF、JWT 安全 | 必须 |
| **DX** | API 文档完整、错误消息可操作 | 建议 |
| **Performance** | 查询计划、N+1、缓存策略 | 性能敏感时 |

## 三、Release Pipeline

```
main 分支
    ↓ git pull
Run tests (pytest / jest / go test)
    ↓ all green
Push to remote
    ↓
Open PR (或直接 push to main for small projects)
    ↓
CI Pipeline:
  ├── Lint & format check
  ├── Unit tests
  ├── Integration tests
  ├── Security scan
  └── Build
    ↓
Merge PR
    ↓
Deploy:
  ├── Run migrations
  ├── Deploy new version
  ├── Health check
  └── Canary monitor (5-30 min)
    ↓
Document: update API docs, changelog
    ↓
Retro: record learnings
```

## 四、与 Backend Domain 现有规则的关系

本 topic 与以下 backend rules 互补：
- `api-design-rules.md` → API Design Gate 标准
- `backend-security-checklist.md` → Security Gate 标准
- `database-modeling-rules.md` → Database Gate 标准
- `deployment-and-env-rules.md` → Ship 阶段标准
- `error-handling-and-logging-rules.md` → Code Review 参考

本 topic 提供的是**流程框架**（什么时候做什么），backend rules 提供的是**执行标准**（怎么做才合格）。

## 五、简化版（小型后端项目）

小型项目可以使用精简流程：

```
Think → Plan (简化) → Build → Review (仅 code review) → Ship → Reflect
```

跳过：
- DX review（单人项目）
- 跨模型交叉审查（成本考虑）
- Canary monitor（非生产环境）
- 安全审查（无认证/支付/用户数据）
