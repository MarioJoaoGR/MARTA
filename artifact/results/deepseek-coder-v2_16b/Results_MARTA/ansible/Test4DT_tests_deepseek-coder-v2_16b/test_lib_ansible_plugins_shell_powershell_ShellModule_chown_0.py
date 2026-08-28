
import pytest
from ansible.plugins.shell.powershell import ShellModule

# Test case for checking if the chown method raises NotImplementedError when called
def test_chown_method_raises_not_implemented_error():
    shell_module = ShellModule()
    with pytest.raises(NotImplementedError) as exc_info:
        shell_module.chown(['file1', 'file2'], 'user')
    assert str(exc_info.value) == 'chown is not implemented for Powershell'
