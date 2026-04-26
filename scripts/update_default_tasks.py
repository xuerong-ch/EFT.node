"""
Fetch the latest task graph from tarkov.dev and overwrite default_tasks.json.

Usage:
    python scripts/update_default_tasks.py [--help]

Requires:
    pip install -r requirements.txt
"""

import argparse
import json
import sys
from pathlib import Path

API_URL = "https://api.tarkov.dev/graphql"

QUERY = """
{
  tasks {
    id
    name
    trader { id name }
    taskRequirements { task { id } status }
    objectives { id description type }
  }
}
"""


def fetch_tasks():
    import requests

    print("Fetching tasks from tarkov.dev ...", file=sys.stderr)
    resp = requests.post(API_URL, json={"query": QUERY}, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    if "errors" in data:
        for err in data["errors"]:
            print(f"GraphQL error: {err['message']}", file=sys.stderr)
        sys.exit(1)
    return data["data"]["tasks"]


def build_graph(tasks):
    nodes = []
    edges = []
    seen = set()

    for task in tasks:
        if not task:
            continue
        tid = task["id"]
        if tid in seen:
            continue
        seen.add(tid)

        trader_name = task.get("trader", {}).get("name") if task.get("trader") else None
        nodes.append({
            "id": tid,
            "name": task["name"],
            "trader": trader_name,
        })

        for req in task.get("taskRequirements", []) or []:
            req_task = req.get("task") if req else None
            if req_task and req_task.get("id"):
                edges.append({
                    "id": f"{tid}-{req_task['id']}",
                    "source": req_task["id"],
                    "target": tid,
                    "status": req.get("status") or ["required"],
                })

    return {"nodes": nodes, "edges": edges}


def main():
    parser = argparse.ArgumentParser(
        description="Update default_tasks.json from tarkov.dev"
    )
    parser.parse_args()

    tasks = fetch_tasks()
    graph = build_graph(tasks)

    out = Path(__file__).resolve().parent.parent / "default_tasks.json"
    out.write_text(json.dumps(graph, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(graph['nodes'])} tasks, {len(graph['edges'])} edges -> {out}", file=sys.stderr)


if __name__ == "__main__":
    main()
