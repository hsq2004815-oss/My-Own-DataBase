# Agent Download Workflow

## 文件用途

为 Agent 提供 GitHub 项目/文件下载决策流程，减少下载失败、慢速 clone、代理误用和安全泄露风险。

## 决策树

### A. 是否需要完整仓库？

- 只需要 README / docs / 单文件：优先 raw/release/file 下载。
- 需要浏览源码结构：优先 shallow clone。
- 需要 Git 历史：必须用户明确要求；默认不下载历史。

### B. 公开还是私有？

- 公开仓库：可以使用普通 GitHub、fgit/fastgit、受控 gh-proxy、公共 raw/release 代理。
- 私有仓库：不要使用公共代理；优先官方 GitHub 或自建受控代理。
- URL 含 token、credential、signed 参数：不要使用公共代理。

### C. 下载优先级

1. 普通 shallow clone：

   ```bash
   git clone --depth=1 https://github.com/<owner>/<repo>.git
   ```

2. 慢或失败时 fgit：

   ```bash
   fgit clone https://github.com/<owner>/<repo>.git --depth=1
   ```

3. fgit 不可用时 fastgit：

   - 按 fastgit README 使用对应命令。
   - 如果当前环境没有 fastgit 或无法确认命令格式，不要编造命令，改用下一步 archive/raw/release 下载策略。

4. clone 不行时 archive zip：

   ```bash
   curl http://localhost:8080/https://github.com/<owner>/<repo>/archive/refs/heads/main.zip -o repo-main.zip
   ```

5. release/raw 文件：
   - github-proxy 生成代理 URL。
   - gh-proxy 自建服务下载 raw/release/archive。

## Agent 输出记录格式

下载或导入完成后，Agent 应记录：

- source repository:
- local path:
- method used:
- fallback tools used:
- public/private judgment:
- whether token/credential appeared:
- files read:
- files not modified:
- safety notes:

## 失败处理

- 每个方法最多尝试有限次数。
- 失败时记录错误摘要，不要无限切换公共代理。
- 如果公共代理要求输入 token 或 private URL，立即停止。
- 如果 archive 下载成功但缺少 `.git`，后续应按快照项目处理。

## 安全原则

- 公共代理只用于公开开源资源。
- 私有资源只走官方 GitHub、VPN、公司网络或自建受控代理。
- 不在日志、Markdown、metadata 中保存 token。
- 不运行下载项目的安装脚本。
- 不修改 raw 源码；整理内容写入 processed/wiki/rules。
