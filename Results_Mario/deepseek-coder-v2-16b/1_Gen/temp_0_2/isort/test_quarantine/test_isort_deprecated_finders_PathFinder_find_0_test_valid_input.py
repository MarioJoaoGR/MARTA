
import os
import sysconfig
import glob
from pathlib import Path
import importlib.machinery
from isort.deprecated.finders import sections
from isort.config import Config

class PathFinder:
    """
    A class to find and identify the section (stdlib, thirdparty, firstparty) of a given module based on its location in various paths.

    Parameters:
        config (Config): An instance of the Config class containing configuration settings for path finding.
        path (str): The base directory from which to start searching for the module. Defaults to ".".

    Attributes:
        config (Config): Configuration object used for determining search paths and other settings.
        paths (list): A list of directories to search for the module.
        virtual_env (str | None): Path to the virtual environment if detected, otherwise None.
        virtual_env_src (str): The path to the 'src' directory within the virtual environment or an empty string if not found.
        conda_env (str | None): Path to the Conda environment if detected, otherwise None.

    Methods:
        find(module_name: str) -> str | None: Searches for and identifies the section of the given module name.
            Returns 'sections.THIRDPARTY' if found in a third-party path, 'sections.STDLIB' if found in the standard library path, 
            'sections.FIRSTPARTY' if found in the first-party paths, or None if not found.

    Examples:
        >>> pf = PathFinder(config=Config(), path=".")
        >>> pf.find("os")
        'stdlib'
        
        >>> pf = PathFinder(config=Config(), path="/path/to/project")
        >>> pf.find("numpy")
        'thirdparty'
        
        >>> pf = PathFinder(config=Config(), path="~/my_env")
        >>> pf.find("pandas")
        'firstparty'

    Note:
        The function relies on the configuration settings and paths to determine the section of the module, including handling virtual environments 
        and Conda environments if they are detected. It also supports case-insensitive path matching on Windows by normalizing paths.
    """
    def __init__(self, config: Config, path: str = ".") -> None:
        super().__init__(config)

        # restore the original import path (i.e. not the path to bin/isort)
        root_dir = os.path.abspath(path)
        src_dir = f"{root_dir}/src"
        self.paths = [root_dir, src_dir]

        # virtual env
        self.virtual_env = self.config.virtual_env or os.environ.get("VIRTUAL_ENV")
        if self.virtual_env:
            self.virtual_env = os.path.realpath(self.virtual_env)
        self.virtual_env_src = ""
        if self.virtual_env:
            self.virtual_env_src = f"{self.virtual_env}/src/"
            for venv_path in glob(f"{self.virtual_env}/lib/python*/site-packages"):
                if venv_path not in self.paths:
                    self.paths.append(venv_path)
            for nested_venv_path in glob(f"{self.virtual_env}/lib/python*/*/site-packages"):
                if nested_venv_path not in self.paths:
                    self.paths.append(nested_venv_path)
            for venv_src_path in glob(f"{self.virtual_env}/src/*"):
                if os.path.isdir(venv_src_path):
                    self.paths.append(venv_src_path)

        # conda
        self.conda_env = self.config.conda_env or os.environ.get("CONDA_PREFIX") or ""
        if self.conda_env:
            self.conda_env = os.path.realpath(self.conda_env)
            for conda_path in glob(f"{self.conda_env}/lib/python*/site-packages"):
                if conda_path not in self.paths:
                    self.paths.append(conda_path)
            for nested_conda_path in glob(f"{self.conda_env}/lib/python*/*/site-packages"):
                if nested_conda_path not in self.paths:
                    self.paths.append(nested_conda_path)

        # handle case-insensitive paths on windows
        self.stdlib_lib_prefix = os.path.normcase(sysconfig.get_paths()["stdlib"])
        if self.stdlib_lib_prefix not in self.paths:
            self.paths.append(self.stdlib_lib_prefix)

        # add system paths
        for system_path in sys.path[1:]:
            if system_path not in self.paths:
                self.paths.append(system_path)

    def find(self, module_name: str) -> str | None:
        for prefix in self.paths:
            package_path = "/".join((prefix, module_name.split(".")[0]))
            path_obj = Path(package_path).resolve()
            is_module = (
                exists_case_sensitive(package_path + ".py")
                or any(
                    exists_case_sensitive(package_path + ext_suffix)
                    for ext_suffix in importlib.machinery.EXTENSION_SUFFIXES
                )
                or exists_case_sensitive(package_path + "/__init__.py")
            )
            is_package = exists_case_sensitive(package_path) and os.path.isdir(package_path)
            if is_module or is_package:
                if (
                    "site-packages" in prefix
                    or "dist-packages" in prefix
                    or (self.virtual_env and self.virtual_env_src in prefix)
                ):
                    return sections.THIRDPARTY
                if os.path.normcase(prefix) == self.stdlib_lib_prefix:
                    return sections.STDLIB
                if self.conda_env and self.conda_env in prefix:
                    return sections.THIRDPARTY
                for src_path in self.config.src_paths:
                    if src_path in path_obj.parents and not self.config.is_skipped(path_obj):
                        return sections.FIRSTPARTY

                if os.path.normcase(prefix).startswith(self.stdlib_lib_prefix):
                    return sections.STDLIB  # pragma: no cover - edge case for one OS. Hard to test.

                return self.config.default_section
        return None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_PathFinder_find_0_test_valid_input
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_valid_input.py:8:0: E0401: Unable to import 'isort.config' (import-error)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_valid_input.py:8:0: E0611: No name 'config' in module 'isort' (no-name-in-module)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_valid_input.py:56:27: E1101: Instance of 'PathFinder' has no 'config' member (no-member)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_valid_input.py:62:29: E1102: glob is not callable (not-callable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_valid_input.py:65:36: E1102: glob is not callable (not-callable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_valid_input.py:68:33: E1102: glob is not callable (not-callable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_valid_input.py:73:25: E1101: Instance of 'PathFinder' has no 'config' member (no-member)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_valid_input.py:76:30: E1102: glob is not callable (not-callable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_valid_input.py:79:37: E1102: glob is not callable (not-callable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_valid_input.py:89:27: E0602: Undefined variable 'sys' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_valid_input.py:98:16: E0602: Undefined variable 'exists_case_sensitive' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_valid_input.py:100:20: E0602: Undefined variable 'exists_case_sensitive' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_valid_input.py:103:19: E0602: Undefined variable 'exists_case_sensitive' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_valid_input.py:105:25: E0602: Undefined variable 'exists_case_sensitive' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_valid_input.py:117:32: E1101: Instance of 'PathFinder' has no 'config' member (no-member)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_valid_input.py:118:60: E1101: Instance of 'PathFinder' has no 'config' member (no-member)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_valid_input.py:124:23: E1101: Instance of 'PathFinder' has no 'config' member (no-member)


"""