
import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture(scope="module")
def shell_module():
    return ShellModule()

def test_path_has_trailing_slash_unix_style(shell_module):
    assert not shell_module.path_has_trailing_slash("C:/path/to/file")
    assert shell_module.path_has_trailing_slash("C:/path/to/file/")

def test_path_has_trailing_slash_windows_style(shell_module):
    assert not shell_module.path_has_trailing_slash("C:\\path\\to\\file")
    assert shell_module.path_has_trailing_slash("C:\\path\\to\\file\\")
