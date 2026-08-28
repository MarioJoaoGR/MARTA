
import pytest
from ansible.plugins.shell import powershell

@pytest.fixture(scope="function")
def shell_module():
    return powershell.ShellModule()

# Test for valid input with single quotes
def test_valid_input_single_quotes(shell_module):
    value = "'hello world'"
    result = shell_module._unquote(value)
    assert result == "hello world"

# Test for valid input with double quotes
def test_valid_input_double_quotes(shell_module):
    value = '"hello world"'
    result = shell_module._unquote(value)
    assert result == "hello world"

# Test for invalid input without quotes
def test_invalid_input_no_quotes(shell_module):
    value = ' hello world '
    result = shell_module._unquote(value)
    assert result == " hello world "
