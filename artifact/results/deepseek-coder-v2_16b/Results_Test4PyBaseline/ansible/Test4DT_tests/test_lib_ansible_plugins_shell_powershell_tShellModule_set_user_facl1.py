
import pytest
from ansible.plugins.shell import powershell

# Create an instance of ShellModule
@pytest.fixture
def shell_module():
    return powershell.ShellModule()

# Test case 3: Calling set_user_facl should raise NotImplementedError
def test_set_user_facl_not_implemented(shell_module):
    paths = ['C:\\path\\to\\file1.txt']  # Single file for simplicity
    user = 'JohnDoe'
    mode = 'Read'
    
    with pytest.raises(NotImplementedError) as e:
        shell_module.set_user_facl(paths, user, mode)
    assert str(e.value) == "set_user_facl is not implemented for Powershell"
