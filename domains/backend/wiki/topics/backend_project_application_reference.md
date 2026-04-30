# 后端项目应用参考 —— 对 6 类项目的架构启发

> 生成时间：2026-04-30
> 数据来源：`raw/github/repos/architecture.of.internet-product` + backend domain 知识库
> 目标：为未来开发不同类型项目时提供可直接参考的架构模式和仓库资料索引

## 一、小黄桌面 AI 助手

### 1.1 项目特点
- Windows 桌面应用 + Python 后端
- 语音唤醒 → STT → AI 处理 → TTS → UI 展示
- 需要离线能力（至少核心链路）
- 插件化扩展（未来技能）

### 1.2 核心模式

| 模式 | 来自仓库的参考 | 应用方式 |
|------|-------------|---------|
| **插件化架构** | `Software Architecture in Industrial Applications.pdf`, `4+1view-architecture.pdf` | 技能系统设计：核心引擎 + 技能插件接口 |
| **异步任务** | `Kafka深度解析.pdf`（模式，非直接使用） | 语音→STT→AI 每一步是异步任务，用简单队列调度 |
| **多级缓存** | `Redis实现分析.pdf`, `高性能Web架构之缓存体系.pdf` | 对话上下文缓存、热词缓存 |
| **进程间通信** | — | JSON-RPC over stdio（现有方案，无需仓库资料） |
| **日志系统** | `百度-海量日志分析架构.pdf`（结构化日志思想） | 语音识别链路日志、错误追踪 |

### 1.3 不适用模式
- 微服务拆分（单机桌面应用不需要）
- 读写分离（单用户场景）
- 分布式事务（单机无分布式）

### 1.4 推荐架构

```
Electron 壳 (React UI)
    │ IPC
Python 引擎
    ├── 音频模块 (PyAudioWPatch)
    ├── 唤醒词检测 (ONNX 模型)
    ├── VAD + STT (FunASR SenseVoice)
    ├── AI 对话 (本地/云端 LLM)
    ├── TTS (edge-tts/Piper)
    └── 技能插件系统
            ├── 天气查询
            ├── 文件搜索
            └── (更多...)
```

---

## 二、个人 AI 数据库系统 (My Own DataBase)

### 2.1 项目特点
- FastAPI 后端 + SQLite 检索索引
- 多领域知识库 (UI/自动化/后端/语音)
- 智能体友好 API (brief/search)
- 本地运行，低资源消耗

### 2.2 核心模式

| 模式 | 来自仓库的参考 | 应用方式 |
|------|-------------|---------|
| **分层架构** | `京东应用架构设计.pdf`, `backend-layered-architecture-rules.md` | FastAPI Controller → Service → 检索引擎 |
| **读写分离** | `网易-数据库系统的优化与调优.pdf` | SQLite 写入和检索读分离（WAL 模式） |
| **缓存策略** | `微博Cache架构设计实践.pdf` | 检索结果缓存 (TTL 按数据变化频率调整) |
| **文件元数据管理** | `云存储系统设计.pdf`, `GlusterFS系统原理剖析.pdf` | 素材 metadata + 文件实体分离 |
| **搜索引擎** | `Elasticsearch集群中JVM问题的应对之策.pdf` | FTS5 全文索引设计参考 |

### 2.3 不适用模式
- 消息队列（除非数据量特别大才引入）
- 微服务（单体 FastAPI 足够）
- 分布式数据库（SQLite 本地运行）

### 2.4 推荐架构

```
FastAPI (backend_api/)
    ├── Controller 层 (路由 + 参数校验)
    ├── Service 层 (检索策略 + 排序)
    ├── Repository 层 (SQLite + FTS5)
    │       ├── ui_chunks.db
    │       ├── backend_references.db
    │       ├── ui_assets.db
    │       └── ...
    └── Scripts (brief.py + 各 domain 管线)
```

---

## 三、资料收集入库系统

