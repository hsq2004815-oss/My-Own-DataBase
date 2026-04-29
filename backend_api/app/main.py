from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Annotated, Any

from fastapi import Body, FastAPI, HTTPException, Query
from pydantic import BaseModel


ROOT = Path(__file__).resolve().parents[2]
UI_DB_PATH = ROOT / "runtime" / "db" / "sqlite" / "ui_design" / "ui_design_references.db"
WORKFLOW_DB_PATH = ROOT / "runtime" / "db" / "sqlite" / "agent_workflow" / "agent_workflow_references.db"
AUTOMATION_DB_PATH = ROOT / "runtime" / "db" / "sqlite" / "automation" / "automation_references.db"
BACKEND_DB_PATH = ROOT / "runtime" / "db" / "sqlite" / "backend" / "backend_references.db"
UI_ASSET_METADATA_DIR = ROOT / "domains" / "ui_assets" / "processed" / "metadata"
API_REQUEST_LOG_PATH = ROOT / "runtime" / "logs" / "api_requests.jsonl"

app = FastAPI(
    title="DataBase Knowledge API",
    description="Local API for retrieving curated knowledge chunks.",
    version="0.1.0",
)


def log_api_request(
    method: str,
    endpoint: str,
    params: dict[str, Any] | None = None,
    result: dict[str, Any] | None = None,
    status: str = "ok",
) -> None:
    event = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "method": method,
        "endpoint": endpoint,
        "status": status,
        "params": params or {},
        "result": result or {},
    }
    try:
        API_REQUEST_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        with API_REQUEST_LOG_PATH.open("a", encoding="utf-8") as f:
            f.write(json.dumps(event, ensure_ascii=False, separators=(",", ":")) + "\n")
    except OSError:
        pass


class ChunkResult(BaseModel):
    chunk_id: str
    record_id: str
    source_name: str
    source_url: str
    page_type: str
    section: str
    content: str
    tokens: int
    metadata: dict[str, Any]


class ReferenceSummary(BaseModel):
    record_id: str
    source_name: str
    source_url: str
    page_type: str
    signal_strength: str
    evidence_level: str
    ai_summary: str


class WorkflowChunkResult(BaseModel):
    chunk_id: str
    record_id: str
    workflow_type: str
    source_name: str
    source_url: str
    section: str
    content: str
    tokens: int
    metadata: dict[str, Any]


class WorkflowReferenceSummary(BaseModel):
    record_id: str
    source_name: str
    source_url: str
    workflow_type: str
    signal_strength: str
    evidence_level: str
    ai_summary: str


class AutomationChunkResult(BaseModel):
    chunk_id: str
    record_id: str
    automation_type: str
    source_name: str
    source_url: str
    section: str
    content: str
    tokens: int
    metadata: dict[str, Any]


class AutomationReferenceSummary(BaseModel):
    record_id: str
    source_name: str
    source_url: str
    automation_type: str
    signal_strength: str
    evidence_level: str
    ai_summary: str


class BackendChunkResult(BaseModel):
    chunk_id: str
    source_type: str
    title: str
    relative_path: str
    section: str
    content: str
    summary: str
    tags: list[str]
    keywords: list[str]
    priority: str
    trust_level: str
    metadata: dict[str, Any]


class AssetResult(BaseModel):
    asset_id: str
    asset_type: str
    usage_policy: str
    file_path: str
    preview_path: str = ""
    original_path: str = ""
    source_name: str = ""
    source_url: str = ""
    license_label: str = ""
    style_tags: list[str] = []
    use_cases: list[str] = []
    ai_summary: str = ""


class BriefResponse(BaseModel):
    brief: str
    ui_queries: list[str]
    workflow_queries: list[str]
    automation_queries: list[str]
    backend_queries: list[str]
    asset_queries: list[str]
    ui_chunks: list[ChunkResult]
    workflow_chunks: list[WorkflowChunkResult]
    automation_chunks: list[AutomationChunkResult]
    backend_chunks: list[BackendChunkResult]
    asset_suggestions: list[AssetResult]
    guidance: list[str]


class BriefRequest(BaseModel):
    task: str
    ui_limit: int = 8
    workflow_limit: int = 5
    automation_limit: int = 0
    backend_limit: int = 6
    asset_limit: int = 6


MOTION_ASSET_BOOTSTRAP_QUERIES = [
    "小动画",
    "微交互",
    "loading animation",
    "hover motion",
    "button animation",
    "animated icon",
    "lottie animation",
    "motion reference",
    "hero background motion",
]
UI_BOOTSTRAP_TERMS = (
    "ui",
    "frontend",
    "front-end",
    "前端",
    "界面",
    "网站",
    "网页",
    "页面",
    "portfolio",
    "作品集",
    "简历",
    "landing page",
    "落地页",
    "homepage",
    "官网",
    "dashboard",
    "saas",
    "app ui",
)
PREMIUM_MOTION_BOOTSTRAP_TERMS = (
    "高级",
    "高端",
    "动效",
    "动画",
    "小动画",
    "motion",
    "lottie",
    "视觉效果",
    "visual effect",
    "visual effects",
    "交互高级",
    "微交互",
    "loading animation",
    "hover motion",
    "button animation",
    "animated icon",
)


def needs_motion_asset_bootstrap(task: str) -> bool:
    normalized = task.casefold()
    return any(term.casefold() in normalized for term in UI_BOOTSTRAP_TERMS) and any(
        term.casefold() in normalized for term in PREMIUM_MOTION_BOOTSTRAP_TERMS
    )


def needs_backend_context(task: str) -> bool:
    normalized = task.casefold()
    return any(term.casefold() in normalized for term in BACKEND_CONTEXT_TERMS)




UI_QUERY_RULES: list[tuple[tuple[str, ...], str]] = [
    (("premium", "high-end", "high end", "高级", "高端", "审美", "质感", "visual anchor", "视觉锚点", "非模板", "设计自检", "执行质量"), "premium UI execution visual anchor non generic layout"),
    (("workspace", "web app", "app ui", "ui kit", "project workspace", "AI Project Workspace", "工作台", "工作区", "项目空间"), "liquid glass web app ui kit"),
    (("video hero layout", "video hero", "hero layout", "top-aligned", "bottom-left", "HLS hero", "MP4 background", "视频首屏", "底部左对齐", "顶部压迫式"), "video hero layout patterns"),
    (("two panel hero", "split hero", "双栏", "双栏玻璃", "双栏 液态玻璃"), "two panel liquid glass hero"),
    (("coding education", "technical education", "bootcamp", "HLS", "vertical grid", "SVG glow", "编程教育", "网格线", "光晕"), "technical education HLS hero"),
    (("grayscale glass", "strict grayscale", "灰度玻璃", "灰度玻璃拟态"), "strict grayscale liquid glass hero"),
    (("premium", "high-end", "high end", "高级", "高端", "审美", "质感", "cinematic", "电影感"), "premium web ui"),
    (("landing page", "homepage", "首页", "官网", "落地页", "产品页"), "premium landing page"),
    (("video hero", "video-first", "video background", "hero", "floating navbar", "视频背景", "视频 hero", "沉浸式"), "cinematic video hero"),
    (("portfolio", "作品集", "agency", "设计机构"), "portfolio editorial dark landing page"),
    (("saas", "SaaS", "developer saas", "开发者工具"), "monochrome saas editorial typography"),
    (("liquid glass", "glass", "玻璃", "frosted", "backdrop"), "liquid glass"),
    (("ambient", "dynamic background", "scene", "scenery", "ecology", "ecological", "aurora", "caustics", "动态背景", "动态景色", "背景景色", "生态", "生态界面", "氛围背景", "环境背景"), "ambient dynamic background liquid glass"),
    (("aurora", "haze", "mist", "atmospheric", "极光", "雾气", "光带", "氛围雾"), "aurora haze background"),
    (("caustics", "water", "refractive", "liquid light", "水纹", "水面", "折射", "流光", "液态光"), "water caustics liquid glass background"),
    (("particle", "particles", "data current", "data flow", "telemetry", "star dust", "粒子", "数据流", "星尘", "流动数据"), "data current particle background"),
    (("dark", "neon", "暗色", "黑色"), "dark glass neon"),
    (("motion", "animation", "动效", "动画"), "website reveal"),
    (("notification", "toast", "message", "通知", "消息"), "notification"),
    (("typography", "headline", "文字", "标题"), "kinetic typography"),
    (("dashboard", "仪表盘", "数据", "chart", "图表"), "data visualization"),
    (("form", "modal", "表单", "弹窗"), "glass form modal"),
    (("table", "data table", "表格"), "data table"),
    (("empty", "空状态"), "empty state"),
    (("pricing", "价格", "plan", "订阅"), "pricing page"),
    (("chat", "assistant", "ai chat", "聊天"), "ai chat interface"),
]

