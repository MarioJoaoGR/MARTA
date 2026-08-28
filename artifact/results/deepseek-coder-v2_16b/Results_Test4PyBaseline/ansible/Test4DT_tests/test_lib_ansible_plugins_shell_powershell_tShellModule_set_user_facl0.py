
import pytest
from ansible.plugins.shell import powershell

# Create an instance of ShellModule
@pytest.fixture
def shell_module():
    return powershell.ShellModule()

# Test case 1: Setting ACLs for a User on Multiple Files
def test_set_user_facl_multiple_files(shell_module):
    paths = ['C:\\path\\to\\file1.txt', 'C:\\path\\to\\file2.txt']
    user = 'JohnDoe'
    mode = 'Read'
    
    with pytest.raises(NotImplementedError) as e:
        shell_module.set_user_facl(paths, user, mode)
    assert str(e.value) == "set_user_facl is not implemented for Powershell"

# Test case 2: Setting ACLs for a User on a Single File
def test_set_user_facl_single_file(shell_module):
    path = 'C:\\path\\to\\file1.txt'
    user = 'JohnDoe'
    mode = 'Read'
    
    with pytest.raises(NotImplementedError) as e:
        shell_module.set_user_facl([path], user, mode)