"""Register large local asset libraries as collection-level metadata.

Use this for icon libraries, UI kits, templates, and other repositories where
per-file metadata would create too much noise.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
METADATA_DIR = ROOT / "domains" / "ui_assets" / "processed" / "metadata"
REGISTRY_LOG = ROOT / "domains" / "ui_assets" / "registry" / "collection_log.jsonl"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def slugify(value: str) -> str:
    result = "".join(ch.lower() if ch.isalnum() else "-" for ch in value)
    while "--" in result:
        result = result.replace("--", "-")
    return result.strip("-") or "collection"


def count_files(path: Path) -> tuple[int, int]:
    count = 0
    size = 0
    for item in path.rglob("*"):
        if not item.is_file():
            continue
        if ".git" in item.parts or "node_modules" in item.parts:
            continue
        count += 1
        size += item.stat().st_size
    return count, size


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def append_log(event: dict[str, Any]) -> None:
    REGISTRY_LOG.parent.mkdir(parents=True, exist_ok=True)
    with REGISTRY_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False, separators=(",", ":")) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Register a local asset collection.")
    parser.add_argument("path", type=Path)
    parser.add_argument("--name", required=True)
    parser.add_argument("--collection-type", default="asset_collection")
    parser.add_argument(
        "--usage-policy",
        choices=["direct_use", "inspiration_only", "internal_reference", "review_required", "unknown"],
        default="review_required",
    )
    parser.add_argument("--license", default="review required")
    parser.add_argument("--license-notes", default="Review license before using this collection in a project.")
    parser.add_argument("--tags", default="", help="Comma-separated style or library tags.")
    parser.add_argument("--source-url", default="")
    args = parser.parse_args()

    collection_path = args.path.resolve()
    if not collection_path.exists() or not collection_path.is_dir():
        raise SystemExit(f"Collection folder not found: {collection_path}")

    file_count, size_bytes = count_files(collection_path)
    digest = hashlib.sha1(str(collection_path).encode("utf-8")).hexdigest()[:8]
    asset_id = f"{slugify(args.name)}-{digest}"
    tags = [tag.strip() for tag in args.tags.split(",") if tag.strip()]
    metadata = {
        "asset_id": asset_id,
        "domain": "ui_assets",
        "asset_type": args.collection_type,
        "usage_policy": args.usage_policy,
        "files": {
            "file_path": str(collection_path),
            "preview_path": "",
            "original_path": str(collection_path),
            "sha1": digest,
            "size_bytes": size_bytes,
            "extension": "",
        },
        "source": {
            "name": args.name,
            "url": args.source_url,
            "captured_at": utc_now(),
            "notes": f"Collection-level registration. Approximate file_count={file_count}.",
        },
        "license": {
            "label": args.license,
            "notes": args.license_notes,
        },
        "style_tags": tags,
        "use_cases": [],
        "avoid_when": [],
        "implementation_notes": [
            "Registered as a collection to avoid per-file metadata noise.",
            "Inspect the collection documentation and license before direct use.",
        ],
        "quality": {
            "curation_status": "new",
            "notes": "Collection-level metadata; individual files are not indexed yet.",
        },
        "retrieval": {
            "ai_summary": f"{args.name} collection registered for UI asset lookup. Review usage policy and license before use.",
            "prompt_tags": tags + [args.collection_type.replace("_", "-")],
            "negative_prompt_tags": [],
        },
    }
    metadata_path = METADATA_DIR / f"{asset_id}.json"
    write_json(metadata_path, metadata)
    append_log(
        {
            "registered_at": utc_now(),
            "asset_id": asset_id,
            "path": str(collection_path),
            "metadata_path": str(metadata_path),
            "file_count": file_count,
            "size_bytes": size_bytes,
        }
    )
    print(f"registered {asset_id} -> {metadata_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
