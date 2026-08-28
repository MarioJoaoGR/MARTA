
import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture(scope="module")
def shell_module():
    return ShellModule()

def test_ShellModule_expand_user_basic(shell_module):
    # Test expanding a path containing '~' to the user's home directory
    expanded_path = shell_module.expand_user('~\Documents\Report.txt')
    assert expanded_path == "C:\\Users\\username\\Documents\\Report.txt"  # Assuming the current user is 'username'

    # Test expanding an absolute path without expansion needed
    absolute_path = shell_module.expand_user('C:\Program Files\SomeFile.txt')
    assert absolute_path == "C:\\Program Files\\SomeFile.txt"

    # Test expanding a path without a tilde present
    unchanged_path = shell_module.expand_user('Documents\Report.txt')
    assert unchanged_path == "Documents\\Report.txt"
