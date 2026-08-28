
# Module: ansible.cli.console
# test_console_cli.py
from ansible.cli.console import ConsoleCLI
import pytest

@pytest.fixture(scope="module")
def console_cli():
    return ConsoleCLI({'host-pattern': 'app*.dc*:!app01*'})

# Test initialization and default values
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