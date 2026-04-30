# 后端系统设计模式 —— 从互联网架构案例提炼

> 生成时间：2026-04-30
> 数据来源：`raw/github/repos/architecture.of.internet-product` + backend domain 现有 rules
> 目标：提炼可复用的通用架构模式，覆盖 Agent 开发后端项目的最常见场景

## 一、总览：模式地图

```
                    ┌──────────────────────────────┐
                    │      API 网关 / 接口层        │
                    │  认证、限流、路由、版本管理     │
                    └──────────┬───────────────────┘
                               │
               ┌───────────────┴───────────────┐
               │                               │
    ┌──────────┴──────────┐        ┌──────────┴──────────┐
    │    同步服务层         │        │    异步任务层         │
    │  分层架构 (CSR)       │        │  消息队列 + Worker    │
    │  模块化服务拆分        │        │  失败重试 + 幂等      │
    └──────────┬──────────┘        └──────────┬──────────┘
               │                               │
    ┌──────────┴──────────┐        ┌──────────┴──────────┐
    │     数据持久层        │        │    文件与元数据        │
    │  读写分离/分库分表     │        │  对象存储 + DB 索引    │
    │  缓存策略 (多级缓存)   │        │  异步处理 + CDN       │
    └─────────────────────┘        └─────────────────────┘
               │                               │
    ┌──────────┴───────────────────────────────┴──────────┐
    │                   可观测性层                           │
    │    结构化日志 → 集中收集 → 监控告警 → 链路追踪          │
    └─────────────────────────────────────────────────────┘
```

## 二、核心模式详解

### P1 — 分层架构 (Controller-Service-Repository)

**来源：** eBay 架构演进、微博架构、backend rules (`backend-layered-architecture-rules.md`)

```
Request → Controller (参数校验/权限) → Service (业务逻辑) → Repository (数据访问) → DB
                                            ↕
                                        外部服务 / 消息队列
```

**关键原则：**
- Controller 层只做参数校验和响应格式化，不写业务逻辑
- Service 层是事务边界，一个业务操作 = 一个 service method
- Repository 层抽象数据访问，方便替换存储实现
- 跨层依赖只向下（Controller → Service → Repository），不反向

**适用场景：** API 服务、管理后台、小程序后端、AI 工具后台

**来自仓库的实战案例：**
- 京东应用架构设计（服务层 + 数据层分离）
- eBay 架构演进（从单体到分层服务）

---

### P2 — 模块化服务拆分

**来源：** 微博平台架构、滴滴架构演进、backend rules (`backend-layered-architecture-rules.md`)

**拆分原则：**
1. 按业务域拆分（用户/订单/文件/通知）
2. 模块间通过明确接口通信，不共享数据库
3. 每个模块独立可部署/可测试
4. 新项目从单体开始，不做过早微服务拆分

```
单项目多模块                →     多服务（仅在必要时）
src/                         svc-user/
├── user/                    svc-order/
├── order/                   svc-file/
├── file/                    svc-notification/
├── notification/            (仅当模块间需要独立扩缩容/部署时才拆分)
└── shared/
```

**适用场景：** 从小项目演进到中大型项目时的自然过渡

**来自仓库的实战案例：**
- 豆瓣架构演进（从单体到模块化）
- 滴滴架构演变（业务增长驱动架构拆分）

---

### P3 — 异步任务队列

**来源：** Kafka/RabbitMQ 资料、backend rules (`performance-and-stability-rules.md`)

```
请求 → 快速响应 202 Accepted
         │
         └→ 消息队列 (Redis/Kafka/RabbitMQ)
               │
               └→ Worker 异步处理 → 结果存储 → 客户端轮询/Webhook 通知
```

**设计要点：**
- 消息体包含 task_id + 必要参数，保持轻量
- Worker 必须实现幂等（同一条消息消费多次结果一致）
- 失败重试：指数退避 (1s → 2s → 4s → 8s)，最大重试次数
- 死信队列兜底（超过最大重试的消息进入死信，人工处理）

