"""Validate backend SQLite/FTS search results against Phase 2C expected targets."""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_TESTS = ROOT / "domains" / "backend" / "output" / "search_tests" / "backend-search-test-expected-targets.json"
DEFAULT_DB_PATH = ROOT / "runtime" / "db" / "sqlite" / "backend" / "backend_references.db"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def tokenize(query: str) -> list[str]:
    raw_terms = re.findall(r"[\w\u4e00-\u9fff]+", query, re.UNICODE)
    terms = []
    for term in raw_terms:
        if len(term) < 2 or term.lower() in {"and", "with", "the", "for"}:
            continue
        terms.append(term)
    return list(dict.fromkeys(terms))


def fts_query(query: str) -> str:
    terms = tokenize(query)
    return " OR ".join(f'"{term}"' for term in terms) if terms else query


def has_fts(conn: sqlite3.Connection) -> bool:
    row = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='backend_chunks_fts'").fetchone()
    return row is not None


def search_fts(conn: sqlite3.Connection, query: str, limit: int) -> list[sqlite3.Row]:
    try:
        return conn.execute(
            """
            SELECT c.chunk_id, c.source_type, c.title, c.relative_path, c.section, c.content,
                   c.tags_json, c.keywords_json, c.priority, c.trust_level
            FROM backend_chunks_fts f
            JOIN backend_chunks c ON c.chunk_id = f.chunk_id
            WHERE backend_chunks_fts MATCH ?
            ORDER BY bm25(backend_chunks_fts)
            LIMIT ?
            """,
            (fts_query(query), limit),
        ).fetchall()
    except sqlite3.OperationalError:
        return []


def search_like(conn: sqlite3.Connection, query: str, limit: int) -> list[sqlite3.Row]:
    terms = tokenize(query)
    if not terms:
        terms = [query]
    clauses = []
    params: list[Any] = []
    for term in terms:
        pattern = f"%{term}%"
        clauses.append(
            "(title LIKE ? OR relative_path LIKE ? OR section LIKE ? OR content LIKE ? OR tags_json LIKE ? OR keywords_json LIKE ?)"
        )
        params.extend([pattern, pattern, pattern, pattern, pattern, pattern])
    params.append(max(limit * 5, limit))
    return conn.execute(
        f"""
        SELECT chunk_id, source_type, title, relative_path, section, content,
               tags_json, keywords_json, priority, trust_level
        FROM backend_chunks
        WHERE {" OR ".join(clauses)}
        LIMIT ?
        """,
        params,
    ).fetchall()


def parse_json_list(value: str) -> list[str]:
    try:
        data = json.loads(value)
    except json.JSONDecodeError:
        return []
    return [str(item) for item in data] if isinstance(data, list) else []


def row_to_result(row: sqlite3.Row) -> dict[str, Any]:
    tags = parse_json_list(row["tags_json"])
    keywords = parse_json_list(row["keywords_json"])
    return {
        "chunk_id": row["chunk_id"],
        "source_type": row["source_type"],
        "title": row["title"],
        "relative_path": row["relative_path"],
        "section": row["section"],
        "tags": tags,
        "keywords": keywords,
        "priority": row["priority"],
        "trust_level": row["trust_level"],
        "content_preview": " ".join(str(row["content"]).split())[:240],
    }


def validate_one(conn: sqlite3.Connection, test: dict[str, Any], limit: int, use_fts: bool) -> dict[str, Any]:
    rows = search_fts(conn, test["query"], limit) if use_fts else []
    if len(rows) < limit:
        seen = {row["chunk_id"] for row in rows}
        for row in search_like(conn, test["query"], limit):
            if row["chunk_id"] not in seen:
                rows.append(row)
                seen.add(row["chunk_id"])
            if len(rows) >= limit:
                break
    results = [row_to_result(row) for row in rows[:limit]]
    matched_files = sorted({result["relative_path"] for result in results})
    matched_tags = sorted({tag for result in results for tag in result["tags"]})
    expected_files = test.get("expected_files", [])
    expected_types = set(test.get("must_include_source_types", []))
    expected_files_hit = sum(1 for path in expected_files if path in matched_files)
    source_types_hit = len(expected_types.intersection({result["source_type"] for result in results}))
    if expected_files_hit > 0 and source_types_hit >= max(1, len(expected_types)):
        status = "pass"
    elif expected_files_hit > 0 or source_types_hit > 0 or results:
        status = "partial"
    else:
        status = "fail"
    return {
        "query": test["query"],
        "language": test.get("language", ""),
        "intent": test.get("intent", ""),
        "status": status,
        "top_results": results,
        "matched_files": matched_files,
        "matched_tags": matched_tags[:40],
        "expected_files_hit_count": expected_files_hit,
        "expected_source_types_hit_count": source_types_hit,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate backend local SQLite search.")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB_PATH)
    parser.add_argument("--tests", type=Path, default=DEFAULT_TESTS)
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    if not args.db.exists():
        raise SystemExit(f"Database not found: {args.db}")
    test_payload = load_json(args.tests)
    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    try:
        use_fts = has_fts(conn)
        results = [validate_one(conn, test, args.limit, use_fts) for test in test_payload.get("tests", [])]
    finally:
        conn.close()

    summary = {
        "total": len(results),
        "pass": sum(1 for result in results if result["status"] == "pass"),
        "partial": sum(1 for result in results if result["status"] == "partial"),
        "fail": sum(1 for result in results if result["status"] == "fail"),
    }
    report = {
        "domain": "backend",
        "db_path": str(args.db),
        "limit": args.limit,
        "fts_used": use_fts,
        "summary": summary,
        "results": results,
    }
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if summary["fail"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
