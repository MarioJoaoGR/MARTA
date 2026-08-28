
import pytest
from ansible.plugins.shell.powershell import ShellModule

# Test that checks if ShellModule raises NotImplementedError when calling chmod method
def test_chmod_method():
    shell = ShellModule()
    with pytest.raises(NotImplementedError) as excinfo:
        shell.chmod(['test_file'], '755')
    assert str(excinfo.value) == 'chmod is not implemented for Powershell'
