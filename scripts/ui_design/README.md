# UI Design Scripts

这个目录用于维护 UI 设计知识域的采集、清洗、切块、索引脚本。当前脚本都只使用 Python 标准库。

## 已实现脚本

1. `normalize_reference.py`: 校验并规范化 `processed/references/*.json`，确保字段、页面类型、证据等级和检索摘要可用。
2. `make_chunks.py`: 把 reference 记录拆成面向大模型检索的短 chunk，输出到 `domains/ui_design/processed/reference_chunks`。
3. `build_sqlite_index.py`: 把 references 和 chunks 写入 `runtime/db/sqlite/ui_design/ui_design_references.db`，并启用 SQLite FTS5 全文检索。
4. `search_ui.py`: 查询本地 UI 检索库，返回适合给大模型使用的 chunk 摘要。

## 推荐运行顺序

```powershell
python E:\DataBase\scripts\ui_design\normalize_reference.py --check
python E:\DataBase\scripts\ui_design\make_chunks.py
python E:\DataBase\scripts\ui_design\build_sqlite_index.py
python E:\DataBase\scripts\ui_design\search_ui.py "website reveal" --limit 5
```

For the premium UI rule layer, also verify:

```powershell
python E:\DataBase\scripts\ui_design\search_ui.py "premium cinematic glass landing page" --limit 8
python E:\DataBase\scripts\ui_design\search_ui.py "liquid glass video hero blur typography" --limit 8
python E:\DataBase\scripts\ui_design\search_ui.py "高级 玻璃 拟态 landing page 视频 背景" --limit 8
python E:\DataBase\scripts\ui_design\search_ui.py "video hero layout bottom left HLS glass navbar" --limit 8
python E:\DataBase\scripts\ui_design\search_ui.py "双栏 液态玻璃 灰度 视频背景 Hero" --limit 8
python E:\DataBase\scripts\ui_design\search_ui.py "编程教育 HLS 背景 网格线 光晕 首屏" --limit 8
```

## 当前验证结果

- `normalize_reference.py --check`: validated 44 UI reference record(s)
- `make_chunks.py`: created 264 chunk(s) from 44 reference record(s)
- `build_sqlite_index.py`: indexed 44 reference record(s) and 264 chunk(s), FTS5 enabled
- `search_ui.py "website reveal" --limit 3`: returned Swishy website reveal chunks
- `search_ui.py "notification" --limit 3`: returned notification/message motion chunks, after one broader dialog match
- `search_ui.py "kinetic typography" --limit 3`: returned Swishy kinetic typography chunks
- `search_ui.py "data visualization" --limit 3`: returned Swishy dashboard/data-viz chunks
- `search_ui.py "video hero layout bottom left HLS glass navbar" --limit 8`: returns `pattern-video-hero-layout-variants`, technical HLS, cinematic hero, and CTA/navbar chunks.
- `search_ui.py "双栏 液态玻璃 灰度 视频背景 Hero" --limit 8`: returns two-panel Liquid Glass hero and strict grayscale glass hero chunks first.
- `search_ui.py "编程教育 HLS 背景 网格线 光晕 首屏" --limit 8`: returns technical education HLS hero chunks first.

## Optional Sources

- Liquid Glass: 可选视觉风格，不是默认偏好。只有任务明确要求玻璃拟态、Liquid Glass、frosted blur、半透明胶囊控件、折射高光、彩色边缘光等效果，或该风格被明确选中时，才应检索并采用这组资料。
- Swishy.ai: 可选动效模式源，适合提取 kinetic typography、notification/message stack、website reveal blur、data visualization motion、device/product showcase 等“动效意图”。只存摘要和模式，不复制模板代码、视频输出或素材。
- Video Hero Layout Patterns: 用于 Hero / Landing Page / SaaS Homepage / Portfolio First Screen / coding education first screen。不要把它误用于 Web App、Dashboard、Workspace 组件系统。

## 下一步

1. 改进 `search_ui.py` 的多词查询 ranking。
2. 继续补充 page-level 记录：pricing page、AI chat interface、animated dashboard。
3. 可新增一个 `examples/liquid_glass_motion_demo`，把 Liquid Glass 与 Swishy motion 模式合并成可运行样例。
