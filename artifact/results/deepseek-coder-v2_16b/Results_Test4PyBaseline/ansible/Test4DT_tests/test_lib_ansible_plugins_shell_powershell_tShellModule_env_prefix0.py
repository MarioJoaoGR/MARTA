# Module: ansible.plugins.shell.powershell
import pytest
from ansible.plugins.shell import powershell

# Fixture to create an instance of ShellModule for PowerShell
@pytest.fixture(scope="module")
def shell_module():
    return powershell.ShellModule()

# Test case for the env_prefix method with no parameters
def test_env_prefix_powershell(shell_module):
    assert shell_module.env_prefix() == ""
