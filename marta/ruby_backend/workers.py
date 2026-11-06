"""Bounded native generation; one event loop and one committing coordinator.

LLM awaits may overlap. Ruby subprocess calls and retrieval remain synchronous
on that loop. No additional model/index instances or per-method project copies.
"""
import asyncio
import os
from contextlib import ExitStack
from pathlib import Path
import time
from types import MappingProxyType

from .backend import RubyBackend
from .execution import GenerationWorkspace

POLICY = "round-barrier-strided-workers-v1"


def validate_workers(project, ask=None):
    count = project.generation_workers
    if type(count) is not int or count not in (1, 2, 4):
        raise ValueError("generation_workers must be 1, 2 or 4")
    if type(project.round_barrier) is not bool:
        raise ValueError("round_barrier must be a boolean")
    if count == 1 and not project.round_barrier:
        return
    if not project.isolate_execution or type(project.backend) is not RubyBackend:
        raise ValueError("Coordinated generation requires isolate_execution and the native RubyBackend")
    if ask is not None:
        owner = getattr(ask, "client", None) or getattr(ask, "__self__", None)
        legacy = any(getattr(provider, "records_llm_attempts", False) is True
                     or getattr(provider, "legacy_singleton_metrics", False) is True
                     for provider in (ask, owner) if provider is not None)
        if getattr(ask, "response_api", False) is not True or legacy:
            raise ValueError("Coordinated generation requires request-local ChatReply responses without shared legacy counters")


def example_snapshot(project):
    """Read available examples once at the round barrier, not per request.

    The exact definition/task filename lookup remains in RubyProject. Read only
    the same 400 characters repair prompts can use; no full-suite text history.
    """
    folders = {}
    for value in project._all_spec_paths():
        path = Path(os.path.abspath(os.path.join(project.root_dir, value)))
        if path.is_symlink():
            raise ValueError("Example snapshot requires regular generated specs")
        with path.open(encoding="utf-8") as stream:
            folders.setdefault(str(path.parent), {})[path.name] = stream.read(400)
    return MappingProxyType({folder: MappingProxyType(values) for folder, values in folders.items()})


class GenerationWorkers:
    def __init__(self, project):
        validate_workers(project)
        self.project = project
        self.stack = ExitStack()
        self.slots = {}

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return self.stack.__exit__(*exc)

    def _slot(self, index):
        if index not in self.slots:
            self.slots[index] = self.stack.enter_context(GenerationWorkspace(self.project))
        return self.slots[index]

    def verify_inputs(self):
        for slot in self.slots.values():
            slot.verify_inputs()

    def coverage(self, specs):
        # Reuse slot zero rather than allocate an extra coordinator repository.
        self.verify_inputs()
        result = self._slot(0).coverage(specs)
        self.verify_inputs()
        return result

    async def generate_round(self, jobs, ask, attempts, recorder, round_number):
        """Return/publish in target order, irrespective of completion order.

        Fixed striding makes worker assignment independent of latency. Results
        remain private until all scheduled jobs finish. A failed/interrupted
        round drains cancelled tasks and archives completed private candidates.
        """
        validate_workers(self.project, ask)
        if not jobs:
            return []
        examples = example_snapshot(self.project)
        results = [None] * len(jobs)
        slots = [None] * len(jobs)
        count = min(self.project.generation_workers, len(jobs))

        async def worker(index):
            workspace = self._slot(index)
            for position in range(index, len(jobs), count):
                target, path, coverage_info = jobs[position]
                child = recorder.fork(worker=index + 1, ronda=round_number,
                                      definition_id=target.analysis_id,
                                      metodo=target.method.qualified_name)
                child.score.first_run = round_number == 0
                workspace.recorder = child
                started = time.monotonic()
                status = "interrupted"
                try:
                    with recorder.contexto(worker=index + 1, definition_id=target.analysis_id):
                        result = await self.project._generate_target(
                            target, path, ask, attempts, child, workspace, coverage_info,
                            examples=examples, publish=False)
                    results[position], slots[position] = result, workspace
                    status = "accepted_candidate" if result.success else "no_tests"
                finally:
                    recorder.collect_worker(index + 1, child)
                    child.evento(tipo="worker_task_finished", status=status,
                                 seconds=time.monotonic() - started,
                                 llm_calls=child.score.llm_calls,
                                 usage_unknown_calls=child.score.llm_usage_unknown_calls,
                                 interrupted_requests=child.score.llm_interrupted_requests)

        tasks = [asyncio.create_task(worker(index)) for index in range(count)]
        published = set()
        try:
            await asyncio.gather(*tasks)
            self.verify_inputs()
            # No awaits during publication. Only the coordinator writes outputs.
            for position, outcome in enumerate(results):
                if outcome.success:
                    slots[position].publish(outcome)
                    published.add(position)
            recorder.evento(tipo="generation_barrier", ronda=round_number, policy=POLICY,
                            workers=count, candidates=len(jobs), examples_policy="previous-round-snapshot")
            return results
        except BaseException:
            for task in tasks:
                if not task.done():
                    task.cancel()
            await asyncio.gather(*tasks, return_exceptions=True)
            for position, outcome in enumerate(results):
                if outcome is not None and outcome.success and position not in published:
                    slots[position].archive_candidate(outcome.spec_path)
            raise
