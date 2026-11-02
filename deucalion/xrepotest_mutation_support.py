"""Audited Mutant execution, separate from frozen core evaluation/generation.

No benchmark sources, generated suites, mutation operators or installed gems are
patched. All configuration and hooks are written only in disposable workspaces.
"""
import hashlib
import json
import os
import signal
from pathlib import Path
import re
import subprocess
import time

POLICY = "isolated-focal-mutation-v1"
ANSI = re.compile(r"\x1b\[[0-9;]*m")


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def resolve_subject(task, repo):
    """Match name AND official source range, including Ruby operator names.

    Never strip sub-project prefixes or fall back to a guessed class/first
    same-named method. Runtime inspection must subsequently confirm identity.
    """
    from tree_sitter import Language, Parser
    import tree_sitter_ruby
    parts = Path(task["file_path"]).parts
    if len(parts) < 2 or Path(task["file_path"]).is_absolute() or ".." in parts:
        raise ValueError("Unsafe focal path")
    rel = Path(*parts[1:])
    path = Path(repo) / rel
    source = path.read_text().encode()
    if source.decode() != task["file_content"]:
        raise ValueError("Focal source differs from official task")
    tree = Parser(Language(tree_sitter_ruby.language())).parse(source)
    region = task["function_component"]
    stack, matches = [tree.root_node], []
    while stack:
        node = stack.pop()
        stack.extend(node.children)
        if node.type not in ("method", "singleton_method"):
            continue
        name = node.child_by_field_name("name")
        if (name is not None and source[name.start_byte:name.end_byte].decode() == task["function_name"]
                and node.start_point.row + 1 == region["start_line"]
                and node.end_point.row + 1 == region["end_line"]):
            matches.append(node)
    if len(matches) != 1:
        raise ValueError("Expected exactly one definition at official name/range")
    node = matches[0]
    if source[node.start_byte:node.end_byte].decode().strip() != task["focal_code"].strip():
        raise ValueError("Focal code differs at official range")
    ancestors, parent = [], node.parent
    while parent is not None:
        ancestors.append(parent)
        parent = parent.parent
    namespace, singleton = [], False
    for parent in reversed(ancestors):
        if parent.type in ("class", "module"):
            name = parent.child_by_field_name("name")
            if name is None:
                raise ValueError("Anonymous lexical scope")
            text = source[name.start_byte:name.end_byte].decode()
            if not re.fullmatch(r"(?:::)?[A-Z]\w*(?:::[A-Z]\w*)*", text):
                raise ValueError("Nonconstant lexical scope")
            namespace = ([] if text.startswith("::") else namespace) + text.lstrip(":").split("::")
            singleton = False  # A nested named scope starts its own method table.
        elif parent.type == "singleton_class":
            value = parent.child_by_field_name("value")
            if value is None or source[value.start_byte:value.end_byte] != b"self":
                raise ValueError("Non-self singleton class needs explicit runtime resolution")
            singleton = True
        elif parent.type == "assignment":
            left, right = parent.child_by_field_name("left"), parent.child_by_field_name("right")
            if left is not None and right is not None:
                lhs = source[left.start_byte:left.end_byte].decode()
                rhs = source[right.start_byte:right.end_byte].decode()
                if re.fullmatch(r"[A-Z]\w*", lhs) and re.match(r"(?:Class|Module|Struct)\.new\b", rhs):
                    namespace.append(lhs)
                    singleton = False
        elif parent.type in ("method", "singleton_method"):
            raise ValueError("Nested method needs explicit runtime resolution")
        # A block may preserve or change self. This is only a candidate:
        # the runtime bootstrap must verify its exact file and source range.
    if not namespace:
        raise ValueError("No named owner")
    if node.type == "singleton_method":
        receiver = node.child_by_field_name("object")
        if receiver is None or source[receiver.start_byte:receiver.end_byte] != b"self":
            raise ValueError("Non-self singleton receiver needs explicit runtime resolution")
        singleton = True
    return {"subject": "::".join(namespace) + ("." if singleton else "#") + task["function_name"],
            "file": rel.as_posix(), "start_line": region["start_line"],
            "end_line": region["end_line"], "source_sha256": sha(path)}


