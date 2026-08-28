
import pytest
from ansible.plugins.shell import powershell

# Create an instance of ShellModule
@pytest.fixture(scope="module")
def shell_module():
    return powershell.ShellModule()

# Test cases for get_remote_filename method
def test_get_remote_filename_with_no_extension(shell_module):
    pathname = "C:\\path\\to\\script"
    remote_filename = shell_module.get_remote_filename(pathname)
    assert remote_filename == 'script.ps1'

def test_get_remote_filename_with_existing_extension(shell_module):
    pathname = "C:\\path\\to\\script.exe"
    remote_filename = shell_module.get_remote_filename(pathname)
    assert remote_filename == 'script.exe'

def test_get_remote_filename_with_different_extension(shell_module):
    pathname = "C:\\path\\to\\script.txt"
    remote_filename = shell_module.get_remote_filename(pathname)
    assert remote_filename == 'script.txt.ps1'

def test_get_remote_filename_with_empty_string(shell_module):
    pathname = ""
    with pytest.raises(Exception):  # Assuming the function raises an exception for empty strings
        shell_module.get_remote_filename(pathname)

def test_get_remote_filename_with_none(shell_module):
    pathname = None
    with pytest.raises(Exception):  # Assuming the function raises an exception for None values
        shell_module.get_remote_filename(pathname)
