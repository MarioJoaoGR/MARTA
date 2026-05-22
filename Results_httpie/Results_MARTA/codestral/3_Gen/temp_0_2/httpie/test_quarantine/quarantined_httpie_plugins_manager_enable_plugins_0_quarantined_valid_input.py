
from pathlib import Path
from contextlib import nullcontext, ContextManager
from unittest.mock import patch
import httpie.plugins.manager as manager

def enable_plugins(plugins_dir: Optional[Path]) -> ContextManager[None]:
    if plugins_dir is None:
        return nullcontext()
    else:
        with patch('httpie.plugins.manager.get_site_paths', return_value=['mocked_path']):
            return _load_directories(manager.get_site_paths(plugins_dir))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_plugins_manager_enable_plugins_0_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_enable_plugins_0_test_valid_input.py:3:0: E0611: No name 'ContextManager' in module 'contextlib' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_enable_plugins_0_test_valid_input.py:7:32: E0602: Undefined variable 'Optional' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_enable_plugins_0_test_valid_input.py:12:19: E0602: Undefined variable '_load_directories' (undefined-variable)


"""