def parse_result(stdout, stderr, exit_code, identity):
    """Reject startup errors, partial runs and neutral failures as measurements."""
    clean = ANSI.sub("", stdout)
    counts = {}
    for key in ("Mutations", "Results", "Kills", "Alive", "Timeouts"):
        values = re.findall(r"^\s*" + key + r"\s*:\s*(\d+)\s*$", clean, re.M)
        if values:
            counts[key.lower()] = int(values[-1])
    valid = (exit_code in (0, 1) and bool(identity.get("verified"))
             and counts.get("mutations", 0) > 0
             and counts.get("results") == counts.get("mutations")
             and counts.get("kills", -1) + counts.get("alive", -1) == counts.get("mutations")
             and counts.get("timeouts") == 0
             and "Neutral failure" not in clean and "Neutral failure" not in stderr)
    return {"valid": valid, "counts": counts,
            "mutation_score": counts["kills"] / counts["mutations"] if valid else None}


def execute(command, repo, timeout):
    """Kill the whole Mutant worker group on timeout; preserve diagnostic logs."""
    with subprocess.Popen(command, cwd=repo, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, text=True, start_new_session=True) as proc:
        try:
            stdout, stderr = proc.communicate(timeout=timeout)
            return stdout, stderr, proc.returncode
        except subprocess.TimeoutExpired:
            try:
                os.killpg(proc.pid, signal.SIGTERM)
            except ProcessLookupError:
                pass
            try:
                stdout, stderr = proc.communicate(timeout=10)
            except subprocess.TimeoutExpired:
                try:
                    os.killpg(proc.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                stdout, stderr = proc.communicate()
            return stdout, stderr, None


def run_mutant(task, suite_path, repo, output, timeout=900, action="run"):
    """Execute pinned Mutant with runtime subject and test-isolation assertions."""
    import yaml
    repo, suite_path, output = Path(repo).resolve(), Path(suite_path).resolve(), Path(output).resolve()
    suite_path.relative_to(repo)
    output.mkdir(parents=True, exist_ok=False)
    identity = resolve_subject(task, repo)
    spec_helper = repo / "spec/spec_helper.rb"
    if not spec_helper.is_file():
        raise ValueError("Expected project spec_helper")
    guard = repo / ".xrepo_mutation_guard.rb"
    guard.write_text("require 'rspec'\nRSpec.configure do |c|\n"
        "c.define_derived_metadata do |m|\n"
        "p = m[:absolute_file_path] || m[:file_path]\n"
        "own = p && File.expand_path(p) == " + json.dumps(str(suite_path)) + "\n"
        "m[:mutant] = !!own\n"
        "m[:mutant_expression] = " + json.dumps(identity["subject"]) + " if own\n"
        "end\nend\n")
    config = {"integration": {"name": "rspec", "arguments": ["--options", "/dev/null", str(suite_path)]},
              "matcher": {"subjects": [identity["subject"]]},
              "includes": ["spec", "lib"] + sorted(str(p) for p in repo.glob("*/lib")),
              "requires": ["rspec", str(guard), str(spec_helper), str(repo / identity["file"])],
              "jobs": 4, "usage": "opensource"}
    (repo / "mutant.yml").write_text(yaml.safe_dump(config))
    bootstrap = Path(__file__).parent / "rb/xrepotest_mutation_bootstrap.rb"
    expected = {**identity, "file": str(repo / identity["file"]), "suite": str(suite_path),
                "audit": str(output / "identity.json")}
    (output / "expected.json").write_text(json.dumps(expected, indent=2) + "\n")
    command = ["bundle", "exec", "ruby", str(bootstrap), str(output / "expected.json")]
    command += ["run"] if action == "run" else ["environment", "show"]
    started = time.monotonic()
    stdout, stderr, code = execute(command, repo, timeout)
    (output / "stdout.txt").write_text(stdout)
    (output / "stderr.txt").write_text(stderr)
    actual = json.loads((output / "identity.json").read_text()) if (output / "identity.json").exists() else {}
    result = {"policy": POLICY, "task_id": task["task_id"], "action": action,
              "expected": identity, "identity": actual, "exit_code": code,
              "suite_sha256": sha(suite_path), "bootstrap_sha256": sha(bootstrap),
              "support_sha256": sha(__file__), "config": config, "command": command,
              "seconds": time.monotonic() - started,
              **parse_result(stdout, stderr, code, actual)}
    (output / "result.json").write_text(json.dumps(result, indent=2) + "\n")
    return result
