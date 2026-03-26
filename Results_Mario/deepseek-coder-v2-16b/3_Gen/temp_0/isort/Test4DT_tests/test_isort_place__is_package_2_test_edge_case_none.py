
import pytest
from pathlib import Path

def exists_case_sensitive(p):
    return True if str(p).endswith('package') else False

def _is_package(path: Path) -> bool:
    """Determines if a given path is a package by checking if the path exists and is a directory on Windows, considering case sensitivity, or if it exists on any operating system.

    Parameters:
        path (Path): The file system path to check for existence and whether it's a directory. It should be an instance of Path representing the full path to the file or directory you want to verify.

    Returns:
        bool: True if the path exists as a directory on Windows, considering case sensitivity, or if it exists on any operating system; False otherwise.

    Examples:
        >>> _is_package(Path("C:\\path\\to\\package"))
        True
        >>> _is_package(Path("C:\\path\\to\\Package"))
        False
        >>> _is_package(Path("/usr/local/lib/python/package"))
        True
    """
    return exists_case_sensitive(str(path)) and path.is_dir()

def test_edge_case_none():
    assert not _is_package(None)
