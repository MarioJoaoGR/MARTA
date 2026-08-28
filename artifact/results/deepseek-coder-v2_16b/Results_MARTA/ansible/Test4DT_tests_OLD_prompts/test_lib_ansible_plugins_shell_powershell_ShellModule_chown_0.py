
import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_chown_not_implemented(shell_module):
    with pytest.raises(NotImplementedError) as excinfo:
        shell_module.chown(['file1', 'file2'], 'user')
    assert str(excinfo.value) == 'chown is not implemented for Powershell'
