"""Atomic output and conservative round-level generation checkpoints.

A checkpoint certifies a completed, jointly validated round, including failed
attempts. Files left by an interrupted round are evidence, not accepted output.
"""
from __future__ import annotations

from contextlib import contextmanager
import fcntl
import hashlib
import json
import os
from pathlib import Path
import shutil
import tempfile


def atomic_write(path, content):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix="." + path.name + ".", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def atomic_json(path, value):
    atomic_write(path, json.dumps(value, sort_keys=True, indent=2) + "\n")


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=True).encode()).hexdigest()


def file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


DEPENDENCY_POLICY = "project-declarations-v2"
MARTA_OUTPUT_DIRS = frozenset((".marta_ruby_cache", ".marta_generation", "marta_specs",
                               "run_results", "rejected_specs"))


def dependency_files(root, *, output_root=None):
    """Find real declarations, pruning owned outputs before entering their trees.

    A distinct output root is excluded only when inside the project. Preserve
    declarations of ordinary subprojects, including a nested run_results folder.
    """
    root_abs = os.path.abspath(root)
    excluded_output = None
    if output_root is not None:
        canonical_root, output = Path(root).resolve(), Path(output_root).resolve()
        if output != canonical_root and output.is_relative_to(canonical_root):
            excluded_output = os.path.join(root_abs, str(output.relative_to(canonical_root)))
    found = []
    for directory, children, names in os.walk(root):
        at_root = os.path.abspath(directory) == root_abs
        children[:] = sorted(name for name in children
                             if not name.startswith(".") and name not in
                             ("vendor", "node_modules", "marta_specs", "rejected_specs")
                             and not (at_root and name in MARTA_OUTPUT_DIRS)
                             and os.path.join(os.path.abspath(directory), name) != excluded_output
                             and not os.path.islink(os.path.join(directory, name)))
        for name in sorted(names):
            if name in ("Gemfile", "Gemfile.lock") or name.endswith(".gemspec"):
                found.append(os.path.join(directory, name))
    return sorted(found)


class ResumeValidationError(RuntimeError):
    """Saved validated output changed, or another writer owns this output."""


class RoundCheckpoints:
    POLICY = "validated-rounds-v1"

    def __init__(self, output, recipe, event):
        self.output = Path(output).absolute()
        self.directory = self.output / ".marta_generation"
        self.path = self.directory / "rounds.json"
        self.recipe = recipe
        self.event = event
        self.state = self._empty()

    def _empty(self):
        return {"policy": self.POLICY, "recipe": self.recipe,
                "fingerprint": digest(self.recipe), "rounds": [], "files": {}}

    @contextmanager
    def locked(self):
        self.directory.mkdir(parents=True, exist_ok=True)
        with (self.directory / "writer.lock").open("a") as stream:
            try:
                fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError as exc:
                raise ResumeValidationError("Another generation owns this output directory") from exc
            try:
                yield self
            finally:
                fcntl.flock(stream, fcntl.LOCK_UN)

    def _specs(self):
        return {p.relative_to(self.output).as_posix(): p
                for p in (self.output / "marta_specs").rglob("*.rb") if p.is_file()}

    def _archive(self, paths, reason, include_checkpoint=False):
        paths = list(paths)
        if not paths and not (include_checkpoint and self.path.exists()):
            return
        directory = self.output / "rejected_specs"
        directory.mkdir(parents=True, exist_ok=True)
        archive = Path(tempfile.mkdtemp(prefix="resume_", dir=directory))
        for path in paths:
            destination = archive / path.relative_to(self.output)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(path), str(destination))
        if include_checkpoint and self.path.exists():
            shutil.move(str(self.path), str(archive / "rounds.json"))
        atomic_json(archive / "reason.json", {"reason": reason,
                    "files": [p.relative_to(self.output).as_posix() for p in paths]})
        self.event(tipo="resume_archive", reason=reason, archived=str(archive))

    def _valid(self, state):
        if not isinstance(state, dict) or state.get("policy") != self.POLICY:
            return False
        if state.get("recipe") != self.recipe or state.get("fingerprint") != digest(self.recipe):
            return False
        rounds, files = state.get("rounds"), state.get("files")
        if not isinstance(rounds, list) or not isinstance(files, dict) or (files and not rounds):
            return False
        for index, entry in enumerate(rounds):
            if (not isinstance(entry, dict) or type(entry.get("round")) is not int
                    or entry["round"] != index or not isinstance(entry.get("outcomes"), list)):
                return False
            for outcome in entry["outcomes"]:
                if (not isinstance(outcome, dict) or not isinstance(outcome.get("method"), str)
                        or type(outcome.get("success")) is not bool):
                    return False
        return all(isinstance(name, str) and name.startswith("marta_specs/")
                   and ".." not in Path(name).parts and isinstance(value, str)
                   and len(value) == 64 for name, value in files.items())

    def _verify_saved_files(self):
        for name, expected in self.state["files"].items():
            path = self.output / name
            if not path.is_file() or path.is_symlink() or file_hash(path) != expected:
                raise ResumeValidationError(
                    "Validated spec changed or disappeared: " + name +
                    "; preserve this output and start an independent output directory")

    def prepare(self, requested_rounds, trusted_seed=()):
        try:
            saved = json.loads(self.path.read_text())
        except (OSError, ValueError):
            saved = None
        specs = self._specs()
        if self._valid(saved):
            self.state = saved
            if len(saved["rounds"]) > requested_rounds:
                raise ResumeValidationError("Requested fewer rounds than the completed checkpoint")
            self._verify_saved_files()
            extra = [path for name, path in specs.items() if name not in saved["files"]]
            self._archive(extra, "Uncommitted files from outside completed rounds")
        else:
            # Only the explicit paired-ablation contract can supply an external
            # round-zero seed. Mere existence never certifies an ordinary spec.
            trusted = {Path(p).absolute() for p in trusted_seed}
            self._archive([p for p in specs.values() if p not in trusted],
                          "Missing, incompatible or invalid generation checkpoint", True)
        return len(self.state["rounds"])

    def archive_uncommitted(self, reason):
        """Preserve uncertified candidates without touching saved rounds/specs."""
        self._archive((path for name, path in self._specs().items()
                       if name not in self.state["files"]), reason)

    def commit(self, round_number, outcomes):
        if round_number != len(self.state["rounds"]):
            raise ResumeValidationError("Nonsequential generation checkpoint")
        self._verify_saved_files()
        specs = self._specs()
        if any(path.is_symlink() for path in specs.values()):
            raise ResumeValidationError("Generated specs must be regular files, not symlinks")
        state = dict(self.state, files={name: file_hash(path) for name, path in specs.items()},
                     rounds=self.state["rounds"] + [{"round": round_number, "outcomes": [
                         {"method": o.method, "success": o.success, "attempts": o.attempts,
                          "spec_path": o.spec_path, "last_error": o.last_error}
                         for o in outcomes]}])
        atomic_json(self.path, state)
        self.state = state
        self.event(tipo="round_checkpoint", ronda=round_number, checkpoint=str(self.path),
                   fingerprint=state["fingerprint"], retained_specs=len(state["files"]))
