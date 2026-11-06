"""Optional repository copies for native Ruby execution, not an OS sandbox.

One lazy copy per invocation, reused across methods/rounds. Analysis and retrieval
remain owned by the coordinator. No installation, model request or worker pool.
"""
import copy
import os
from pathlib import Path
import shutil
import tempfile
import time

from .backend import RubyBackend
from .checkpoints import DEPENDENCY_POLICY, MARTA_OUTPUT_DIRS, atomic_write, dependency_files, file_hash
from .generate import generate_spec_for_method

POLICY = "native-project-workspace-v1"


ENVIRONMENT_KEYS = ("PATH", "MARTA_RUBY_BIN", "MARTA_RSPEC_BIN", "MARTA_RUBY_ENV",
                    "GEM_HOME", "GEM_PATH", "BUNDLE_GEMFILE", "BUNDLE_APP_CONFIG", "RUBYOPT", "RUBYLIB")


def relocate_environment(env, original, destination):
    """Remap repository-local paths; installed runtimes remain external."""
    original, destination = Path(original).resolve(), Path(destination).resolve()
    result = dict(env)
    def remap(value):
        path = Path(value)
        if not path.is_absolute():
            return value
        path = path.resolve()
        return str(destination / path.relative_to(original)) if path.is_relative_to(original) else str(path)
    for key in ("BUNDLE_GEMFILE", "BUNDLE_APP_CONFIG", "GEM_HOME", "MARTA_RUBY_ENV",
                "MARTA_RUBY_BIN", "MARTA_RSPEC_BIN"):
        if result.get(key):
            result[key] = remap(result[key])
    for key in ("PATH", "GEM_PATH", "RUBYLIB"):
        if key in result:
            result[key] = os.pathsep.join(remap(p) for p in result[key].split(os.pathsep))
    if str(original) in result.get("RUBYOPT", ""):
        raise ValueError("RUBYOPT references the original project; supply a relocatable environment")
    return result


