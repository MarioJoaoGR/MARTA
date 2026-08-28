
import pytest
from ansible.plugins.shell.powershell import ShellModule
import ntpath

@pytest.fixture(scope="module")
def shell_module():
    return ShellModule()

# Test valid input
def test_valid_input(shell_module):
    path = shell_module.join_path('c:', 'windows', 'system32')
    assert path == 'c:\\windows\\system32'

# Test edge cases including None and empty list
@pytest.mark.parametrize("args", [None, []])
def test_edge_case(shell_module, args):
    with pytest.raises(TypeError):
        shell_module.join_path(*args)

# Test invalid inputs to ensure error handling is in place
@pytest.mark.parametrize("args", ["invalid", 123])
def test_invalid_input(shell_module, args):
    with pytest.raises(TypeError):
        shell_module.join_path(*args)