WORKFLOW_QUERY_RULES: list[tuple[tuple[str, ...], str]] = [
    (("api", "database", "数据库", "知识库", "调用"), "api first"),
    (("frontend", "ui", "页面", "前端", "design", "设计"), "knowledge first frontend"),
    (("claude", "cursor", "codex", "agent", "智能体"), "api first"),
    (("windows", "bash", "powershell", "path", "路径"), "windows paths"),
    (("report", "handoff", "汇报", "交接", "证据"), "handoff report"),
    (("fail", "error", "失败", "报错", "恢复"), "failure recovery"),
]

AUTOMATION_QUERY_RULES: list[tuple[tuple[str, ...], str]] = [
    (("upload", "file", "input[type=file]", "chooser", "文件", "上传"), "file upload"),
    (("playwright", "locator", "selector", "actionability", "点击", "选择器"), "playwright locator"),
    (("cdp", "chrome", "edge", "browser", "session", "浏览器", "登录态"), "chrome cdp"),
    (("windows", "powershell", "path", "process", "port", "路径", "端口", "进程"), "windows powershell"),
    (("overlay", "modal", "iframe", "dropdown", "弹窗", "遮罩", "下拉"), "overlay modal iframe"),
    (("trace", "screenshot", "evidence", "debug", "fail", "error", "验证", "证据", "报错", "恢复"), "failure recovery"),
    (("security", "safe", "remote debugging", "安全"), "security boundary"),
]

BACKEND_QUERY_RULES: list[tuple[tuple[str, ...], str]] = [
    (("api", "接口", "后台接口", "openapi", "swagger", "pagination", "分页", "error code", "错误码", "idempotency", "幂等"), "backend api design error handling pagination idempotency"),
    (("database", "数据库", "postgres", "postgresql", "mysql", "sqlite", "schema", "table", "表结构", "迁移", "索引"), "database modeling migration indexes constraints audit fields"),
    (("auth", "login", "jwt", "session", "rbac", "permission", "权限", "登录", "注册", "管理员", "鉴权", "授权"), "auth permission jwt refresh token rbac security"),
    (("security", "safe", "secret", "csrf", "cors", "rate limit", "安全", "密钥", "限流"), "backend security checklist secrets cors rate limit"),
    (("deploy", "deployment", "docker", "compose", "env", "ci", "上线", "部署", "环境变量", "健康检查"), "deployment docker compose env health check logging"),
    (("rag", "agent", "ai backend", "openai", "llm", "sse", "stream", "vector", "embedding", "大模型", "流式", "向量", "检索增强"), "ai backend rag agent sse streaming vector ingestion"),
    (("queue", "task", "webhook", "worker", "celery", "background", "任务队列", "异步", "回调"), "backend task queue webhook background worker"),
    (("github", "open source", "开源项目", "项目分析"), "github backend project analysis quality checklist"),
]

BACKEND_CONTEXT_TERMS = (
    "backend",
    "后端",
    "后台",
    "服务端",
    "api",
    "接口",
    "database",
    "数据库",
    "postgres",
    "postgresql",
    "mysql",
    "sqlite",
    "auth",
    "login",
    "jwt",
    "session",
    "rbac",
    "permission",
    "权限",
    "登录",
    "注册",
    "docker",
    "deploy",
    "部署",
    "rag",
    "大模型",
    "sse",
    "webhook",
    "queue",
    "任务队列",
)


ASSET_QUERY_RULES: list[tuple[tuple[str, ...], str]] = [
    (("dynamic", "motion", "video", "background", "scene", "scenery", "ecology", "ambient", "动态", "动感", "视频", "背景", "景色", "生态", "氛围"), "dynamic background motion reference"),
    (("screenshot", "reference", "inspiration", "interface", "screen", "高级", "前沿", "参考", "截图", "界面", "审美"), "ui screenshot reference inspiration"),
    (("font", "typography", "typeface", "文字", "字体", "排版", "标题"), "font typography"),
    (("icon", "icons", "lucide", "tabler", "heroicon", "remix", "图标"), "icon library"),
    (("component", "ui kit", "button", "modal", "window", "control", "组件", "按钮", "弹窗", "窗口", "控件"), "ui kit component library"),
    (("lottie", "animation", "micro interaction", "动效", "动画", "微交互"), "lottie animation library"),
]




QUERY_SYNONYMS: dict[str, str] = {
    "玻璃生态": "liquid glass",
    "玻璃拟态": "liquid glass",
    "液态玻璃": "liquid glass",
    "毛玻璃": "liquid glass",
    "磨砂玻璃": "liquid glass",
    "液态玻璃工作台": "liquid glass web app ui kit",
    "玻璃工作台": "liquid glass web app ui kit",
    "玻璃工作区": "liquid glass web app ui kit",
    "ai project workspace": "liquid glass web app ui kit",
    "workspace ui": "liquid glass web app ui kit",
    "web app ui kit": "liquid glass web app ui kit",
    "saas dashboard": "liquid glass web app ui kit",
    "视觉锚点": "visual anchor premium UI execution",
    "非模板": "non generic layout premium UI execution",
    "非模板化": "non generic layout premium UI execution",
    "设计自检": "design self check premium UI execution",
    "执行质量": "premium UI execution quality",
    "技术可视化": "technical visualization visual anchor",
    "项目专属视觉": "project specific visuals visual anchor",
    "玻璃质感检查": "glass quality check",
    "组件密度": "component density",
    "高级": "premium web ui",
    "高端": "premium web ui",
    "高级审美": "premium web ui",
    "高端首页": "premium landing page",
    "官网": "premium landing page",
    "落地页": "premium landing page",
    "视频背景": "cinematic video hero",
    "视频首页": "cinematic video hero",
    "视频首屏": "video hero layout patterns",
    "高级视频首屏": "video hero layout patterns",
    "底部左对齐": "bottom left video hero",
    "顶部压迫式": "top aligned video hero",
    "双栏玻璃首屏": "two panel liquid glass hero",
    "双栏液态玻璃": "two panel liquid glass hero",
    "灰度玻璃拟态": "strict grayscale liquid glass hero",
    "编程教育首屏": "technical education HLS hero",
    "网格线": "vertical grid overlay HLS hero",
    "光晕": "SVG glow HLS hero",
    "沉浸式": "cinematic video hero",
    "作品集": "portfolio editorial dark landing page",
    "半透明": "translucent",
    "背景模糊": "backdrop-filter",
    "动态背景": "ambient dynamic background liquid glass",
    "动态景色": "ambient dynamic background liquid glass",
    "背景景色": "ambient dynamic background liquid glass",
    "生态界面": "ambient dynamic background liquid glass",
    "氛围背景": "ambient dynamic background liquid glass",
    "环境背景": "ambient dynamic background liquid glass",
    "极光": "aurora haze background",
    "雾气": "aurora haze background",
    "光带": "aurora haze background",
    "氛围雾": "aurora haze background",
    "水纹": "water caustics liquid glass background",
    "水面": "water caustics liquid glass background",
    "折射": "water caustics liquid glass background",
    "流光": "water caustics liquid glass background",
    "液态光": "water caustics liquid glass background",
    "粒子": "data current particle background",
    "数据流": "data current particle background",
    "星尘": "data current particle background",
    "流动数据": "data current particle background",
    "暗色玻璃": "dark glass neon",
    "黑色玻璃": "dark glass neon",
    "霓虹": "dark glass neon",
    "动效": "website reveal",
    "动画": "website reveal",
    "入场动画": "website reveal",
    "页面入场": "website reveal",
    "揭示动画": "website reveal",
    "通知": "notification",
    "消息": "notification",
    "弹窗": "modal",
    "表单弹窗": "glass form modal",
    "表单": "form validation",
    "校验": "form validation",
    "仪表盘": "dashboard",
    "数据可视化": "data visualization",
    "图表": "data visualization",
    "文字动效": "kinetic typography",
    "打字机": "kinetic typography",
    "智能体": "agent",
    "知识库": "api first",
    "数据库": "api first",
    "交接报告": "handoff report",
    "汇报": "handoff report",
    "路径": "windows paths",
    "报错": "failure recovery",
    "自动化": "playwright locator",
    "浏览器自动化": "playwright locator",
    "文件上传": "file upload",
    "上传文件": "file upload",
    "选择器": "playwright locator",
    "弹窗遮罩": "overlay modal iframe",
    "远程调试": "chrome cdp",
    "登录态": "chrome cdp",
    "截图": "evidence report",
    "证据": "evidence report",
}


