
# Module: ansible.plugins.shell.powershell
import pytest
from ansible.plugins.shell import powershell

# Create an instance of ShellModule
@pytest.fixture
def shell_module():
    return powershell.ShellModule()

# Test cases for path_has_trailing_slash method
def test_path_has_trailing_slash_windows(shell_module):
    # Test with a Windows path ending with backslash
    assert shell_module.path_has_trailing_slash("C:\\some\\directory\\") == True

def test_path_has_trailing_slash_unix(shell_module):
    # Test with a Unix path ending with forward slash
    assert shell_module.path_has_trailing_slash("C:/some/directory/") == True

def test_path_has_trailing_slash_no_slash(shell_module):
    # Test with a path without trailing slash
    assert shell_module.path_has_trailing_slash("C:\\some\\directory") == False

def test_path_has_trailing_slash_mixed(shell_module):
    # Test with a mixed path style
    assert shell_module.path_has_trailing_slash("C:/some/directory") == False

# Additional test cases for the untested lines (101-102)
def test_path_has_trailing_slash_unquote(shell_module):
    # Test with a path after unquoting it
    assert shell_module.path_has_trailing_slash("C:\\some\\directory\\") == True
    assert shell_module.path_has_trailing_slash("C:/some/directory/") == True

def test_path_has_trailing_slash_empty(shell_module):
    # Test with an empty path
    assert shell_module.path_has_trailing_slash("") == False
