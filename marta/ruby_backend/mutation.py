"""Optional native Mutant 0.15.1 evaluation; no dependency installation.

Uses the identity/isolation contract established by the frozen XRepo executor,
without changing or importing that benchmark-specific implementation.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import re
import signal
import subprocess
import time

from .checkpoints import atomic_json, file_hash
from .ruby_ast import ruby_bin
from .runner import run_rspec

POLICY = "native-focal-mutation-v1"
BOOTSTRAP = Path(__file__).parent / "rb/marta_mutation.rb"


def execute(command, cwd, timeout, *, env=None):
    with subprocess.Popen(command, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          text=True, errors="replace", start_new_session=True, env=env) as proc:
        try:
            out, err = proc.communicate(timeout=timeout)
            return out, err, proc.returncode
        except subprocess.TimeoutExpired:
            for sig, wait in ((signal.SIGTERM, 5), (signal.SIGKILL, None)):
                try:
                    os.killpg(proc.pid, sig)
                except ProcessLookupError:
                    pass
                try:
                    out, err = proc.communicate(timeout=wait)
                    return out, err, None
                except subprocess.TimeoutExpired:
                    continue


def parse_result(stdout, stderr, exit_code, identity):
    clean = re.sub(r"\x1b\[[0-9;]*m", "", stdout)
    counts = {}
    for key in ("Mutations", "Results", "Kills", "Alive", "Timeouts"):
        values = re.findall(r"^\s*" + key + r"\s*:\s*(\d+)\s*$", clean, re.M)
        if values:
            counts[key.lower()] = int(values[-1])
    valid = (exit_code in (0, 1) and identity.get("verified") is True
             and counts.get("mutations", 0) > 0
             and counts.get("results") == counts.get("mutations")
             and identity.get("mutations") == counts.get("mutations")
             and counts.get("kills", -1) + counts.get("alive", -1) == counts.get("mutations")
             and counts.get("timeouts") == 0
             and "Neutral failure" not in clean and "Neutral failure" not in stderr)
    return {"valid": valid, "counts": counts,
            "mutation_score": counts["kills"] / counts["mutations"] if valid else None}


def run_mutation(identity, suite, repo, output, *, load_paths, requires=(),
                 timeout=300, jobs=1, usage, bundle=False, env=None):
    """The caller supplies a disposable workspace and the exact focal identity."""
    if usage not in ("opensource", "commercial"):
        raise ValueError("Declare the Mutant usage mode explicitly")
    if type(timeout) is not int or timeout < 1 or type(jobs) is not int or jobs < 1:
        raise ValueError("Mutation timeout/jobs must be positive integers")
    repo, suite, output = Path(repo).resolve(), Path(suite).resolve(), Path(output).resolve()
    suite.relative_to(repo)
    source = (repo / identity["file"]).resolve()
    source.relative_to(repo)
    output.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    base = ["bundle", "exec", ruby_bin(env)] if bundle else [ruby_bin(env)]
    result = {"policy": POLICY, "valid": False, "mutation_score": None,
              "expected": identity, "suite_sha256": file_hash(suite), "jobs": jobs,
              "timeout": timeout, "usage": usage, "bundle": bundle,
              "bootstrap_sha256": file_hash(BOOTSTRAP), "implementation_sha256": file_hash(__file__)}
    source_hash = file_hash(source)
    result["source_sha256"] = source_hash
    try:
        probe = ('require "json"; require "rspec"; require "mutant"; require "mutant/integration/rspec"; '
                 'puts JSON.generate({ruby: RUBY_VERSION, mutant: Mutant::VERSION, '
                 'mutant_rspec: Gem.loaded_specs.fetch("mutant-rspec").version.to_s, '
                 'rspec_core: Gem.loaded_specs.fetch("rspec-core").version.to_s})')
        out, err, code = execute(base + ["-e", probe], repo, 30, **({"env": env} if env is not None else {}))
        result["toolchain"] = {"stdout": out, "stderr": err, "exit_code": code}
        versions = json.loads(out) if code == 0 else {}
        result["toolchain"]["versions"] = versions
        if not isinstance(versions, dict):
            raise ValueError("Invalid mutation toolchain report")
        if code != 0 or versions.get("mutant") != "0.15.1" or versions.get("mutant_rspec") != "0.15.1":
            result.update(status="unavailable", reason="Mutant/mutant-rspec 0.15.1 unavailable in the supplied environment")
        else:
            baseline = run_rspec(str(suite), load_paths=list(load_paths), cwd=str(repo),
                                 requires=list(requires), isolated=True, use_bundle=bundle, **({"env": env} if env is not None else {}))
            result["baseline"] = {"valid": baseline.all_passed, "report_valid": baseline.report_valid,
                                  "exit_code": baseline.exit_code, "output": baseline.output}
            if not baseline.all_passed:
                result.update(status="unavailable", reason="The exact staged suite failed its baseline")
            else:
                guard = output / "guard.rb"
                guard.write_text("require 'rspec'\nRSpec.configure do |c|\nc.define_derived_metadata do |m|\n"
                    "p = m[:absolute_file_path] || m[:file_path]\n"
                    "own = p && File.expand_path(p) == " + json.dumps(str(suite)) + "\n"
                    "m[:mutant] = !!own\nm[:mutant_expression] = " + json.dumps(identity["subject"]) + " if own\nend\nend\n")
                config = {"integration": {"name": "rspec", "arguments": ["--options", "/dev/null", str(suite)]},
                          "matcher": {"subjects": [identity["subject"]]}, "includes": list(load_paths),
                          "requires": ["rspec", str(guard), *requires, str(source)],
                          "jobs": jobs, "usage": usage}
                # Mutant 0.15.1 reads these fixed paths (no --config option).
                # Only the supplied disposable workspace is changed.
                for rel in (".mutant.yml", "config/mutant.yml", "mutant.yml"):
                    candidate = repo / rel
                    candidate.parent.resolve().relative_to(repo)
                    if candidate.exists() or candidate.is_symlink():
                        candidate.unlink()
                config_file = repo / "mutant.yml"
                config_file.write_text(json.dumps(config, indent=2) + "\n")  # JSON is valid YAML.
                (output / "mutant.yml").write_bytes(config_file.read_bytes())
                expected = {**identity, "file": str(source), "suite": str(suite),
                            "audit": str(output / "identity.json")}
                atomic_json(output / "expected.json", expected)
                command = base + [str(BOOTSTRAP), str(output / "expected.json"), "run"]
                out, err, code = execute(command, repo, timeout, **({"env": env} if env is not None else {}))
                (output / "stdout.txt").write_text(out)
                (output / "stderr.txt").write_text(err)
                audit = json.loads((output / "identity.json").read_text()) if (output / "identity.json").exists() else {}
                result.update(config=config, command=command, identity=audit, exit_code=code,
                              diagnostic_tail=err[-3000:],
                              **parse_result(out, err, code, audit))
                result["status"] = "measured" if result["valid"] else "unavailable"
                if not result["valid"]:
                    result["reason"] = "Mutation identity, isolation, completion or timeout validation failed"
    except (OSError, ValueError, RuntimeError) as error:
        result.update(status="unavailable", valid=False, mutation_score=None, reason=str(error))
    source_after = file_hash(source) if source.is_file() else None
    suite_after = file_hash(suite) if suite.is_file() else None
    if source_after != source_hash or suite_after != result["suite_sha256"]:
        result.update(valid=False, mutation_score=None, status="unavailable",
                      reason="Staged focal source or suite changed during evaluation")
    result["seconds"] = time.monotonic() - started
    atomic_json(output / "result.json", result)
    return result
