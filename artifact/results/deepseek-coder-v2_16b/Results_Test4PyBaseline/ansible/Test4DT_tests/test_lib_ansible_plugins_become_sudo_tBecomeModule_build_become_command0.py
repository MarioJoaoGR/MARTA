# Module: ansible.plugins.become.sudo
import pytest
from ansible.plugins.become.sudo import BecomeModule

# Test cases for build_become_command method
def test_build_become_command_with_command():
    become_module = BecomeModule()
    command = "ls -l"
    is_shell = False
    result = become_module.build_become_command(cmd=command, shell=is_shell)
    assert result == 'sudo ls -l'

def test_build_become_command_without_command():
    become_module = BecomeModule()
    command = None
    is_shell = False
    result = become_module.build_become_command(cmd=command, shell=is_shell)
    assert result == None

def test_build_become_command_with_custom_flags():
    become_module = BecomeModule()
    command = "ls -l"
    is_shell = False
    flags = "-n"
    become_module.set_option('become_flags', flags)
    result = become_module.build_become_command(cmd=command, shell=is_shell)
    assert result == 'sudo ls -l'  # The '-n' flag should be ignored for backward compatibility

def test_build_become_command_with_password():
    become_module = BecomeModule()
    command = "ls -l"
    is_shell = False
    password = "test_password"
    become_module.set_option('become_pass', password)
    result = become_module.build_become_command(cmd=command, shell=is_shell)
    assert result == f'sudo ls -l -p "[sudo via ansible, key=%s] password:"' % (become_module._id)

def test_build_become_command_with_user():
    become_module = BecomeModule()
    command = "ls -l"
    is_shell = False
    user = "test_user"
    become_module.set_option('become_user', user)
    result = become_module.build_become_command(cmd=command, shell=is_shell)
    assert result == f'sudo ls -l -u {user}'

# Additional test cases for edge cases and potential failures
def test_build_become_command_without_password():
    become_module = BecomeModule()
    command = "ls -l"
    is_shell = False
    result = become_module.build_become_command(cmd=command, shell=is_shell)
    assert result == 'sudo ls -l'  # No password should be added if not set

def test_build_become_command_with_empty_flags():
    become_module = BecomeModule()
    command = "ls -l"
    is_shell = False
    flags = ""
    become_module.set_option('become_flags', flags)
    result = become_module.build_become_command(cmd=command, shell=is_shell)
    assert result == 'sudo ls -l'  # Empty flags should not affect the command
