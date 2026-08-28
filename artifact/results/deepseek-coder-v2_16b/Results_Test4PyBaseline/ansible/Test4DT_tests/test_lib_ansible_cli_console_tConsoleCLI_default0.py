# Module: ansible.cli.console
import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console_cli():
    args = {'host-pattern': 'app*.dc*:!app01*'}
    return ConsoleCLI(args)

def test_default_with_shell_command(console_cli):
    with patch('ansible.cli.console.display') as mock_display:
        result = console_cli.default('! yum update -y')
        assert not result, "Expected False because the command should run a shell command"
        mock_display.error.assert_called_with("Unable to build command: %s" % '! yum update -y')

def test_default_with_ansible_module(console_cli):
    with patch('ansible.cli.console.display') as mock_display:
        result = console_cli.default('command some_module_argument')
        assert not result, "Expected False because the command should run an Ansible module"
        mock_display.error.assert_called_with("Unable to build command: %s" % 'command some_module_argument')

def test_default_forceshell(console_cli):
    with patch('ansible.cli.console.display') as mock_display:
        result = console_cli.default('force_shell_command', forceshell=True)
        assert not result, "Expected False because the command should force use of the shell module"
        mock_display.error.assert_called_with("Unable to build command: %s" % 'force_shell_command')

def test_default_ignores_commented_line(console_cli):
    result = console_cli.default('# this is a commented line')
    assert not result, "Expected False because the command should be ignored"

def test_no_hosts_found(console_cli):
    with patch('ansible.cli.console.display') as mock_display:
        console_cli.cwd = None
        result = console_cli.default('command some_module_argument')
        assert not result, "Expected False because no hosts were found"
        mock_display.error.assert_called_with("No hosts found")

if __name__ == "__main__":
    pytest.main()
