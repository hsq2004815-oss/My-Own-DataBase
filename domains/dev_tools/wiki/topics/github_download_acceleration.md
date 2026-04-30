# GitHub Download Acceleration

## 文件用途

为 Agent 在下载 GitHub 公开仓库、release、raw 文件、archive 时提供稳定优先级和工具选择。该文档只整理下载策略，不要求开发新功能。

## 适用场景

- Agent 需要导入公开 GitHub 项目作为参考。
- `git clone` 速度慢、失败、超时。
- 需要下载 GitHub release asset、raw 文件或仓库 archive。
- 需要判断 fgit、fastgit、github-proxy、gh-proxy 的使用边界。

## 总体优先策略

1. **优先普通 Git shallow clone**
   - 默认先使用官方 GitHub URL。
   - 优先执行：

     ```bash
     git clone --depth=1 https://github.com/<owner>/<repo>.git
     ```

   - 只需要读取源码/README 时，不要完整 clone 历史。

2. **clone 慢或失败时尝试 fgit**
   - 使用：

     ```bash
     fgit clone https://github.com/<owner>/<repo>.git --depth=1
     ```

   - 适合公开仓库的 clone / pull / fetch。
   - fgit 可临时配置 Git mirror/proxy，完成后应恢复配置；如果异常中断，需要检查 `.gitconfig` 或 `.git/config`。

3. **fgit 不可用时尝试 fastgit**
   - 按 fastgit README 使用对应命令，不在规则中编造具体命令。
   - fastgit 是 Python 工具，README 描述其支持镜像源测速、缓存和代理配置。
   - 可作为 fgit 的备选。

4. **clone 不行时使用 gh-proxy archive zip**
   - 适合只需要快照、不需要 Git 历史的公开仓库。
   - 示例：

     ```bash
     curl http://localhost:8080/https://github.com/<owner>/<repo>/archive/refs/heads/main.zip -o repo-main.zip
     ```

   - 优先使用自建或可信 gh-proxy，不使用陌生公共代理处理敏感链接。

5. **release/raw 文件使用 github-proxy 或 gh-proxy**
   - github-proxy 适合生成 raw / release 代理 URL。
   - gh-proxy 适合自建 HTTP reverse proxy 直接下载 release、raw、archive。

## 工具定位

| 工具 | 主要用途 | 推荐优先级 | 注意事项 |
| --- | --- | --- | --- |
| `git clone --depth=1` | 官方浅克隆 | 最高 | 最安全、最少依赖 |
| fgit | GitHub git 命令加速 | clone 失败后的第一备选 | 不支持 SSH/submodule；可能临时改 Git 配置 |
| fastgit | Python Git 加速工具 | fgit 不可用时 | release 下载仍是 TODO；依赖镜像源 |
| gh-proxy | 自建 GitHub reverse proxy | archive/raw/release 下载 | 需要部署与安全配置 |
| github-proxy | GitHub URL 转换 CLI/lib | raw/release URL 生成 | 只是 URL 转换工具，不是代理服务 |

## 安全边界

- 不通过公共代理下载私有仓库。
- 不通过公共代理下载带 token、signed URL、credential 的链接。
- 不把 GitHub PAT、账号密码、私有仓库 URL 写进公共代理 URL。
- 对私有仓库优先使用官方 GitHub、公司网络、VPN、自建受控代理。
- 自建 gh-proxy 应优先绑定 localhost 或放在可信反向代理后，并启用认证/限流。

## Agent 使用建议

- 下载前先判断是否真的需要完整仓库；只需要阅读 README/docs 时，可以先用 raw 文件或 archive。
- 默认使用 `--depth=1`，避免引入大量历史对象。
- 下载失败要记录尝试过的命令和失败原因，不要无限重试。
- 项目导入后只作为参考；不要把 sample 项目写法直接升格为核心规则。

## 关联 metadata

- `processed/metadata/fgit.metadata.json`
- `processed/metadata/fastgit.metadata.json`
- `processed/metadata/github-proxy.metadata.json`
- `processed/metadata/gh-proxy.metadata.json`
