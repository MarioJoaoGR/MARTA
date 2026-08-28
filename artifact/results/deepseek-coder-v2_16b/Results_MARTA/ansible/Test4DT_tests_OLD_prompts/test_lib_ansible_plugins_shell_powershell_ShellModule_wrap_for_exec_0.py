
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.shell.powershell import ShellModule

# Test case for the wrap_for_exec method in PowerShell Module
def test_wrap_for_exec():
    shell_module = ShellModule()
    
    with patch('builtins.print'):  # Mocking print to avoid actual output during tests
        wrapped_cmd = shell_module.wrap_for_exec('Get-Process')
        assert wrapped_cmd == '& Get-Process; exit $LASTEXITCODE'
