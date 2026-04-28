"""Build a local SQLite + FTS index for automation records."""

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_REFERENCE_DIR = ROOT / "domains" / "automation" / "processed" / "references"
DEFAULT_CHUNK_DIR = ROOT / "domains" / "automation" / "processed" / "chunks"
DEFAULT_DB_PATH = ROOT / "runtime" / "db" / "sqlite" / "automation" / "automation_references.db"

def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def iter_json(path: Path) -> list[Path]:
    return sorted(path.glob("*.json"))

def create_schema(conn: sqlite3.Connection) -> bool:
    conn.executescript("""
        DROP TABLE IF EXISTS references_meta;
        DROP TABLE IF EXISTS chunks;
        DROP TABLE IF EXISTS sources;
        DROP TABLE IF EXISTS chunks_fts;
        CREATE TABLE sources (source_id TEXT PRIMARY KEY, name TEXT NOT NULL, url TEXT NOT NULL, source_type TEXT NOT NULL, license_notes TEXT NOT NULL);
        CREATE TABLE references_meta (
          record_id TEXT PRIMARY KEY, source_id TEXT NOT NULL, source_name TEXT NOT NULL, source_url TEXT NOT NULL,
          automation_type TEXT NOT NULL, signal_strength TEXT NOT NULL, evidence_level TEXT NOT NULL, ai_summary TEXT NOT NULL, record_json TEXT NOT NULL
        );
        CREATE TABLE chunks (
          chunk_id TEXT PRIMARY KEY, record_id TEXT NOT NULL, automation_type TEXT NOT NULL, source_name TEXT NOT NULL, source_url TEXT NOT NULL,
          section TEXT NOT NULL, content TEXT NOT NULL, tokens INTEGER NOT NULL, metadata_json TEXT NOT NULL
        );
    """)
    try:
        conn.execute("""CREATE VIRTUAL TABLE chunks_fts USING fts5(chunk_id UNINDEXED, record_id UNINDEXED, automation_type, section, content);""")
        return True
    except sqlite3.OperationalError:
        return False

def source_id_from_record(record: dict[str, Any]) -> str:
    return record["source"]["name"].lower().replace("/", "-").replace(" ", "-")

def insert_reference(conn: sqlite3.Connection, record: dict[str, Any]) -> None:
    source_id = source_id_from_record(record)
    conn.execute("INSERT OR REPLACE INTO sources (source_id, name, url, source_type, license_notes) VALUES (?, ?, ?, ?, ?)", (source_id, record["source"]["name"], record["source"]["url"], record["source"]["source_type"], record["source"]["license_notes"]))
    conn.execute("""INSERT OR REPLACE INTO references_meta
        (record_id, source_id, source_name, source_url, automation_type, signal_strength, evidence_level, ai_summary, record_json)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (record["record_id"], source_id, record["source"]["name"], record["source"]["url"], record["automation_type"], record["quality"]["signal_strength"], record["quality"]["evidence_level"], record["retrieval"]["ai_summary"], json.dumps(record, ensure_ascii=False)))

def insert_chunk(conn: sqlite3.Connection, chunk: dict[str, Any], has_fts: bool) -> None:
    conn.execute("""INSERT OR REPLACE INTO chunks
        (chunk_id, record_id, automation_type, source_name, source_url, section, content, tokens, metadata_json)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (chunk["chunk_id"], chunk["record_id"], chunk["automation_type"], chunk["source_name"], chunk["source_url"], chunk["section"], chunk["content"], int(chunk["tokens"]), json.dumps(chunk.get("metadata", {}), ensure_ascii=False)))
    if has_fts:
        conn.execute("INSERT INTO chunks_fts (chunk_id, record_id, automation_type, section, content) VALUES (?, ?, ?, ?, ?)", (chunk["chunk_id"], chunk["record_id"], chunk["automation_type"], chunk["section"], chunk["content"]))

def main() -> int:
    parser = argparse.ArgumentParser(description="Build SQLite index for automation references.")
    parser.add_argument("--references", type=Path, default=DEFAULT_REFERENCE_DIR)
    parser.add_argument("--chunks", type=Path, default=DEFAULT_CHUNK_DIR)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB_PATH)
    args = parser.parse_args()
    reference_files = iter_json(args.references)
    chunk_files = [path for path in iter_json(args.chunks) if path.name != "all_automation_chunks.json"]
    if not reference_files:
        raise SystemExit(f"No reference JSON files found at {args.references}")
    if not chunk_files:
        raise SystemExit(f"No chunk JSON files found at {args.chunks}; run make_chunks.py first")
    args.db.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(args.db)
    try:
        has_fts = create_schema(conn)
        for path in reference_files:
            insert_reference(conn, load_json(path))
        chunk_count = 0
        for path in chunk_files:
            for chunk in load_json(path):
                insert_chunk(conn, chunk, has_fts)
                chunk_count += 1
        conn.commit()
    finally:
        conn.close()
    print(f"indexed {len(reference_files)} automation record(s) and {chunk_count} chunk(s) to {args.db} (fts5={'enabled' if has_fts else 'unavailable'})")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
