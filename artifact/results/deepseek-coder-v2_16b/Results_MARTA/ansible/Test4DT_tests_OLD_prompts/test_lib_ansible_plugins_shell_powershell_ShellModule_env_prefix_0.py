
import pytest
from ansible.plugins.shell.powershell import ShellModule
from unittest.mock import patch, MagicMock

def test_env_prefix():
    powershell = ShellModule()
    result = powershell.env_prefix()
    assert result == ""
