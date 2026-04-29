"""Build the backend SQLite/FTS retrieval index from Phase 2C chunks."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sqlite3
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CHUNK_FILE = (
    ROOT
    / "domains"
    / "backend"
    / "processed"
    / "chunks"
    / "retrieval_ready"
    / "backend-retrieval-chunks.jsonl"
)
DEFAULT_DB_PATH = ROOT / "runtime" / "db" / "sqlite" / "backend" / "backend_references.db"

VALID_PRIORITIES = {"high", "medium", "low"}
VALID_TRUST_LEVELS = {"core_reference", "good_reference", "sample_only", "low_reference", "not_applicable"}
SECRET_RE = re.compile(
    r"(BEGIN [A-Z ]*PRIVATE KEY|AKIA[0-9A-Z]{16}|sk-[A-Za-z0-9_-]{20,}|"
    r"ghp_[A-Za-z0-9_]{20,}|Bearer\s+[A-Za-z0-9._~+/-]{20,}|"
    r"password\s*[:=]\s*[^\s`\"'<>]+|jwt_secret\s*[:=]\s*[^\s`\"'<>]+|"
    r"secret\s*[:=]\s*[^\s`\"'<>]+)",
    re.IGNORECASE,
)
ALLOWED_SECRET_CONTEXT_RE = re.compile(
    r"(CHANGE_ME|REPLACE_WITH_RANDOM_SECRET|REPLACE_WITH_PASSWORD|placeholder|example|示例|原文|疑似|secret management)",
    re.IGNORECASE,
)
SOURCE_LIKE_RE = re.compile(
    r"(?m)(^\s*(def|class|function|import|from|const|let|var)\s+|"
    r"^\s*[A-Za-z_][A-Za-z0-9_]*\s*=\s*function\b|"
    r"^\s*#include\s+|^\s*package\s+[A-Za-z0-9_.]+;)"
)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def load_chunks(path: Path) -> tuple[list[dict[str, Any]], list[str]]:
    chunks: list[dict[str, Any]] = []
    errors: list[str] = []
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            if not line.strip():
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"line {line_no}: JSON parse error: {exc}")
                continue
            if not isinstance(item, dict):
                errors.append(f"line {line_no}: item is not an object")
                continue
            item["_line_no"] = line_no
            chunks.append(item)
    return chunks, errors


def has_secret_like_text(value: str) -> bool:
    for match in SECRET_RE.finditer(value):
        if not ALLOWED_SECRET_CONTEXT_RE.search(match.group(0)):
            return True
    return False


def source_like_score(value: str) -> int:
    return len(SOURCE_LIKE_RE.findall(value))


def validate_chunks(chunks: list[dict[str, Any]]) -> tuple[list[str], dict[str, Any]]:
    errors: list[str] = []
    ids: list[str] = []
    for chunk in chunks:
        line_no = chunk.get("_line_no", "?")
        chunk_id = str(chunk.get("chunk_id", "")).strip()
        ids.append(chunk_id)
        if chunk.get("domain") != "backend":
            errors.append(f"line {line_no}: domain must be backend")
        if not chunk_id:
            errors.append(f"line {line_no}: chunk_id is empty")
        if not str(chunk.get("content", "")).strip():
            errors.append(f"line {line_no}: content is empty")
        if not str(chunk.get("source_type", "")).strip():
            errors.append(f"line {line_no}: source_type is empty")
        if chunk.get("priority") not in VALID_PRIORITIES:
            errors.append(f"line {line_no}: invalid priority {chunk.get('priority')!r}")
        if chunk.get("trust_level") not in VALID_TRUST_LEVELS:
            errors.append(f"line {line_no}: invalid trust_level {chunk.get('trust_level')!r}")
        if not chunk.get("tags") or not chunk.get("keywords"):
            errors.append(f"line {line_no}: tags/keywords must be present")
        combined = json.dumps(chunk, ensure_ascii=False)
        if has_secret_like_text(combined):
            errors.append(f"line {line_no}: secret-like content detected")
        if source_like_score(str(chunk.get("content", ""))) > 12:
            errors.append(f"line {line_no}: source-code-like content is too dense")

    duplicate_ids = sorted(chunk_id for chunk_id, count in Counter(ids).items() if chunk_id and count > 1)
    for chunk_id in duplicate_ids:
        errors.append(f"duplicate chunk_id: {chunk_id}")

    stats = {
        "input_chunks": len(chunks),
        "duplicate_chunk_ids": duplicate_ids,
        "source_type_distribution": dict(sorted(Counter(str(c.get("source_type", "")) for c in chunks).items())),
        "priority_distribution": dict(sorted(Counter(str(c.get("priority", "")) for c in chunks).items())),
        "trust_level_distribution": dict(sorted(Counter(str(c.get("trust_level", "")) for c in chunks).items())),
        "expected_write_count": len(chunks),
    }
    return errors, stats


def create_schema(conn: sqlite3.Connection) -> bool:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS backend_chunks (
          chunk_id TEXT PRIMARY KEY,
          domain TEXT NOT NULL,
          source_type TEXT NOT NULL,
          title TEXT NOT NULL,
          relative_path TEXT NOT NULL,
          section TEXT NOT NULL,
          content TEXT NOT NULL,
          summary TEXT NOT NULL,
          tags_json TEXT NOT NULL,
          keywords_json TEXT NOT NULL,
          priority TEXT NOT NULL,
          trust_level TEXT NOT NULL,
          target_use_cases_json TEXT NOT NULL,
          related_rules_json TEXT NOT NULL,
          related_topics_json TEXT NOT NULL,
          metadata_json TEXT NOT NULL,
          updated_at TEXT NOT NULL
        );
        CREATE INDEX IF NOT EXISTS idx_backend_chunks_domain ON backend_chunks(domain);
        CREATE INDEX IF NOT EXISTS idx_backend_chunks_source_type ON backend_chunks(source_type);
        CREATE INDEX IF NOT EXISTS idx_backend_chunks_priority ON backend_chunks(priority);
        CREATE INDEX IF NOT EXISTS idx_backend_chunks_trust_level ON backend_chunks(trust_level);
        """
    )
    try:
        conn.execute(
            """
            CREATE VIRTUAL TABLE IF NOT EXISTS backend_chunks_fts USING fts5(
              chunk_id UNINDEXED,
              source_type,
              title,
              section,
              content,
              summary,
              tags,
              keywords
            );
            """
        )
        return True
    except sqlite3.OperationalError:
        return False


