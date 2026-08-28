
import pytest
from ansible.plugins.shell import powershell

# Assuming shell_module is an instance of ShellModule
@pytest.fixture
def shell_module():
    return powershell.ShellModule()

# Test cases for _encode_script method
def test__encode_script_basic(shell_module):
    # Basic script encoding
    encoded_command = shell_module._encode_script('Get-Process')
    assert isinstance(encoded_command, str)
    assert len(encoded_command) > 0

def test__encode_script_as_list(shell_module):
    # Encoding a script and returning as a list
    encoded_command = shell_module._encode_script('Get-Process', as_list=True)
    assert isinstance(encoded_command, list)