# Module: ansible.plugins.shell.powershell
import pytest
from ansible.plugins.shell import powershell

# Import the ShellModule class from the specified module
shell_module = powershell.ShellModule()

def test_build_module_command_basic():
    command = shell_module.build_module_command('env=USERPROFILE', 'powershell', 'Get-Process')
    assert isinstance(command, str), "Expected a string representation of the command"

def test_build_module_command_empty_cmd():
    command = shell_module.build_module_command('env=USERPROFILE', 'powershell', '')
    assert isinstance(command, str), "Expected a base64-encoded bootstrap wrapper script"

def test_build_module_command_custom_shebang():
    command = shell_module.build_module_command('env=USERPROFILE', '#!powershell', 'Get-Process')
    assert isinstance(command, str), "Expected a string representation of the command with custom shebang"

def test_build_module_command_arg_path():
    command = shell_module.build_module_command('env=USERPROFILE', 'powershell', 'Get-Process', arg_path='-Name *process*')
    assert isinstance(command, str), "Expected a string representation of the command with argument path"

def test_build_module_command_empty_shebang_and_cmd():
    command = shell_module.build_module_command('env=USERPROFILE', '', '')
    assert isinstance(command, str), "Expected a base64-encoded bootstrap wrapper script for empty shebang and cmd"
