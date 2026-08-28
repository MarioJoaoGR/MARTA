
import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture(scope="module")
def powershell_module():
    return ShellModule()

def test_env_prefix(powershell_module):
    result = powershell_module.env_prefix()
    assert result == ""
