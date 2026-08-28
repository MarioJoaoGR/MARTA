
import pytest
from ansible.plugins.shell import powershell
import pkgutil
import shlex
from ansible.module_utils._text import to_text

# Import the ShellModule class from the specified module
shell_module = powershell.ShellModule()

def test_build_module_command_empty_cmd():
    command = shell_module.build_module_command('env=USERPROFILE', 'powershell', '')
    assert isinstance(command, str), "Expected a base64-encoded bootstrap wrapper script"
    assert len(command) > 0, "The encoded script should not be empty"

def test_build_module_command_non_empty_cmd():
    command = shell_module.build_module_command('env=USERPROFILE', 'powershell', 'Get-Process')
    assert isinstance(command, str), "Expected a string representation of the command"