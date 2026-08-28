
import pytest
from unittest.mock import patch
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture(scope="function")
def shell_module():
    return ShellModule()

def test_ShellModule__unquote_basic(shell_module):
    # Test basic functionality with a string wrapped in single quotes
    result = shell_module._unquote("'hello world'")
    assert result == "hello world"

    # Test basic functionality with a string wrapped in double quotes
    result = shell_module._unquote('"hello world"')
    assert result == "hello world"

    # Test basic functionality with a string without quotes and leading/trailing whitespace
    result = shell_module._unquote(' hello world ')
    assert result == ' hello world '

    # Test basic functionality with an unmatched single quote at the end
    result = shell_module._unquote("'hello world")
    assert result == "'hello world"
