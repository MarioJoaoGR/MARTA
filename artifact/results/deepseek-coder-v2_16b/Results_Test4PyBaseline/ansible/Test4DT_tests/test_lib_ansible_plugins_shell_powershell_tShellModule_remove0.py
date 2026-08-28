# Module: ansible.plugins.shell.powershell
import pytest
from ansible.plugins.shell import powershell

# Create an instance of ShellModule
@pytest.fixture(scope="module")
def shell_module():
    return powershell.ShellModule()

# Test cases for removing a file in PowerShell environment
@pytest.mark.parametrize("path, recurse, expected", [
    ("C:\\path\\to\\file", False, "Remove-Item 'C:\\path\\to\\file' -Force;"),
])
def test_remove_file(shell_module, path, recurse, expected):
    assert shell_module.remove(path, recurse) == expected

# Test cases for removing a directory in PowerShell environment
@pytest.mark.parametrize("path, recurse, expected", [
    ("C:\\path\\to\\directory", True, "Remove-Item 'C:\\path\\to\\directory' -Force -Recurse;"),
])
def test_remove_directory(shell_module, path, recurse, expected):
    assert shell_module.remove(path, recurse) == expected
