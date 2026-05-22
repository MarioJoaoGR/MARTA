
import pytest
from pathlib import Path
from contextlib import nullcontext, ContextManager
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import enable_plugins

def test_valid_input():
    with patch('sys.path', []):
        # Test when plugins_dir is None
        result = enable_plugins(None)
        assert isinstance(result, nullcontext)
    
        # Test when plugins_dir is a valid Path object
        plugins_dir = Path('/valid/directory')
        with patch('sys.path', ['/original/path']):
            result = enable_plugins(plugins_dir)
            assert isinstance(result, type(nullcontext()))  # Assuming nullcontext returns the same type as itself

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_plugins_manager_enable_plugins_1_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_enable_plugins_1_test_valid_input.py:4:0: E0611: No name 'ContextManager' in module 'contextlib' (no-name-in-module)


"""