class GenerationWorkspace:
    def __init__(self, project, recorder=None):
        if type(project.backend) is not RubyBackend:
            raise ValueError("Execution isolation supports the native RubyBackend only; custom/benchmark backends need their own workspace protocol")
        self.project = project
        self.recorder = recorder or project._recorder()
        self.original = Path(project.root_dir).resolve()
        self.output = Path(project.out_root()).resolve()
        self.temp = self.root = self.backend = None
        self.inputs = {Path(p).resolve(): file_hash(p) for p in
                       set(project.files + [str(self.original / p) for p in project.library_files or []]
                           + dependency_files(project.root_dir, output_root=self.output))}
        if any(not p.is_relative_to(self.original) for p in self.inputs):
            raise ValueError("Execution isolation requires source files inside the project")

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        if self.temp is not None:
            self.temp.cleanup()

    def ensure(self):
        if self.root is not None:
            return
        parent = Path(tempfile.gettempdir()).resolve()
        if parent == self.original or parent.is_relative_to(self.original):
            raise ValueError("Execution workspace temporary directory must be outside the project")
        started = time.monotonic()
        self.temp = tempfile.TemporaryDirectory(prefix="marta-generation-", dir=parent)
        self.root = Path(self.temp.name) / "repo"
        excluded = MARTA_OUTPUT_DIRS | {".git"}
        def ignore(directory, names):
            return [name for name in names if name == ".git" or
                    (Path(directory) == self.original and name in excluded) or
                    (self.output != self.original and Path(directory, name).resolve() == self.output)]
        # Do not follow links into another repository, installed environment or
        # source file. A relocatable, link-free input is required in this opt-in mode.
        for directory, dirs, files in os.walk(self.original, followlinks=False):
            skip = ignore(directory, dirs + files)
            dirs[:] = [name for name in dirs if name not in skip]
            for name in dirs + [n for n in files if n not in skip]:
                if Path(directory, name).is_symlink():
                    raise ValueError("Execution isolation requires a symlink-free project: " + str(Path(directory, name)))
        shutil.copytree(self.original, self.root, ignore=ignore, symlinks=True)
        if any(p.is_symlink() for p in self.root.rglob("*")):
            raise ValueError("Execution input acquired a symlink while being copied")
        self.backend = copy.copy(self.project.backend)
        env = dict(self.project._execution_environment())
        env = relocate_environment(env, self.original, self.root)
        temporary = Path(self.temp.name) / "tmp"
        temporary.mkdir()
        env.update(TMPDIR=str(temporary), TMP=str(temporary), TEMP=str(temporary))
        self.backend.bind_environment(env)
        self.backend.extra_load_paths = [self.remap(p) for p in self.project._load_path_list()]
        self.backend.requires = [self.remap(p, helper=True) for p in
                                 getattr(self.project.backend, "requires", [])]
        self.backend.coverage_requires = [self.remap(p, helper=True) for p in
                                          getattr(self.project.backend, "coverage_requires", [])]
        self.verify_inputs()
        self.recorder.evento(tipo="execution_workspace", policy=POLICY, dependency_policy=DEPENDENCY_POLICY,
                                        copies=1, seconds=time.monotonic() - started)

    def remap(self, value, *, helper=False):
        path = Path(value)
        if not path.is_absolute():
            # Require names are not paths. Reject relative escapes either way.
            if ".." in path.parts:
                raise ValueError("Execution path escapes the project: " + str(value))
            return str(value)
        path = path.resolve()
        if path.is_relative_to(self.original):
            mapped = self.root / path.relative_to(self.original)
            if mapped.exists() or not helper:
                return str(mapped)
        if helper and path.is_file():
            folder = Path(self.temp.name) / "preloads"
            folder.mkdir(exist_ok=True)
            import hashlib
            target = folder / (hashlib.sha256(str(path).encode()).hexdigest() + ".rb")
            # One small helper copy, no per-method copy if unchanged.
            if not target.exists():
                shutil.copyfile(path, target)
            return str(target)
        raise ValueError("External load paths require a relocatable environment: " + str(value))

    def verify_inputs(self):
        for path, expected in self.inputs.items():
            if not path.is_file() or file_hash(path) != expected:
                raise RuntimeError("Project input changed during isolated execution: " + str(path))
            if self.root is not None:
                copied = self.root / path.relative_to(self.original)
                if copied.is_symlink() or not copied.is_file() or file_hash(copied) != expected:
                    raise RuntimeError("Workspace input changed during execution: " + str(path.relative_to(self.original)))

    def _public_path(self, value):
        path = Path(os.path.abspath(os.path.join(self.original, value)))
        folder = self.output / "marta_specs"
        if not path.is_relative_to(folder) or path.resolve() != path:
            raise ValueError("Spec publication must stay inside the output marta_specs directory")
        return path, path.relative_to(folder)

    async def generate(self, *, publish=True, **kwargs):
        public, relative = self._public_path(kwargs["spec_path"])
        self.ensure()  # Before the first LLM request, once per invocation.
        private = self.root / "marta_specs" / relative
        arguments = dict(kwargs, cwd=str(self.root), spec_path=str(private.relative_to(self.root)),
                         backend=self.backend, load_paths=self.backend.extra_load_paths)
        arguments["extra_requires"] = [self.remap(p, helper=True) for p in kwargs.get("extra_requires") or []]
        try:
            outcome = await generate_spec_for_method(**arguments)
            if outcome.success:
                self._candidate_content(private, outcome)
                outcome.spec_path = kwargs["spec_path"]
                if publish:
                    self.publish(outcome)
            return outcome
        except BaseException:
            self.archive_candidate(kwargs["spec_path"])
            raise

    def _candidate_content(self, private, outcome):
        if private.is_symlink() or not private.is_file():
            raise RuntimeError("Validated candidate changed before publication")
        content = private.read_text()
        if content != outcome.spec_code + "\n":
            raise RuntimeError("Validated candidate changed before publication")
        return content

    def publish(self, outcome):
        public, relative = self._public_path(outcome.spec_path)
        content = self._candidate_content(self.root / "marta_specs" / relative, outcome)
        atomic_write(public, content)

    def archive_candidate(self, spec_path):
        # Evidence only; never accept a completed/interrupted private candidate.
        _, relative = self._public_path(spec_path)
        private = self.root / "marta_specs" / relative
        if private.is_file() and not private.is_symlink():
            folder = self.output / "rejected_specs"
            folder.mkdir(parents=True, exist_ok=True)
            archive = Path(tempfile.mkdtemp(prefix="execution_", dir=folder))
            shutil.copyfile(private, archive / private.name)

    def coverage(self, spec_paths):
        self.ensure()
        self.verify_inputs()
        folder = self.root / "marta_specs"
        if folder.is_symlink():
            raise RuntimeError("Workspace spec directory became a symlink")
        if folder.exists():
            shutil.rmtree(folder)
        staged, snapshots = [], []
        for spec in spec_paths:
            public, relative = self._public_path(spec)
            target = folder / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            expected = file_hash(public)
            shutil.copyfile(public, target)
            if file_hash(target) != expected:
                raise RuntimeError("Suite file changed while staging for validation")
            snapshots.append((public, target, expected))
            staged.append(str(target))
        source = Path(self.project.abs_source).resolve().relative_to(self.original)
        result = self.backend.run_coverage(str(source), staged, cwd=str(self.root))
        self.verify_inputs()
        for public, target, expected in snapshots:
            if any(p.is_symlink() or not p.is_file() or file_hash(p) != expected for p in (public, target)):
                raise RuntimeError("Suite file changed during isolated validation")
        return result
