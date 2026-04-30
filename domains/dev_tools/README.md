# Dev Tools Domain

## 用途

`dev_tools` 领域用于整理本地开发工具、Agent 工具链和 GitHub 下载/导入流程。当前重点是 GitHub 下载加速工具的 metadata、wiki topic 和 rules。

## 当前内容

- `processed/metadata/`: GitHub 下载加速工具的结构化 metadata。
- `wiki/topics/`: 人类可读的下载策略、仓库导入模板和 Agent 下载流程。
- `rules/`: Agent 必须遵守的 GitHub 导入与代理使用规则。
- `raw/`: 本地保留的第三方 raw 项目源码，只作为维护阶段只读资料。

## GitHub raw 项目策略

- GitHub 仓库可只保留 `metadata/wiki/rules` 等 curated 产物进入版本库。
- 大型 raw 源码可以保留本地，不要求默认上传。
- 不修改 raw 项目源码。
- 不运行 raw 项目的安装、构建、测试命令，除非用户明确授权。

## Agent 使用规则

- 优先读取 `rules/` 和 `wiki/`。
- 不要默认整库读取 `raw/`。
- 需要检查来源时，只读打开相关 raw 项目的 README/docs。
- 公共代理只用于公开资源，不用于私有仓库、token 链接或 credential URL。
