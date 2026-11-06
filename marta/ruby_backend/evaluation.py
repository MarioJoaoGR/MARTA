"""Read-only post-generation observations, independent of generation decisions."""
from __future__ import annotations

from dataclasses import asdict
import copy
from pathlib import Path
import shutil
import tempfile
import time

from .backend import RubyBackend
from .checkpoints import atomic_json, dependency_files, file_hash
from .mutation import run_mutation
from .execution import relocate_environment, ENVIRONMENT_KEYS

POLICY = "ruby-post-evaluation-v1"


def coverage_record(value):
    if value is None:
        return None
    from .coverage_runner import MethodCoverage
    return {name: getattr(value, name, None) for name in MethodCoverage.__dataclass_fields__}


def cost_snapshot(recorder):
    score = recorder.score
    return {"scope": "current_recorder_process_only", "llm_calls": score.llm_calls,
            "usage_unknown_calls": score.llm_usage_unknown_calls,
            "interrupted_requests": score.llm_interrupted_requests,
            "prompt_tokens": score.prompt_tokens, "completion_tokens": score.completion_tokens,
            "llm_seconds": sum(p["segundos_chamadas"] for p in score.por_fase.values()),
            "by_phase": copy.deepcopy(score.por_fase), "subprocesses": copy.deepcopy(score.subprocessos),
            "token_usage_note": "Per-request usage when available; opaque/legacy callbacks remain explicitly unverified. No monetary cost inferred."}


def round_observation(targets, before, after, outcomes, start_cost, end_cost, seconds):
    observations = []
    for index, target in targets:
        a, b = before.get(index), after.get(index)
        ac, bc = getattr(a, "covered_lines", None), getattr(b, "covered_lines", None)
        ae, be = getattr(a, "executable_lines", None), getattr(b, "executable_lines", None)
        delta = bc - ac if all(type(n) is int for n in (ac, bc, ae, be)) and ae == be else None
        observations.append({"target_index": index, "definition_id": target.analysis_id,
                             "task_id": target.task_id, "before": coverage_record(a),
                             "after": coverage_record(b), "covered_line_delta": delta})
    return {"policy": POLICY, "targets": observations,
            "accepted_generations": sum(o.success for o in outcomes),
            "rejected_generations": sum(not o.success for o in outcomes),
            "new_cost": {key: end_cost[key] - start_cost[key] for key in
                         ("llm_calls", "prompt_tokens", "completion_tokens", "llm_seconds",
                          "usage_unknown_calls", "interrupted_requests") if key in start_cost and key in end_cost},
            "wall_seconds": seconds,
            "interpretation": "Observed round-level association, not causal credit to a repair/context component. Missing baseline is not zero."}


def summarize_mutation(rows, requested):
    if not requested:
        return {"requested": False, "valid_measurements": 0, "ms_all_targets_zero_imputed": None,
                "ms_valid_only": None, "pooled_diagnostic": None}
    valid = [r["mutation"] for r in rows if r["mutation"].get("valid") is True]
    killed = sum(r["counts"]["kills"] for r in valid)
    total = sum(r["counts"]["mutations"] for r in valid)
    return {"requested": True, "targets": len(rows), "valid_measurements": len(valid),
            "unavailable": len(rows) - len(valid),
            "ms_all_targets_zero_imputed": sum(r["mutation_score"] for r in valid) / len(rows) if rows else None,
            "ms_valid_only": sum(r["mutation_score"] for r in valid) / len(valid) if valid else None,
            "pooled_diagnostic": killed / total if total else None,
            "total_killed_valid": killed, "total_mutants_valid": total,
            "convention": "All-target macro explicitly imputes unavailable as zero; per-target unavailable stays null. Valid-only and pooled use only complete valid runs."}


def _copy_workspace(project, destination):
    root = Path(project.root_dir).resolve()
    output = Path(project.out_root()).resolve()
    excluded = {".git", ".marta_ruby_cache", ".marta_generation", "run_results", "marta_specs"}
    def ignore(directory, names):
        return [name for name in names if name in excluded or
                (output != root and (Path(directory) / name).resolve() == output)]
    shutil.copytree(root, destination, symlinks=True, ignore=ignore)


