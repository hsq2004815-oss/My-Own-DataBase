# Database Modeling Rules

## 文件用途

为 Agent 设计数据库 schema、ORM model、migration、索引、约束和数据生命周期提供规则。

## 适用场景

- 设计表结构。
- 生成 ORM model。
- 生成 Alembic/Prisma/TypeORM migration。
- 设计 RAG metadata 和 pgvector 表。
- 评审数据库结构。

## 优先读取条件

- 数据库、表结构、model、schema、migration、Alembic、Prisma、TypeORM、SQLAlchemy、PostgreSQL、SQLite、索引、约束。

## 适合的项目类型

- 个人项目
- FastAPI + SQLite/PostgreSQL
- Express + Prisma + PostgreSQL
- NestJS + TypeORM
- RAG/pgvector 后端

## 不适合的项目类型

- 纯前端任务
- 无持久化需求的一次性脚本
- 未明确需求的分布式数据库架构

## 推荐做法

- 默认生成 migration，不只改 ORM model。
- 每张业务表明确主键、唯一约束、外键、必要索引、created_at、updated_at。
- 软删除只在需要恢复、审计或引用保留时使用。
- 多字段查询按真实查询路径设计复合索引。
- 个人项目可先 SQLite，涉及并发、权限、RAG、队列或部署时优先 PostgreSQL。
- RAG metadata 必须包含 document_id/file_id/user scope 以支持隔离查询。

## 禁止做法

- 不要只生成表、不生成 migration。
- 不要所有字段都建索引。
- 不要用字符串 role/status 但没有枚举或约束。
- 不要把密码、refresh token 明文入库。
- 不要默认把 SQLite 当 RAG/pgvector 生产方案。

## Agent 生成代码时必须遵守的规则

1. 新增或修改表必须生成 migration。
2. 所有唯一业务键必须有唯一约束。
3. 所有外键关系必须说明级联/限制策略。
4. 所有 token/secret 存储必须 hash 或加密，不能明文。
5. RAG 向量表必须支持 metadata filter 和权限范围。
6. 迁移命令只能写入文档，不在本阶段执行。

## 常见失败案例

- 只改 `schema.prisma` 不生成 migration。
- 查询频繁的 user_id/status 没有索引。
- 软删除字段存在但查询没有过滤。
- refresh token 明文存储。
- RAG 检索全库搜索导致跨用户泄露。

## 检查清单

- [ ] migration 存在
- [ ] 约束和索引明确
- [ ] 时间字段明确
- [ ] 软删除决策明确
- [ ] token/secret 不明文
- [ ] RAG metadata 支持隔离

## 推荐参考来源

- FastAPI official docs
- PostgreSQL official docs
- Redis official docs
- Docker / Docker Compose official docs
- OpenAPI Specification
- OWASP API Security Top 10
- OAuth2 / OpenID Connect official resources
- Stripe API idempotency docs
- GitHub REST API docs
- Microsoft REST API Guidelines
- Martin Fowler Monolith First
- 本地 backend GitHub 项目分析报告

## 关联文件

- rules/backend-layered-architecture-rules.md
- rules/auth-and-permission-rules.md
- rules/ai-backend-design-rules.md
- wiki/checklists/database-design-checklist.md
- wiki/patterns/controller-service-repository-pattern.md
