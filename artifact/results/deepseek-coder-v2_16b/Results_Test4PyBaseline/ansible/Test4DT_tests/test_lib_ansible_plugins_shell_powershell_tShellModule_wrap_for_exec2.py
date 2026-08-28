
import pytest
from ansible.plugins.shell import powershell

# Create an instance of ShellModule (powershell)
@pytest.fixture
def shell_module():
    return powershell.ShellModule()

# Test case for wrapping a simple command
def test_wrap_for_exec_simple_command(shell_module):
    cmd = "Get-Date"
    wrapped_cmd = shell_module.wrap_for_exec(cmd)
    assert wrapped_cmd == '& Get-Date; exit $LASTEXITCODE'

# Test case for wrapping a command with spaces
def test_wrap_for_exec_command_with_spaces(shell_module):
    cmd = "Get-ChildItem"
    wrapped_cmd = shell_module.wrap_for_exec(cmd)
    assert wrapped_cmd == '& Get-ChildItem; exit $LASTEXITCODE'

# Test case for wrapping a command with special characters
def test_wrap_for_exec_command_with_special_chars(shell_module):
    cmd = "Get-EventLog"
    wrapped_cmd = shell_module.wrap_for_exec(cmd)