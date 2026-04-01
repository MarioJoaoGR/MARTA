
from pathlib import Path
import os

def _is_package(path: Path) -> bool:
    """Determines if a given path is a Python package by checking if it exists and is a directory on the filesystem.

    This function uses `os.path.exists` to check for the existence of the path and ensures that the path is a directory using `path.is_dir()`. It is specifically designed to work with file system paths, making sure to account for case sensitivity on Windows systems while providing basic checks on other operating systems.

    Parameters:
        path (Path): The file path to check as a potential package location. This should be an instance of `pathlib.Path`.

    Returns:
        bool: True if the path exists and is a directory, False otherwise.

    Example:
        >>> _is_package(Path("C:\\PythonPackages\\my_package"))
        True
        >>> _is_package(Path("C:\\PythonPackages\\MyPackage"))
        False

    Note:
        This function is intended for use in environments where the file system preserves case information, such as Windows. On macOS and Linux, it will only check if the path exists and points to a directory. For other operating systems, it performs a basic existence check without considering case sensitivity.
    """
    return os.path.exists(str(path)) and path.is_dir()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.06s =============================
"""