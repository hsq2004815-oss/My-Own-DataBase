"""Search the local UI design SQLite index."""

from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DB_PATH = ROOT / "runtime" / "db" / "sqlite" / "ui_design" / "ui_design_references.db"


def search_fts(conn: sqlite3.Connection, query: str, limit: int) -> list[sqlite3.Row]:
    try:
        return conn.execute(
            """
            SELECT c.chunk_id, c.record_id, c.source_name, c.page_type, c.section, c.content
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
        SELECT chunk_id, record_id, source_name, page_type, section, content
        FROM chunks
        WHERE content LIKE ? OR page_type LIKE ? OR section LIKE ?
        LIMIT ?
        """,
        (pattern, pattern, pattern, max(limit * 6, limit)),
    ).fetchall()


def query_terms(query: str) -> list[str]:
    aliases = {
        "高级": "premium",
        "高端": "premium",
        "视觉锚点": "visual anchor",
        "非模板": "non generic layout",
        "非模板化": "non generic layout",
        "技术可视化": "technical visualization",
        "项目专属视觉": "project specific visuals",
        "玻璃质感检查": "glass quality check",
        "设计自检": "design self check",
        "组件密度": "component density",
        "玻璃": "liquid glass glassmorphism",
        "拟态": "glassmorphism",
        "工作台": "workspace web app ui kit",
        "工作区": "workspace web app ui kit",
        "项目空间": "workspace web app ui kit",
        "视频": "video",
        "视频首屏": "video hero layout",
        "高级视频首屏": "video hero layout",
        "底部左对齐": "bottom left hero",
        "顶部压迫式": "top aligned hero",
        "双栏": "two panel split hero",
        "液态玻璃": "liquid glass",
        "灰度": "strict grayscale",
        "编程教育": "technical education",
        "网格线": "vertical grid",
        "光晕": "svg glow",
        "背景": "background",
        "字体": "typography",
        "动效": "motion",
        "首页": "landing page",
    }
    expanded = query
    for source, target in aliases.items():
        if source in expanded:
            expanded = f"{expanded} {target}"
    terms: list[str] = []
    for raw in expanded.replace("/", " ").replace("-", " ").split():
        term = raw.strip().lower()
        if len(term) >= 2 and term not in {"and", "with", "the", "for", "page"}:
            terms.append(term)
    return list(dict.fromkeys(terms))


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
    params.append(max(limit * 40, 200))
    return conn.execute(
        f"""
        SELECT chunk_id, record_id, source_name, page_type, section, content
        FROM chunks
        WHERE {" OR ".join(clauses)}
        LIMIT ?
        """,
        params,
    ).fetchall()


def score_row(row: sqlite3.Row, query: str) -> int:
    haystack = " ".join(
        str(row[key]).lower()
        for key in ("chunk_id", "record_id", "source_name", "page_type", "section", "content")
    )
    score = 0
    for term in query_terms(query):
        if term in haystack:
            score += 10
    terms = set(query_terms(query))
    if (
        "execution" in terms
        or "anchor" in terms
        or "generic" in terms
        or "quality" in terms
        or "visualization" in terms
        or "self" in terms
        or "density" in terms
        or "check" in terms
    ):
        if "implementation-premium-ui-execution-quality-rules" in haystack:
            score += 150
    if "glass" in terms or "liquid" in terms or "glassmorphism" in terms:
        if "liquid-glass-premium-system" in haystack:
            score += 55
        if "liquid-glass-web-app-ui-kit" in haystack:
            score += 50
        if "implementation-premium-ui-execution-quality-rules" in haystack:
            score += 30
    if "workspace" in terms or "dashboard" in terms or "app" in terms or "kit" in terms:
        if "liquid-glass-web-app-ui-kit" in haystack:
            score += 70
    if "video" in terms or "hero" in terms:
        if "cinematic-video-hero" in haystack:
            score += 55
        if "pattern-video-hero-layout-variants" in haystack:
            score += 80
    if "bottom" in terms or "top" in terms or "aligned" in terms:
        if "pattern-video-hero-layout-variants" in haystack:
            score += 70
    if "panel" in terms or "split" in terms:
        if "two-panel-liquid-glass-hero" in haystack:
            score += 130
    if "hls" in terms or "education" in terms or "technical" in terms or "grid" in terms or "glow" in terms:
        if "technical-education-hls-hero" in haystack:
            score += 85
    if "grayscale" in terms or "strict" in terms:
        if "strict-grayscale-liquid-glass-hero" in haystack:
            score += 130
    if "cta" in terms or "navbar" in terms or "menu" in terms:
        if "premium-video-cta-and-navbar" in haystack:
            score += 65
    if "typography" in terms or "type" in terms:
        if "typography" in haystack:
            score += 55
    if "motion" in terms or "blur" in terms:
        if "motion-blurtext" in haystack or "motion-reveal" in haystack:
            score += 45
    if "landing" in terms:
        if "landing-page-premium-section-composition" in haystack:
            score += 25
    if "premium" in haystack:
        score += 8
    if "premium-ui-execution" in haystack:
        score += 25
    if "user distilled premium web ui prompt set" in haystack:
        score += 12
    if row["section"] in {"implementation", "layout", "overview"}:
        score += 4
    return score


def rank_rows(rows: list[sqlite3.Row], query: str, limit: int) -> list[sqlite3.Row]:
    deduped = {row["chunk_id"]: row for row in rows}
    ranked = sorted(deduped.values(), key=lambda row: score_row(row, query), reverse=True)
    selected: list[sqlite3.Row] = []
    per_record: dict[str, int] = {}
    for row in ranked:
        count = per_record.get(row["record_id"], 0)
        if count >= 2:
            continue
        selected.append(row)
        per_record[row["record_id"]] = count + 1
        if len(selected) >= limit:
            return selected
    for row in ranked:
        if row in selected:
            continue
        selected.append(row)
        if len(selected) >= limit:
            return selected
    return selected


def compact(text: str, max_chars: int = 420) -> str:
    text = " ".join(text.split())
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 3].rstrip() + "..."


def main() -> int:
    parser = argparse.ArgumentParser(description="Search UI design chunks.")
    parser.add_argument("query", help="Search query, for example: dashboard, data table, premium, ai app")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB_PATH)
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()

    if not args.db.exists():
        raise SystemExit(f"Database not found: {args.db}. Run build_sqlite_index.py first.")

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    try:
        candidates = (
            search_fts(conn, args.query, args.limit)
            + search_like(conn, args.query, args.limit)
            + search_like_terms(conn, args.query, args.limit)
        )
        rows = rank_rows(candidates, args.query, args.limit)
    finally:
        conn.close()

    if not rows:
        print("No results")
        return 0

    for i, row in enumerate(rows, start=1):
        print(f"[{i}] {row['chunk_id']} | {row['source_name']} | {row['page_type']} | {row['section']}")
        print(compact(row["content"]))
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
