# Backend Processed Retrieval Preparation

`domains/backend/processed` 存放 backend 领域从 raw 分析到后续检索索引之间的中间产物。本目录当前处于 Phase 2C retrieval preparation 阶段。

- `processed/cleaned_text/github_projects` 是项目分析 Markdown。
- `processed/metadata/github_projects` 是项目分析 metadata。
- `processed/chunks/github_projects` 是项目级 chunks。
- `processed/chunks/retrieval_ready/backend-retrieval-chunks.jsonl` 是下一阶段检索索引输入。
- `processed/manifest/backend-content-inventory.json` 是内容总清单。
- `processed/manifest/backend-chunk-manifest.json` 是 chunk 统计和质量检查。
- `processed/manifest/backend-retrieval-routing-map.json` 是任务路由映射。

当前阶段不包含真实 SQLite 索引，不包含 BM25/vector index，不包含 embedding，也不包含 `backend_api` 或 `/brief` 接入。Phase 2D 才能作为单独任务读取 JSONL、构建 SQLite/BM25，并接入本地 API。
