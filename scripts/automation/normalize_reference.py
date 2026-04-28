"""Normalize and validate automation reference records."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
TEMPLATE_PATH = ROOT / "common" / "templates" / "automation_reference.template.json"
TAXONOMY_PATH = ROOT / "common" / "taxonomy" / "automation_types.json"
DEFAULT_INPUT_DIR = ROOT / "domains" / "automation" / "processed" / "references"
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

def automation_types() -> set[str]:
    data = load_json(TAXONOMY_PATH)
    return {item["id"] for item in data.get("automation_types", [])}

def iter_json_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    return sorted(path.glob("*.json"))

def validate_record(record: dict[str, Any], allowed_types: set[str], path: Path) -> None:
    required = ["record_id", "source", "domain", "automation_type", "tooling", "quality", "retrieval"]
    missing = [key for key in required if not record.get(key)]
    if missing:
        raise ValidationError(f"{path}: missing required fields: {', '.join(missing)}")
    if record["automation_type"] not in allowed_types:
        raise ValidationError(f"{path}: unknown automation_type '{record['automation_type']}'")
    if not record.get("steps"):
        raise ValidationError(f"{path}: steps are required")
    if not record.get("retrieval", {}).get("ai_summary"):
        raise ValidationError(f"{path}: retrieval.ai_summary is required")

def normalize_record(path: Path, template: dict[str, Any], allowed_types: set[str]) -> dict[str, Any]:
    raw = load_json(path)
    if not isinstance(raw, dict):
        raise ValidationError(f"{path}: expected a JSON object")
    record = deep_merge(template, raw)
    validate_record(record, allowed_types, path)
    return record

def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize automation references.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    template = load_json(TEMPLATE_PATH)
    allowed_types = automation_types()
    files = iter_json_files(args.input)
    if not files:
        raise SystemExit(f"No JSON files found at {args.input}")
    records = []
    for path in files:
        record = normalize_record(path, template, allowed_types)
        records.append(record)
        if not args.check:
            write_json(args.output_dir / f"{record['record_id']}.json", record)
    print(("validated" if args.check else "normalized") + f" {len(records)} automation record(s)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
