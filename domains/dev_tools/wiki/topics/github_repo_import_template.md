# GitHub Repo Import Template

## 文件用途

为 Agent 导入 GitHub 公开项目提供可复用流程模板。该模板用于下载、记录来源、做只读分析，不用于运行不可信代码。

## 推荐导入流程

### 1. 明确目标

- 项目用途：
- 需要读取的内容：
  - README
  - docs
  - examples
  - package/build config
  - source structure
- 是否需要完整 Git 历史：默认不需要。

### 2. 优先浅克隆

```bash
git clone --depth=1 https://github.com/<owner>/<repo>.git
```

导入后记录：

- repo:
- branch/tag:
- clone command:
- local path:
- imported_at:
- purpose:

### 3. clone 慢或失败时尝试 fgit

```bash
fgit clone https://github.com/<owner>/<repo>.git --depth=1
```

记录：

- fallback tool: fgit
- reason:
- success/failure:

### 4. fgit 不可用时尝试 fastgit

按 fastgit README 使用对应命令。如果当前环境无法确认 fastgit 的实际命令格式，不要编造命令，记录为“fastgit 未确认/未使用”，再进入 archive 下载 fallback。

记录：

- fallback tool: fastgit
- mirror/proxy mode:
- success/failure:

### 5. clone 不可行时使用 archive

适合只读快照：

```bash
curl http://localhost:8080/https://github.com/<owner>/<repo>/archive/refs/heads/main.zip -o <repo>-main.zip
```

记录：

- archive URL:
- proxy used:
- checksum if available:
- extracted path:

### 6. release/raw 文件下载

对于单文件或 release asset：

- github-proxy：生成 raw/release 代理 URL。
- gh-proxy：通过自建 reverse proxy 下载 raw/release/archive。

记录：

- source URL:
- converted URL:
- proxy type:
- whether public/private:

## Metadata 记录模板

```json
{
  "id": "dev_tools_github_project_<name>",
  "project_name": "<name>",
  "domain": "dev_tools",
  "source_type": "github_project",
  "local_path": "E:\\DataBase\\domains\\dev_tools\\raw\\github\\repos\\<name>",
  "summary": "",
  "primary_use": [],
  "recommended_agent_usage": [],
  "capabilities": [],
  "limitations": [],
  "security_notes": [],
  "trust_level": "good_reference",
  "retrieval": {
    "prompt_tags": [],
    "keywords": []
  }
}
```

## 禁止事项

- 不修改 raw 项目源码。
- 不运行不可信 install/build/test 命令，除非用户明确授权。
- 不把 private repo URL、token URL、GitHub PAT 写入公共代理。
- 不通过公共代理下载私有仓库。
- 不把单个 sample 项目结论提升为核心规则。
