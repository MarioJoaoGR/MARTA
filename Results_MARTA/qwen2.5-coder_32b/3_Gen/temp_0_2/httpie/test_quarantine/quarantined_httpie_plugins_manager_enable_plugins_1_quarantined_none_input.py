
from pathlib import Path
from contextlib import nullcontext, ContextManager
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import enable_plugins

def test_none_input():
    with patch('httpie.plugins.manager.nullcontext', return_value=MagicMock()) as mock_nullcontext:
        cm = enable_plugins(None)
        assert isinstance(cm, nullcontext), f"Expected {nullcontext}, but got {type(cm)}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_plugins_manager_enable_plugins_1_test_none_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_manager_enable_plugins_1_test_none_input.py:3:0: E0611: No name 'ContextManager' in module 'contextlib' (no-name-in-module)


"""