"""Apply the two authorized coverage fixes to the pinned evaluator in Docker.

Fail closed on a different upstream file. Preserve its original bytes and a
readable diff; record hashes for every evaluator module in the environment.
Neither benchmark data nor Ruby project sources are written by this script.
"""
import difflib
import hashlib
import json
from pathlib import Path

UPSTREAM_SHA256 = "0b03a6073e13dfc7bade9fb86327aea22a1c756b720eb5540b8c372076da929d"
REVISION = "coverage-order-and-exact-path-v1"


def corrected_source(raw):
    if hashlib.sha256(raw).hexdigest() != UPSTREAM_SHA256:
        raise ValueError("Unexpected upstream evaluator; refusing to patch")
    source = raw.decode("utf-8").replace("\r\n", "\n")
    start = source.index("# Explicitly load the focal file")
    end = source.index("require 'rspec/core'", start)
    focal_load = source[start:end]
    corrected = source[:start] + source[end:]
    run = "RSpec::Core::Runner.run([ARGV[0]], $stderr, $stdout)\n"
    if corrected.count(run) != 1:
        raise ValueError("Unexpected coverage wrapper")
    corrected = corrected.replace(run, run + "\n" + focal_load, 1)
    start = corrected.index("            matched_file = None")
    end = corrected.index("            if matched_file:", start)
    corrected = (corrected[:start]
                 + "            matched_file = next((key for key in coverage_data\n"
                 + "                                 if str(Path(key).resolve()) == focal_file_abs), None)\n\n"
                 + corrected[end:])
    compile(corrected, "ruby/command_utils.py", "exec")
    diff = "".join(difflib.unified_diff(source.splitlines(True), corrected.splitlines(True),
                                     fromfile="a/ruby/command_utils.py",
                                     tofile="b/ruby/command_utils.py"))
    # Do not turn the whole upstream CRLF file into an unrelated formatting diff.
    newline = "\r\n" if b"\r\n" in raw else "\n"
    return corrected.replace("\n", newline).encode("utf-8"), diff


def evaluator_hashes(app):
    return {f"{name}/{p.name}": hashlib.sha256(p.read_bytes()).hexdigest()
            for name in ("base", "ruby") for p in sorted((app / name).glob("*.py"))}


def main():
    app, record = Path("/app"), Path("/opt/xrepo")
    target = app / "ruby/command_utils.py"
    raw = target.read_bytes()
    corrected, diff = corrected_source(raw)
    before = evaluator_hashes(app)
    backup = record / "original/ruby/command_utils.py"
    backup.parent.mkdir(parents=True, exist_ok=True)
    backup.write_bytes(raw)
    patch = record / "evaluator-coverage.patch"
    patch.write_text(diff)
    target.write_bytes(corrected)
    after = evaluator_hashes(app)
    if [name for name in before if before[name] != after[name]] != ["ruby/command_utils.py"]:
        raise RuntimeError("Unexpected change outside coverage helper")
    manifest_path = record / "environment.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["evaluator"] = {"revision": REVISION, "files_before": before,
                             "files_after": after,
                             "patch_sha256": hashlib.sha256(patch.read_bytes()).hexdigest()}
    manifest["recipe"][Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Evaluator repaired: {REVISION}; original and diff preserved", flush=True)


if __name__ == "__main__":
    main()
