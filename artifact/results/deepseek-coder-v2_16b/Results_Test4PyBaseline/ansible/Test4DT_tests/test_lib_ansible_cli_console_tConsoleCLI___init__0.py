
# Module: ansible.cli.console
# test_console_cli.py
from ansible.cli.console import ConsoleCLI
import pytest

@pytest.fixture(scope="module")
def console_cli():
    return ConsoleCLI({'host-pattern': 'app*.dc*:!app01*'})

def test_initialization(console_cli):
    assert isinstance(console_cli, ConsoleCLI)
    assert console_cli.intro == 'Welcome to the ansible console. Type help or ? to list commands.\n'
    assert console_cli.cwd == '*'
    assert console_cli.remote_user is None
    assert console_cli.become is None
    assert console_cli.become_user is None
    assert console_cli.become_method is None
    assert console_cli.check_mode is None
    assert console_cli.diff is None
    assert console_cli.forks is None
    assert console_cli.task_timeout is None

def test_default_host_pattern(console_cli):
    # Assuming the default host pattern should be set if not provided in args
    assert console_cli.cwd == '*'

def test_custom_host_pattern(console_cli):
    cli = ConsoleCLI({'host-pattern': 'test*.group'})
    assert cli.cwd == 'test*.group'

def test_additional_configuration(console_cli):
    cli = ConsoleCLI({'host-pattern': 'app*.dc*:!app01*', 'remote_user': 'admin', 'become': True})
    assert cli.remote_user == 'admin'
    assert cli.become is True

def test_help_command(console_cli):
    with pytest.raises(SystemExit) as e:
        console_cli.onecmd('help')
    assert str(e.value) == ''

def test_exit_command(console_cli):
    with pytest.raises(SystemExit) as e:
        console_cli.onecmd('exit')
    assert str(e.value) == ''
