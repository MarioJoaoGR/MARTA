"""Preliminary evaluation of whole, generation-complete XRepoTest projects.

Infrastructure utility kept outside the active generation fingerprint. It reads
final suites only, never calls an LLM, and never writes to generation/. Results
are a named, immutable subset snapshot, not a 675-task benchmark result.
"""
import argparse
from collections import Counter
import copy
import hashlib
import json
import os
from pathlib import Path
import shutil

from benchmark.xrepotest.protocol import (DATA_SHA256, UPSTREAM_COMMIT, atomic_json,
                                         digest, load_tasks, locked_run)
from benchmark.xrepotest.run import workspace
from benchmark.xrepotest.runtime import (environment_manifest, project_environment,
                                        validate_evaluator)


def snapshot_projects(tasks, generation, projects):
    known = {t["file_path"].split("/", 1)[0] for t in tasks}
    if not projects or set(projects) - known:
        raise ValueError("Specify nonempty, known projects")
    selected = [t for t in tasks if t["file_path"].split("/", 1)[0] in projects]
    responses = []
    for task in selected:
        tid = task["task_id"]
        folder = generation / "tasks" / str(tid)
        state = json.loads((folder / "state.json").read_text())
        if state.get("task_id") != tid or state.get("status") not in {"complete", "no_tests"}:
            raise ValueError("Task {} unfinished; whole-project preview refused".format(tid))
        code = (folder / "final_spec.rb").read_text() if state["status"] == "complete" else ""
        if state["status"] == "complete" and not code.strip():
            raise ValueError("Completed task {} has no final suite".format(tid))
        responses.append({"task_id": tid, "response": [code] if code.strip() else []})
    return selected, responses


def evaluation_order(tasks):
    counts = Counter(t["file_path"].split("/", 1)[0] for t in tasks)
    return sorted(tasks, key=lambda t: (counts[t["file_path"].split("/", 1)[0]],
                                        t["file_path"].split("/", 1)[0], t["task_id"]))


def project_checkpoint(output, tasks, name, calculate_summary):
    selected = [t for t in tasks if t["file_path"].split("/", 1)[0] == name]
    files = [output / "tasks" / (str(t["task_id"]) + ".json") for t in selected]
    if not all(p.exists() for p in files):
        return
    results = [json.loads(p.read_text()) for p in files]
    report = {"preliminary": True, "project": name,
              "task_ids": [t["task_id"] for t in selected],
              "no_tests": sum(not r["test"] for r in results),
              "summary": calculate_summary(results)}
    atomic_json(output / "project_summaries" / (name + ".json"), report)
    print("PROJECT_COMPLETE: " + json.dumps(report), flush=True)


