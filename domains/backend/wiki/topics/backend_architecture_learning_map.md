# 后端架构学习地图 —— 从入门到精通的知识路径

> 生成时间：2026-04-30
> 数据来源：`raw/github/repos/architecture.of.internet-product` + backend domain 现有知识库
> 用途：给 Agent 和开发者提供一个分层、分主题的学习路径

## 一、学习路径总图

```
层级 0: 基础编程能力
     │
层级 1: 单机后端 → API 设计、数据库建模、分层架构
     │
层级 2: 分布式基础 → 缓存、消息队列、读写分离、反向代理
     │
层级 3: 分布式进阶 → 共识算法、分布式事务、微服务治理
     │
层级 4: 运维与稳定性 → 日志监控、CI/CD、容器化、安全
     │
层级 5: 专业领域 → AI 后端、实时系统、金融系统、大规模架构
```

## 二、各层级学习资源

### 层级 0：基础编程能力

**前置要求：** 至少熟悉一门后端语言（Python/Go/Node.js/Java）

| 主题 | 仓库资源 | backend domain 规则 |
|------|---------|-------------------|
| Python 高性能编程 | `Python3.5中async_await特性的实现.pdf`, `pygrunn2014.pdf` | — |
| 并发编程基础 | `并发编程实战.pptx` | `performance-and-stability-rules.md` |
| C++ 内存调试 | `Memory-and-C++-debugging-at-EA-2015.pptx` | — |
| 编程语言理论基础 | `fundamental-concepts-in-programming-languages.pdf` | — |

---

### 层级 1：单机后端 —— 地基

**掌握目标：** 能独立开发一个 API 服务、管理后台或小程序后端

| 主题 | 仓库资源 | backend domain 规则 |
|------|---------|-------------------|
| 分层架构 | `京东应用架构设计.pdf` | `backend-layered-architecture-rules.md` |
| API 设计 | `互联网交互设计方法.ppt` (产品层面) | `api-design-rules.md` |
| 数据库建模 | `分布式数据库设计及反范式设计.pdf` | `database-modeling-rules.md` |
| 错误处理 | — | `error-handling-and-logging-rules.md` |
| 认证授权 | `支付应用数据安全标准.pdf` | `auth-and-permission-rules.md` |

**推荐论文（经典必读）：**
- `No Silver Bullet — Essence and Accidents of Software Engineering` (Brooks, 1987) — 理解软件工程的本质复杂性
- `Big Ball of Mud` (Foote & Yoder, 1999) — 理解为什么大多数系统会变乱
- `The Open-Closed Principle` (Meyer, 1988) — 软件可扩展性的基础

---

### 层级 2：分布式基础 —— 支柱

**掌握目标：** 理解分布式系统的基本组件，能设计支撑 10w-100w 用户的服务

| 主题 | 仓库资源 | backend domain 规则 |
|------|---------|-------------------|
| **缓存架构** | `Redis实现分析.pdf`, `微博Cache架构设计实践.pdf`, `高性能Web架构之缓存体系.pdf` | `performance-and-stability-rules.md` |
| **消息队列** | `Kafka深度解析.pdf`, `RabbitMQ使用参考-YS.pdf` | — |
| **读写分离/数据库中间件** | `网易-数据库系统的优化与调优.pdf`, `Codis-intro.pdf` | `database-modeling-rules.md` |
| **反向代理/负载均衡** | `ngx_lua在又拍云的应用.pdf` | — |
| **搜索引擎** | `Elasticsearch集群中JVM问题的应对之策.pdf` | — |

**推荐论文：**
- `Hints for Computer System Design` (Lampson, 1983) — 系统设计智慧集
- `Harvest, Yield, and Scalable Tolerant Systems` (Fox & Brewer, 1999) — CAP 理论前身
- `A Note on Distributed Computing` (Waldo et al., 1994) — 本地 vs 远程的本质区别

---

### 层级 3：分布式进阶 —— 高阶

**掌握目标：** 理解分布式共识、事务、微服务治理，能设计高可用系统

| 主题 | 仓库资源 | backend domain 规则 |
|------|---------|-------------------|
| **共识算法** | `paxos的直观解释.pdf`, `Paxos Made Simple` (论文), `raft.pdf` | — |
| **分布式事务** | `Life-Beyond-Distributed-Transactions.pdf`, `团贷网分布式事务消息.pdf` | — |
| **微服务/服务治理** | `京东服务框架实践.pdf`, `滴滴架构演变及应用实践.pdf` | `backend-layered-architecture-rules.md` |
| **高可用设计** | `高可用可伸缩架构实用经验谈.pdf`, `雪球高可用改造分享.pdf` | — |
| **大规模存储** | `GlusterFS系统原理剖析.pdf`, `OceanBase1.pdf`, `TiDB自动化运维.pdf` | — |

**推荐论文（Google 经典三驾马车 + 后续）：**
- `GFS` (2003) — 分布式文件系统经典
- `BigTable` (2006) — 分布式结构化存储（HBase 前身）
- `MapReduce` (2004) — 分布式计算模型
- `Spanner` (2012) — 全球分布式数据库
- `Dapper` (2010) — 分布式链路追踪（Zipkin/Jaeger 前身）
- `Borg` (2015) — 集群管理（Kubernetes 前身）

---

### 层级 4：运维与稳定性 —— 护城河

