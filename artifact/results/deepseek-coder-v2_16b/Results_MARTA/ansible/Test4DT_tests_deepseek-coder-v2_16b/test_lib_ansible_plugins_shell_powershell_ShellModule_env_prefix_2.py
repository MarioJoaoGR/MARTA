
import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture(scope="module")
def shell_module():
    return ShellModule()

def test_env_prefix_returns_empty_string(shell_module):
    result = shell_module.env_prefix()
    assert result == ""
