
import pytest
from ansible.plugins.shell import powershell
import base64

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

# Additional tests for uncovered lines
def test__encode_script_empty_script(shell_module):
    # Encoding an empty script
    encoded_command = shell_module._encode_script('')
    assert isinstance(encoded_command, str)
    assert len(encoded_command) > 0

def test__encode_script_special_characters(shell_module):
    # Script with special characters
    script = 'Get-Process | Select-Object -ExpandProperty Name'
    encoded_command = shell_module._encode_script(script)
    assert isinstance(encoded_command, str)
    assert len(encoded_command) > 0

def test__encode_script_strict_mode(shell_module):
    # Script with strict mode enabled
    script = 'Get-Process'
    encoded_command = shell_module._encode_script(script, strict_mode=True)
    assert isinstance(encoded_command, str)
    assert len(encoded_command) > 0