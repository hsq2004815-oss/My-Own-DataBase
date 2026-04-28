# ui_design

UI 设计专题知识域。

## 内容范围
- 设计规范
- 品牌风格
- 组件与界面参考
- 设计案例与总结

## 数据流
raw -> processed -> wiki -> output

## 说明
- raw: 原始资料、网页、文档、图片、仓库
- processed: 清洗文本、分块、元数据、版本
- wiki: 沉淀后的长期知识
- output: 草稿、答案、报告、最终稿
- registry: 数据源、文件索引、标签体系

## 默认 UI 生成策略

普通 UI、前端、landing page、SaaS 官网、portfolio 和产品页任务，优先读取高级审美总规则，再结合具体 page_type、组件 reference 和用户 brief。

默认优先级：

1. `wiki/topics/premium-web-ui-initial-aesthetic-rules.md`
2. `wiki/topics/liquid-glass-design-system.md`
3. `wiki/topics/liquid-glass-web-app-ui-kit.md` for Web App / SaaS Workspace / Dashboard component systems
4. `wiki/topics/cinematic-video-hero-rules.md`
5. `wiki/topics/premium-typography-and-layout-rules.md`
6. `wiki/topics/motion-interaction-premium-rules.md`
7. `wiki/topics/landing-page-section-patterns.md`

`design-*.md` 品牌文件作为参考，不作为默认高级审美核心。如果品牌 topic 信息不足，不要让它覆盖 premium rules。具体业务页面再结合 page_type、component references、素材授权状态和用户 brief。

注意：`liquid-glass-web-app-ui-kit.md` 属于高级 Web App / Dashboard / Workspace 组件系统，不是普通 landing page 规则。任务出现 AI Project Workspace、SaaS dashboard、workspace UI、app UI kit、搜索/标签/卡片/弹窗/校验/toast 等需求时优先使用它。
