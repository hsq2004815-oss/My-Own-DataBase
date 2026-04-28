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
        "玻璃": "liquid glass glassmorphism",
        "拟态": "glassmorphism",
        "视频": "video",
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
    params.append(max(limit * 12, limit))
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
    if "glass" in terms or "liquid" in terms or "glassmorphism" in terms:
        if "liquid-glass-premium-system" in haystack:
            score += 55
    if "video" in terms or "hero" in terms:
        if "cinematic-video-hero" in haystack:
            score += 55
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
