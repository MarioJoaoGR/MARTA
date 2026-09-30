"""Exercise the production loading recipes for every official focal file.

Each check is a fresh RSpec process in a disposable repository, using the same
Bundler/configuration/temporary-spec location as generation. No LLM is called.
"""
import argparse
import hashlib
import json
from pathlib import Path
import tempfile

from benchmark.xrepotest.protocol import DATA_SHA256, atomic_json, load_tasks, source_inventory
from benchmark.xrepotest.run import workspace
from benchmark.xrepotest.runtime import environment_manifest, project_environment
from marta.ruby_backend import loading
from marta.ruby_backend import dependencies
from marta.ruby_backend.runner import run_rspec


def loading_fingerprint():
    return hashlib.sha256(b"\0".join(p.read_bytes() for p in
                         (Path(loading.__file__), Path(dependencies.__file__), dependencies.HELPER))).hexdigest()


def check(root, rel, plan, behavior=""):
    focal = (root / rel).resolve()
    package = root / plan["package"]
    spec = package / "spec/temp_spec.rb"
    spec.parent.mkdir(parents=True, exist_ok=True)
    prelude = "\n".join("require " + json.dumps(r) for r in plan["requires"])
    code = (prelude + '\nRSpec.describe "production loading diagnostic" do\n'
            '  it "loads the exact production file" do\n'
            f'    expect($LOADED_FEATURES).to include({json.dumps(str(focal))})\n'
            f'    {behavior}\n'
            '  end\nend\n')
    spec.write_text(code)
    result = run_rspec(str(spec), cwd=str(package), use_bundle=True, isolated=False, use_guard=False)
    return {"passed": result.all_passed and bool(result.examples),
            "output": result.output, "spec": code, "plan": plan}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--report", required=True, type=Path)
    args = p.parse_args()
    tasks = load_tasks(Path("/app/xrepotest/ruby_functions.jsonl"))
    report = {"diagnostic_only": True, "ready": False, "dataset": DATA_SHA256,
              "environment": environment_manifest(), "loading_code": loading_fingerprint(),
              "policy": loading.LOADING_POLICY, "projects": {}, "checks": {}}
    atomic_json(args.report, report)
    with tempfile.TemporaryDirectory(prefix="marta-loading-") as tmp:
        for name in sorted({t["file_path"].split("/")[0] for t in tasks}):
            rows = [t for t in tasks if t["file_path"].startswith(name + "/")]
            source = Path("/app/repo_data") / name
            inventory = source_inventory(source, rows)
            report["projects"][name] = {k: inventory[k] for k in ("source_digest", "runtime_digest")}
            root = Path(tmp) / name
            workspace(source, root)
            with project_environment(root, name):
                index = dependencies.bundle_index(root)
            for rel in sorted({t["file_path"].split("/", 1)[1] for t in rows}):
                prefix = next(lp for lp in inventory["load_paths"] if rel.startswith(lp + "/"))
                focal = rel[len(prefix) + 1:-3]
                with project_environment(root, name):
                    plan = loading.loading_plan(root, rel, focal, index)
                if not plan["entry"]:
                    result = {"passed": False, "plan": plan, "output": "No unambiguous production entry file"}
                else:
                    with project_environment(root, name):
                        result = check(root, rel, plan)
                report["checks"][name + "/" + rel] = result
                if not result["passed"]:
                    print(name + "/" + rel + ": FAILED\n" + result["output"][-1400:], flush=True)
            # Regression for the actual incident: merely loading session.rb
            # succeeds, but constructing a real session requires capybara.rb.
            if name == "capybara":
                rel = "lib/capybara/session.rb"
                with project_environment(root, name):
                    plan = loading.loading_plan(root, rel, "capybara/session", index)
                    report["session_regression"] = check(root, rel, plan,
                        'expect(Capybara::Session.new(:rack_test).config.run_server).to eq(true)')
            checks = [v for k, v in report["checks"].items() if k.startswith(name + "/")]
            print(f"{name}: {sum(c['passed'] for c in checks)}/{len(checks)} focal files load", flush=True)
            atomic_json(args.report, report)
    report["ready"] = all(c["passed"] for c in report["checks"].values()) and report["session_regression"]["passed"]
    atomic_json(args.report, report)
    print(f"Loading ready: {report['ready']}; {len(report['checks'])} focal files", flush=True)
    if not report["ready"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
