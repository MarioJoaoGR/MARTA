
import sys
from pathlib import Path
from typing import Iterable, Iterator
import os
import unittest.mock as mock

def _load_directories(site_dirs: Iterable[Path]) -> Iterator[None]:
    """
    Dynamically adds directories from a list of Path objects to the Python path and yields control,
    then removes those directories from the Python path after yielding.

    Parameters:
        site_dirs (Iterable[Path]): An iterable containing Path objects representing directories to be added to the Python path.

    Returns:
        Iterator[None]: An iterator that does not yield any values; its purpose is to execute side effects, specifically modifying the Python path and removing the added directories after yielding control.

    Example:
        To use this function, you would call it with a list of Path objects representing the directories you want to include in the Python path temporarily. For example:
        
        ```python
        from pathlib import Path
        site_dirs = [Path('/path/to/site1'), Path('/path/to/site2')]
        for _ in _load_directories(site_dirs):
            # The function modifies the Python path and then removes it after yielding.
            pass
        ```
    """
    plugin_dirs = [os.fspath(site_dir) for site_dir in site_dirs]
    sys.path.extend(plugin_dirs)
    try:
        yield
    finally:
        for plugin_dir in plugin_dirs:
            sys.path.remove(plugin_dir)

# Test case to verify the behavior of _load_directories with an empty list
def test_empty_list():
    site_dirs = []
    with mock.patch('sys.path', [], create=True):  # Mock sys.path to be a mutable list
        original_len = len(sys.path)
        for _ in _load_directories(site_dirs):
            pass
        assert len(sys.path) == original_len, "The length of sys.path should not change when site_dirs is empty"
