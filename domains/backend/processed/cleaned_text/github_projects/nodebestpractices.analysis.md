# nodebestpractices

## 1. 项目定位

- Node.js 最佳实践文档
- 测试和质量规则候选
- 错误处理规则候选
- 安全/生产规则候选
- Dockerfile sample
- 项目结构文档

## 2. 技术栈

- 后端框架：文档示例含 Express
- 数据库：未发现
- ORM：未发现
- migration 工具：未发现
- 认证方式：未发现
- 权限方式：未发现
- 缓存：未发现
- 队列：未发现
- 文件存储：未发现
- 部署方式：Dockerfile example、GitHub Actions 文档流程
- 测试工具：文档覆盖 Jest/测试实践；仓库自身 markdownlint
- 文档工具：README 多语言、sections
- CI/CD：GitHub Actions for docs/lint

## 3. 目录结构观察

- sections 下按 codestyle、docker、errorhandling、performance、production、projectstructure、security、testingandquality 分类。
- README 多语言，内容是规则集合。
- sections/examples/dockerfile 提供 Node Dockerfile 示例。
- 不是业务源码模板。

## 4. API 设计观察

- 非应用项目，未提供 REST API。
- 可作为 API/Express 通用工程实践背景，不是接口设计源码证据。

## 5. 数据库设计观察

- 未发现数据库/ORM/migration。
- 不适合数据库规则来源。

## 6. 鉴权和权限观察

- 未发现项目级 JWT/Session/RBAC。
- 安全章节可作为 checklist 背景，但不提供权限实现样本。

## 7. 错误处理和日志观察

- sections/errorhandling 覆盖错误流程测试等实践。
- 适合作为错误处理规则的外部社区支持来源。
- 无项目运行日志实现。

## 8. 部署和环境变量观察

- sections/docker 与 Dockerfile example 可参考。
- 不是完整 compose/backend deploy 模板。

## 9. 测试和质量观察

- 文档强调测试命名、AAA、CI、middleware 测试等。
- 仓库自身主要是 markdownlint。
- 对核心规则库价值高，对模板代码价值低。

## 10. 可提炼规则

- 规则 1：Node 核心规则应强调错误流程测试、CI、Docker layer caching、非 root/small image 等生产实践。
  - 来源观察：nodebestpractices sections 覆盖 errorhandling、testingandquality、docker、production。
  - 适合场景：Node/Express/NestJS 通用规则。
  - Agent 生成代码时应该怎么做：生成错误中间件测试、CI lint/test、Dockerfile 多阶段/缓存/非 root，不只生成业务代码。
- 规则 2：最佳实践文档只能支持通用 rules，不能替代具体项目模板。
  - 来源观察：该仓库是文档集合，express-ts-pg-prisma 和 NestJS 项目提供源码证据。
  - 适合场景：规则交叉验证。
  - Agent 生成代码时应该怎么做：将文档规则与实际项目结构共同满足后再提升为核心规则。

## 11. 不建议照搬的地方

- 不要把文档仓库当完整 Express 模板。
- 部分示例 Node 版本较旧，只取原则不照搬版本。
- 没有数据库/鉴权源码。

## 12. 适合进入哪些知识库文件

- rules/backend-security-checklist.md：安全章节可支持 checklist。
- rules/error-handling-and-logging-rules.md：错误流程测试和错误处理最佳实践可入候选。
- rules/deployment-and-env-rules.md：Docker/production 建议可支持 Node 部署规则。
- rules/backend-project-template-rules.md：通用 Node 项目结构/质量建议可作背景来源。

## 13. 项目质量评分

- README 清晰度：5/5
- 目录结构清晰度：4/5
- 测试完整度：0/5
- Docker / 部署完整度：3/5
- 数据库迁移完整度：0/5
- 权限系统完整度：0/5
- 日志异常完整度：4/5
- 对个人项目的参考价值：4/5
- 对中型项目的参考价值：4/5
- 是否适合进入核心规则库：5/5

trust_level：`core_reference`
