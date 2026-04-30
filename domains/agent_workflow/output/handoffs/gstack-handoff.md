# gstack Handoff

## 项目来源
- **GitHub**: https://github.com/garrytan/gstack
- **License**: MIT
- **主语言**: TypeScript (Bun runtime)
- **主 domain**: agent_workflow
- **副 domain**: automation, backend
- **收录路径**: `E:\DataBase\domains\agent_workflow\raw\github_projects\gstack`
- **克隆方式**: `git clone --depth=1`
- **是否使用数据库中的加速克隆工具**: 否。数据库中 dev_tools 域有 fgit/fastgit/gh-proxy 规则文档，但无可执行工具安装在系统中。使用普通 git clone 直接成功。

## 项目定位
将 Claude Code 变成一支 23 人的虚拟工程团队，覆盖 Think→Plan→Build→Review→Test→Ship→Reflect 完整软件交付流程。让单个 builder + AI agent 团队达到传统 20 人团队的产出。

## 核心能力
- 23 角色虚拟工程团队（CEO/Eng Manager/Designer/QA/Security/Release/SRE/Writer）
- Think→Plan→Build→Review→Test→Ship→Reflect 7 阶段工作流
- 真实浏览器 QA（持久化 Chromium + 反 bot + 自然语言 sidebar）
- 多重审查闸门（CEO/设计/工程/DX/安全）
- 跨模型交叉验证（Claude × OpenAI Codex）
- 多 agent 浏览器协调（pair-agent）
- 完整设计管线（consultation→shotgun→HTML）
- Prompt injection 3 层防御
- 10 种 AI agent 跨平台支持
- 团队模式 auto-update（无 vendored files）

## 技术栈
- **运行时**: Bun 1.0+ (TypeScript)
- **浏览器**: Playwright, Puppeteer-core
- **ML**: @huggingface/transformers (prompt injection 分类)
- **Tunnel**: @ngrok/ngrok (pair-agent 远程连接)
- **SDK**: @anthropic-ai/claude-agent-sdk, @anthropic-ai/sdk
- **构建**: Bun compile (独立二进制)

## 通用复用价值
gstack 为以下场景提供通用能力：
1. **任何需要多 agent 协作的 AI 工程项目**：角色分工、审查闸门、上下文传递
2. **Web 前端项目**：设计审查管线、浏览器 QA、多方案设计探索
3. **后端/API 项目**：工程审查、安全审计、测试覆盖自动化、DX 审查
4. **浏览器自动化项目**：持久化浏览器 daemon、domain skills、CDP 逃生舱
5. **AI 助手项目**：跨模型验证、agent 知识积累、周回顾机制
6. **开源项目维护**：自动文档同步、发布流程标准化

## 值得沉淀的通用知识
- 角色化 agent 技能体系的设计方法（如何定义角色的职责边界和上下文传递）
- 多阶段质量闸门的工程实践（如何在 agent pipeline 中嵌入审查点）
- 跨模型 agent 交叉验证的价值和局限（两个模型一致 ≠ 绝对正确）
- 持久化浏览器 daemon 的安全架构（沙箱、prompt injection 防御、cookie 管理）
- 模板驱动的跨平台 skill 生成（SKILL.md.tmpl → 多 host 输出）
- Agent 知识积累机制的设计（learn + retro + domain skills 的协同）

## 可迁移到哪些项目类型
- **Web 前端项目**: 设计审查 + 浏览器 QA 管线可直接适配
- **后端/API 项目**: 工程审查 + 安全审计 + DX 审查可直接适配
- **浏览器自动化项目**: GStack Browser daemon 架构可参考
- **桌面助手项目**: 角色化 agent 团队和 7 阶段流程可启发架构设计
- **AI Agent 项目**: 跨模型验证 + agent 知识积累是最直接的迁移价值
- **文档/报告项目**: document-release 自动文档同步模式通用性强

## 可选应用案例：小黄
gstack 可以在以下方面启发小黄未来工程工作流：
- **语音驱动的开发流程**: gstack 已有语音友好触发短语设计，小黄可直接学习其"自然语言 → 正确技能路由"模式
- **角色化 agent 团队**: 如果小黄未来需要管理多个语音 agent 子任务，gstack 的 23 角色分工体系是很好的参考
- **review gate 思想**: 小黄的语音识别结果可以借鉴"多重验证闸门"提高准确率
- **retro + learn**: 小黄的语音交互可以建立类似的"使用历史→偏好学习→质量改进"循环

