"""Normalize and validate UI reference records.

This script intentionally uses only the Python standard library so the
knowledge base can be maintained without installing project dependencies.
"""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
TEMPLATE_PATH = ROOT / "common" / "templates" / "ui_reference.template.json"
TAXONOMY_PATH = ROOT / "common" / "taxonomy" / "ui_page_types.json"
DEFAULT_INPUT_DIR = ROOT / "domains" / "ui_design" / "processed" / "references"
DEFAULT_OUTPUT_DIR = DEFAULT_INPUT_DIR


class ValidationError(Exception):
    pass


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def deep_merge(defaults: Any, value: Any) -> Any:
    if isinstance(defaults, dict) and isinstance(value, dict):
        merged = copy.deepcopy(defaults)
        for key, item in value.items():
            merged[key] = deep_merge(merged.get(key), item)
        return merged
    if value in (None, "") and defaults not in (None, ""):
        return copy.deepcopy(defaults)
    return copy.deepcopy(value)


def iter_json_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    return sorted(path.glob("*.json"))


def taxonomy_page_types() -> set[str]:
    taxonomy = load_json(TAXONOMY_PATH)
    return {item["id"] for item in taxonomy.get("page_types", [])}


def validate_record(record: dict[str, Any], page_types: set[str], path: Path) -> None:
    required = ["record_id", "source", "domain", "page_type", "quality", "retrieval"]
    missing = [key for key in required if not record.get(key)]
    if missing:
        raise ValidationError(f"{path}: missing required fields: {', '.join(missing)}")

    source = record.get("source", {})
    source_required = ["name", "url", "source_type", "license_notes"]
    source_missing = [key for key in source_required if not source.get(key)]
    if source_missing:
        raise ValidationError(f"{path}: missing source fields: {', '.join(source_missing)}")

    if record["page_type"] not in page_types:
        raise ValidationError(
            f"{path}: unknown page_type '{record['page_type']}'. "
            f"Add it to {TAXONOMY_PATH} or use an existing page type."
        )

    quality = record.get("quality", {})
    if quality.get("signal_strength") not in {"high", "medium", "low"}:
        raise ValidationError(f"{path}: quality.signal_strength must be high, medium, or low")
    if quality.get("evidence_level") not in {
        "direct_spec",
        "screenshot_observed",
        "summary_only",
        "link_only",
    }:
        raise ValidationError(f"{path}: invalid quality.evidence_level")

    retrieval = record.get("retrieval", {})
    if not retrieval.get("ai_summary"):
        raise ValidationError(f"{path}: retrieval.ai_summary is required for useful search")


def normalize_record(path: Path, template: dict[str, Any], page_types: set[str]) -> dict[str, Any]:
    raw = load_json(path)
    if not isinstance(raw, dict):
        raise ValidationError(f"{path}: expected a JSON object")
    record = deep_merge(template, raw)
    validate_record(record, page_types, path)
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize UI reference records.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT_DIR, help="Input JSON file or directory.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR, help="Output directory.")
    parser.add_argument("--check", action="store_true", help="Validate only; do not write normalized files.")
    args = parser.parse_args()

    template = load_json(TEMPLATE_PATH)
    page_types = taxonomy_page_types()
    files = iter_json_files(args.input)
    if not files:
        raise SystemExit(f"No JSON files found at {args.input}")

    normalized = []
    for path in files:
        record = normalize_record(path, template, page_types)
        normalized.append(record)
        if not args.check:
            output_path = args.output_dir / f"{record['record_id']}.json"
            write_json(output_path, record)

    action = "validated" if args.check else "normalized"
    print(f"{action} {len(normalized)} UI reference record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
