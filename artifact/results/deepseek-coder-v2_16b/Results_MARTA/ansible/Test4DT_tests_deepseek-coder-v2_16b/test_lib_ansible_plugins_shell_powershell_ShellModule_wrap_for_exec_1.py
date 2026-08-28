
import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture(scope="module")
def shell_module():
    return ShellModule()

def test_wrap_for_exec_powershell(shell_module):
    cmd = 'Get-Process'
    wrapped_cmd = shell_module.wrap_for_exec(cmd)
    assert wrapped_cmd == '& Get-Process; exit $LASTEXITCODE'

def test_wrap_for_exec_cmd(shell_module):
    cmd = 'echo Hello, World!'
    wrapped_cmd = shell_module.wrap_for_exec(cmd)
    assert wrapped_cmd == '& echo Hello, World!; exit $LASTEXITCODE'
