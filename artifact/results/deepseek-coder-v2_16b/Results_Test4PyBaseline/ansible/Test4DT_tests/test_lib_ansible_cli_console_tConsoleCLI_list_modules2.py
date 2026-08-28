
# Module: ansible.cli.console
# test_consolecli.py
from ansible.cli.console import ConsoleCLI
import pytest

@pytest.fixture
def console():
    args = {'host-pattern': 'app*.dc*:!app01*'}
    return ConsoleCLI(args)

def test_initialization(console):
    assert isinstance(console, ConsoleCLI)
    assert console.intro == 'Welcome to the ansible console. Type help or ? to list commands.\n'
    assert console.cwd == '*'