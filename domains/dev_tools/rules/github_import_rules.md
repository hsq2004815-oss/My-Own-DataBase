# GitHub Import Rules

## 文件用途

约束 Agent 导入 GitHub 项目、release、raw 文件时的下载顺序、安全边界和记录格式。

## 强制优先级

1. **优先官方浅克隆**

   ```bash
   git clone --depth=1 https://github.com/<owner>/<repo>.git
   ```

2. **普通 clone 慢或失败时尝试 fgit**

   ```bash
   fgit clone https://github.com/<owner>/<repo>.git --depth=1
   ```

3. **fgit 不可用或失败时尝试 fastgit**

   - 按 fastgit README 使用对应命令；如果无法确认命令格式，不要编造命令。
   - fastgit 作为 fgit 备选，不作为默认第一选择。

4. **clone 不行时使用 gh-proxy archive zip**

   - 只需要源码快照时，可以下载 archive zip。
   - 优先使用自建或可信 gh-proxy。

5. **release/raw 文件使用 github-proxy 或 gh-proxy**

   - github-proxy 用于生成 raw/release 代理 URL。
   - gh-proxy 用于受控下载 release/raw/archive。

## 必须遵守的安全规则

- 不通过公共代理下载私有仓库。
- 不通过公共代理下载带 token、credential、signed URL 的链接。
- 不把 GitHub PAT、账号密码、私有 URL 写入文档、日志、metadata。
- 不运行下载项目的 install/build/test 命令，除非用户明确授权。
- 不修改 raw 项目源码。
- 不删除、移动、覆盖 raw 目录。
- 自建 gh-proxy 对外暴露时必须考虑认证、限流、SSRF 防护和访问范围。

## Agent 行为规则

- 下载前判断是否需要完整仓库；默认不下载 Git 历史。
- 只读分析项目 README/docs/source structure。
- 下载失败时按优先级逐步 fallback，并记录原因。
- 对公共代理返回的内容保持怀疑，必要时校验来源和 checksum。
- 导入内容只作为参考，不把项目样例直接升格为核心规则。

## 输出记录要求

每次导入或下载后记录：

- repository / URL
- public/private 判断
- method used
- command used
- fallback sequence
- local path
- files read
- raw source modified: must be `false`
- security notes

## 推荐工具映射

| 任务 | 首选 | 备选 |
| --- | --- | --- |
| 公开仓库源码导入 | `git clone --depth=1` | fgit, fastgit |
| clone 失败但只需源码快照 | gh-proxy archive zip | GitHub archive URL |
| release asset 下载 | github-proxy URL / gh-proxy | 原始 GitHub release URL |
| raw 单文件下载 | github-proxy URL / gh-proxy | raw.githubusercontent.com |
| 私有仓库 | 官方 GitHub / VPN / 自建受控代理 | 不使用公共代理 |

## 关联主题

- `wiki/topics/github_download_acceleration.md`
- `wiki/topics/github_repo_import_template.md`
- `wiki/topics/agent_download_workflow.md`
- `processed/metadata/fgit.metadata.json`
- `processed/metadata/fastgit.metadata.json`
- `processed/metadata/github-proxy.metadata.json`
- `processed/metadata/gh-proxy.metadata.json`

---

## Related Knowledge

### Belongs To
- [Dev Tools AGENT_USAGE](../AGENT_USAGE.md)
- [Dev Tools Wiki Index](../wiki/index.md)

### Related Topics
- [Agent Download Workflow](../wiki/topics/agent_download_workflow.md)
- [GitHub Download Acceleration](../wiki/topics/github_download_acceleration.md)
- [GitHub Repo Import Template](../wiki/topics/github_repo_import_template.md)
