
import pytest
from ansible.plugins.shell.powershell import ShellModule

def test_unquote_removes_single_quotes():
    shell_module = ShellModule()
    assert shell_module._unquote("'hello world'") == "hello world"

def test_unquote_removes_double_quotes():
    shell_module = ShellModule()
    assert shell_module._unquote('"hello world"') == "hello world"

def test_unquote_handles_whitespace():
    shell_module = ShellModule()
    assert shell_module._unquote(' hello world ') == ' hello world '

def test_unquote_returns_original_if_no_quotes():
    shell_module = ShellModule()
    assert shell_module._unquote("hello world") == "hello world"

def test_unquote_handles_single_unmatched_quote():
    shell_module = ShellModule()
    assert shell_module._unquote("'hello world") == "'hello world"
