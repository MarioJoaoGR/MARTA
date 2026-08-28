# Module: ansible.plugins.shell.powershell
import pytest
from ansible.plugins.shell import powershell

# Create an instance of ShellModule (powershell)
@pytest.fixture
def shell_module():
    return powershell.ShellModule()

def test_wrap_for_exec_powershell(shell_module):
    cmd = "Get-Process"
    wrapped_cmd = shell_module.wrap_for_exec(cmd)
    assert wrapped_cmd == '& Get-Process; exit $LASTEXITCODE'

def test_wrap_for_exec_cmd(shell_module):
    cmd = "dir"
    wrapped_cmd = shell_module.wrap_for_exec(cmd)
    assert wrapped_cmd == '& dir; exit $LASTEXITCODE'
