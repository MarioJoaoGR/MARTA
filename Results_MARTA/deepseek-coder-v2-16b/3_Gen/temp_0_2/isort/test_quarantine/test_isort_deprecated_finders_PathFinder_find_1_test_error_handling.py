
import os
import sysconfig
import glob
from pathlib import Path
import importlib.machinery
from isort.deprecated.finders import sections

class PathFinder:
    """
    A class for finding and managing Python import paths, particularly useful when dealing with virtual environments or Conda environments.

    Parameters:
        config (Config): An instance of a configuration object that provides settings necessary for path discovery.
        path (str, optional): The base directory from which to start searching for additional paths. Defaults to the current working directory (".").

    Attributes:
        paths (list): A list of directories to be included in the Python import search path. This includes the root directory specified by `path`, a source subdirectory within that root, and various virtual environment or Conda environment-specific paths.
        virtual_env (str): The absolute path to the active virtual environment, if one is activated.
        virtual_env_src (str): The "src" subdirectory of the virtual environment, if it exists.
        conda_env (str): The absolute path to the Conda environment, if one is activated.

    Methods:
        None directly callable from outside the class, as all functionality is encapsulated within the `__init__` method.

    Examples:
        To use this class with a default configuration and starting directory:
            finder = PathFinder(config=my_config)
        
        To initialize with a specific path:
            finder = PathFinder(config=my_config, path="/custom/directory")

    Notes:
        This class dynamically discovers and includes paths based on the presence of active virtual environments or Conda environments. It also handles case-insensitive paths on Windows systems by normalizing them. The `paths` attribute is a list that includes the root directory specified by `path`, the "src" subdirectory within that root, any site-packages directories found in the virtual environment or Conda environment, and system paths excluding the first entry (which typically points to the current script's location).
    """
    def __init__(self, config: 'Config', path: str = ".") -> None:
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
        """Finds the section (standard library, third-party, or first-party) where a given module should be placed based on its name and location within the project's import paths.

        Parameters:
            - `module_name` (str): The name of the module to locate.

        Returns:
            - str | None: Returns the section identifier ('stdlib', 'thirdparty', or 'firstparty') where the module is located, or None if it cannot be found.

        Usage:
            This function helps in determining the appropriate import section for a given module within a Python project. It checks against configured paths and prefixes to identify whether the module belongs to the standard library, third-party libraries, or the local codebase. The results are used by other parts of the 'isort' tool to organize imports alphabetically according to their sections.
        """
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
************* Module Test4DT_tests.test_isort_deprecated_finders_PathFinder_find_1_test_error_handling
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_1_test_error_handling.py:45:27: E1101: Instance of 'PathFinder' has no 'config' member (no-member)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_1_test_error_handling.py:51:29: E1102: glob is not callable (not-callable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_1_test_error_handling.py:54:36: E1102: glob is not callable (not-callable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_1_test_error_handling.py:57:33: E1102: glob is not callable (not-callable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_1_test_error_handling.py:62:25: E1101: Instance of 'PathFinder' has no 'config' member (no-member)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_1_test_error_handling.py:65:30: E1102: glob is not callable (not-callable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_1_test_error_handling.py:68:37: E1102: glob is not callable (not-callable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_1_test_error_handling.py:78:27: E0602: Undefined variable 'sys' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_1_test_error_handling.py:98:16: E0602: Undefined variable 'exists_case_sensitive' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_1_test_error_handling.py:100:20: E0602: Undefined variable 'exists_case_sensitive' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_1_test_error_handling.py:103:19: E0602: Undefined variable 'exists_case_sensitive' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_1_test_error_handling.py:105:25: E0602: Undefined variable 'exists_case_sensitive' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_1_test_error_handling.py:117:32: E1101: Instance of 'PathFinder' has no 'config' member (no-member)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_1_test_error_handling.py:118:60: E1101: Instance of 'PathFinder' has no 'config' member (no-member)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_1_test_error_handling.py:124:23: E1101: Instance of 'PathFinder' has no 'config' member (no-member)


"""