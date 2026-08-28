
import pytest
from ansible.plugins.shell.powershell import ShellModule
import os

@pytest.fixture
def shell_module():
    return ShellModule()

def test_ShellModule_get_remote_filename_basic(shell_module):
    # Test when the pathname does not have a .ps1 or .exe extension
    remote_filename = shell_module.get_remote_filename("C:\\path\\to\\script")
    assert remote_filename == 'script.ps1'

    # Test when the pathname already has a .ps1 extension
    remote_filename = shell_module.get_remote_filename("C:\\path\\to\\script.ps1")
    assert remote_filename == 'script.ps1'

    # Test when the pathname already has a .exe extension
    remote_filename = shell_module.get_remote_filename("C:\\path\\to\\script.exe")
    assert remote_filename == 'script.exe'