注意：gstack 主要是 AI 编码 agent 的工作流，小黄是语音桌面助手。角色分工和流程设计思想可迁移，但具体实现完全不同。

## 不建议直接复用的部分
- 具体的 SKILL.md 提示词文本（为 Claude Code 设计，不适合直接翻译为 OpenClaw/Codex 规则）
- GStack Browser 的完整实现（与桌面助手需求不同）
- 遥测基础设施（Supabase schema、edge functions）
- CI/CD 配置（.github/workflows, .gitlab-ci.yml 项目特定）
- Team mode auto-update 机制（依赖 Claude Code 特定 hooks）
- bun.lock 锁定文件
- 测试 fixture 中的安全 benchmark 响应数据

## 安全 / 许可证 / 平台风险
- **许可证**: MIT — 无限制
- **安全风险**: Playwright/Puppeteer 浏览器沙箱依赖操作系统安全；ngrok tunnel 暴露本地端口；需大量权限
- **平台限制**: macOS 原生最佳；Windows 11 需 Git Bash/WSL + 额外 Node.js（Bun Playwright pipe transport bug）
- **大型文件**: 测试目录有 1 个 12MB+ 安全 benchmark fixture（`browse/test/fixtures/security-bench-haiku-responses.json`），非生产代码
- **密钥检查**: .env.example 仅含占位符示例密钥，无真实凭据泄露

## 建议知识集成员生成的数据库文档
- `domains/agent_workflow/wiki/topics/gstack-agentic-development-workflow.md`
- `domains/agent_workflow/wiki/topics/virtual-engineering-team-skills.md`
- `domains/agent_workflow/wiki/patterns/think-plan-build-review-test-ship-reflect.md`
- `domains/agent_workflow/wiki/patterns/role-based-agent-review-gates.md`
- `domains/agent_workflow/wiki/patterns/agent-retro-learning-loop.md`
- `domains/automation/wiki/topics/persistent-browser-daemon-for-agent-qa.md`
- `domains/automation/wiki/patterns/browser-qa-with-persistent-session.md`
- `domains/backend/wiki/topics/agentic-software-delivery-pipeline.md`

## 检索关键词
**中文**: AI 工程工作流、多角色 agent、虚拟工程团队、Claude Code 工作流、Codex 工作流、代码审查、设计审查、浏览器 QA、发布检查、复盘机制、agent 软件交付、AI 辅助开发流程、agent 角色分工、skill 模板驱动、跨模型验证、浏览器自动化测试、安全审计 agent、部署后监控

**英文**: gstack、agentic software delivery、virtual engineering team、Claude Code skills、Codex workflow、review gate、browser QA、ship gate、retro loop、persistent browser daemon、prompt injection defense、cross-model review、design pipeline、pair agent、AI coding workflow、multi-agent coordination、Garry Tan

## 后续集成优先级
★★★★★ (最高 — 对任何 AI agent 项目和开发流程标准化都有直接参考价值)

## 给知识集成员的下一步建议
1. 读取 `E:\DataBase\domains\agent_workflow\output\reports\gstack-raw-analysis-report.md` 了解完整分析
2. 读取 `E:\DataBase\domains\agent_workflow\raw\github_projects\gstack\ARCHITECTURE.md` 了解系统设计决策
3. 读取 `E:\DataBase\domains\agent_workflow\raw\github_projects\gstack\ETHOS.md` 了解 builder 哲学（Boil the Lake, Search Before Building, User Sovereignty）
4. 读取 `E:\DataBase\domains\agent_workflow\raw\github_projects\gstack\BROWSER.md` 了解浏览器系统完整命令参考
5. 从 analysis report 和 chunks 中提取通用知识，生成上方建议的 8 个数据库文档
6. 重点关注以下可跨项目复用的通用模式：
   a. 角色化 agent 团队设计方法论
   b. 多阶段质量闸门的工程实现
   c. 持久化浏览器 daemon 的安全架构
   d. 跨模型交叉验证的价值判断框架
   e. Agent 知识积累机制（learn + retro + domain skills）
7. 不要将 gstack 的具体 SKILL.md 内容原样转为规则——提炼通用方法论，保留可迁移模式
8. 不要修改 `domains/voice_assistant/` 下任何文件——gstack 与小黄无关
