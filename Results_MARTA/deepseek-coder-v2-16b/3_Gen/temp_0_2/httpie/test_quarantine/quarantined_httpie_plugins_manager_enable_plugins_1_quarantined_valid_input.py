
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from contextlib import nullcontext
from httpie.plugins.manager import enable_plugins

def test_valid_input():
    with patch('httpie.plugins.manager.get_site_paths') as mock_get_site_paths:
        mock_get_site_paths.return_value = ['/mocked/path1', '/mocked/path2']
        
        context_manager = enable_plugins(Path('/valid/directory'))
        
        assert isinstance(context_manager, type(nullcontext()))
        
        with patch('sys.path', []):  # Mock sys.path to check if paths are added temporarily
            with context_manager:
                from httpie.plugins.manager import _load_directories
                mock_get_site_paths.assert_called_once_with(Path('/valid/directory'))
                assert '/mocked/path1' in sys.path
                assert '/mocked/path2' in sys.path
        
        # Check if paths are removed after context manager is exited
        with patch('sys.path', ['other_path']):
            from httpie.plugins.manager import _load_directories
            assert '/mocked/path1' not in sys.path
            assert '/mocked/path2' not in sys.path

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_plugins_manager_enable_plugins_1_test_valid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_enable_plugins_1_test_valid_input.py:20:42: E0602: Undefined variable 'sys' (undefined-variable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_enable_plugins_1_test_valid_input.py:21:42: E0602: Undefined variable 'sys' (undefined-variable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_enable_plugins_1_test_valid_input.py:26:42: E0602: Undefined variable 'sys' (undefined-variable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_enable_plugins_1_test_valid_input.py:27:42: E0602: Undefined variable 'sys' (undefined-variable)


"""