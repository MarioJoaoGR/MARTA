"""Select the documented container environment for each project/work copy."""
from contextlib import contextmanager
import json
import hashlib
import os
from pathlib import Path

MANIFEST = Path("/opt/xrepo/environment.json")


def environment_manifest():
    return json.loads(MANIFEST.read_text()) if MANIFEST.is_file() else None


def validate_evaluator(actual_hashes):
    manifest = environment_manifest()
    expected = (manifest or {}).get("evaluator", {}).get("files_after")
    if expected is not None and actual_hashes != expected:
        raise ValueError("Evaluator files differ from the documented repaired environment")


def _trust_project_git(root, env):
    """Trust exact image/workspace repositories for this subprocess tree only.

    Singularity keeps the caller's UID while image files belong to root.
    Bundler reads Git gemspecs even with a frozen, fully installed bundle.
    Resolve vendor symlinks so disposable workspaces trust the shared snapshot,
    without disabling ownership checks for unrelated repositories.
    """
    root = Path(root).resolve()
    repositories = {root} if (root / ".git").exists() else set()
    for marker in root.glob("vendor/bundle/ruby/*/bundler/gems/*/.git"):
        repositories.add(marker.parent.resolve())
    count = int(env.get("GIT_CONFIG_COUNT", "0"))
    for repository in sorted(repositories):
        env[f"GIT_CONFIG_KEY_{count}"] = "safe.directory"
        env[f"GIT_CONFIG_VALUE_{count}"] = str(repository)
        count += 1
    if repositories:
        env["GIT_CONFIG_COUNT"] = str(count)


def project_env(root, name, base=None):
    env = dict(os.environ if base is None else base)
    manifest = environment_manifest()
    if manifest is None:
        return env  # Original image remains usable for diagnosis.
    project = manifest["projects"][name]
    lock = Path(root).resolve() / (project["gemfile"] + ".lock")
    if hashlib.sha256(lock.read_bytes()).hexdigest() != project["lock_sha256"]:
        raise ValueError(f"{name}: bundle lock differs from the documented environment")
    if project.get("ruby_prefix"):
        for key in ("GEM_HOME", "GEM_PATH", "RUBYOPT", "MARTA_RUBY_BIN", "MARTA_RSPEC_BIN", "MARTA_RUBY_ENV"):
            env.pop(key, None)
        env["PATH"] = project["ruby_prefix"] + "/bin:" + env.get("PATH", "")
    if project.get("bundle_config"):
        env["BUNDLE_APP_CONFIG"] = project["bundle_config"]
    env.update(project.get("env", {}))
    # Resolve against the task's disposable copy, never the original project.
    env["BUNDLE_GEMFILE"] = str(Path(root).resolve() / project["gemfile"])
    env["BUNDLE_FROZEN"] = "true"
    _trust_project_git(root, env)
    return env


@contextmanager
def project_environment(root, name):
    # The adapters run tasks sequentially. Restore even when an evaluator fails.
    before = dict(os.environ)
    try:
        os.environ.clear()
        os.environ.update(project_env(root, name, before))
        yield
    finally:
        os.environ.clear()
        os.environ.update(before)
