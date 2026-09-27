"""MARTA feedback in the XRepoTest Ruby/Bundler environment.

Final reported metrics come from the upstream evaluator with documented fixes.
Generated code is exercised at its eventual spec/temp_spec.rb location.
"""
from pathlib import Path

from marta.ruby_backend.backend import RubyBackend
from marta.ruby_backend import coverage_runner, runner
from marta.ruby_backend.project import RubyProject


def joined_specs(paths) -> str:
    # Each round adds examples to a single final suite, not another sample.
    return "\n\n".join(Path(p).read_text() for p in paths if Path(p).is_file())


class XRepoBackend(RubyBackend):
    def _package_root(self, cwd):
        # Match the official evaluator's nearest-Gemfile rule, including ROM's
        # core/, repository/ and changeset/ subprojects.
        focal = getattr(self, "focal_source_rel", None)
        if focal:
            root = Path(cwd).resolve()
            current = (root / focal).parent
            while current == root or root in current.parents:
                if (current / "Gemfile").is_file():
                    return str(current)
                current = current.parent
        return cwd

    @staticmethod
    def _stage(paths, cwd):
        spec = Path(cwd) / "spec/temp_spec.rb"
        spec.parent.mkdir(parents=True, exist_ok=True)
        spec.write_text(joined_specs(paths))
        return str(spec)

    def run_tests(self, test_path, load_paths, cwd, requires_extra=None):
        if requires_extra or getattr(self, "requires", None):
            raise ValueError("XRepoTest requires must be in exported test code, not hidden preloads")
        path = Path(test_path)
        if not path.is_absolute():
            path = Path(cwd) / path
        package = self._package_root(cwd)
        staged = self._stage([path], package)
        result = runner.run_rspec(staged, cwd=package, use_bundle=True,
                                 isolated=False, use_guard=False)
        result.all_passed = result.all_passed and any(e.status == "passed" for e in result.examples)
        return result

    def run_coverage(self, source_dir, test_paths, cwd):
        paths = [Path(p) if Path(p).is_absolute() else Path(cwd) / p for p in test_paths]
        package = self._package_root(cwd)
        staged = self._stage(paths, package)
        return coverage_runner.run_line_coverage(source_dir, [staged], cwd=package,
                                                isolated=False, use_bundle=True)


class XRepoProject(RubyProject):
    def _example_passing_spec(self, target):
        # No information from previously generated benchmark answers enters
        # another task's prompt. Production-code summaries remain available.
        return None
