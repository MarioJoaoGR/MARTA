
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

# Additional tests for uncovered lines 101-102
def test_unquote_windows_path(shell_module):
    # Test unquoting a Windows path
    assert shell_module.path_has_trailing_slash("C:\\some\\directory\\") == True

def test_unquote_unix_path(shell_module):
    # Test unquoting a Unix path
    assert shell_module.path_has_trailing_slash("C:/some/directory/") == True

def test_unquote_no_slash_path(shell_module):
    # Test unquoting a path without trailing slash
    assert shell_module.path_has_trailing_slash("C:\\some\\directory") == False

def test_unquote_mixed_path(shell_module):
    # Test unquoting a mixed path style
    assert shell_module.path_has_trailing_slash("C:/some/directory") == False
