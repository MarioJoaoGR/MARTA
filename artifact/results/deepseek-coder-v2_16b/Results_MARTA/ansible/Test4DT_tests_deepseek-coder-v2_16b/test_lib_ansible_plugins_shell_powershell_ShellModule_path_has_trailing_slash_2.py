
import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture(scope="module")
def shell_module():
    return ShellModule()

def test_path_has_trailing_slash_unix_style(shell_module):
    # Test path with Unix-like slash
    assert not shell_module.path_has_trailing_slash("C:/path/to/file")
    
    # Test path with Unix-like trailing slash
    assert shell_module.path_has_trailing_slash("C:/path/to/file/")

def test_path_has_trailing_slash_windows_style(shell_module):
    # Test path with Windows backslash
    assert not shell_module.path_has_trailing_slash("C:\\path\\to\\file")
    
    # Test path with Windows trailing backslash
    assert shell_module.path_has_trailing_slash("C:\\path\\to\\file\\")