def _stage(project, specs, destination):
    _copy_workspace(project, destination)
    root = Path(project.root_dir).resolve()
    stage = destination / ".marta_post_evaluation"
    stage.mkdir(exist_ok=False)
    suite = stage / "generated_spec.rb"
    suite.write_text("\n\n".join(path.read_text() for path in specs) + "\n")
    def remap(value):
        candidate = Path(value)
        if not candidate.is_absolute():
            return value
        try:
            mapped = destination / candidate.resolve().relative_to(root)
            if mapped.exists():
                return str(mapped)
        except ValueError:
            pass
        if candidate.is_file():
            target = stage / ("preload_" + str(len(list(stage.glob('preload_*')))) + ".rb")
            shutil.copyfile(candidate, target)
            return str(target)
        else:
            raise ValueError("External load paths need an explicit relocatable environment")
    paths = []
    for path in project._load_path_list():
        p = Path(remap(path))
        paths.append(str(p if p.is_absolute() else destination / p))
    requires = [remap(value) for value in list(getattr(project.backend, "requires", None) or [])
                + list(getattr(project.backend, "coverage_requires", None) or [])]
    return suite, paths, requires


def evaluate_project(project, *, mutation=False, mutation_usage=None, timeout=300, jobs=1,
                     bundle=False, limit=None, generation_cost=None):
    """Evaluate stored generated suites; never invoke analysis or an LLM.

    A unique evidence directory is created for each request. The whole retained
    generated suite is the test population, not human tests or best attempts.
    """
    if mutation and mutation_usage not in ("opensource", "commercial"):
        raise ValueError("Mutation requires an explicit usage mode")
    if type(timeout) is not int or timeout < 1 or type(jobs) is not int or jobs < 1:
        raise ValueError("Evaluation timeout/jobs must be positive integers")
    if limit is not None and (type(limit) is not int or limit < 1):
        raise ValueError("Evaluation limit must be positive")
    targets = list(enumerate(project.targets))[:limit]
    parent = Path(project.out_root()) / "run_results/evaluations"
    parent.mkdir(parents=True, exist_ok=True)
    output = Path(tempfile.mkdtemp(prefix="evaluation_", dir=parent))
    specs = [Path(project.root_dir, p).resolve() for p in project._all_spec_paths()]
    tracked = sorted(set([Path(p).resolve() for p in project.files] + specs
                         + [Path(p).resolve() for p in dependency_files(project.root_dir)]
                         + [Path(p).resolve() for p in list(getattr(project.backend, "requires", None) or [])
                            + list(getattr(project.backend, "coverage_requires", None) or []) if Path(p).is_file()]))
    snapshot = {str(p): file_hash(p) for p in tracked}
    manifest = {"policy": POLICY, "status": "running", "inputs": snapshot,
                "suite_files": [str(p) for p in specs], "mutation_requested": mutation,
                "generation_cost": copy.deepcopy(generation_cost),
                "environment": {key: project._execution_environment().get(key) for key in ENVIRONMENT_KEYS},
                "implementation": {name: file_hash(Path(__file__).parent / name)
                                   for name in ("evaluation.py", "execution.py", "mutation.py", "rb/marta_mutation.rb")},
                "scope": "Normal Ruby backend; accumulated generated suite. Not an XRepoTest task evaluator."}
    atomic_json(output / "manifest.json", manifest)
    started = time.monotonic()
    try:
        cov, baseline_error = {}, None
        if specs:
            try:
                if type(project.backend) is not RubyBackend:
                    raise ValueError("Post-evaluation supports the normal RubyBackend only; use the benchmark adapter for XRepoTest")
                with tempfile.TemporaryDirectory(prefix="marta-baseline-") as tmp:
                    repo = Path(tmp) / "repo"
                    suite, load_paths, requires = _stage(project, specs, repo)
                    backend = copy.copy(project.backend)
                    backend.bind_environment(relocate_environment(project._execution_environment(), project.root_dir, repo))
                    backend.extra_load_paths = load_paths
                    backend.requires, backend.coverage_requires = requires, []
                    source_dir = repo / Path(project.abs_source).resolve().relative_to(Path(project.root_dir).resolve())
                    result = backend.run_coverage(str(source_dir), [str(suite)], cwd=str(repo))
                    atomic_json(output / "baseline.json", asdict(result))
                    if not result.suite_result or not result.suite_result.all_passed:
                        raise ValueError("Staged accumulated suite has no valid passing RSpec report")
                    for index, target in targets:
                        lines = result.files.get(target.source_rel)
                        if lines:
                            cov[index] = backend.synthesize_coverage(target.method, lines,
                                result.branches.get(target.source_rel), result.methods.get(target.source_rel))
            except Exception as error:
                baseline_error = str(error)
        rows = []
        for index, target in targets:
            row = {"target_index": index, "definition_id": target.analysis_id,
                   "task_id": target.task_id, "method": target.method.qualified_name,
                   "source": target.source_rel, "start_line": target.method.start_line,
                   "end_line": target.method.end_line,
                   "coverage": coverage_record(cov.get(index)),
                   "mutation": {"valid": False, "mutation_score": None,
                                "status": "not_requested" if not mutation else "unavailable"}}
            if mutation:
                result = row["mutation"]
                if not specs:
                    result["reason"] = "No generated suite"
                elif baseline_error:
                    result["reason"] = "Invalid accumulated suite: " + baseline_error
                elif type(project.backend) is not RubyBackend:
                    result["reason"] = "This mutation adapter supports the normal RubyBackend only"
                else:
                    try:
                        source = Path(target.file_path).resolve()
                        relative = source.relative_to(Path(project.root_dir).resolve())
                        subject = target.method.qualified_name
                        if not re_subject(subject):
                            raise ValueError("Target has no supported named Mutant owner")
                        with tempfile.TemporaryDirectory(prefix="marta-post-eval-") as tmp:
                            repo = Path(tmp) / "repo"
                            suite, load_paths, requires = _stage(project, specs, repo)
                            if file_hash(repo / relative) != snapshot[str(source)]:
                                raise ValueError("Copied focal source differs from input snapshot")
                            result = run_mutation({"subject": subject, "file": relative.as_posix(),
                                "start_line": target.method.start_line, "end_line": target.method.end_line},
                                suite, repo, output / "mutation" / str(index), load_paths=load_paths,
                                requires=requires, timeout=timeout, jobs=jobs, usage=mutation_usage, bundle=bundle,
                                env=relocate_environment(project._execution_environment(), project.root_dir, repo))
                        row["mutation"] = result
                    except Exception as error:
                        row["mutation"]["reason"] = str(error)
            rows.append(row)
            atomic_json(output / "targets" / (str(index) + ".json"), row)
        if snapshot != {str(p): file_hash(p) for p in tracked}:
            raise RuntimeError("Evaluation inputs changed; no complete report certified")
        report = {"policy": POLICY, "status": "complete", "targets": rows,
                  "suite": {"files": len(specs), "valid": bool(specs) and baseline_error is None,
                            "status": "no_tests" if not specs else "invalid" if baseline_error else "passed",
                            "error": baseline_error},
                  "mutation": summarize_mutation(rows, mutation),
                  "generation_cost": copy.deepcopy(generation_cost),
                  "evaluation_seconds": time.monotonic() - started,
                  "utility_note": "Coverage/invocation and mutation are observations. No learned reward, component-level causal attribution or monetary estimate."}
        atomic_json(output / "report.json", report)
        manifest.update(status="complete", report_sha256=file_hash(output / "report.json"))
        atomic_json(output / "manifest.json", manifest)
        return output / "report.json"
    except BaseException as error:
        manifest.update(status="interrupted" if not isinstance(error, Exception) else "failed", error=str(error))
        atomic_json(output / "manifest.json", manifest)
        raise


def re_subject(subject):
    import re
    return bool(re.fullmatch(r"[A-Z]\w*(?:::[A-Z]\w*)*[.#].+", subject))