def normalize_query(query: str) -> str:
    normalized = query.strip()
    lowered = normalized.lower()
    if lowered in QUERY_SYNONYMS:
        return QUERY_SYNONYMS[lowered]
    for source, target in QUERY_SYNONYMS.items():
        if source in normalized:
            return target
    return normalized


def dedupe_strings(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        normalized = item.strip()
        key = normalized.lower()
        if normalized and key not in seen:
            seen.add(key)
            result.append(normalized)
    return result


def derive_queries(brief: str, rules: list[tuple[tuple[str, ...], str]], defaults: list[str]) -> list[str]:
    lower = brief.lower()
    queries: list[str] = []
    for triggers, query in rules:
        if any(trigger.lower() in lower for trigger in triggers):
            queries.append(query)
    if not queries:
        queries.extend(defaults)
    return dedupe_strings(queries)[:5]


def merge_ui_chunks(groups: list[list[ChunkResult]], limit: int) -> list[ChunkResult]:
    seen: set[str] = set()
    merged: list[ChunkResult] = []
    for group in groups:
        for chunk in group:
            if chunk.chunk_id in seen:
                continue
            seen.add(chunk.chunk_id)
            merged.append(chunk)
            if len(merged) >= limit:
                return merged
    return merged


def merge_workflow_chunks(groups: list[list[WorkflowChunkResult]], limit: int) -> list[WorkflowChunkResult]:
    seen: set[str] = set()
    merged: list[WorkflowChunkResult] = []
    for group in groups:
        for chunk in group:
            if chunk.chunk_id in seen:
                continue
            seen.add(chunk.chunk_id)
            merged.append(chunk)
            if len(merged) >= limit:
                return merged
    return merged


def merge_automation_chunks(groups: list[list[AutomationChunkResult]], limit: int) -> list[AutomationChunkResult]:
    seen: set[str] = set()
    merged: list[AutomationChunkResult] = []
    for group in groups:
        for chunk in group:
            if chunk.chunk_id in seen:
                continue
            seen.add(chunk.chunk_id)
            merged.append(chunk)
            if len(merged) >= limit:
                return merged
    return merged


def derive_asset_queries(brief: str) -> list[str]:
    defaults = [
        "dynamic background motion reference",
        "ui screenshot reference inspiration",
        "ui kit component library",
    ]
    return derive_queries(brief, ASSET_QUERY_RULES, defaults)


def safe_list(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    return [str(item) for item in value if str(item).strip()]


def load_asset_records() -> list[dict[str, Any]]:
    if not UI_ASSET_METADATA_DIR.exists():
        return []
    records: list[dict[str, Any]] = []
    for path in UI_ASSET_METADATA_DIR.glob("*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(data, dict) and data.get("asset_id"):
            records.append(data)
    return records


def asset_to_result(record: dict[str, Any]) -> AssetResult:
    files = record.get("files") if isinstance(record.get("files"), dict) else {}
    source = record.get("source") if isinstance(record.get("source"), dict) else {}
    license_data = record.get("license") if isinstance(record.get("license"), dict) else {}
    retrieval = record.get("retrieval") if isinstance(record.get("retrieval"), dict) else {}
    return AssetResult(
        asset_id=str(record.get("asset_id", "")),
        asset_type=str(record.get("asset_type", "unknown")),
        usage_policy=str(record.get("usage_policy", "unknown")),
        file_path=str(files.get("file_path", record.get("file_path", ""))),
        preview_path=str(files.get("preview_path", record.get("preview_path", ""))),
        original_path=str(files.get("original_path", record.get("original_path", ""))),
        source_name=str(source.get("name", record.get("source_name", ""))),
        source_url=str(source.get("url", record.get("source_url", ""))),
        license_label=str(license_data.get("label", record.get("license_label", ""))),
        style_tags=safe_list(record.get("style_tags")),
        use_cases=safe_list(record.get("use_cases")),
        ai_summary=str(retrieval.get("ai_summary", record.get("ai_summary", ""))),
    )


def preferred_asset_types(query: str) -> set[str]:
    lower = query.lower()
    preferred: set[str] = set()
    if any(term in lower for term in ("dynamic", "motion", "video", "background", "scene", "ecology", "ambient", "hero", "cinematic", "动态", "视频", "背景", "生态")):
        preferred.update({"motion_reference", "background_video", "background_image", "texture"})
    if any(term in lower for term in ("screenshot", "reference", "inspiration", "interface", "screen", "portfolio", "landing", "saas", "dark", "glass", "liquid", "参考", "截图", "界面", "审美", "高级", "高端", "简历", "作品集", "玻璃")):
        preferred.add("screenshot_reference")
    if any(term in lower for term in ("font", "typography", "typeface", "字体", "排版")):
        preferred.add("font")
    if any(term in lower for term in ("icon", "icons", "lucide", "tabler", "heroicon", "remix", "图标")):
        preferred.update({"icon", "asset_collection"})
    if any(term in lower for term in ("component", "ui kit", "button", "modal", "window", "control", "组件", "按钮", "弹窗", "窗口")):
        preferred.update({"asset_collection", "component_code", "surface", "control"})
    if any(term in lower for term in ("lottie", "animation", "loading", "hover motion", "micro interaction", "json animation", "animated icon", "lightweight", "小动画", "动效", "动画", "微交互", "加载动画", "按钮动画", "图标动画", "lottie 动画")):
        preferred.update({"asset_collection", "motion_reference"})
    return preferred


def asset_query_terms(query: str) -> list[str]:
    aliases = {
        "高级": "premium high-end",
        "高端": "premium high-end",
        "简历": "portfolio resume",
        "作品集": "portfolio",
        "网站": "website landing page",
        "动态背景": "dynamic background hero-background ambient-motion",
        "背景": "background hero-background",
        "动效": "motion motion-reference",
        "动画": "motion motion-reference",
        "小动画": "small-animation lottie micro-interaction lightweight-ui-animation",
        "微交互": "micro-interaction lottie web-ui-motion",
        "加载动画": "loading-animation lottie json-animation",
        "按钮动画": "button-animation hover-motion lottie",
        "图标动画": "animated-icon lottie",
        "Lottie 动画": "lottie animation json-animation web-ui-motion",
        "lottie 动画": "lottie animation json-animation web-ui-motion",
        "玻璃": "liquid glass liquid-glass glassmorphism",
        "按钮": "button kit control",
        "截图": "screenshot inspiration",
    }
    expanded = query
    for source, target in aliases.items():
        if source in expanded:
            expanded = f"{expanded} {target}"
    terms = query_terms(expanded)
    for raw in expanded.replace("-", " ").replace("_", " ").split():
        term = raw.strip().lower()
        if len(term) >= 2:
            terms.append(term)
    return dedupe_strings(terms)


def asset_score(record: dict[str, Any], query: str, query_index: int = 0) -> int:
    result = asset_to_result(record)
    retrieval = record.get("retrieval") if isinstance(record.get("retrieval"), dict) else {}
    prompt_tags = safe_list(retrieval.get("prompt_tags"))
    files = record.get("files") if isinstance(record.get("files"), dict) else {}
    source = record.get("source") if isinstance(record.get("source"), dict) else {}
    haystack = " ".join(
        [
            result.asset_id,
            result.asset_type,
            result.usage_policy,
            result.file_path,
            str(files.get("original_path", "")),
            str(source.get("name", "")),
            result.ai_summary,
            " ".join(result.style_tags),
            " ".join(result.use_cases),
            " ".join(prompt_tags),
        ]
    ).lower()
    terms = asset_query_terms(query)
    preferred = preferred_asset_types(query)

    score = max(0, 80 - query_index * 5)
    if result.asset_type in preferred:
        score += 60
    if result.usage_policy == "inspiration_only":
        score += 14
    elif result.usage_policy == "internal_reference":
        score += 12
    elif result.usage_policy == "direct_use":
        score += 10
    elif result.usage_policy == "review_required":
        score += 4

    if terms and all(term in haystack for term in terms):
        score += 35
    score += sum(10 for term in terms if term in result.asset_id.lower() or term in result.asset_type.lower())
    score += sum(7 for term in terms if term in " ".join(prompt_tags).lower())
    score += sum(3 for term in terms if term in haystack)

    if result.asset_type == "font" and "font" not in preferred:
        score -= 20
    if result.asset_type == "asset_collection" and preferred & {"icon", "asset_collection", "component_code", "surface", "control"}:
        score += 12
    return score


def search_assets_records(
    q: str,
    limit: int,
    asset_type: str | None = None,
    usage_policy: str | None = None,
) -> list[AssetResult]:
    records = load_asset_records()
    if asset_type:
        records = [record for record in records if record.get("asset_type") == asset_type]
    if usage_policy:
        records = [record for record in records if record.get("usage_policy") == usage_policy]
    ranked = sorted(
        ((asset_score(record, q), record) for record in records),
        key=lambda item: item[0],
        reverse=True,
    )
    return [asset_to_result(record) for _, record in ranked[:limit]]


def merge_ranked_assets(groups: list[tuple[str, list[AssetResult]]], limit: int) -> list[AssetResult]:
    best: dict[str, tuple[int, AssetResult]] = {}
    selected: list[AssetResult] = []
    seen: set[str] = set()
    per_query_floor = 1

    for query_index, (query, assets) in enumerate(groups):
        ranked = sorted(
            ((asset_score(asset.dict(), query, query_index), asset) for asset in assets),
            key=lambda item: item[0],
            reverse=True,
        )
        added = 0
        for _, asset in ranked:
            if asset.asset_id in seen:
                continue
            selected.append(asset)
            seen.add(asset.asset_id)
            added += 1
            if added >= per_query_floor or len(selected) >= limit:
                break
        for score, asset in ranked:
            current = best.get(asset.asset_id)
            if current is None or score > current[0]:
                best[asset.asset_id] = (score, asset)

    for _, asset in sorted(best.values(), key=lambda item: item[0], reverse=True):
        if len(selected) >= limit:
            break
        if asset.asset_id in seen:
            continue
        selected.append(asset)
        seen.add(asset.asset_id)
    return selected[:limit]




SECTION_PRIORITY: dict[str, int] = {
    "implementation": 45,
    "layout": 35,
    "interaction": 32,
    "accessibility": 30,
    "components": 26,
    "api": 26,
    "steps": 25,
    "verification": 22,
    "prompt_contract": 22,
    "failure_modes": 18,
    "handoff": 18,
    "overview": 8,
}

EVIDENCE_PRIORITY: dict[str, int] = {
    "tested": 18,
    "direct_spec": 16,
    "observed": 14,
    "documented": 13,
    "official": 13,
    "screenshot_observed": 12,
    "summary_only": 8,
    "draft": 2,
    "link_only": 1,
}


def query_terms(query: str) -> list[str]:
    return [term for term in normalize_query(query).lower().replace("-", " ").split() if len(term) >= 2]


def chunk_score(chunk: ChunkResult | WorkflowChunkResult | AutomationChunkResult, query: str, query_index: int) -> int:
    terms = query_terms(query)
    haystack = f"{chunk.chunk_id} {chunk.record_id} {chunk.section} {chunk.source_name} {chunk.content}".lower()
    metadata = chunk.metadata or {}
    prompt_tags = " ".join(metadata.get("prompt_tags", [])).lower()
    evidence = str(metadata.get("evidence_level", "")).lower()
    signal = str(metadata.get("signal_strength", "")).lower()

    score = max(0, 80 - query_index * 6)
    score += SECTION_PRIORITY.get(chunk.section, 0)
    score += EVIDENCE_PRIORITY.get(evidence, 0)
    if signal == "high":
        score += 10
    elif signal == "medium":
        score += 4

    if terms and all(term in haystack for term in terms):
        score += 35
    score += sum(12 for term in terms if term in chunk.record_id.lower() or term in chunk.chunk_id.lower())
    score += sum(8 for term in terms if term in prompt_tags)
    score += sum(3 for term in terms if term in haystack)

    if "implementation" in chunk.record_id.lower() or "parameters" in chunk.record_id.lower():
        score += 18
    if chunk.section == "overview" and any(section in haystack for section in ("implementation", "parameters")):
        score += 6
    return score


def backend_chunk_score(chunk: BackendChunkResult, query: str, query_index: int) -> int:
    terms = query_terms(query)
    haystack = (
        f"{chunk.chunk_id} {chunk.source_type} {chunk.title} {chunk.relative_path} "
        f"{chunk.section} {chunk.summary} {chunk.content} {' '.join(chunk.tags)} {' '.join(chunk.keywords)}"
    ).lower()

    score = max(0, 80 - query_index * 6)
    score += SECTION_PRIORITY.get(chunk.section.lower(), 0)
    if chunk.priority == "high":
        score += 16
    elif chunk.priority == "medium":
        score += 8
    if chunk.trust_level in {"high", "official"}:
        score += 12
    elif chunk.trust_level == "medium":
        score += 6
    if terms and all(term in haystack for term in terms):
        score += 35
    score += sum(12 for term in terms if term in chunk.chunk_id.lower() or term in chunk.title.lower())
    score += sum(8 for term in terms if term in " ".join(chunk.keywords).lower())
    score += sum(3 for term in terms if term in haystack)
    if chunk.source_type in {"rule", "checklist", "pattern"}:
        score += 12
    return score


def merge_ranked_ui_chunks(groups: list[tuple[str, list[ChunkResult]]], limit: int) -> list[ChunkResult]:
    best: dict[str, tuple[int, ChunkResult]] = {}
    selected: list[ChunkResult] = []
    seen: set[str] = set()
    per_query_floor = 2 if limit >= len(groups) * 2 else 1

    for query_index, (query, chunks) in enumerate(groups):
        ranked = sorted(
            ((chunk_score(chunk, query, query_index), chunk) for chunk in chunks),
            key=lambda item: item[0],
            reverse=True,
        )
        added = 0
        for _, chunk in ranked:
            if chunk.chunk_id in seen:
                continue
            selected.append(chunk)
            seen.add(chunk.chunk_id)
            added += 1
            if added >= per_query_floor or len(selected) >= limit:
                break
        for score, chunk in ranked:
            current = best.get(chunk.chunk_id)
            if current is None or score > current[0]:
                best[chunk.chunk_id] = (score, chunk)

    for _, chunk in sorted(best.values(), key=lambda item: item[0], reverse=True):
        if len(selected) >= limit:
            break
        if chunk.chunk_id in seen:
            continue
        selected.append(chunk)
        seen.add(chunk.chunk_id)
    return selected[:limit]


def merge_ranked_workflow_chunks(groups: list[tuple[str, list[WorkflowChunkResult]]], limit: int) -> list[WorkflowChunkResult]:
    best: dict[str, tuple[int, WorkflowChunkResult]] = {}
    selected: list[WorkflowChunkResult] = []
    seen: set[str] = set()
    per_query_floor = 1

    for query_index, (query, chunks) in enumerate(groups):
        ranked = sorted(
            ((chunk_score(chunk, query, query_index), chunk) for chunk in chunks),
            key=lambda item: item[0],
            reverse=True,
        )
        added = 0
        for _, chunk in ranked:
            if chunk.chunk_id in seen:
                continue
            selected.append(chunk)
            seen.add(chunk.chunk_id)
            added += 1
            if added >= per_query_floor or len(selected) >= limit:
                break
        for score, chunk in ranked:
            current = best.get(chunk.chunk_id)
            if current is None or score > current[0]:
                best[chunk.chunk_id] = (score, chunk)

    for _, chunk in sorted(best.values(), key=lambda item: item[0], reverse=True):
        if len(selected) >= limit:
            break
        if chunk.chunk_id in seen:
            continue
        selected.append(chunk)
        seen.add(chunk.chunk_id)
    return selected[:limit]


def merge_ranked_automation_chunks(groups: list[tuple[str, list[AutomationChunkResult]]], limit: int) -> list[AutomationChunkResult]:
    best: dict[str, tuple[int, AutomationChunkResult]] = {}
    selected: list[AutomationChunkResult] = []
    seen: set[str] = set()
    per_query_floor = 1

    for query_index, (query, chunks) in enumerate(groups):
        ranked = sorted(
            ((chunk_score(chunk, query, query_index), chunk) for chunk in chunks),
            key=lambda item: item[0],
            reverse=True,
        )
        added = 0
        for _, chunk in ranked:
            if chunk.chunk_id in seen:
                continue
            selected.append(chunk)
            seen.add(chunk.chunk_id)
            added += 1
            if added >= per_query_floor or len(selected) >= limit:
                break
        for score, chunk in ranked:
            current = best.get(chunk.chunk_id)
            if current is None or score > current[0]:
                best[chunk.chunk_id] = (score, chunk)

    for _, chunk in sorted(best.values(), key=lambda item: item[0], reverse=True):
        if len(selected) >= limit:
            break
        if chunk.chunk_id in seen:
            continue
        selected.append(chunk)
        seen.add(chunk.chunk_id)
    return selected[:limit]


def merge_ranked_backend_chunks(groups: list[tuple[str, list[BackendChunkResult]]], limit: int) -> list[BackendChunkResult]:
    best: dict[str, tuple[int, BackendChunkResult]] = {}
    selected: list[BackendChunkResult] = []
    seen: set[str] = set()
    per_query_floor = 1

    for query_index, (query, chunks) in enumerate(groups):
        ranked = sorted(
            ((backend_chunk_score(chunk, query, query_index), chunk) for chunk in chunks),
            key=lambda item: item[0],
            reverse=True,
        )
        added = 0
        for _, chunk in ranked:
            if chunk.chunk_id in seen:
                continue
            selected.append(chunk)
            seen.add(chunk.chunk_id)
            added += 1
            if added >= per_query_floor or len(selected) >= limit:
                break
        for score, chunk in ranked:
            current = best.get(chunk.chunk_id)
            if current is None or score > current[0]:
                best[chunk.chunk_id] = (score, chunk)

    for _, chunk in sorted(best.values(), key=lambda item: item[0], reverse=True):
        if len(selected) >= limit:
            break
        if chunk.chunk_id in seen:
            continue
        selected.append(chunk)
        seen.add(chunk.chunk_id)
    return selected[:limit]


def connect_db(path: Path, missing_detail: str) -> sqlite3.Connection:
    if not path.exists():
        raise HTTPException(status_code=503, detail=missing_detail)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def connect() -> sqlite3.Connection:
    return connect_db(
        UI_DB_PATH,
        f"UI database not found: {UI_DB_PATH}. Run scripts/ui_design/build_sqlite_index.py first.",
    )


def connect_workflow() -> sqlite3.Connection:
    return connect_db(
        WORKFLOW_DB_PATH,
        f"Agent workflow database not found: {WORKFLOW_DB_PATH}. Run scripts/agent_workflow/build_sqlite_index.py first.",
    )


def connect_automation() -> sqlite3.Connection:
    return connect_db(
        AUTOMATION_DB_PATH,
        f"Automation database not found: {AUTOMATION_DB_PATH}. Run scripts/automation/build_sqlite_index.py first.",
    )


def connect_backend() -> sqlite3.Connection:
    return connect_db(
        BACKEND_DB_PATH,
        f"Backend database not found: {BACKEND_DB_PATH}. Run scripts/backend/build_sqlite_index.py first.",
    )


def parse_metadata(raw: str) -> dict[str, Any]:
    try:
        data = json.loads(raw or "{}")
        return data if isinstance(data, dict) else {}
    except json.JSONDecodeError:
        return {}


def parse_json_list(raw: str) -> list[str]:
    try:
        data = json.loads(raw or "[]")
    except json.JSONDecodeError:
        return []
    return safe_list(data)


def row_to_chunk(row: sqlite3.Row) -> ChunkResult:
    return ChunkResult(
        chunk_id=row["chunk_id"],
        record_id=row["record_id"],
        source_name=row["source_name"],
        source_url=row["source_url"],
        page_type=row["page_type"],
        section=row["section"],
        content=row["content"],
        tokens=int(row["tokens"]),
        metadata=parse_metadata(row["metadata_json"]),
    )


def row_to_workflow_chunk(row: sqlite3.Row) -> WorkflowChunkResult:
    return WorkflowChunkResult(
        chunk_id=row["chunk_id"],
        record_id=row["record_id"],
        workflow_type=row["workflow_type"],
        source_name=row["source_name"],
        source_url=row["source_url"],
        section=row["section"],
        content=row["content"],
        tokens=int(row["tokens"]),
        metadata=parse_metadata(row["metadata_json"]),
    )


def row_to_automation_chunk(row: sqlite3.Row) -> AutomationChunkResult:
    return AutomationChunkResult(
        chunk_id=row["chunk_id"],
        record_id=row["record_id"],
        automation_type=row["automation_type"],
        source_name=row["source_name"],
        source_url=row["source_url"],
        section=row["section"],
        content=row["content"],
        tokens=int(row["tokens"]),
        metadata=parse_metadata(row["metadata_json"]),
    )


def row_to_backend_chunk(row: sqlite3.Row) -> BackendChunkResult:
    return BackendChunkResult(
        chunk_id=row["chunk_id"],
        source_type=row["source_type"],
        title=row["title"],
        relative_path=row["relative_path"],
        section=row["section"],
        content=row["content"],
        summary=row["summary"],
        tags=parse_json_list(row["tags_json"]),
        keywords=parse_json_list(row["keywords_json"]),
        priority=row["priority"],
        trust_level=row["trust_level"],
        metadata=parse_metadata(row["metadata_json"]),
    )


def search_fts(conn: sqlite3.Connection, query: str, limit: int) -> list[sqlite3.Row]:
    try:
        return conn.execute(
            """
            SELECT c.chunk_id, c.record_id, c.source_name, c.source_url, c.page_type,
                   c.section, c.content, c.tokens, c.metadata_json
            FROM chunks_fts f
            JOIN chunks c ON c.chunk_id = f.chunk_id
            WHERE chunks_fts MATCH ?
            LIMIT ?
            """,
            (query, max(limit * 6, limit)),
        ).fetchall()
    except sqlite3.OperationalError:
        return []


def search_like(conn: sqlite3.Connection, query: str, limit: int) -> list[sqlite3.Row]:
    pattern = f"%{query}%"
    return conn.execute(
        """
        SELECT chunk_id, record_id, source_name, source_url, page_type,
               section, content, tokens, metadata_json
        FROM chunks
        WHERE content LIKE ? OR page_type LIKE ? OR section LIKE ? OR source_name LIKE ?
        LIMIT ?
        """,
        (pattern, pattern, pattern, pattern, max(limit * 6, limit)),
    ).fetchall()


def search_like_terms(conn: sqlite3.Connection, query: str, limit: int) -> list[sqlite3.Row]:
    terms = query_terms(query)
    if not terms:
        return []
    clauses = []
    params: list[str | int] = []
    for term in terms:
        clauses.append("(content LIKE ? OR page_type LIKE ? OR section LIKE ? OR source_name LIKE ?)")
        pattern = f"%{term}%"
        params.extend([pattern, pattern, pattern, pattern])
    params.append(max(limit * 12, limit))
    return conn.execute(
        f"""
        SELECT chunk_id, record_id, source_name, source_url, page_type,
               section, content, tokens, metadata_json
        FROM chunks
        WHERE {" OR ".join(clauses)}
        LIMIT ?
        """,
        params,
    ).fetchall()


def search_ui_chunks(q: str, limit: int) -> list[ChunkResult]:
    normalized_q = normalize_query(q)
    candidate_limit = max(10, min(50, limit * 4))
    with connect() as conn:
        rows = (
            search_fts(conn, normalized_q, candidate_limit)
            + search_like(conn, normalized_q, candidate_limit)
            + search_like_terms(conn, normalized_q, candidate_limit)
        )
    chunks = [row_to_chunk(row) for row in rows]
    chunks = list({chunk.chunk_id: chunk for chunk in chunks}.values())
    return sorted(chunks, key=lambda chunk: chunk_score(chunk, normalized_q, 0), reverse=True)[:limit]


@app.get("/")
def read_root() -> dict[str, str]:
    return {"status": "ok", "message": "DataBase Knowledge API is ready"}


@app.get("/health")
def health() -> dict[str, Any]:
    db_exists = UI_DB_PATH.exists()
    payload: dict[str, Any] = {
        "status": "ok" if db_exists else "degraded",
        "ui_db_path": str(UI_DB_PATH),
        "ui_db_exists": db_exists,
        "workflow_db_path": str(WORKFLOW_DB_PATH),
        "workflow_db_exists": WORKFLOW_DB_PATH.exists(),
        "automation_db_path": str(AUTOMATION_DB_PATH),
        "automation_db_exists": AUTOMATION_DB_PATH.exists(),
        "backend_db_path": str(BACKEND_DB_PATH),
        "backend_db_exists": BACKEND_DB_PATH.exists(),
        "ui_asset_metadata_path": str(UI_ASSET_METADATA_DIR),
        "ui_asset_metadata_exists": UI_ASSET_METADATA_DIR.exists(),
        "ui_assets": len(load_asset_records()),
    }
    if db_exists:
        with connect() as conn:
            payload["references"] = conn.execute("SELECT COUNT(*) FROM references_meta").fetchone()[0]
            payload["chunks"] = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
    if WORKFLOW_DB_PATH.exists():
        with connect_workflow() as conn:
            payload["workflow_references"] = conn.execute("SELECT COUNT(*) FROM references_meta").fetchone()[0]
            payload["workflow_chunks"] = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
    if AUTOMATION_DB_PATH.exists():
        with connect_automation() as conn:
            payload["automation_references"] = conn.execute("SELECT COUNT(*) FROM references_meta").fetchone()[0]
            payload["automation_chunks"] = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
    if BACKEND_DB_PATH.exists():
        with connect_backend() as conn:
            payload["backend_chunks"] = conn.execute("SELECT COUNT(*) FROM backend_chunks").fetchone()[0]
    log_api_request(
        "GET",
        "/health",
        result={
            "status": payload["status"],
            "ui_references": payload.get("references"),
            "ui_chunks": payload.get("chunks"),
            "workflow_references": payload.get("workflow_references"),
            "workflow_chunks": payload.get("workflow_chunks"),
            "automation_references": payload.get("automation_references"),
            "automation_chunks": payload.get("automation_chunks"),
            "backend_chunks": payload.get("backend_chunks"),
            "ui_assets": payload.get("ui_assets"),
        },
    )
    return payload


@app.get("/ui/search", response_model=list[ChunkResult])
def search_ui(
    q: Annotated[str, Query(min_length=1, description="Search query, for example: liquid glass")],
    limit: Annotated[int, Query(ge=1, le=50)] = 5,
) -> list[ChunkResult]:
    normalized_q = normalize_query(q)
    chunks = search_ui_chunks(q, limit)
    log_api_request(
        "GET",
        "/ui/search",
        params={"q": q, "normalized_q": normalized_q, "limit": limit},
        result={"count": len(chunks), "chunk_ids": [chunk.chunk_id for chunk in chunks]},
    )
    return chunks


@app.get("/ui/references", response_model=list[ReferenceSummary])
def list_references(
    page_type: Annotated[str | None, Query()] = None,
    limit: Annotated[int, Query(ge=1, le=200)] = 50,
) -> list[ReferenceSummary]:
    sql = """
        SELECT record_id, source_name, source_url, page_type, signal_strength,
               evidence_level, ai_summary
        FROM references_meta
    """
    params: list[Any] = []
    if page_type:
        sql += " WHERE page_type = ?"
        params.append(page_type)
    sql += " ORDER BY record_id LIMIT ?"
    params.append(limit)

    with connect() as conn:
        rows = conn.execute(sql, params).fetchall()
    references = [ReferenceSummary(**dict(row)) for row in rows]
    log_api_request(
        "GET",
        "/ui/references",
        params={"page_type": page_type, "limit": limit},
        result={"count": len(references), "record_ids": [reference.record_id for reference in references]},
    )
    return references


@app.get("/ui/reference/{record_id}")
def get_reference(record_id: str) -> dict[str, Any]:
    with connect() as conn:
        row = conn.execute(
            "SELECT record_json FROM references_meta WHERE record_id = ?",
            (record_id,),
        ).fetchone()
    if row is None:
        log_api_request(
            "GET",
            "/ui/reference/{record_id}",
            params={"record_id": record_id},
            status="not_found",
        )
        raise HTTPException(status_code=404, detail=f"Reference not found: {record_id}")
    try:
        data = json.loads(row["record_json"])
    except json.JSONDecodeError as exc:
        raise HTTPException(status_code=500, detail=f"Stored reference JSON is invalid: {exc}") from exc
    log_api_request(
        "GET",
        "/ui/reference/{record_id}",
        params={"record_id": record_id},
        result={"record_id": data.get("record_id"), "page_type": data.get("page_type")},
    )
    return data


@app.get("/assets/search", response_model=list[AssetResult])
def search_assets(
    q: Annotated[str, Query(min_length=1, description="Search UI assets, for example: dynamic background")],
    limit: Annotated[int, Query(ge=1, le=50)] = 8,
    asset_type: Annotated[str | None, Query()] = None,
    usage_policy: Annotated[str | None, Query()] = None,
) -> list[AssetResult]:
    assets = search_assets_records(q=q, limit=limit, asset_type=asset_type, usage_policy=usage_policy)
    log_api_request(
        "GET",
        "/assets/search",
        params={"q": q, "limit": limit, "asset_type": asset_type, "usage_policy": usage_policy},
        result={"count": len(assets), "asset_ids": [asset.asset_id for asset in assets]},
    )
    return assets


@app.get("/assets/reference/{asset_id}")
def get_asset_reference(asset_id: str) -> dict[str, Any]:
    asset_paths = UI_ASSET_METADATA_DIR.glob("*.json") if UI_ASSET_METADATA_DIR.exists() else []
    for path in asset_paths:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(data, dict) and data.get("asset_id") == asset_id:
            log_api_request(
                "GET",
                "/assets/reference/{asset_id}",
                params={"asset_id": asset_id},
                result={"asset_id": asset_id, "asset_type": data.get("asset_type")},
            )
            return data
    log_api_request(
        "GET",
        "/assets/reference/{asset_id}",
        params={"asset_id": asset_id},
        status="not_found",
    )
    raise HTTPException(status_code=404, detail=f"Asset reference not found: {asset_id}")



def search_workflow_fts(conn: sqlite3.Connection, query: str, limit: int) -> list[sqlite3.Row]:
    try:
        return conn.execute(
            """
            SELECT c.chunk_id, c.record_id, c.workflow_type, c.source_name, c.source_url,
                   c.section, c.content, c.tokens, c.metadata_json
            FROM chunks_fts f
            JOIN chunks c ON c.chunk_id = f.chunk_id
            WHERE chunks_fts MATCH ?
            LIMIT ?
            """,
            (query, limit),
        ).fetchall()
    except sqlite3.OperationalError:
        return []


def search_workflow_like(conn: sqlite3.Connection, query: str, limit: int) -> list[sqlite3.Row]:
    pattern = f"%{query}%"
    return conn.execute(
        """
        SELECT chunk_id, record_id, workflow_type, source_name, source_url,
               section, content, tokens, metadata_json
        FROM chunks
        WHERE content LIKE ? OR workflow_type LIKE ? OR section LIKE ? OR source_name LIKE ?
        LIMIT ?
        """,
        (pattern, pattern, pattern, pattern, limit),
    ).fetchall()


def search_workflow_chunks(q: str, limit: int) -> list[WorkflowChunkResult]:
    normalized_q = normalize_query(q)
    with connect_workflow() as conn:
        rows = search_workflow_fts(conn, normalized_q, limit) or search_workflow_like(conn, normalized_q, limit)
    return [row_to_workflow_chunk(row) for row in rows]


@app.get("/workflow/search", response_model=list[WorkflowChunkResult])
def search_workflow(
    q: Annotated[str, Query(min_length=1, description="Search query, for example: api first")],
    limit: Annotated[int, Query(ge=1, le=50)] = 5,
) -> list[WorkflowChunkResult]:
    normalized_q = normalize_query(q)
    chunks = search_workflow_chunks(q, limit)
    log_api_request(
        "GET",
        "/workflow/search",
        params={"q": q, "normalized_q": normalized_q, "limit": limit},
        result={"count": len(chunks), "chunk_ids": [chunk.chunk_id for chunk in chunks]},
    )
    return chunks


@app.get("/workflow/references", response_model=list[WorkflowReferenceSummary])
def list_workflow_references(
    workflow_type: Annotated[str | None, Query()] = None,
    limit: Annotated[int, Query(ge=1, le=200)] = 50,
) -> list[WorkflowReferenceSummary]:
    sql = """
        SELECT record_id, source_name, source_url, workflow_type, signal_strength,
               evidence_level, ai_summary
        FROM references_meta
    """
    params: list[Any] = []
    if workflow_type:
        sql += " WHERE workflow_type = ?"
        params.append(workflow_type)
    sql += " ORDER BY record_id LIMIT ?"
    params.append(limit)
    with connect_workflow() as conn:
        rows = conn.execute(sql, params).fetchall()
    references = [WorkflowReferenceSummary(**dict(row)) for row in rows]
    log_api_request(
        "GET",
        "/workflow/references",
        params={"workflow_type": workflow_type, "limit": limit},
        result={"count": len(references), "record_ids": [reference.record_id for reference in references]},
    )
    return references


@app.get("/workflow/reference/{record_id}")
def get_workflow_reference(record_id: str) -> dict[str, Any]:
    with connect_workflow() as conn:
        row = conn.execute(
            "SELECT record_json FROM references_meta WHERE record_id = ?",
            (record_id,),
        ).fetchone()
    if row is None:
        log_api_request(
            "GET",
            "/workflow/reference/{record_id}",
            params={"record_id": record_id},
            status="not_found",
        )
        raise HTTPException(status_code=404, detail=f"Workflow reference not found: {record_id}")
    try:
        data = json.loads(row["record_json"])
    except json.JSONDecodeError as exc:
        raise HTTPException(status_code=500, detail=f"Stored workflow reference JSON is invalid: {exc}") from exc
    log_api_request(
        "GET",
        "/workflow/reference/{record_id}",
        params={"record_id": record_id},
        result={"record_id": data.get("record_id"), "workflow_type": data.get("workflow_type")},
    )
    return data


def search_automation_fts(conn: sqlite3.Connection, query: str, limit: int) -> list[sqlite3.Row]:
    try:
        return conn.execute(
            """
            SELECT c.chunk_id, c.record_id, c.automation_type, c.source_name, c.source_url,
                   c.section, c.content, c.tokens, c.metadata_json
            FROM chunks_fts f
            JOIN chunks c ON c.chunk_id = f.chunk_id
            WHERE chunks_fts MATCH ?
            LIMIT ?
            """,
            (query, limit),
        ).fetchall()
    except sqlite3.OperationalError:
        return []


def search_automation_like(conn: sqlite3.Connection, query: str, limit: int) -> list[sqlite3.Row]:
    pattern = f"%{query}%"
    return conn.execute(
        """
        SELECT chunk_id, record_id, automation_type, source_name, source_url,
               section, content, tokens, metadata_json
        FROM chunks
        WHERE content LIKE ? OR automation_type LIKE ? OR section LIKE ? OR source_name LIKE ?
        LIMIT ?
        """,
        (pattern, pattern, pattern, pattern, limit),
    ).fetchall()


def search_automation_chunks(q: str, limit: int) -> list[AutomationChunkResult]:
    normalized_q = normalize_query(q)
    candidate_limit = max(10, min(50, limit * 4))
    with connect_automation() as conn:
        rows = search_automation_fts(conn, normalized_q, candidate_limit) or search_automation_like(conn, normalized_q, candidate_limit)
    chunks = [row_to_automation_chunk(row) for row in rows]
    return sorted(chunks, key=lambda chunk: chunk_score(chunk, normalized_q, 0), reverse=True)[:limit]


@app.get("/automation/search", response_model=list[AutomationChunkResult])
def search_automation(
    q: Annotated[str, Query(min_length=1, description="Search query, for example: file upload")],
    limit: Annotated[int, Query(ge=1, le=50)] = 5,
) -> list[AutomationChunkResult]:
    normalized_q = normalize_query(q)
    chunks = search_automation_chunks(q, limit)
    log_api_request(
        "GET",
        "/automation/search",
        params={"q": q, "normalized_q": normalized_q, "limit": limit},
        result={"count": len(chunks), "chunk_ids": [chunk.chunk_id for chunk in chunks]},
    )
    return chunks


@app.get("/automation/references", response_model=list[AutomationReferenceSummary])
def list_automation_references(
    automation_type: Annotated[str | None, Query()] = None,
    limit: Annotated[int, Query(ge=1, le=200)] = 50,
) -> list[AutomationReferenceSummary]:
    sql = """
        SELECT record_id, source_name, source_url, automation_type, signal_strength,
               evidence_level, ai_summary
        FROM references_meta
    """
    params: list[Any] = []
    if automation_type:
        sql += " WHERE automation_type = ?"
        params.append(automation_type)
    sql += " ORDER BY record_id LIMIT ?"
    params.append(limit)
    with connect_automation() as conn:
        rows = conn.execute(sql, params).fetchall()
    references = [AutomationReferenceSummary(**dict(row)) for row in rows]
    log_api_request(
        "GET",
        "/automation/references",
        params={"automation_type": automation_type, "limit": limit},
        result={"count": len(references), "record_ids": [reference.record_id for reference in references]},
    )
    return references


@app.get("/automation/reference/{record_id}")
def get_automation_reference(record_id: str) -> dict[str, Any]:
    with connect_automation() as conn:
        row = conn.execute(
            "SELECT record_json FROM references_meta WHERE record_id = ?",
            (record_id,),
        ).fetchone()
    if row is None:
        log_api_request(
            "GET",
            "/automation/reference/{record_id}",
            params={"record_id": record_id},
            status="not_found",
        )
        raise HTTPException(status_code=404, detail=f"Automation reference not found: {record_id}")
    try:
        data = json.loads(row["record_json"])
    except json.JSONDecodeError as exc:
        raise HTTPException(status_code=500, detail=f"Stored automation reference JSON is invalid: {exc}") from exc
    log_api_request(
        "GET",
        "/automation/reference/{record_id}",
        params={"record_id": record_id},
        result={"record_id": data.get("record_id"), "automation_type": data.get("automation_type")},
    )
    return data


def search_backend_fts(conn: sqlite3.Connection, query: str, limit: int) -> list[sqlite3.Row]:
    try:
        return conn.execute(
            """
            SELECT c.chunk_id, c.source_type, c.title, c.relative_path, c.section,
                   c.content, c.summary, c.tags_json, c.keywords_json, c.priority,
                   c.trust_level, c.metadata_json
            FROM backend_chunks_fts f
            JOIN backend_chunks c ON c.chunk_id = f.chunk_id
            WHERE backend_chunks_fts MATCH ?
            LIMIT ?
            """,
            (query, limit),
        ).fetchall()
    except sqlite3.OperationalError:
        return []


def search_backend_like(conn: sqlite3.Connection, query: str, limit: int) -> list[sqlite3.Row]:
    pattern = f"%{query}%"
    return conn.execute(
        """
        SELECT chunk_id, source_type, title, relative_path, section, content, summary,
               tags_json, keywords_json, priority, trust_level, metadata_json
        FROM backend_chunks
        WHERE content LIKE ? OR summary LIKE ? OR title LIKE ? OR section LIKE ?
              OR source_type LIKE ? OR tags_json LIKE ? OR keywords_json LIKE ?
        LIMIT ?
        """,
        (pattern, pattern, pattern, pattern, pattern, pattern, pattern, limit),
    ).fetchall()


def search_backend_like_terms(conn: sqlite3.Connection, query: str, limit: int) -> list[sqlite3.Row]:
    terms = query_terms(query)
    if not terms:
        return []
    clauses = []
    params: list[str | int] = []
    for term in terms:
        clauses.append(
            "(content LIKE ? OR summary LIKE ? OR title LIKE ? OR section LIKE ? "
            "OR source_type LIKE ? OR tags_json LIKE ? OR keywords_json LIKE ?)"
        )
        pattern = f"%{term}%"
        params.extend([pattern, pattern, pattern, pattern, pattern, pattern, pattern])
    params.append(limit)
    return conn.execute(
        f"""
        SELECT chunk_id, source_type, title, relative_path, section, content, summary,
               tags_json, keywords_json, priority, trust_level, metadata_json
        FROM backend_chunks
        WHERE {" OR ".join(clauses)}
        LIMIT ?
        """,
        params,
    ).fetchall()


def search_backend_chunks(q: str, limit: int) -> list[BackendChunkResult]:
    normalized_q = normalize_query(q)
    candidate_limit = max(10, min(80, limit * 5))
    with connect_backend() as conn:
        rows = (
            search_backend_fts(conn, normalized_q, candidate_limit)
            + search_backend_like(conn, normalized_q, candidate_limit)
            + search_backend_like_terms(conn, normalized_q, candidate_limit)
        )
    chunks = [row_to_backend_chunk(row) for row in rows]
    chunks = list({chunk.chunk_id: chunk for chunk in chunks}.values())
    return sorted(chunks, key=lambda chunk: backend_chunk_score(chunk, normalized_q, 0), reverse=True)[:limit]


@app.get("/backend/search", response_model=list[BackendChunkResult])
def search_backend(
    q: Annotated[str, Query(min_length=1, description="Search backend engineering chunks, for example: JWT RBAC")],
    limit: Annotated[int, Query(ge=1, le=50)] = 5,
) -> list[BackendChunkResult]:
    normalized_q = normalize_query(q)
    chunks = search_backend_chunks(q, limit)
    log_api_request(
        "GET",
        "/backend/search",
        params={"q": q, "normalized_q": normalized_q, "limit": limit},
        result={"count": len(chunks), "chunk_ids": [chunk.chunk_id for chunk in chunks]},
    )
    return chunks


def build_brief_response(
    task: str,
    ui_limit: int = 8,
    workflow_limit: int = 5,
    automation_limit: int = 0,
    backend_limit: int = 6,
    asset_limit: int = 6,
) -> BriefResponse:
    ui_limit = max(1, min(ui_limit, 30))
    workflow_limit = max(1, min(workflow_limit, 20))
    automation_limit = max(0, min(automation_limit, 20))
    backend_limit = max(0, min(backend_limit, 20))
    asset_limit = max(0, min(asset_limit, 30))
    ui_queries = derive_queries(task, UI_QUERY_RULES, ["dashboard", "form validation", "website reveal"])
    workflow_queries = dedupe_strings(["api first", "knowledge first frontend", "handoff report"] + derive_queries(task, WORKFLOW_QUERY_RULES, []))[:5]
    automation_queries = derive_queries(task, AUTOMATION_QUERY_RULES, []) if automation_limit else []
    backend_queries = derive_queries(task, BACKEND_QUERY_RULES, ["backend api design"]) if backend_limit and needs_backend_context(task) else []
    asset_queries = derive_asset_queries(task) if asset_limit else []

    ui_groups = [(query, search_ui_chunks(q=query, limit=max(8, min(12, ui_limit * 2)))) for query in ui_queries]
    workflow_groups = [(query, search_workflow_chunks(q=query, limit=max(6, min(10, workflow_limit * 2)))) for query in workflow_queries]
    automation_groups = [
        (query, search_automation_chunks(q=query, limit=max(6, min(10, automation_limit * 2))))
        for query in automation_queries
    ] if automation_limit else []
    backend_groups = [
        (query, search_backend_chunks(q=query, limit=max(6, min(14, backend_limit * 2))))
        for query in backend_queries
    ] if backend_queries else []
    asset_groups = [
        (query, search_assets_records(q=query, limit=max(8, min(20, asset_limit * 2))))
        for query in asset_queries
    ] if asset_limit else []

    ui_chunks = merge_ranked_ui_chunks(ui_groups, ui_limit)
    workflow_chunks = merge_ranked_workflow_chunks(workflow_groups, workflow_limit)
    automation_chunks = merge_ranked_automation_chunks(automation_groups, automation_limit) if automation_groups else []
    backend_chunks = merge_ranked_backend_chunks(backend_groups, backend_limit) if backend_groups else []
    asset_suggestions = merge_ranked_assets(asset_groups, asset_limit) if asset_groups else []

    guidance = [
        "Use the returned workflow chunks as the execution protocol.",
        "Use the returned UI chunks as design constraints, not decorative suggestions.",
        "For UI generation, apply the premium UI execution self-check before coding and before final output: choose visual direction, hero pattern, material system, visual anchor, component system, motion strategy, and report record_id/rules used.",
        "Use asset_suggestions according to usage_policy: inspiration_only is visual reference only, review_required needs license review before direct use, direct_use can be used as a project asset.",
        "Report exact queries and chunk_ids in the final handoff.",
        "If chunks or assets are irrelevant or missing, call /ui/search, /workflow/search, /assets/search, or /automation/search with narrower terms.",
    ]
    if automation_chunks:
        guidance.insert(
            2,
            "Use the returned automation chunks only for explicit browser automation, upload, CDP, selector, or verification tasks.",
        )
    if backend_chunks:
        guidance.insert(
            2,
            "Use the returned backend chunks for API, database, auth, security, deployment, AI backend, and GitHub backend project constraints.",
        )
    if needs_motion_asset_bootstrap(task):
        guidance.append(
            "This high-end UI motion task requires additional /assets/search calls for: "
            + ", ".join(MOTION_ASSET_BOOTSTRAP_QUERIES)
            + ". Final output must report retrieved asset_id/chunk_id, usage_policy, direct-use versus inspiration-only status, and CSS/SVG/Canvas/Lottie/video implementation method. If no direct_use animation asset is found, state: 未检索到可用 direct_use 动画素材，因此使用 CSS/SVG/Canvas 复刻动效。"
        )
    return BriefResponse(
        brief=task,
        ui_queries=ui_queries,
        workflow_queries=workflow_queries,
        automation_queries=automation_queries,
        backend_queries=backend_queries,
        asset_queries=asset_queries,
        ui_chunks=ui_chunks,
        workflow_chunks=workflow_chunks,
        automation_chunks=automation_chunks,
        backend_chunks=backend_chunks,
        asset_suggestions=asset_suggestions,
        guidance=guidance,
    )


@app.get("/brief", response_model=BriefResponse)
def build_brief(
    task: Annotated[str, Query(min_length=3, description="Task brief, for example: build a liquid glass AI dashboard")],
    ui_limit: Annotated[int, Query(ge=1, le=30)] = 8,
    workflow_limit: Annotated[int, Query(ge=1, le=20)] = 5,
    automation_limit: Annotated[int, Query(ge=0, le=20)] = 0,
    backend_limit: Annotated[int, Query(ge=0, le=20)] = 6,
    asset_limit: Annotated[int, Query(ge=0, le=30)] = 6,
) -> BriefResponse:
    response = build_brief_response(
        task=task,
        ui_limit=ui_limit,
        workflow_limit=workflow_limit,
        automation_limit=automation_limit,
        backend_limit=backend_limit,
        asset_limit=asset_limit,
    )
    log_api_request(
        "GET",
        "/brief",
        params={
            "task": task,
            "ui_limit": ui_limit,
            "workflow_limit": workflow_limit,
            "automation_limit": automation_limit,
            "backend_limit": backend_limit,
            "asset_limit": asset_limit,
        },
        result={
            "ui_queries": response.ui_queries,
            "workflow_queries": response.workflow_queries,
            "automation_queries": response.automation_queries,
            "backend_queries": response.backend_queries,
            "asset_queries": response.asset_queries,
            "ui_chunk_ids": [chunk.chunk_id for chunk in response.ui_chunks],
            "workflow_chunk_ids": [chunk.chunk_id for chunk in response.workflow_chunks],
            "automation_chunk_ids": [chunk.chunk_id for chunk in response.automation_chunks],
            "backend_chunk_ids": [chunk.chunk_id for chunk in response.backend_chunks],
            "asset_ids": [asset.asset_id for asset in response.asset_suggestions],
        },
    )
    return response


@app.post("/brief", response_model=BriefResponse)
def post_brief(request: Annotated[BriefRequest, Body()]) -> BriefResponse:
    response = build_brief_response(
        task=request.task,
        ui_limit=request.ui_limit,
        workflow_limit=request.workflow_limit,
        automation_limit=request.automation_limit,
        backend_limit=request.backend_limit,
        asset_limit=request.asset_limit,
    )
    log_api_request(
        "POST",
        "/brief",
        params={
            "task": request.task,
            "ui_limit": request.ui_limit,
            "workflow_limit": request.workflow_limit,
            "automation_limit": request.automation_limit,
            "backend_limit": request.backend_limit,
            "asset_limit": request.asset_limit,
        },
        result={
            "ui_queries": response.ui_queries,
            "workflow_queries": response.workflow_queries,
            "automation_queries": response.automation_queries,
            "backend_queries": response.backend_queries,
            "asset_queries": response.asset_queries,
            "ui_chunk_ids": [chunk.chunk_id for chunk in response.ui_chunks],
            "workflow_chunk_ids": [chunk.chunk_id for chunk in response.workflow_chunks],
            "automation_chunk_ids": [chunk.chunk_id for chunk in response.automation_chunks],
            "backend_chunk_ids": [chunk.chunk_id for chunk in response.backend_chunks],
            "asset_ids": [asset.asset_id for asset in response.asset_suggestions],
        },
    )
    return response
