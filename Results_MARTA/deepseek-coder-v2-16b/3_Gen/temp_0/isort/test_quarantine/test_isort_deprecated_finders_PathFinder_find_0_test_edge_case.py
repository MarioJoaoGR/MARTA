
import os
import sysconfig
import glob
from pathlib import Path
import importlib.machinery
from isort.deprecated.finders import sections

class PathFinder:
    """
    A class to find and identify the section (stdlib, thirdparty, firstparty) of a Python module based on its location in the file system.

    Parameters:
        config (Config): An instance of the Config class which contains configuration settings for path finding.
        path (str): The initial directory path from which to start searching for modules. Defaults to the current working directory (".").

    Attributes:
        config (Config): Configuration object containing various settings.
        paths (list): A list of directories to search for Python modules and packages.
        virtual_env (str | None): The path to the virtual environment, if one is active.
        virtual_env_src (str): The path within the virtual environment where Python source files are located.
        conda_env (str | None): The path to the Conda environment, if one is active.

    Methods:
        find(module_name: str) -> str | None: Searches for a module by its name and returns its section classification ('stdlib', 'thirdparty', or 'firstparty').

    Returns:
        str | None: The section of the found module, or None if the module is not found.

    Examples:
        >>> config = Config()  # Assuming Config class initialization sets up necessary configurations.
        >>> path_finder = PathFinder(config, "path/to/start")
        >>> result = path_finder.find("os")
        >>> print(result)  # Output will depend on where 'os' module is located relative to the paths in config and environment specifics.
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
************* Module Test4DT_tests.test_isort_deprecated_finders_PathFinder_find_0_test_edge_case
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_edge_case.py:37:31: E0602: Undefined variable 'Config' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_edge_case.py:46:27: E1101: Instance of 'PathFinder' has no 'config' member (no-member)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_edge_case.py:52:29: E1102: glob is not callable (not-callable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_edge_case.py:55:36: E1102: glob is not callable (not-callable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_edge_case.py:58:33: E1102: glob is not callable (not-callable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_edge_case.py:63:25: E1101: Instance of 'PathFinder' has no 'config' member (no-member)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_edge_case.py:66:30: E1102: glob is not callable (not-callable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_edge_case.py:69:37: E1102: glob is not callable (not-callable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_edge_case.py:79:27: E0602: Undefined variable 'sys' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_edge_case.py:88:16: E0602: Undefined variable 'exists_case_sensitive' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_edge_case.py:90:20: E0602: Undefined variable 'exists_case_sensitive' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_edge_case.py:93:19: E0602: Undefined variable 'exists_case_sensitive' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_edge_case.py:95:25: E0602: Undefined variable 'exists_case_sensitive' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_edge_case.py:107:32: E1101: Instance of 'PathFinder' has no 'config' member (no-member)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_edge_case.py:108:60: E1101: Instance of 'PathFinder' has no 'config' member (no-member)
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_edge_case.py:114:23: E1101: Instance of 'PathFinder' has no 'config' member (no-member)


"""