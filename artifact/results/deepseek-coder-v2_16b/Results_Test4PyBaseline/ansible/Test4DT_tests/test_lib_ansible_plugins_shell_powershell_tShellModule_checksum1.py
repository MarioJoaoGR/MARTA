
import pytest
from ansible.plugins.shell import powershell

# Create an instance of ShellModule for PowerShell
@pytest.fixture
def shell_module():
    return powershell.ShellModule()

def test_checksum_file(shell_module):
    path = "C:\\path\\to\\file"
    script = shell_module.checksum(path)
    assert isinstance(script, str), "Expected a base64-encoded string but got something else."
    # Add more assertions to validate the content of the script if necessary

def test_checksum_directory(shell_module):
    path = "D:\\directory"
    script = shell_module.checksum(path)