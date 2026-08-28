
import pytest
from ansible.plugins.shell.powershell import ShellModule

def test_env_prefix():
    powershell = ShellModule()
    result = powershell.env_prefix()
    assert result == ""
