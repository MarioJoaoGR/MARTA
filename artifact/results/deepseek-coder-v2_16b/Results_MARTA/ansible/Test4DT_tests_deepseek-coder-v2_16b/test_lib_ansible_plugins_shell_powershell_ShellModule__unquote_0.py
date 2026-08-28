
import pytest
from ansible.plugins.shell import powershell

@pytest.fixture(scope="module")
def shell_module():
    return powershell.ShellModule()

def test_unquote_removes_single_quotes(shell_module):
    result = shell_module._unquote("'hello world'")
    assert result == "hello world"

def test_unquote_handles_no_quotes(shell_module):
    result = shell_module._unquote('hello world')
    assert result == 'hello world'

def test_unquote_ignores_whitespace(shell_module):
    result = shell_module._unquote(' hello world ')
    assert result == ' hello world '

def test_unquote_handles_unmatched_single_quotes(shell_module):
    result = shell_module._unquote("'hello world")
    assert result == "'hello world"
