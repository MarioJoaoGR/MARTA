
import unittest.mock as mock
from httpie.plugins.manager import enable_plugins
from contextlib import nullcontext
from pathlib import Path
from typing import Optional, ContextManager

def test_valid_input():
    with mock.patch('sys.path', []):  # Mock the sys.path to be an empty list initially
        plugins_dir = Path('/some/directory')
        context_manager = enable_plugins(plugins_dir)
        
        assert isinstance(context_manager, ContextManager)
        with context_manager:
            # Assert that the directory has been added to sys.path temporarily
            assert str(plugins_dir) in sys.path
            
        # After the context manager is exited, assert that the directory has been removed from sys.path
        assert str(plugins_dir) not in sys.path

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_plugins_manager_enable_plugins_2_test_valid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_enable_plugins_2_test_valid_input.py:16:39: E0602: Undefined variable 'sys' (undefined-variable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_enable_plugins_2_test_valid_input.py:19:39: E0602: Undefined variable 'sys' (undefined-variable)


"""