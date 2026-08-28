
import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console():
    return ConsoleCLI({'host-pattern': 'app*.dc*:!app01*'})

# Test case for initialization of ConsoleCLI instance
def test_initialization(console):
    assert isinstance(console, ConsoleCLI)
    assert console.intro == 'Welcome to the ansible console. Type help or ? to list commands.\n'
    assert console.groups == []
    assert console.hosts == []
    assert console.pattern is None
    assert console.variable_manager is None
    assert console.loader is None
    assert console.passwords == {}
    assert console.modules is None
    assert console.cwd == '*'
    assert console.remote_user is None
    assert console.become is None
    assert console.become_user is None
    assert console.become_method is None
    assert console.check_mode is None
    assert console.diff is None
    assert console.forks is None