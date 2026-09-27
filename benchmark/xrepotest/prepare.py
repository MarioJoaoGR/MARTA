"""Validate the pinned image sources, task mapping and installed bundles offline."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import subprocess
import sys

from .protocol import IMAGE, DATA_SHA256, UPSTREAM_COMMIT, atomic_json, load_tasks, source_inventory
from .runtime import environment_manifest, project_env


def inspect_repositories(tasks, repos: Path, ruby: str, bundle_check: bool = True) -> dict:
    helper = Path(__file__).resolve().parents[2] / "marta/ruby_backend/rb/marta_parse.rb"
    groups = defaultdict(list)
    for t in tasks:
        groups[t["file_path"].split("/", 1)[0]].append(t)
    report = {"image": IMAGE, "dataset_sha256": DATA_SHA256,
              "evaluator_commit": UPSTREAM_COMMIT, "projects": {}, "ready": True,
              "mutation_ready": bool(bundle_check)}
    report["environment"] = environment_manifest()
    for name, rows in sorted(groups.items()):
        root = repos / name
        item = {"tasks": len(rows), "errors": [], "mutation_errors": []}
        report["projects"][name] = item
        env = project_env(root, name)
        try:
            item.update(source_inventory(root, rows))
            parsed = {}
            for rel in item["code_files"]:
                proc = subprocess.run([ruby, str(helper), str(root / rel)],
                                      capture_output=True, text=True, timeout=60, env=env)
                if proc.returncode:
                    raise ValueError(f"Prism failed: {rel}: {proc.stderr[-500:]}")
                data = json.loads(proc.stdout)
                if data.get("errors"):
                    raise ValueError(f"Prism errors: {rel}: {data['errors']}")
                parsed[rel] = data["methods"]
            item["analysis_methods"] = sum(map(len, parsed.values()))
            item["constructors"] = sum(m["name"] == "initialize" for ms in parsed.values() for m in ms)
            identities = Counter((m.get("owner"), m["name"], m.get("singleton"))
                                 for ms in parsed.values() for m in ms)
            item["ambiguous_method_names"] = sum(n > 1 for n in identities.values())
            for t in rows:
                rel = t["file_path"].split("/", 1)[1]
                c = t["function_component"]
                matches = [m for m in parsed[rel] if m["name"] == t["function_name"]
                           and m["start_line"] == c["start_line"]
                           and m["end_line"] == c["end_line"]]
                if len(matches) != 1:
                    item["errors"].append(f"Task {t['task_id']}: {len(matches)} exact Prism matches")
            if bundle_check:
                for args in (["bundle", "check"], ["bundle", "exec", "rspec", "--version"]):
                    proc = subprocess.run(args, cwd=root, capture_output=True, text=True, timeout=90, env=env)
                    if proc.returncode:
                        item["errors"].append(f"{' '.join(args)}: {(proc.stdout + proc.stderr)[-2000:]}")
                try:
                    proc = subprocess.run(["bundle", "exec", "mutant", "--version"], cwd=root,
                                          capture_output=True, text=True, timeout=30, env=env)
                    if proc.returncode:
                        item["mutation_errors"].append((proc.stdout + proc.stderr)[-2000:])
                except (OSError, subprocess.TimeoutExpired) as exc:
                    item["mutation_errors"].append(str(exc))
        except (OSError, ValueError, subprocess.TimeoutExpired) as exc:
            item["errors"].append(str(exc))
        if item["errors"]:
            report["ready"] = False
        if item["errors"] or item["mutation_errors"]:
            report["mutation_ready"] = False
        print(f"{name}: {len(rows)} tasks; {item.get('analysis_methods', '?')} analysis methods; "
              f"{len(item['errors'])} errors", flush=True)
    return report


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--dataset", type=Path, required=True)
    p.add_argument("--repos", type=Path, default=Path("/app/repo_data"))
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--ruby", default="ruby")
    p.add_argument("--sources-only", action="store_true", help="Static audit only; not runtime readiness")
    args = p.parse_args()
    report = inspect_repositories(load_tasks(args.dataset), args.repos, args.ruby,
                                  bundle_check=not args.sources_only)
    report["runtime_checked"] = not args.sources_only
    atomic_json(args.output, report)
    sys.exit(0 if report["ready"] else 1)


if __name__ == "__main__":
    main()
