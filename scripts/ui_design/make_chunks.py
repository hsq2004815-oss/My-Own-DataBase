"""Create retrieval chunks from normalized UI reference records."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_REFERENCE_DIR = ROOT / "domains" / "ui_design" / "processed" / "references"
DEFAULT_CHUNK_DIR = ROOT / "domains" / "ui_design" / "processed" / "reference_chunks"


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def as_sentence_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items if item)


def rough_tokens(text: str) -> int:
    return max(1, len(text.replace("\n", " ").split()))


def make_chunk(record: dict[str, Any], section: str, title: str, body: str) -> dict[str, Any]:
    record_id = record["record_id"]
    content = (
        f"# {record['source']['name']} - {title}\n\n"
        f"Page type: {record['page_type']}\n"
        f"Use cases: {', '.join(record.get('use_cases', []))}\n"
        f"Evidence: {record['quality']['evidence_level']} / {record['quality']['signal_strength']}\n"
        f"Source: {record['source']['url']}\n\n"
        f"{body.strip()}\n\n"
        f"AI summary: {record['retrieval']['ai_summary']}"
    )
    return {
        "chunk_id": f"{record_id}-{section}",
        "record_id": record_id,
        "source_name": record["source"]["name"],
        "source_url": record["source"]["url"],
        "page_type": record["page_type"],
        "section": section,
        "content": content,
        "tokens": rough_tokens(content),
        "metadata": {
            "signal_strength": record["quality"]["signal_strength"],
            "evidence_level": record["quality"]["evidence_level"],
            "prompt_tags": record["retrieval"].get("prompt_tags", []),
            "negative_prompt_tags": record["retrieval"].get("negative_prompt_tags", []),
        },
    }


def chunks_for_record(record: dict[str, Any]) -> list[dict[str, Any]]:
    chunks: list[dict[str, Any]] = []

    overview_parts = [
        f"Visual traits:\n{as_sentence_list(record.get('visual_traits', []))}",
        f"Use when:\n{as_sentence_list(record.get('use_cases', []))}",
        f"Avoid when:\n{as_sentence_list(record.get('avoid_when', []))}",
    ]
    chunks.append(make_chunk(record, "overview", "Overview", "\n\n".join(overview_parts)))

    section_map = [
        ("layout", "Layout Rules", "layout_rules"),
        ("components", "Component Patterns", "component_patterns"),
        ("interaction", "Interaction States", "interaction_states"),
        ("accessibility", "Accessibility Notes", "accessibility_notes"),
        ("implementation", "Implementation Hints", "implementation_hints"),
    ]
    for section, title, key in section_map:
        values = record.get(key, [])
        if values:
            chunks.append(make_chunk(record, section, title, as_sentence_list(values)))

    return chunks


def main() -> int:
    parser = argparse.ArgumentParser(description="Create chunks from UI reference records.")
    parser.add_argument("--references", type=Path, default=DEFAULT_REFERENCE_DIR, help="Reference JSON directory.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_CHUNK_DIR, help="Chunk output directory.")
    args = parser.parse_args()

    reference_files = sorted(args.references.glob("*.json"))
    if not reference_files:
        raise SystemExit(f"No reference JSON files found at {args.references}")

    all_chunks: list[dict[str, Any]] = []
    for path in reference_files:
        record = load_json(path)
        chunks = chunks_for_record(record)
        write_json(args.output_dir / f"{record['record_id']}.json", chunks)
        all_chunks.extend(chunks)

    write_json(args.output_dir / "all_reference_chunks.json", all_chunks)
    print(f"created {len(all_chunks)} chunk(s) from {len(reference_files)} reference record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