### 3.1 项目特点
- GitHub 仓库下载 + 分析 + 入库
- 多渠道来源（GitHub / Web / 上传）
- 自动化 pipeline 处理
- 结构化存储和检索

### 3.2 核心模式

| 模式 | 来自仓库的参考 | 应用方式 |
|------|-------------|---------|
| **异步任务队列** | `Kafka深度解析.pdf`, `RabbitMQ使用参考.pdf` | 下载 → 分析 → 生成 metadata → 入库 pipeline |
| **内容哈希去重** | `分布式文件系统` 的思想 | SHA-256 content hash 去重（已在 backend rules 中实现） |
| **日志监控** | `唯品会日日志平台建设.pdf` | 下载状态、分析进度、错误追踪 |
| **幂等设计** | `Life-Beyond-Distributed-Transactions.pdf` | 同一 URL 多次下载幂等处理 |
| **失败重试** | 通用架构实践 | 指数退避 + 死信队列 |

### 3.3 推荐架构

```
采集层 (GitHub/WWW/Upload)
    ↓
消息队列 (简单的 Redis Queue)
    ↓
Worker Pool
    ├── 下载 Worker (git clone / curl)
    ├── 分析 Worker (README/Metadata 提取)
    └── 入库 Worker (SQLite / PostgreSQL)
    ↓
检索层 (FastAPI + FTS5)
```

---

## 四、Windows 工具/自动化工具

### 4.1 项目特点
- 单机 Windows 运行
- 文件处理、批量操作
- GUI + CLI 双模式
- 轻量、快速启动

### 4.2 核心模式

| 模式 | 来自仓库的参考 | 应用方式 |
|------|-------------|---------|
| **插件化架构** | 软件架构经典模式 | 工具功能以插件形式扩展 |
| **文件元数据管理** | 文件系统设计思想 | 批量操作的文件追踪和管理 |
| **结构化日志** | 日志系统设计 | 操作记录和 Undo 支持 |
| **本地缓存** | 缓存策略 | 文件 hash 缓存避免重复处理 |

### 4.3 推荐架构

```
CLI/GUI 入口
    ↓
核心引擎
    ├── 文件处理模块
    ├── 任务队列 (本地)
    ├── 配置管理
    └── 日志/Undo 模块
```

---

## 五、小程序/网页后台

### 5.1 项目特点
- RESTful API 或 GraphQL
- 用户系统（登录/注册/权限）
- 数据库 + 文件存储
- 可能部署到云服务器

### 5.2 核心模式

| 模式 | 来自仓库的参考 | 应用方式 |
|------|-------------|---------|
| **分层架构 (CSR)** | `京东应用架构设计.pdf`, `backend-layered-architecture-rules.md` | 标准三层架构 |
| **API 设计** | 接口设计规范 | RESTful + 分页 + 统一响应格式 |
| **认证授权 (RBAC)** | `auth-and-permission-rules.md` | JWT + refresh token |
| **读写分离** | `网易-数据库系统的优化与调优.pdf` | 读多写少场景 |
| **缓存** | `Redis实现分析.pdf` | 热点数据缓存 |
| **安全** | `backend-security-checklist.md` | SQL 注入/XSS/CSRF 防护 |
| **部署** | `deployment-and-env-rules.md` | Docker Compose + 健康检查 |

### 5.3 推荐架构

```
Nginx (反向代理 + HTTPS)
    ↓
FastAPI / Express (应用层)
    ├── Auth (JWT + RBAC)
    ├── Business Logic
    └── Data Access
    ↓           ↓
PostgreSQL   Redis
(主数据库)    (缓存)
```

---

## 六、后端 API 服务 (通用)

### 6.1 项目特点
- 不限定具体业务
- 可能是微服务中的一个或多个服务
- 需要稳定、可扩展、可运维

### 6.2 核心模式（按优先级排列）

