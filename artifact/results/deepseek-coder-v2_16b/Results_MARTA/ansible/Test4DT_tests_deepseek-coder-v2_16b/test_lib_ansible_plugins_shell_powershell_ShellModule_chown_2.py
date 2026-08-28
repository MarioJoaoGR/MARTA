
import pytest
from ansible.plugins.shell.powershell import ShellModule

# Test scenario 1: Creating an instance of ShellModule and calling the chown method without raising NotImplementedError
def test_chown_not_implemented():
    shell_module = ShellModule()
    with pytest.raises(NotImplementedError) as excinfo:
        shell_module.chown(['file1', 'file2'], 'user')
    assert str(excinfo.value) == 'chown is not implemented for Powershell'
