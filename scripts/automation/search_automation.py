"""Search the local automation SQLite index."""

from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DB_PATH = ROOT / "runtime" / "db" / "sqlite" / "automation" / "automation_references.db"

def search_fts(conn: sqlite3.Connection, query: str, limit: int) -> list[sqlite3.Row]:
    try:
        return conn.execute("""SELECT c.chunk_id, c.record_id, c.automation_type, c.source_name, c.section, c.content
            FROM chunks_fts f JOIN chunks c ON c.chunk_id = f.chunk_id
            WHERE chunks_fts MATCH ? LIMIT ?""", (query, limit)).fetchall()
    except sqlite3.OperationalError:
        return []

def search_like(conn: sqlite3.Connection, query: str, limit: int) -> list[sqlite3.Row]:
    pattern = f"%{query}%"
    return conn.execute("""SELECT chunk_id, record_id, automation_type, source_name, section, content
        FROM chunks WHERE content LIKE ? OR automation_type LIKE ? OR section LIKE ? LIMIT ?""", (pattern, pattern, pattern, limit)).fetchall()

def compact(text: str, max_chars: int = 420) -> str:
    text = " ".join(text.split())
    return text if len(text) <= max_chars else text[: max_chars - 3].rstrip() + "..."

def main() -> int:
    parser = argparse.ArgumentParser(description="Search automation chunks.")
    parser.add_argument("query")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB_PATH)
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()
    if not args.db.exists():
        raise SystemExit(f"Database not found: {args.db}. Run build_sqlite_index.py first.")
    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    try:
        rows = search_fts(conn, args.query, args.limit) or search_like(conn, args.query, args.limit)
    finally:
        conn.close()
    if not rows:
        print("No results")
        return 0
    for i, row in enumerate(rows, start=1):
        print(f"[{i}] {row['chunk_id']} | {row['automation_type']} | {row['section']}")
        print(compact(row["content"]))
        print()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
