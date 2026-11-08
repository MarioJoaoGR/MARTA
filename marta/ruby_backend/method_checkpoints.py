"""Replay completed method outcomes under the native round writer lock."""
from dataclasses import asdict
import json
import os
from pathlib import Path
import shutil

from .checkpoints import ResumeValidationError, atomic_json, atomic_write, digest
from .generate import GenOutcome


class MethodCheckpoints:
    def __init__(self, rounds, number, jobs, root):
        self.directory = rounds.directory / "methods" / str(number)
        self.output = rounds.output
        self.jobs = [(target.method.qualified_name, target.analysis_id, target.task_id,
                      path, coverage) for target, path, coverage in jobs]
        self.paths = [Path(os.path.abspath(os.path.join(root, job[3]))) for job in self.jobs]
        self.plan = {
            "policy": "validated-method-prefix-v1",
            "round": number,
            "baseline": digest(rounds.state),
            "jobs": digest(self.jobs),
        }

    def _path(self, index):
        return self.directory / f"{index}.json"

    def _candidate(self, index, outcome):
        method, _, _, expected_path, _ = self.jobs[index]
        if outcome.method != method or type(outcome.success) is not bool:
            raise ResumeValidationError("Method checkpoint identity mismatch")
        if not outcome.success:
            if outcome.spec_path is not None or outcome.spec_code is not None:
                raise ResumeValidationError("Failed method checkpoint contains a candidate")
            return None
        path = self.paths[index]
        relative = path.relative_to(self.output)
        if (outcome.spec_path != expected_path or not isinstance(outcome.spec_code, str)
                or not outcome.spec_code.strip() or relative.parts[0] != "marta_specs"
                or path.resolve() != self.output.resolve() / relative):
            raise ResumeValidationError("Invalid method checkpoint candidate")
        return path

    def replay(self):
        plan_path = self.directory / "plan.json"
        try:
            records = {p.name for p in self.directory.glob("*.json")} - {"plan.json"}
            if plan_path.exists():
                if json.loads(plan_path.read_text()) != self.plan:
                    raise ResumeValidationError("Pending method checkpoints use a different round plan")
            elif records:
                raise ResumeValidationError("Pending method checkpoint plan is missing")
            else:
                atomic_json(plan_path, self.plan)
            if len(records) > len(self.jobs) or records != {self._path(i).name for i in range(len(records))}:
                raise ResumeValidationError("Method checkpoints must form a contiguous prefix")
            recovered = []
            for index in range(len(records)):
                record = json.loads(self._path(index).read_text())
                fields = record["outcome"]
                if record["digest"] != digest(fields):
                    raise ResumeValidationError("Method checkpoint checksum mismatch")
                outcome = GenOutcome(**fields)
                path = self._candidate(index, outcome)
                if path is not None and (path.exists() or path.is_symlink()):
                    raise ResumeValidationError("Method checkpoint would overwrite a retained spec")
                recovered.append((path, outcome))
        except (OSError, ValueError, TypeError, KeyError) as error:
            raise ResumeValidationError("Cannot validate pending method checkpoints") from error
        # Verify the entire prefix before publishing a candidate. The round
        # still has to pass the same accumulated-suite gate as a fresh run.
        for path, outcome in recovered:
            if path is not None:
                atomic_write(path, outcome.spec_code + "\n")
        return [outcome for _, outcome in recovered]

    def save(self, index, outcome):
        path = self._candidate(index, outcome)
        if path is not None and (not path.is_file() or path.read_text() != outcome.spec_code + "\n"):
            raise ResumeValidationError("Validated method candidate changed before checkpoint")
        fields = asdict(outcome)
        atomic_json(self._path(index), {"outcome": fields, "digest": digest(fields)})

    def invalidate(self):
        atomic_json(self.directory / "plan.json", {"invalid": "generation inputs changed"})

    def retire(self):
        # The certified round ledger is already durable. A stale journal for
        # this round is ignored even if cleanup is interrupted.
        shutil.rmtree(self.directory, ignore_errors=True)
