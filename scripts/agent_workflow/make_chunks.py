"""Create retrieval chunks from agent workflow reference records."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_REFERENCE_DIR = ROOT / "domains" / "agent_workflow" / "processed" / "references"
DEFAULT_CHUNK_DIR = ROOT / "domains" / "agent_workflow" / "processed" / "chunks"


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

def bullet(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items if item)

def rough_tokens(text: str) -> int:
    return max(1, len(text.replace("\n", " ").split()))

def make_chunk(record: dict[str, Any], section: str, title: str, body: str) -> dict[str, Any]:
    content = (
        f"# {record['record_id']} - {title}\n\n"
        f"Workflow type: {record['workflow_type']}\n"
        f"Agent targets: {', '.join(record.get('agent_targets', []))}\n"
        f"Goal: {record.get('goal', '')}\n"
        f"Evidence: {record['quality']['evidence_level']} / {record['quality']['signal_strength']}\n"
        f"Source: {record['source']['url']}\n\n"
        f"{body.strip()}\n\n"
        f"AI summary: {record['retrieval']['ai_summary']}"
    )
    return {
        "chunk_id": f"{record['record_id']}-{section}",
        "record_id": record["record_id"],
        "workflow_type": record["workflow_type"],
        "source_name": record["source"]["name"],
        "source_url": record["source"]["url"],
        "section": section,
        "content": content,
        "tokens": rough_tokens(content),
        "metadata": {
            "agent_targets": record.get("agent_targets", []),
            "signal_strength": record["quality"]["signal_strength"],
            "evidence_level": record["quality"]["evidence_level"],
            "prompt_tags": record["retrieval"].get("prompt_tags", []),
            "negative_prompt_tags": record["retrieval"].get("negative_prompt_tags", []),
        },
    }

def chunks_for_record(record: dict[str, Any]) -> list[dict[str, Any]]:
    sections = [
        ("overview", "Overview", [f"When to use:\n{bullet(record.get('when_to_use', []))}", f"Inputs required:\n{bullet(record.get('inputs_required', []))}"]),
        ("steps", "Execution Steps", [bullet(record.get("steps", []))]),
        ("api", "API Calls", [bullet(record.get("api_calls", []))]),
        ("prompt_contract", "Prompt Contract", [bullet(record.get("prompt_contract", []))]),
        ("verification", "Verification", [bullet(record.get("verification", []))]),
        ("failure_modes", "Failure Modes", [bullet(record.get("failure_modes", []))]),
        ("handoff", "Handoff Report", [bullet(record.get("handoff_report", []))]),
    ]
    chunks = []
    for section, title, parts in sections:
        body = "\n\n".join(part for part in parts if part.strip())
        if body.strip():
            chunks.append(make_chunk(record, section, title, body))
    return chunks

def main() -> int:
    parser = argparse.ArgumentParser(description="Create agent workflow chunks.")
    parser.add_argument("--references", type=Path, default=DEFAULT_REFERENCE_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_CHUNK_DIR)
    args = parser.parse_args()
    files = sorted(args.references.glob("*.json"))
    if not files:
        raise SystemExit(f"No reference JSON files found at {args.references}")
    all_chunks = []
    for path in files:
        record = load_json(path)
        chunks = chunks_for_record(record)
        write_json(args.output_dir / f"{record['record_id']}.json", chunks)
        all_chunks.extend(chunks)
    write_json(args.output_dir / "all_agent_workflow_chunks.json", all_chunks)
    print(f"created {len(all_chunks)} chunk(s) from {len(files)} agent workflow record(s)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
