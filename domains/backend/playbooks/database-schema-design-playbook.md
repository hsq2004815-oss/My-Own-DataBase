# Database Schema Design Playbook

PostgreSQL / SQLite / MySQL schema design with constraints, indexes, and migration planning.

## When to use

- Designing new tables or schemas
- Adding indexes, constraints, migrations
- User mentions "数据库", "表结构", "schema", "索引", "migration", "DDL", "RBAC"

## Read first

- `domains/backend/AGENT_USAGE.md`
- `domains/backend/rules/database-modeling-rules.md`
- `domains/backend/wiki/checklists/database-design-checklist.md`
- `domains/backend/wiki/topics/database-modeling-and-indexing.md`

## Required outputs

For every schema task, produce ALL of these:

1. **Entity list** — what are the nouns? (User, Order, Product, etc.)
2. **Table definitions** — per table: columns, types, defaults, nullable
3. **Primary keys** — UUID or serial? Composite?
4. **Foreign keys** — explicit REFERENCES with ON DELETE policy
5. **Unique constraints** — beyond PK, what can't repeat?
6. **Indexes** — which queries need them? Composite where needed
7. **Audit fields** — `created_at`, `updated_at` on every table
8. **Soft delete policy** — `deleted_at` or explicit archive table?
9. **RBAC boundary** — which tables need row-level or column-level access control?
10. **Migration plan** — forward + rollback, not just "run this SQL"
11. **Data integrity risks** — circular FKs, cascade depth, NULL meaning
12. **Typical query patterns** — what queries will hit this schema most?

## Anti-patterns

| Don't | Do instead |
|-------|-----------|
| Field list without types/constraints | Full DDL with NOT NULL, DEFAULT, CHECK |
| No indexes beyond PK | Index on FK columns and query predicates |
| JSON column for structured data | Normalize into tables unless truly schema-less |
| No audit fields | `created_at`, `updated_at` on every table |
| No migration/rollback plan | Forward migration + explicit rollback |
| Premature multi-tenant complexity | Start single-tenant; add tenant_id only when needed |
| Permissions as afterthought | Define RBAC boundary before coding endpoints |

## Completion check

- [ ] Every table has a PRIMARY KEY
- [ ] Every FK column has an index
- [ ] Unique constraints declared, not enforced only in app code
- [ ] Audit fields present
- [ ] Soft delete policy explicit
- [ ] Migration forward AND rollback written
- [ ] Query patterns documented (not just "the app will query this")