**掌握目标：** 能独立运维生产系统、搭建 CI/CD、处理安全事故

| 主题 | 仓库资源 | backend domain 规则 |
|------|---------|-------------------|
| **CI/CD** | `携程-构建可靠的自动化发布体系.pdf` | `deployment-and-env-rules.md` |
| **Docker/K8s** | `深入理解Docker架构与实现.pptx`, `K8S在华为全球IT系统中的实践.pdf` | — |
| **自动化运维** | `滴滴-运维架构演进史.pdf`, `美团云运维体系建设与实践.pdf` | — |
| **安全** | `巡风系统在同程运维安全的实践.pdf`, `YY语音Linux下的主动防御.pdf` | `backend-security-checklist.md` |
| **性能优化** | `Linux Profiling at Netflix.pdf`, `阿里云-网络性能调优.pdf` | `performance-and-stability-rules.md` |
| **日志系统** | `百度-海量日志分析架构.pdf`, `唯品会日日志平台建设.pdf` | `error-handling-and-logging-rules.md` |

---

### 层级 5：专业领域 —— 深度

| 领域 | 仓库资源 |
|------|---------|
| **AI 后端/RAG** | ChatGPT/LLM 论文合集 (~24篇), `用TensorFlow实现智能机器人的原理.pdf` |
| **IM/实时通讯** | `whatsapp技术架构.pdf`, `网易IM云千万级并发.pdf`, `酷狗百万级长连接推送.pdf` |
| **电商/秒杀** | `乐视秒杀：每秒十万笔交易的数据架构解读.pdf`, `eBay架构演进系列` |
| **金融/支付** | `支撑千万亿级交易额的银行云计算架构演进.pdf`, `58到家支付系统架构与实践.pdf` |
| **广告系统** | `百度推荐引擎实践.pdf`, `机器学习在凤巢的深度应用.pdf` |
| **Feed/信息流** | `大数据时代Feed系统架构-杨卫华.pdf`, `微博消息系统架构演进.pdf` |

---

## 三、按角色推荐路径

### 初级后端开发者

**核心：层级 1 → 层级 2**

1. 掌握分层架构 (P1)，能写出结构清晰的 CRUD 代码
2. 理解数据库建模基础，能做单机性能优化
3. 学习缓存和消息队列的基础用法
4. 能使用 Docker 部署自己的服务

**必读论文（3 篇）：**
- No Silver Bullet
- Big Ball of Mud
- Hints for Computer System Design

### 中级后端开发者

**核心：层级 2 → 层级 3**

1. 深入缓存策略（多级缓存、缓存预热/击穿/雪崩）
2. 理解消息队列的内部原理（分区、复制、消费语义）
3. 掌握高可用设计（降级、熔断、限流）
4. 理解分布式共识（至少理解 Paxos/Raft 的基本思想）

**必读论文（5 篇）：**
- GFS + BigTable + MapReduce (Google 三驾马车)
- Paxos Made Simple
- Dynamo (Amazon)

### 架构师

**核心：层级 3 → 层级 4 → 层级 5**

1. 能做系统容量规划和架构决策
2. 理解 CAP/BASE 权衡
3. 设计零停机部署方案
4. 安全架构设计
5. 技术选型与团队组织

**必读论文（10+ 篇）：**
- 上述全部 + Spanner, Dapper, Borg
- The Byzantine Generals Problem
- A Note on Distributed Computing

---

## 四、与 backend domain 现有资源的对照

| 学习目标 | backend domain 资源 | architecture.of.internet-product 资源 |
|---------|-------------------|--------------------------------------|
| 怎么写出规范的 API | `api-design-rules.md` | 京东/微博的架构案例（理解为什么） |
| 怎么设计数据库 | `database-modeling-rules.md` | MySQL/InnoDB/TiDB 优化实战 |
| 怎么做权限系统 | `auth-and-permission-rules.md` | 支付安全标准（安全视角） |
| 怎么部署上线 | `deployment-and-env-rules.md` | 携程/滴滴的运维实战 |
| 怎么做 AI 后端 | `ai-backend-design-rules.md` | ChatGPT/LLM 论文原理 |
| 怎么做消息队列 | — | Kafka 深度解析 + RabbitMQ 参考 |
| 怎么做缓存 | `performance-and-stability-rules.md` | Redis 实现分析 + 微博 Cache 实践 |
| 怎么做日志系统 | `error-handling-and-logging-rules.md` | 百度/唯品会/又拍云日志方案 |

---

## 五、Agent 学习地图使用指南

当 Agent 被问到以下问题时，自动路由到对应层级：

| 用户提问 | 路由到 |
|---------|--------|
| "帮我设计一个 REST API" | 层级 1 + `api-design-rules.md` |
| "这个查询很慢怎么办" | 层级 2 (缓存) + `database-modeling-rules.md` + `performance-and-stability-rules.md` |
| "怎么保证不丢数据" | 层级 3 (分布式事务) + 消息队列 |
| "怎么部署到服务器" | 层级 4 + `deployment-and-env-rules.md` |
| "AI 后端怎么设计" | 层级 5 (AI 后端) + `ai-backend-design-rules.md` |
| "做一个秒杀系统" | 层级 3/5 (高可用/电商) |
| "做一个 IM/消息推送" | 层级 5 (IM/实时通讯) |