**适用场景：** 文件处理、数据导入导出、邮件发送、AI 推理、定时报表

**来自仓库的实战案例：**
- `Kafka深度解析.pdf` — 消息队列架构原理
- `RabbitMQ使用参考-YS.pdf` — 消息队列实践
- `网易IM云千万级并发消息处理能力的架构设计与实践.pdf`

---

### P4 — 多级缓存策略

**来源：** 微博 Redis 优化、Redis/Memcached 资料、backend rules (`performance-and-stability-rules.md`)

```
请求 → 本地缓存 (内存/LRU) → Redis 集群 → DB
         TTL: 秒级              TTL: 分钟级    (持久化)
```

**各级作用：**
| 级别 | 技术 | TTL | 适用数据 |
|------|------|-----|---------|
| L1 本地 | `cachetools`/`lru_cache` | 1-10s | 配置/元数据/热点数据 |
| L2 Redis | Redis String/Hash | 1-30min | 用户 session/查询结果/API 响应 |
| L3 DB | PostgreSQL/MySQL | 永久 | 业务核心数据 |

**缓存更新策略：** Cache-Aside（读时填充，写时失效）

**适用场景：** 所有有查询压力的后端服务

**来自仓库的实战案例：**
- `微博Cache架构设计实践-陈波.pdf`
- `Redis在京东到家的订单中的使用.pdf`
- `Redis实现分析.pdf`
- `高性能Web架构之缓存体系-赵舜东.pdf`

---

### P5 — 数据库读写分离与索引设计

**来源：** MySQL/InnoDB/TiDB 资料、backend rules (`database-modeling-rules.md`)

```
写请求 → Primary DB (Master)
              │ (复制)
读请求 → Replica DB (Slave) × N
```

**通用索引原则：**
- 高频 WHERE 条件列建索引
- 复合索引按区分度高到低排列
- 避免在索引列上做函数运算
- 定期分析慢查询并优化

**适用场景：** 读多写少的应用（管理后台、数据面板、API 服务）

**来自仓库的实战案例：**
- `Buffer Pool Implementation InnoDB vs Oracle.pdf`
- `网易-数据库系统的优化与调优：从理论到实践.pdf`
- `TiDB在Kubernetes平台的自动化运维实践.pdf`

---

### P6 — 日志、监控与告警

**来源：** 日志系统资料、backend rules (`error-handling-and-logging-rules.md`)

```
服务实例 → 结构化日志 (JSON) → 日志收集 (ELK/Loki)
                │
         Metrics (Prometheus) → Grafana 面板
                │
         Trace (OpenTelemetry) → Jaeger/Zipkin
```

**日志最佳实践：**
- 全部使用结构化日志 (JSON 格式)
- 每条日志包含：timestamp, level, service, trace_id, message, context
- ERROR 日志必须包含足够的上下文用于排查（不要只写 "error occurred"）
- 敏感信息（密码/Token）不写入日志

**适用场景：** 所有后端服务（生产环境必备）

**来自仓库的实战案例：**
- `唯品会日日志平台建设.pdf`
- `百度-海量日志分析架构.pdf`
- `ngx_lua在又拍云的应用-日志收集及作用.pdf`

---

### P7 — 文件与元数据管理

**来源：** 分布式文件系统资料、backend rules

```
上传请求 → API 校验 (大小/类型) → 对象存储 (本地/OSS/S3)
                                      │
                              元数据 (文件名/大小/hash/路径) → DB
```

**设计要点：**
- 文件实体存储与元数据存储分离
- 元数据包含 SHA-256 content hash（去重和完整性校验）
- 大文件分块上传 + 断点续传
- 临时文件定期清理

**适用场景：** 资料收集入库系统、个人 AI 数据库系统、文件管理系统