def backup_db(db_path: Path) -> str:
    if not db_path.exists():
        return ""
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = db_path.parent.parent / "backups"
    backup_dir.mkdir(parents=True, exist_ok=True)
    backup_path = backup_dir / f"{db_path.name}.bak_{stamp}"
    shutil.copy2(db_path, backup_path)
    return rel(backup_path)


def upsert_chunks(conn: sqlite3.Connection, chunks: list[dict[str, Any]], has_fts: bool) -> dict[str, int]:
    now = utc_now()
    inserted = 0
    for chunk in chunks:
        metadata = {
            key: value
            for key, value in chunk.items()
            if key not in {"_line_no", "content"}
        }
        conn.execute(
            """
            INSERT INTO backend_chunks (
              chunk_id, domain, source_type, title, relative_path, section, content, summary,
              tags_json, keywords_json, priority, trust_level, target_use_cases_json,
              related_rules_json, related_topics_json, metadata_json, updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(chunk_id) DO UPDATE SET
              domain=excluded.domain,
              source_type=excluded.source_type,
              title=excluded.title,
              relative_path=excluded.relative_path,
              section=excluded.section,
              content=excluded.content,
              summary=excluded.summary,
              tags_json=excluded.tags_json,
              keywords_json=excluded.keywords_json,
              priority=excluded.priority,
              trust_level=excluded.trust_level,
              target_use_cases_json=excluded.target_use_cases_json,
              related_rules_json=excluded.related_rules_json,
              related_topics_json=excluded.related_topics_json,
              metadata_json=excluded.metadata_json,
              updated_at=excluded.updated_at
            """,
            (
                chunk["chunk_id"],
                "backend",
                chunk["source_type"],
                chunk.get("title", ""),
                chunk.get("relative_path", ""),
                chunk.get("section", ""),
                chunk.get("content", ""),
                chunk.get("summary", ""),
                json.dumps(chunk.get("tags", []), ensure_ascii=False),
                json.dumps(chunk.get("keywords", []), ensure_ascii=False),
                chunk.get("priority", ""),
                chunk.get("trust_level", ""),
                json.dumps(chunk.get("target_use_cases", []), ensure_ascii=False),
                json.dumps(chunk.get("related_rules", []), ensure_ascii=False),
                json.dumps(chunk.get("related_topics", []), ensure_ascii=False),
                json.dumps(metadata, ensure_ascii=False),
                now,
            ),
        )
        if has_fts:
            conn.execute("DELETE FROM backend_chunks_fts WHERE chunk_id = ?", (chunk["chunk_id"],))
            conn.execute(
                """
                INSERT INTO backend_chunks_fts
                (chunk_id, source_type, title, section, content, summary, tags, keywords)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    chunk["chunk_id"],
                    chunk["source_type"],
                    chunk.get("title", ""),
                    chunk.get("section", ""),
                    chunk.get("content", ""),
                    chunk.get("summary", ""),
                    " ".join(str(v) for v in chunk.get("tags", [])),
                    " ".join(str(v) for v in chunk.get("keywords", [])),
                ),
            )
        inserted += 1
    return {"upserted": inserted}


def write_report(path: Path | None, payload: dict[str, Any]) -> None:
    if path is None:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build backend SQLite/FTS index.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true", help="Validate and report without writing SQLite")
    mode.add_argument("--write", action="store_true", help="Write backend chunks to SQLite")
    parser.add_argument("--chunks", type=Path, default=DEFAULT_CHUNK_FILE)
    parser.add_argument("--db", type=Path)
    parser.add_argument("--backup", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    chunks, parse_errors = load_chunks(args.chunks)
    validation_errors, stats = validate_chunks(chunks)
    errors = parse_errors + validation_errors
    report: dict[str, Any] = {
        "domain": "backend",
        "generated_at": utc_now(),
        "mode": "dry_run" if args.dry_run else "write",
        "chunk_file": rel(args.chunks),
        "db_path": rel(args.db) if args.db else "",
        "valid": not errors,
        "errors": errors,
        "stats": stats,
        "runtime_written": False,
        "backup_path": "",
        "fts_enabled": False,
        "tables_used": [],
        "write_result": {},
    }

    if args.dry_run:
        write_report(args.report, report)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if not errors else 1

    if errors:
        write_report(args.report, report)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 1
    if args.db is None:
        report["valid"] = False
        report["errors"].append("--write requires --db")
        write_report(args.report, report)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 1
    if not args.backup:
        report["valid"] = False
        report["errors"].append("--write requires --backup")
        write_report(args.report, report)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 1

    db_path = args.db
    db_path.parent.mkdir(parents=True, exist_ok=True)
    report["backup_path"] = backup_db(db_path)
    conn = sqlite3.connect(db_path)
    try:
        conn.execute("BEGIN")
        has_fts = create_schema(conn)
        result = upsert_chunks(conn, chunks, has_fts)
        conn.commit()
        report["runtime_written"] = True
        report["fts_enabled"] = has_fts
        report["tables_used"] = ["backend_chunks"] + (["backend_chunks_fts"] if has_fts else [])
        report["write_result"] = result
    except Exception as exc:
        conn.rollback()
        report["valid"] = False
        report["errors"].append(f"write failed: {exc}")
        raise
    finally:
        conn.close()

    write_report(args.report, report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
