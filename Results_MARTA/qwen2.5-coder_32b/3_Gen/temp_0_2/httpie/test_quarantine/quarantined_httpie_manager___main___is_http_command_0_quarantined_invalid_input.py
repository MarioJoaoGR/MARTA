
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.__main__ import is_http_command
from httpie.environment import Environment
from typing import List, Union

@pytest.fixture
def mock_env():
    env = Environment()
    return env

@pytest.mark.parametrize("args", [
    (['get', 'http://example.com']),
    (['plugins', 'pie.dev/post'])
])
def test_is_http_command(mock_env, args):
    with patch('httpie.manager.cli.COMMANDS', ['get', 'plugins']):
        result = is_http_command(args, mock_env)
        if len(args) >= 1 and args[0] in ['get', 'plugins']:
            assert result == False
        else:
            assert result == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_manager___main___is_http_command_0_test_invalid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager___main___is_http_command_0_test_invalid_input.py:5:0: E0401: Unable to import 'httpie.environment' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager___main___is_http_command_0_test_invalid_input.py:5:0: E0611: No name 'environment' in module 'httpie' (no-name-in-module)


"""