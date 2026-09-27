"""Install Hanami's missing bundle using the Git snapshots in the official image.

Run only inside the derived container. The benchmark's Gemfile, source and
tests are not edited. Bundler configuration and the resolved lock are retained.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import shutil


def main():
    root = Path("/app/repo_data/hanami")
    config = Path("/opt/xrepo/hanami-config")
    config.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    for key in ("GEM_HOME", "GEM_PATH", "RUBYOPT", "BUNDLE_GEMFILE"):
        env.pop(key, None)
    env.update(PATH="/opt/xrepo/ruby33/bin:" + env["PATH"],
               BUNDLE_APP_CONFIG=str(config), BUNDLE_JOBS="2", BUNDLE_RETRY="3")

    def run(*args, capture=False):
        return subprocess.run(args, cwd=root, env=env, check=True, text=True,
                              stdout=subprocess.PIPE if capture else None, timeout=1800).stdout

    files = [p for p in root.rglob("*") if p.is_file()
             and not {"vendor", ".git", ".bundle"}.intersection(p.relative_to(root).parts)
             and p.name != "Gemfile.lock"]
    before = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    run("gem", "install", "--no-document", "bundler:2.4.22", "prism:1.9.0")
    snapshots = {}
    for path in sorted((root / "vendor/bundle/ruby/3.2.0/bundler/gems").iterdir()):
        specs = list(path.glob("*.gemspec"))
        if len(specs) != 1:
            raise RuntimeError(f"Expected one gemspec in {path}")
        name = run("ruby", "-e", "puts Gem::Specification.load(ARGV[0]).name", str(specs[0]), capture=True).strip()
        revision = run("git", "-C", str(path), "rev-parse", "HEAD", capture=True).strip()
        snapshots[name] = {"path": str(path), "revision": revision}
        run("bundle", "_2.4.22_", "config", "set", "--local", "local." + name, str(path))
    if len(snapshots) != 10:
        raise RuntimeError(f"Expected ten published Git snapshots, got {len(snapshots)}")
    pinned = Path(__file__).parent / "locks/hanami.lock"
    if pinned.exists():
        shutil.copyfile(pinned, root / "Gemfile.lock")
        env["BUNDLE_FROZEN"] = "true"
    run("bundle", "_2.4.22_", "config", "set", "--local", "path", "vendor/bundle")
    # No bundle update: local overrides prevent tracking moving main branches.
    run("bundle", "_2.4.22_", "install", "--jobs", "2", "--retry", "3")
    run("bundle", "_2.4.22_", "check")
    run("bundle", "_2.4.22_", "exec", "ruby", "-e", "require 'hanami'; puts Hanami::VERSION")
    run("bundle", "_2.4.22_", "exec", "rspec", "--version")
    after = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    if before != after:
        raise RuntimeError("Installing dependencies modified existing benchmark files")
    lock = root / "Gemfile.lock"
    (config / "repair.json").write_text(json.dumps({
        "ruby": run("ruby", "-v", capture=True).strip(), "git_snapshots": snapshots,
        "lock_sha256": hashlib.sha256(lock.read_bytes()).hexdigest(),
        "preserved_files": before,
    }, indent=2) + "\n")


if __name__ == "__main__":
    main()
