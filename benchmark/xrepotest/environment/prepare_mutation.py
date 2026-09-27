"""Expose the image's Mutant version to project bundles without editing Gemfiles.

The auxiliary Gemfile evaluates the published one and adds only the evaluator
tools. Existing locked gem versions must survive unchanged. Runs in Docker.
"""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess


def locked_versions(path):
    # Gem specs are the four-space entries with versions, including Git/PATH.
    import re
    return dict(re.findall(r"^    ([\w-]+) \(([^)]+)\)$", path.read_text(), re.M))


def prepare(root, env):
    check = subprocess.run(["bundle", "exec", "mutant", "--version"], cwd=root, env=env,
                           capture_output=True, text=True, timeout=30)
    if check.returncode == 0:
        return {"gemfile": "Gemfile", "mutant": check.stdout.strip(), "changed_versions": {}}
    original = root / "Gemfile.lock"
    if not original.exists():
        raise RuntimeError(f"Resolve the original bundle first: {root}")
    before = locked_versions(original)
    hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
              for p in (root / "Gemfile", original)}
    auxiliary = root / "Gemfile.xrepotest"
    auxiliary.write_text('eval_gemfile File.expand_path("Gemfile", __dir__)\n'
                         'gem "mutant", "= 0.15.1", require: false\n'
                         'gem "mutant-rspec", "= 0.15.1", require: false\n')
    lock = Path(str(auxiliary) + ".lock")
    pinned = Path(__file__).parent / "locks" / (root.name + ".evaluation.lock")
    shutil.copyfile(pinned if pinned.exists() else original, lock)
    cache = root / "vendor/cache"
    cache.mkdir(parents=True, exist_ok=True)
    for path in Path("/usr/local/bundle/cache").glob("*.gem"):
        if not (cache / path.name).exists():
            shutil.copy2(path, cache / path.name)
    child = dict(env, BUNDLE_GEMFILE=str(auxiliary))
    if pinned.exists():
        child["BUNDLE_FROZEN"] = "true"
    local = subprocess.run(["bundle", "install", "--local", "--no-cache"], cwd=root, env=child,
                           timeout=600)
    if local.returncode:
        if not pinned.exists():
            raise RuntimeError("Offline resolution failed without a fixed evaluation lock")
        # Some Ruby default gems have no .gem archive in the published image.
        # Fetch only the locked versions; frozen mode forbids re-resolution.
        subprocess.run(["bundle", "install", "--no-cache", "--jobs", "2", "--retry", "3"],
                       cwd=root, env=child, check=True, timeout=600)
    after = locked_versions(lock)
    changed = {n: [v, after.get(n)] for n, v in before.items() if after.get(n) != v}
    if changed:
        raise RuntimeError(f"Existing dependencies changed in {root.name}: {changed}")
    if any(hashlib.sha256((root / n).read_bytes()).hexdigest() != h for n, h in hashes.items()):
        raise RuntimeError(f"Original Gemfile/lock changed in {root.name}")
    check = subprocess.run(["bundle", "exec", "mutant", "--version"], cwd=root, env=child,
                           check=True, capture_output=True, text=True, timeout=30)
    subprocess.run(["bundle", "exec", "rspec", "--version"], cwd=root, env=child,
                   check=True, timeout=30)
    return {"gemfile": auxiliary.name, "mutant": check.stdout.strip(),
            "original_files": hashes, "changed_versions": changed,
            "added_versions": {n: v for n, v in after.items() if n not in before},
            "lock_sha256": hashlib.sha256(lock.read_bytes()).hexdigest()}


def main():
    import argparse
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("projects", nargs="+")
    args = p.parse_args()
    report = {}
    out = Path("/opt/xrepo/mutation-repair.json")
    out.parent.mkdir(exist_ok=True, parents=True)
    for name in args.projects:
        root = Path("/app/repo_data") / name
        env = dict(os.environ)
        if name == "hanami":
            for key in ("GEM_HOME", "GEM_PATH", "RUBYOPT", "BUNDLE_GEMFILE"):
                env.pop(key, None)
            env.update(PATH="/opt/xrepo/ruby33/bin:" + env["PATH"],
                       BUNDLE_APP_CONFIG="/opt/xrepo/hanami-config")
        report[name] = prepare(root, env)
        out.write_text(json.dumps(report, indent=2) + "\n")
        print(f"{name}: {report[name]}", flush=True)


if __name__ == "__main__":
    main()
