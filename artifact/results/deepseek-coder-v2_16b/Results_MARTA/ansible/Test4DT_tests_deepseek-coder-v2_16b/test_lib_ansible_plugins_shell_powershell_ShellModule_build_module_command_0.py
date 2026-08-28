
import pytest
from ansible.plugins.shell.powershell import ShellModule
import pkgutil
import shlex
from textwrap import dedent

@pytest.fixture(scope="module")
def shell_module():
    return ShellModule()

# Test valid inputs
def test_valid_inputs(shell_module):
    cmd = shell_module.build_module_command(env_string="SomeEnvVar=value", shebang="#!powershell", cmd="Write-Output 'Hello, World!'")
    assert isinstance(cmd, str)
    assert "SomeEnvVar=value" in cmd
    assert "#!powershell" in cmd
    assert "Write-Output 'Hello, World!'" in cmd

# Test edge cases
def test_edge_cases(shell_module):
    cmd = shell_module.build_module_command(env_string="SomeEnvVar=value", shebang="#!powershell", cmd="")
    assert isinstance(cmd, str)
    assert "bootstrap_wrapper" in dir(pkgutil)
    assert pkgutil.get_data("ansible.executor.powershell", "bootstrap_wrapper.ps1") is not None

# Test invalid inputs/error handling
def test_invalid_inputs(shell_module):
    with pytest.raises(TypeError):
        shell_module.build_module_command()  # Missing arguments should raise a TypeError
