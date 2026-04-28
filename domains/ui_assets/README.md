# UI Assets

这个知识域用于管理 UI 素材资产：背景、动态视频、纹理、窗口/卡片、按钮/控件、图标、截图参考和组件文件。

`ui_assets` 和 `ui_design` 分工不同：

- `ui_design`: 设计规则、审美原则、实现提示。
- `ui_assets`: 可直接使用或仅供参考的本地素材文件，以及每个素材的 metadata、授权状态和适用场景。

## 目录

- `raw/review_required`: 新导入但尚未确认授权/用途的素材，默认进入这里。
- `raw/direct_use`: 确认可直接用于项目的素材，例如自制、生成、已授权、开源可用素材。
- `raw/inspiration_only`: 只能作为风格参考，不能复制到最终项目的截图、视频或界面参考。
- `raw/internal_reference`: 内部分析用素材。
- `processed/metadata`: 每个素材对应的 JSON metadata。
- `processed/thumbnails`: 后续生成缩略图的位置。
- `processed/chunks`: 后续给检索系统使用的素材摘要 chunks。
- `registry`: 来源清单、导入日志、去重报告。

## 导入素材

先把素材下载到任意临时文件夹，例如：

```powershell
E:\IncomingAssets
```

然后运行：

```powershell
python E:\DataBase\scripts\ui_assets\ingest_assets.py E:\IncomingAssets
```

默认行为：

- 复制文件，不移动源文件。
- 按扩展名和文件名关键词粗分类。
- 生成 `processed/metadata/*.json`。
- 默认 `usage_policy=review_required`，避免把未知授权素材误当可直接使用。

确认授权后，可以重新导入时指定：

```powershell
python E:\DataBase\scripts\ui_assets\ingest_assets.py E:\IncomingAssets --usage-policy direct_use --license "owned/generated/open license"
```

## 使用策略

- `direct_use`: AI 可以把本地文件路径用于项目。
- `inspiration_only`: AI 只能学习风格，不能复制素材到项目。
- `internal_reference`: 内部分析或审美参考。
- `review_required`: 尚未确认，不能直接用于项目。
- `unknown`: 来源或授权不清楚，不能直接用于项目。

## 检索增强

已导入的 `raw/inspiration_only/screenshots` 和 `raw/inspiration_only/videos` 可以用 metadata 增强脚本补充检索字段：

```powershell
python E:\DataBase\scripts\ui_assets\enrich_metadata.py
```

该脚本只更新 `processed/metadata` 和 `processed/chunks`，不会移动或复制 raw 素材。

- Screenshots 会补充 `dark-cinematic`、`liquid-glass`、`floating-navbar`、`giant-typography`、`bento-grid`、`dashboard-preview`、`editorial-layout`、`portfolio-inspiration`、`SaaS-hero` 等标签。
- Videos 会补充 `motion-reference`、`hero-background`、`ambient-motion`、`cinematic-loop`、`glass-refraction`、`particle-background`、`gradient-motion` 等标签。
- Lottie collection 会保持 collection-level，不强行逐个索引文件；当前生成 loading、micro interaction、hover motion、JSON web animation、animated icon 和 implementation notes summary chunks。
- `inspiration_only` 只能作为风格参考，不得复制到项目；没有 `direct_use` 授权时，agent 应用 CSS、SVG、Canvas、WebGL 或自有/生成素材复刻风格。
- `review_required` 不能默认直接商用；Lottie 直接使用前必须确认 license。