| 优先级 | 模式 | 说明 |
|--------|------|------|
| P0 | 分层架构 (CSR) | 所有后端项目的基础 |
| P0 | 结构化日志 | 没有日志的后端是盲人 |
| P0 | 统一错误处理 | 一致的错误码和错误响应 |
| P0 | 配置管理 | 环境变量 + .env (不提交 secret) |
| P1 | 数据库建模 | 合理的表结构和索引 |
| P1 | API 版本化 | `/api/v1/...` |
| P1 | 认证授权 | 根据项目需要选择 JWT/Session |
| P2 | 缓存 | 仅在确实需要时引入 |
| P2 | 消息队列 | 仅在异步任务量大时引入 |
| P2 | 读写分离 | 仅在读压力大时引入 |
| P3 | Docker 化 | 标准化部署 |
| P3 | CI/CD | 自动化测试和发布 |
| P3 | 健康检查 | `/health` 端点 |

---

## 七、Agent 开发后端项目的默认参考原则

当 Codex / Claude / opencode 协助开发任意后端项目时，应遵循以下默认原则：

### 7.1 架构默认

1. **默认分层架构**：Controller → Service → Repository，不做过早抽象
2. **默认单体优先**：除非用户明确要求微服务，否则从单体起步
3. **默认 RESTful API**：除非有明确的实时需求（WebSocket）或复杂查询需求（GraphQL）
4. **默认 PostgreSQL** 或 **SQLite**（本地小项目 SQLite，多用户/生产 PostgreSQL）
5. **默认 FastAPI (Python)** 或 **Express (Node.js)**，根据项目技术栈选择

### 7.2 编码默认

1. 所有 API 返回统一响应格式
2. 所有错误包含可操作的错误消息
3. 所有日志使用结构化格式 (JSON)
4. 所有外部输入必须校验
5. 所有数据库操作使用参数化查询
6. 不在代码中硬编码 secret/token/password
7. 不引入不需要的依赖

### 7.3 参考优先级

```
生产项目：
  backend rules (api-design, database-modeling, auth, security, deployment)
  → architecture.of.internet-product 对应主题案例
  → 官方文档

学习/研究项目：
  architecture.of.internet-product 案例和论文
  → backend rules
  → 官方文档

Agent 快速生成：
  backend rules (直接指导编码)
  → 仅在需要理解"为什么"时查案例
```

### 7.4 不默认做的事

- 不默认引入微服务、Kubernetes、Service Mesh
- 不默认引入复杂 DDD/CQRS/Event Sourcing
- 不默认引入多租户 SaaS 架构
- 不默认做过早的性能优化
- 不默认引用架构仓库中过时的技术方案

### 7.5 当用户要求"参考大厂做法"时

优先查阅 architecture.of.internet-product 中的：

1. Google/Facebook/eBay/Amazon 案例（国际，通用性强）
2. 微博/百度/京东 案例（国内，实战经验丰富）
3. 经典论文区（50+ 篇，理论支撑）
4. 分布式系统/高可用区（通用架构模式）

避免引用：
- 目录为空的公司案例（淘宝/微信/美团）
- 明显过时的具体技术版本
- PDF/PPT 中无法验证的细节

---

## 八、仓库资料对各项目的价值矩阵

| 项目类型 | 分层架构 | 缓存 | MQ | 分布式 | 日志 | 安全 | DevOps | 插件化 |
|---------|:------:|:----:|:--:|:-----:|:----:|:---:|:-----:|:-----:|
| 小黄 AI 助手 | ● | ○ | — | — | ● | — | — | ● |
| 个人数据库 | ● | ● | — | — | ○ | — | — | — |
| 资料采集入库 | ● | ○ | ● | — | ● | — | — | ○ |
| Windows 工具 | ○ | ○ | — | — | ● | — | — | ● |
| 小程序后台 | ● | ● | ○ | ○ | ● | ● | ● | — |
| 通用 API 服务 | ● | ● | ○ | ○ | ● | ● | ● | — |

● 直接参考 | ○ 可选参考 | — 暂不需要
