"""Generate MARTA suites for official XRepoTest tasks in a pinned Ruby image.

Full-project production summaries are shared; each generation task gets its
own working copy, rounds, coverage feedback and output directory.
"""
from __future__ import annotations

import argparse
import asyncio
from collections import defaultdict
import json
import os
from pathlib import Path
import shutil
import time

from .protocol import (DATA_SHA256, IMAGE, UPSTREAM_COMMIT, atomic_json, code_fingerprint, digest,
                       export_responses, locked_run, load_tasks, selectors, source_inventory)

SUMMARY_TRUNCATION_ATTEMPTS = 3


def workspace(source: Path, destination: Path) -> None:
    """Disposable source copy; installed dependencies are reused read-only.

    Image repositories must be mounted read-only when used as the source. We
    never copy or consult the canceled experiment's prepared gems/results.
    """
    source, destination = source.resolve(), destination.resolve()
    if source == destination or source in destination.parents or destination in source.parents:
        raise ValueError("Task workspace and immutable source must be separate trees")
    marker = destination.parent / ".marta-xrepo-workspace"
    if destination.exists() and not marker.exists():
        raise ValueError("Refusing to replace an unmarked existing directory")
    if destination.exists():
        shutil.rmtree(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    marker.write_text(str(source))
    shutil.copytree(source, destination, symlinks=True,
                    ignore=shutil.ignore_patterns("vendor", "coverage", "marta_specs", ".marta_ruby_cache"))
    vendor = source / "vendor"
    if vendor.is_dir():
        (destination / "vendor").symlink_to(vendor, target_is_directory=True)


class SummaryCheckpoints:
    """Cache exact phase prompts, so walltime restarts do not repay phase one."""
    # Each physical request is recorded here, including failures and retries.
    records_llm_attempts = True

    def __init__(self, root, client, recorder, shared_root=None):
        self.root, self.client, self.recorder = root, client, recorder
        self.shared_root = shared_root

    async def __call__(self, system, user):
        key = digest([self.recorder.fase_atual, system, user])
        path = self.root / (key + ".json")
        if (not path.exists() and self.shared_root is not None
                and self.recorder.fase_atual == "sumarios_passagem1"):
            shared = self.shared_root / (key + ".json")
            if shared.exists():
                self.client.last_call = {"cache_hit": True}
                self.recorder.evento(tipo="llm_cache_hit", fase=self.recorder.fase_atual)
                return json.loads(shared.read_text())["response"]
        if path.exists():
            self.client.last_call = {"cache_hit": True}
            self.recorder.evento(tipo="llm_cache_hit", fase=self.recorder.fase_atual)
            return json.loads(path.read_text())["response"]
        for attempt in range(1, SUMMARY_TRUNCATION_ATTEMPTS + 1):
            start = time.monotonic()
            try:
                out = await self.client.aask(system, user)
            except Exception as exc:
                detail = {"erro": repr(exc)[:200]}
                self._record_attempt(detail, None, time.monotonic() - start, attempt)
                self.recorder.evento(tipo="llm_infrastructure_failure", fase=self.recorder.fase_atual,
                                     detail=detail, llm_event_recorded=True)
                raise
            detail = dict(self.client.last_call or {})
            self._record_attempt(detail, out, time.monotonic() - start, attempt)
            # Thinking may exhaust all output tokens before producing content.
            # Classify the finish reason before checking for an empty answer.
            if detail.get("finish_reason") == "length":
                retry = attempt < SUMMARY_TRUNCATION_ATTEMPTS
                self.recorder.evento(tipo="summary_truncated", fase=self.recorder.fase_atual,
                                     detail=detail, summary_attempt=attempt, retry=retry,
                                     llm_event_recorded=True)
                print(f"  summary truncated ({self.recorder.fase_atual}, "
                      f"attempt {attempt}/{SUMMARY_TRUNCATION_ATTEMPTS}); "
                      + ("retrying the same request" if retry else "stopping; checkpoints preserved"),
                      flush=True)
                if retry:
                    continue
                raise RuntimeError("Summary hit the output/context limit in all 3 attempts; checkpoints preserved")
            if detail.get("erro") or not out or not out.strip():
                self.recorder.evento(tipo="llm_infrastructure_failure", fase=self.recorder.fase_atual,
                                     detail=detail, llm_event_recorded=True)
                raise RuntimeError("LLM request failed or returned no text; stopping without marking tasks complete")
            atomic_json(path, {"response": out})
            return out

    def _record_attempt(self, detail, out, seconds, attempt):
        phase = self.recorder.fase_atual
        truncated = detail.get("finish_reason") == "length"
        error = detail.get("erro") or ("empty_response" if not truncated and not (out or "").strip() else None)
        incoming, outgoing = detail.get("prompt_tokens", 0) or 0, detail.get("completion_tokens", 0) or 0
        if hasattr(self.recorder, "score"):
            self.recorder.score.add_llm_call(incoming, outgoing, fase=phase, segundos=seconds,
                                              cortada=truncated, erro=bool(error))
        self.recorder.evento(tipo="llm", fase=phase, summary_attempt=attempt,
                             prompt_tokens=incoming, completion_tokens=outgoing,
                             segundos=round(seconds, 3), cortada=truncated, erro=error,
                             caracteres_resposta=len(out or ""), finish_reason=detail.get("finish_reason"))


async def pipeline(args, tasks, inventories):
    from marta.gptapi import model
    from marta.ruby_backend.recorder import RubyRecorder
    from .backend import XRepoBackend, XRepoProject, joined_specs
    from .runtime import project_environment

    model.temperature = args.temperature
    model.reasoning_effort = {"off": "none", "on": "high", "default": None}[args.thinking]
    model.top_p = args.top_p
    model.presence_penalty = args.presence_penalty
    model.request_timeout = args.request_timeout
    grouped = defaultdict(list)
    for t in tasks:
        grouped[t["file_path"].split("/", 1)[0]].append(t)
    for name, rows in sorted(grouped.items()):
        source = args.repos / name
        analysis_root = args.output / "analysis" / name
        env = inventories[name]
        with project_environment(source, name):
            proj = XRepoProject(root_dir=str(source), source_dir=".", output_root=str(analysis_root),
                                code_files=env["code_files"], load_paths=env["load_paths"],
                                full_context=True, target_selectors=selectors(rows),
                                backend=XRepoBackend()).discover()
        all_targets = list(proj.targets)
        proj.recorder = RubyRecorder(str(analysis_root / "events.jsonl"))
        shared = args.reuse_analysis_from / "analysis" / name / "calls" if args.reuse_analysis_from else None
        checkpointed = SummaryCheckpoints(analysis_root / "calls", model, proj.recorder, shared)
        print(f"{name}: {len(proj.analysis_targets)} context methods; {len(all_targets)} test targets", flush=True)
        start = time.monotonic()
        try:
            await proj.analyze_summaries(ask=checkpointed, enrich=not args.no_graph)
            proj.build_rag()
        finally:
            proj.recorder.end(str(analysis_root), "analysis")
        for target in all_targets:
            tid = target.task_id
            out = args.output / "tasks" / str(tid)
            status_file = out / "state.json"
            if status_file.exists() and json.loads(status_file.read_text()).get("status") in {"complete", "no_tests"}:
                continue
            work = args.work / "tasks" / str(tid) / "repo"
            workspace(source, work)
            proj.targets = [target]
            proj.backend.focal_source_rel = target.source_rel
            proj.root_dir = str(work)
            proj.output_root = str(out)
            target.spec_dir = str(out / "marta_specs")
            # Only files within this guarded experiment may be resumed.
            proj.code_changed = False
            proj.recorder = RubyRecorder(str(out / "events.jsonl"))
            proj.recorder.define_contexto(task_id=tid, project=name)
            atomic_json(status_file, {"status": "running", "task_id": tid})
            print(f"  task {tid}: {target.method.qualified_name}", flush=True)

            async def generate_ask(system, user):
                text = await model.aask(system, user)
                if (model.last_call or {}).get("erro") or not text:
                    raise RuntimeError("LLM transport/empty response; task remains incomplete")
                return text

            try:
                with project_environment(work, name):
                    await proj.generate_rounds(rounds=args.rounds, max_attempts=args.attempts, ask=generate_ask)
                specs = [Path(p) for p in proj._all_spec_paths()]
                specs = [p if p.is_absolute() else work / p for p in specs]
                code = joined_specs(specs)
                # Export accumulated rounds exactly as final evaluation will run
                # them, even if the combined suite fails (failure must be counted).
                if code.strip():
                    (out / "final_spec.rb").write_text(code)
                atomic_json(status_file, {"status": "complete" if code.strip() else "no_tests",
                                          "task_id": tid, "project": name})
                shutil.rmtree(work)
            finally:
                proj.recorder.end(str(out), "generation")
        print(f"{name}: finished; {time.monotonic() - start:.1f}s this process", flush=True)
    export_responses(tasks, args.output, args.output / "processed.jsonl")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--dataset", type=Path, required=True)
    p.add_argument("--repos", type=Path, default=Path("/app/repo_data"))
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--work", type=Path, required=True)
    p.add_argument("--preflight", type=Path, required=True)
    p.add_argument("--model", required=True)
    p.add_argument("--model-digest", required=True, help="Immutable Ollama model digest from /api/tags")
    p.add_argument("--rounds", type=int, default=3)
    p.add_argument("--attempts", type=int, default=3)
    p.add_argument("--temperature", type=float, default=0.0)
    p.add_argument("--top-p", type=float)
    p.add_argument("--presence-penalty", type=float)
    p.add_argument("--request-timeout", type=float, default=500.0)
    p.add_argument("--max-tokens", type=int, default=4096)
    p.add_argument("--thinking", choices=("off", "on", "default"), default="default",
                   help="Ollama boolean thinking: none disables, high enables; recorded in the experiment")
    p.add_argument("--no-graph", action="store_true")
    p.add_argument("--export-only", action="store_true")
    p.add_argument("--validate-only", action="store_true", help="Check inputs without invoking the model or creating a run")
    p.add_argument("--reuse-analysis-from", type=Path, help="Normal experiment: reuse only source-only pass one")
    args = p.parse_args()
    args.output, args.work, args.repos = (p.resolve() for p in (args.output, args.work, args.repos))
    if args.rounds < 1 or args.attempts < 1 or args.max_tokens < 1 or args.request_timeout <= 0:
        p.error("rounds, attempts and max-tokens must be positive")
    if args.top_p is not None and not 0 < args.top_p <= 1:
        p.error("top-p must be in (0, 1]")
    if args.presence_penalty is not None and not -2 <= args.presence_penalty <= 2:
        p.error("presence-penalty must be in [-2, 2]")
    if args.work == args.output or args.work in args.output.parents or args.output in args.work.parents:
        p.error("Work and results must be separate directory trees")
    tasks = load_tasks(args.dataset)
    ready = json.loads(args.preflight.read_text())
    from .runtime import environment_manifest
    if ready.get("environment") != environment_manifest():
        p.error("Container environment differs from the certified preflight")
    if not ready.get("ready") or not ready.get("runtime_checked"):
        p.error("Preflight did not certify all tasks and repository bundles")
    if ready.get("dataset_sha256") != DATA_SHA256 or ready.get("image") != IMAGE:
        p.error("Preflight belongs to another image or dataset")
    inventories = {}
    for name in sorted({t["file_path"].split("/", 1)[0] for t in tasks}):
        inventories[name] = source_inventory(args.repos / name,
                                             [t for t in tasks if t["file_path"].startswith(name + "/")])
        if inventories[name]["source_digest"] != ready["projects"][name]["source_digest"]:
            p.error(f"{name}: inputs changed since preflight")
        if inventories[name]["runtime_digest"] != ready["projects"][name].get("runtime_digest"):
            p.error(f"{name}: runtime files changed since preflight")
    config = {"dataset": DATA_SHA256, "image": IMAGE, "evaluator": UPSTREAM_COMMIT,
              "environment": environment_manifest(),
              "marta_code": code_fingerprint(), "model": args.model, "model_digest": args.model_digest,
              "summary_truncation_attempts": SUMMARY_TRUNCATION_ATTEMPTS,
              "rounds": args.rounds, "attempts": args.attempts, "temperature": args.temperature,
              "thinking": args.thinking,
              "top_p": args.top_p, "presence_penalty": args.presence_penalty,
              "request_timeout": args.request_timeout,
              "max_tokens": args.max_tokens, "no_graph": args.no_graph,
              "context": "production-project", "generation": "independent-task",
              "input_hashes": {n: x["source_digest"] for n, x in inventories.items()},
              "runtime_hashes": {n: x["runtime_digest"] for n, x in inventories.items()},
              "runtime_env": {k: os.getenv(k, "") for k in ("OLLAMA_CTX", "TRANSFORMER_PATH", "MARTA_MAX_CONTEXT_CHARS")}}
    if args.reuse_analysis_from:
        previous = json.loads((args.reuse_analysis_from / "experiment.json").read_text())
        expected = {"schema": "marta-xrepotest-v1", **config, "no_graph": False}
        if not args.no_graph or previous != expected:
            p.error("Pass-one reuse requires a matching normal experiment and --no-graph")
    if args.validate_only:
        print(json.dumps(config, indent=2))
        return
    with locked_run(args.output, config):
        if args.export_only:
            export_responses(tasks, args.output, args.output / "processed.jsonl")
        else:
            os.environ["MODEL"] = args.model
            os.environ["LLM_MAX_TOKENS"] = str(args.max_tokens)
            asyncio.run(pipeline(args, tasks, inventories))


if __name__ == "__main__":
    main()
