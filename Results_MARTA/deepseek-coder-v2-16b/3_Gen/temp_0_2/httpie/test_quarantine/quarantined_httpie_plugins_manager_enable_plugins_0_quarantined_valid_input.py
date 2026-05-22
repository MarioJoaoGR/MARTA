
import unittest.mock as mock
from pathlib import Path
from contextlib import nullcontext, ContextManager
from httpie.plugins.manager import get_site_paths, _load_directories

def enable_plugins(plugins_dir: Optional[Path]) -> ContextManager[None]:
    if plugins_dir is None:
        return nullcontext()
    else:
        with mock.patch('httpie.plugins.manager.get_site_paths') as mock_get_site_paths:
            with mock.patch('httpie.plugins.manager._load_directories') as mock_load_directories:
                # Mock the return value of get_site_paths and _load_directories
                mock_get_site_paths.return_value = ['mocked_path1', 'mocked_path2']
                mock_load_directories.return_value = nullcontext()
                
                return mock_load_directories.return_value

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_plugins_manager_enable_plugins_0_test_valid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_enable_plugins_0_test_valid_input.py:4:0: E0611: No name 'ContextManager' in module 'contextlib' (no-name-in-module)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_enable_plugins_0_test_valid_input.py:7:32: E0602: Undefined variable 'Optional' (undefined-variable)


"""