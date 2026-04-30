# gstack Raw Analysis Report

**分析日期**: 2026-04-30
**分析人**: 通用项目收录员 (Claude Code)
**项目版本**: v1.21.1.0

---

## 1. 项目一句话定位

gstack 将 Claude Code 变成一支虚拟工程团队——CEO 重新思考产品、工程经理锁定架构、设计师抓出 AI 视觉垃圾、审查员发现生产 bug、QA 打开真实浏览器测试、安全官跑 OWASP+STRIDE 审计、发布工程师完成 PR——全部 23 个专家角色，以 slash command + Markdown 驱动，免费，MIT 开源。

## 2. 为什么不是普通 prompt，而是 agentic software delivery workflow

gstack 与普通 prompt 的本质区别：

| 维度 | 普通 Prompt | gstack |
|------|-----------|-------|
| 角色 | 通用助手 | 23 个专业角色，每个有专属方法论 |
| 流程 | 单次问答 | Think→Plan→Build→Review→Test→Ship→Reflect 全流程 |
| 状态传递 | 无 | 上一步产出自动喂养下一步 |
| 质量闸门 | 无 | CEO/设计/工程/DX/安全 多重审查 gate |
| 跨模型 | 单模型 | Claude + Codex 交叉审查 |
| 浏览器 | 无或简陋 | 真实 Chromium，持久化会话，反 bot 隐身 |
| 安全 | 无 | 3 层 prompt injection 防御 |
| 团队 | 单人 | 多人共享，auto-update，版本统一 |

## 3. Think → Plan → Build → Review → Test → Ship → Reflect 流程

每个阶段有明确的技能入口：

```
Think:   /office-hours        → 需求重定义，6 个强制问题
Plan:    /plan-ceo-review     → CEO 视角挑战范围
         /plan-eng-review     → 架构锁定 + 数据流图
         /plan-design-review  → 设计维度评分 0-10
         /plan-devex-review   → DX 审查，20-45 个强制问题
         /autoplan            → 一键跑完 CEO→设计→工程→DX
Build:   (Claude Code 正常实现)
Review:  /review              → Staff Engineer PR 审查
         /codex               → OpenAI Codex 独立审查
         /design-review       → 设计审计 + 修复
         /devex-review        → 实时 DX 审计
         /cso                 → OWASP + STRIDE 安全审计
Test:    /qa                  → 真实浏览器 QA + 自动修复
         /qa-only             → 纯报告模式
         /benchmark           → 性能基准
Ship:    /ship                → 测试→审查→push→PR
         /land-and-deploy     → merge→CI→部署→验证
         /canary              → 部署后监控
         /document-release    → 自动更新全部文档
Reflect: /retro               → 周回顾，个人/全局
         /learn               → 跨会话知识积累
```

## 4. CEO / Designer / Engineering Manager / Release Manager / Doc Engineer / QA 角色分工

| 角色 | 技能 | 核心职责 |
|------|------|---------|
| CEO / Founder | plan-ceo-review | 重新思考问题，4 种范围模式 |
| Eng Manager | plan-eng-review | 架构、数据流、边界条件、测试矩阵 |
| Senior Designer | plan-design-review, design-review, design-html, design-shotgun, design-consultation | 完整设计管线：咨询→探索→审计→实现 |
| DX Lead | plan-devex-review, devex-review | 开发者体验审查 + 实时审计 |
| Staff Engineer | review | 深度代码审查，自动修复明显问题 |
| QA Lead | qa, qa-only, browse | 真实浏览器测试、回归测试自动生成 |
| Security Officer | cso | OWASP Top 10 + STRIDE 威胁建模 |
| Release Engineer | ship, land-and-deploy | 同步→测试→push→PR→merge→部署 |
| SRE | canary | 部署后监控：console 错误、性能退化 |
| Technical Writer | document-release | 全部文档自动更新 |
| Debugger | investigate | 系统化根因分析，3 次修复失败则停止 |

## 5. Claude Code / Codex / OpenClaw 相关能力

- **Claude Code**: 主运行环境，所有 23 个技能均为 Claude Code skills
- **Codex CLI**: `/codex` 技能调用 OpenAI Codex 做独立审查，支持 review/adversarial/consultation 3 种模式
- **OpenClaw**: ACP 协议自动路由，4 个原生 OpenClaw 技能（office-hours, ceo-review, investigate, retro）
- **多平台支持**: setup 脚本自动检测 10 种 AI agent（Claude Code, Codex, OpenCode, Cursor, Factory, Slate, Kiro, Hermes, GBrain, OpenClaw）
- **跨模型交叉审查**: Claude + Codex 同时审查同一分支时，自动生成交叉分析报告（重叠发现 vs 独有发现）

## 6. review gate / QA gate / ship gate / retro loop 机制

