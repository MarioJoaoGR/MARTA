
import pytest
from pathlib import Path
import sys
import os
from unittest.mock import patch, MagicMock

def _load_directories(site_dirs: Iterable[Path]) -> Iterator[None]:
    plugin_dirs = [os.fspath(site_dir) for site_dir in site_dirs]
    sys.path.extend(plugin_dirs)
    try:
        yield
    finally:
        for plugin_dir in plugin_dirs:
            sys.path.remove(plugin_dir)

@pytest.fixture
def mock_site_dirs():
    with patch('sys.path', new=[]):
        yield []

def test_empty_list(_load_directories, mock_site_dirs):
    site_dirs = []
    loader = _load_directories(site_dirs)
    next(loader)  # Start the generator
    assert sys.path == []

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_plugins_manager__load_directories_0_test_empty_list
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager__load_directories_0_test_empty_list.py:8:33: E0602: Undefined variable 'Iterable' (undefined-variable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager__load_directories_0_test_empty_list.py:8:52: E0602: Undefined variable 'Iterator' (undefined-variable)


"""