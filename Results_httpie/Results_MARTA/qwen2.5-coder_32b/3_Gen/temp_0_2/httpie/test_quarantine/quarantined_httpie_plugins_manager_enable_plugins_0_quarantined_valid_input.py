
import pytest
from pathlib import Path
from contextlib import nullcontext
from httpie.plugins.manager import enable_plugins
from unittest.mock import patch, MagicMock

def test_enable_plugins_with_valid_directory():
    with patch('httpie.plugins.manager._load_directories') as mock_load_directories:
        plugins_dir = Path('/some/valid/directory')
        enable_plugins(plugins_dir)
        assert mock_load_directories.called
        args, _ = mock_load_directories.call_args
        assert args[0] == get_site_paths(plugins_dir)

def test_enable_plugins_without_directory():
    with patch('httpie.plugins.manager._load_directories') as mock_load_directories:
        enable_plugins(None)
        assert not mock_load_directories.called

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_plugins_manager_enable_plugins_0_test_valid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_manager_enable_plugins_0_test_valid_input.py:14:26: E0602: Undefined variable 'get_site_paths' (undefined-variable)


"""