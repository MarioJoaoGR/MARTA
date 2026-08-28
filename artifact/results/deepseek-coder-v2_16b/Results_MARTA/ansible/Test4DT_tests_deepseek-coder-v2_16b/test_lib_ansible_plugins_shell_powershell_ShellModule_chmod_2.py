
import pytest
from ansible.plugins.shell.powershell import ShellModule

# Test that checks if the ShellModule class is imported correctly
def test_shell_module_import():
    from ansible.plugins.shell.powershell import ShellModule
    assert ShellModule is not None, "ShellModule should be imported successfully"

# Test that ensures chmod method raises NotImplementedError for PowerShell
@pytest.mark.xfail(reason="chmod method is not implemented for Powershell")
def test_chmod_not_implemented():
    shell = ShellModule()
    with pytest.raises(NotImplementedError) as excinfo:
        shell.chmod(['file1', 'file2'], 755)
    assert "chmod is not implemented for Powershell" in str(excinfo.value), \
           "Expected NotImplementedError for chmod method when using PowerShell"