def write_summary(output, tasks, responses, calculate_summary, *, mutation):
    results = [json.loads((output / "tasks" / (str(t["task_id"]) + ".json")).read_text())
               for t in tasks]
    summary = calculate_summary(results)
    if summary["total_samples"] != len(tasks):
        raise RuntimeError("Subset denominator changed")
    per_project = {}
    for name in sorted({t["file_path"].split("/", 1)[0] for t in tasks}):
        rows = [r for r in results if r["file_path"].split("/", 1)[0] == name]
        per_project[name] = calculate_summary(rows)
    report = {"preliminary": True, "official_task_ids": [t["task_id"] for t in tasks],
              "subset_policy": "All tasks from the explicitly selected completed projects, including no_tests",
              "no_tests": sum(not r["response"] for r in responses),
              "mutation_enabled": mutation, "summary": summary, "by_project": per_project,
              "comparison_note": "This subset is not directly comparable to full-Ruby paper aggregates; "
                                 "comparators require the same task IDs and evaluator."}
    atomic_json(output / "summary.json", summary)
    atomic_json(output / "report.json", report)
    (output / "detailed_results.jsonl").write_text(
        "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in results))
    table = ["# Resultados preliminares MARTA / XRepoTest", "",
             "Subconjunto de projetos completos; tarefas sem testes permanecem no denominador.", "",
             "| Projeto | Tarefas | Compilação | Execução | Invocação | Cobertura focal |",
             "|---|---:|---:|---:|---:|---:|"]
    for name, row in list(per_project.items()) + [("TOTAL do subconjunto", summary)]:
        table.append("| {} | {} | {:.2f}% | {:.2f}% | {:.2f}% | {:.2f}% |".format(
            name, row["total_samples"], row["compiled_rate"], row["test_pass_rate"],
            row["invocation_rate"], row["line_coverage"]))
    table += ["", "Sem testes gerados: {} tarefas.".format(report["no_tests"]),
              "Mutação: {}.".format("ativada" if mutation else "não medida nesta prévia"), "",
              "A invocação é a heurística do avaliador; cobertura pode existir mesmo quando a suite falha.",
              "Usa o ambiente e as duas correções documentadas do avaliador.",
              "Não é uma comparação controlada com os agregados do paper para as 675 tarefas Ruby."]
    (output / "presentation.md").write_text("\n".join(table) + "\n")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", type=Path, required=True)
    parser.add_argument("--generation", type=Path, required=True)
    parser.add_argument("--projects", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--work", type=Path, required=True)
    parser.add_argument("--repos", type=Path, default=Path("/app/repo_data"))
    parser.add_argument("--enable-mutation", action="store_true")
    args = parser.parse_args()
    for name in ("dataset", "generation", "output", "work", "repos"):
        setattr(args, name, getattr(args, name).resolve())
    # Prevent any preliminary evaluator write in generation or a source tree.
    paths = [args.generation, args.output, args.work, args.repos]
    for i, first in enumerate(paths):
        for second in paths[i + 1:]:
            if first == second or first in second.parents or second in first.parents:
                parser.error("Generation, output, work and repositories must be separate trees")
    generation_manifest = json.loads((args.generation / "experiment.json").read_text())
    tasks, responses = snapshot_projects(load_tasks(args.dataset), args.generation,
                                        set(args.projects.split(",")))
    from ruby.evaluator import RubyEvaluator
    from base.metrics import calculate_summary
    import base, ruby
    hashes = {"{}/{}".format(package.__name__, f.name): hashlib.sha256(f.read_bytes()).hexdigest()
              for package in (base, ruby) for f in Path(package.__file__).parent.glob("*.py")}
    validate_evaluator(hashes)
    config = {"preliminary": True, "dataset": DATA_SHA256, "evaluator_commit": UPSTREAM_COMMIT,
              "environment": environment_manifest(), "evaluator_files": hashes,
              "generation_manifest": generation_manifest,
              "task_ids": [t["task_id"] for t in tasks], "responses_digest": digest(responses),
              "adapter": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "mutation": args.enable_mutation}
    with locked_run(args.output, config):
        snapshot = args.output / "responses.jsonl"
        if snapshot.exists():
            actual = [json.loads(line) for line in snapshot.read_text().splitlines()]
            if actual != responses:
                raise ValueError("Preview response snapshot changed")
        else:
            temporary = snapshot.with_suffix(".tmp")
            temporary.write_text("".join(json.dumps(r) + "\n" for r in responses))
            os.replace(temporary, snapshot)
        by_id = {r["task_id"]: r["response"] for r in responses}
        remaining = Counter(t["file_path"].split("/", 1)[0] for t in tasks)
        for number, task in enumerate(evaluation_order(tasks), 1):
            tid = task["task_id"]
            saved = args.output / "tasks" / (str(tid) + ".json")
            name = task["file_path"].split("/", 1)[0]
            if saved.exists():
                remaining[name] -= 1
                if not remaining[name]:
                    project_checkpoint(args.output, tasks, name, calculate_summary)
                continue
            task_root = args.work / str(tid)
            repo = task_root / "repo_data" / name
            workspace(args.repos / name, repo)
            sample = copy.deepcopy(task)
            sample["test"] = by_id[tid]
            print("Preview {}/{}: task {} ({})".format(number, len(tasks), tid, name), flush=True)
            old = Path.cwd()
            try:
                os.chdir(task_root)
                with project_environment(repo, name):
                    detailed, _ = RubyEvaluator().evaluate_dataset(
                        [sample], enable_mutation_testing=args.enable_mutation)
                if len(detailed) != 1 or detailed[0]["task_id"] != tid:
                    raise RuntimeError("Evaluator returned an unexpected task")
                if isinstance(detailed[0].get("logs"), list):
                    detailed[0]["logs"] = [x.decode("utf-8", errors="replace") if isinstance(x, bytes)
                                           else x for x in detailed[0]["logs"]]
                atomic_json(saved, detailed[0])
            finally:
                os.chdir(old)
                shutil.rmtree(repo)
            remaining[name] -= 1
            if not remaining[name]:
                project_checkpoint(args.output, tasks, name, calculate_summary)
        report = write_summary(args.output, tasks, responses, calculate_summary,
                               mutation=args.enable_mutation)
        print(json.dumps(report, indent=2), flush=True)


if __name__ == "__main__":
    main()
