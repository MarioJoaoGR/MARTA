
import pytest
from pathlib import Path
import sys
import os
from typing import Iterable, Iterator

# Assuming _load_directories function definition and necessary imports are provided as per the prompt
def _load_directories(site_dirs: Iterable[Path]) -> Iterator[None]:
    plugin_dirs = [
        os.fspath(site_dir)
        for site_dir in site_dirs
    ]
    sys.path.extend(plugin_dirs)
    try:
        yield
    finally:
        for plugin_dir in plugin_dirs:
            sys.path.remove(plugin_dir)

# Test function to test the behavior with an empty list of directories
def test_empty_list():
    site_dirs = []
    with pytest.raises(StopIteration):  # Since _load_directories is a generator, it should raise StopIteration when done
        for _ in _load_directories(site_dirs):
            pass
    
    # Check if sys.path has been modified correctly
    assert len(sys.path) == original_len, f"Expected length of sys.path to be {original_len}, but got {len(sys.path)}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_plugins_manager__load_directories_0_test_empty_list
httpie/Test4DT_tests_codestral/test_httpie_plugins_manager__load_directories_0_test_empty_list.py:29:28: E0602: Undefined variable 'original_len' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_plugins_manager__load_directories_0_test_empty_list.py:29:79: E0602: Undefined variable 'original_len' (undefined-variable)


"""