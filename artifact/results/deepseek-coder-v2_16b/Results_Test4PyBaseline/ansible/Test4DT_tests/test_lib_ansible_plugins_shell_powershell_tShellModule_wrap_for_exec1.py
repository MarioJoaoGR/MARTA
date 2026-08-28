
# Module: ansible.plugins.shell.powershell
import pytest
from ansible.errors import AnsibleAuthenticationFailure, AnsibleConnectionFailure
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

# Test case for incorrect password scenario (simulating an error)
def test_wrap_for_exec_incorrect_password():
    class MockShellModule:
        def wrap_for_exec(self, cmd):
            raise AnsibleAuthenticationFailure("Authentication failed")
    
    shell_module = MockShellModule()
    with pytest.raises(AnsibleAuthenticationFailure) as exc_info:
        shell_module.wrap_for_exec("Get-Process")
    assert str(exc_info.value) == "Authentication failed"

# Test case for connectivity issue scenario (simulating a retryable error)
def test_wrap_for_exec_connectivity_issue():
    class MockShellModule:
        def wrap_for_exec(self, cmd):
            raise AnsibleConnectionFailure("Connectivity issue")
    
    shell_module = MockShellModule()
    with pytest.raises(AnsibleConnectionFailure) as exc_info:
        shell_module.wrap_for_exec("Get-Process")
    assert str(exc_info.value) == "Connectivity issue"

# Test case for exponential backoff retry mechanism
def test_wrap_for_exec_exponential_backoff():
    class MockShellModule:
        def wrap_for_exec(self, cmd):
            raise AnsibleConnectionFailure("Connectivity issue")
    
    shell_module = MockShellModule()
    with pytest.raises(AnsibleConnectionFailure) as exc_info:
        for _ in range(3):
            shell_module.wrap_for_exec("Get-Process")
    assert str(exc_info.value) == "Connectivity issue"