**来自仓库的实战案例：**
- `GlusterFS分布式文件系统.pdf`
- `云存储系统设计.pdf`
- `OceanBase1.pdf`

---

### P8 — API 网关与接口设计

**来源：** backend rules (`api-design-rules.md`)

```
客户端 → API 网关 (统一入口)
           ├── 认证/鉴权
           ├── 限流
           ├── 请求/响应转换
           ├── 路由到后端服务
           └── 日志/监控
```

**接口设计规范：**
- RESTful 风格：`GET /users/{id}`, `POST /users`, `PUT /users/{id}`, `DELETE /users/{id}`
- 分页规范：`?page=1&page_size=20`
- 统一响应格式：`{"code": 0, "data": {...}, "message": "ok"}`
- 版本策略：`/api/v1/...`

**适用场景：** 所有有 API 的后端服务

---

### P9 — 事件驱动与最终一致性

**来源：** 分布式系统论文、eBay/Amazon 架构

```
服务 A 完成操作 → 发布事件 → 消息队列
                                │
                   ┌────────────┴────────────┐
                   │                         │
              服务 B 订阅                  服务 C 订阅
              (更新搜索索引)               (发送通知)
```

**适用条件：**
- 跨服务的数据一致性要求不严格（最终一致即可）
- 需要解耦的业务操作（如订单完成 → 发通知 + 更新统计）

**不适用场景：** 强一致性要求的操作（账户余额扣减）

**来自仓库的实战案例：**
- `Life-Beyond-Distributed-Transactions.pdf`
- `amazon_dynamo_sosp2007.pdf`（最终一致性经典设计）

---

### P10 — 插件化架构

**来源：** 通用软件架构模式、backend rules

```
核心引擎
├── 插件接口 (Protocol/Interface)
├── 插件注册表 (Registry)
├── 插件 A: 功能扩展
├── 插件 B: 功能扩展
└── 插件 C: 功能扩展
```

**适用场景：** 桌面 AI 助手（小黄）、资料采集系统、自动化工具链

**来自仓库的实战案例：**
- `Software Architecture in Industrial Applications.pdf`
- `4+1view-architecture.pdf`

---

## 三、模式选择决策树

```
需要 API？ → 分层架构 (P1) + 接口设计 (P8)
需要文件处理？ → 异步任务队列 (P3) + 文件元数据管理 (P7)
需要高查询性能？ → 多级缓存 (P4)
需要高写入量？ → 读写分离 (P5)
需要跨服务通信？ → 事件驱动 (P9) 或 同步 API (P1)
需要扩展性？ → 模块化拆分 (P2) 或 插件化 (P10)
上线生产？ → 日志监控 (P6) + 安全 (P8 认证部分)
```

## 四、模式组合示例

### 例 1：资料收集入库系统

```
P1 (分层架构) → P3 (异步任务：采集+处理+入库)
              → P7 (文件元数据：原始文件 + DB 索引)
              → P6 (日志：采集状态 + 错误追踪)
```

### 例 2：桌面 AI 助手后端

```
P1 (分层架构) → P8 (API 设计：语音/文字接口)
              → P3 (异步任务：AI 推理)
              → P4 (缓存：对话上下文)
              → P10 (插件化：技能扩展)
```

### 例 3：管理后台

```
P1 (分层架构) → P8 (API + 权限)
              → P4 (缓存：仪表盘数据)
              → P5 (读写分离：报表查询)
              → P6 (日志：操作审计)
```

## 五、与其他 backend 文档的关系

- `backend-layered-architecture-rules.md` — P1 的详细工程化规范
- `database-modeling-rules.md` — P5 的详细实践指南
- `api-design-rules.md` — P8 的接口设计规范
- `error-handling-and-logging-rules.md` — P6 的实现参考
- `auth-and-permission-rules.md` — P8 认证部分的细则
- `performance-and-stability-rules.md` — P3/P4 的性能规范