- **review gate**: `/review` 做代码审查，自动修复明显问题，标记完整度缺陷
- **QA gate**: `/qa` 在真实浏览器中点击流程，发现问题→原子提交修复→回归测试→重新验证
- **ship gate**: `/ship` 同步 main→运行测试→审查覆盖率→push→打开 PR；`/land-and-deploy` merge→等 CI→部署→验证
- **retro loop**: `/retro` 团队感知的周回顾，个人/全局两种模式；`/learn` 跨会话知识积累
- **autoplan pipeline**: `/autoplan` 一键完成 CEO→设计→工程→DX 审查，自动检测哪些 review 适用

## 7. browser QA / persistent browser / 自动化验证思想

- **GStack Browser**: 基于 Chromium 的持久化浏览器，反 bot 隐身（Google、NYTimes 无验证码）
- **持久化会话**: 浏览器在窗口打开期间保持存活，无空闲超时
- **Sidebar Agent**: 自然语言驱动的浏览器助手，自动路由 Sonnet（快速操作）和 Opus（读取分析）
- **Cookie 导入**: 从 Chrome/Arc/Brave/Edge 导入真实浏览器 cookie 到 headless 会话
- **Handoff 机制**: 遇到 CAPTCHA 时，`$B handoff` 打开可见浏览器在同一页面，解决后 `$B resume` 恢复
- **Domain Skills**: agent 保存每个站点的知识笔记，下次自动激活
- **原始 CDP 逃生舱**: 白名单制的 raw CDP 访问

## 8. skills / commands / agents 的组织方式

- **模板驱动**: 每个 SKILL.md 由 `.tmpl` 模板文件生成，通过 `bun run gen:skill-docs` 编译
- **多 host 支持**: 同一模板可生成 Claude Code、Codex、OpenCode 等不同格式
- **目录组织**: 每个技能一个目录，内含 SKILL.md（生成）、SKILL.md.tmpl（模板）、辅助文件
- **agents/** 目录: 存放 agent 配置（如 openai.yaml）
- **lib/**: 共享 TypeScript 库
- **browse/**: 浏览器 daemon 独立目录（含 CLI、server、test）
- **bin/**: 全局 CLI 工具（gstack-global-discover, gstack-model-benchmark 等）
- **scripts/**: 构建/生成/分析脚本

## 9. 对通用项目开发流程的价值

1. **标准化开发流程**: Think→Plan→Build→Review→Test→Ship→Reflect 是适用于任何软件项目的完整流程
2. **角色化 agent 协作**: 23 个专业角色的设计模式可直接应用于其他 agent workflow
3. **质量闸门自动化**: 多级 review gate 模式确保质量不依赖个人自觉
4. **跨模型验证**: Claude + Codex 双模型交叉审查提高了 bug 发现率
5. **浏览器集成测试**: 真实浏览器 QA 让 agent 能感知 UI 层面的问题
6. **持续学习循环**: retro + learn 机制让 agent 在项目中越用越聪明

## 10. 对 UI / 后端 / 自动化 / AI 助手项目的可迁移价值

| 项目类型 | 可迁移价值 |
|---------|-----------|
| Web 前端 | 设计审查管线、浏览器 QA、design-shotgun 多方案探索、design-html 生产级输出 |
| 后端/API | 工程审查、安全审计、测试覆盖率自动化、devex-review DX 审计 |
| 浏览器自动化 | GStack Browser 持久化会话、domain skills 站点知识、CDP 逃生舱 |
| AI 助手 | 角色化 agent 技能体系、多 agent 协调、跨模型交叉验证 |
| 桌面应用 | qa 浏览器测试方法、ship 发布流程、document-release 文档同步 |

## 11. 许可证、依赖、安全边界和平台限制

- **许可证**: MIT — 完全自由使用、修改、分发
- **运行时**: Bun 1.0+, Node.js (Windows 上 Playwright 兼容性需要)
- **核心依赖**: Playwright, Puppeteer, @huggingface/transformers, @ngrok/ngrok, marked
- **平台**: macOS 原生支持，Windows 11 (Git Bash/WSL)，Linux
- **安全风险**:
  - Playwright/Puppeteer 浏览器沙箱依赖操作系统安全
  - ngrok tunnel 在 pair-agent 中暴露本地端口到公网
  - 大量权限需求（文件系统读写、网络、浏览器驱动）
- **隐私**: 遥测默认关闭，需显式 opt-in

## 12. 哪些内容只适合作为启发，不建议原样复制进数据库规则

- 具体的 SKILL.md 提示词文本（设计为 Claude Code skills 的上下文，不适合直接翻译为 OpenClaw/Codex 规则）
- yarn.lock/bun.lock（锁定文件，不适合作为知识沉淀）
- 具体的 Chrome DevTools Protocol 白名单配置（项目特定）
- 遥测基础设施（Supabase schema、edge functions）
- CI/CD 配置（.github/workflows, .gitlab-ci.yml）
- 团队模式 auto-update 机制的具体实现
