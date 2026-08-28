
import pytest
from unittest.mock import patch
from io import StringIO
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console_cli():
    return ConsoleCLI({'host-pattern': 'app*.dc*:!app01*'})

def test_initialization(console_cli):
    assert isinstance(console_cli, ConsoleCLI)
    assert console_cli.intro == 'Welcome to the ansible console. Type help or ? to list commands.\n'