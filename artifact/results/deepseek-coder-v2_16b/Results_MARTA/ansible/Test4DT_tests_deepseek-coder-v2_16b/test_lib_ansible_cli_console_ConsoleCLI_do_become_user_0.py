
import pytest
from ansible.cli.console import ConsoleCLI
from unittest.mock import patch

@pytest.fixture(scope="module")
def console_cli():
    return ConsoleCLI(args={'host-pattern': 'app*.dc*'})

def test_valid_input(console_cli):
    with patch('builtins.input', return_value='become_user user123'):
        with pytest.raises(SystemExit) as e:
            console_cli.onecmd('become_user user123')
        assert e.type == SystemExit
        assert console_cli.become_user == 'user123'

def test_edge_case(console_cli):
    with patch('builtins.input', return_value='become_user'):
        with pytest.raises(SystemExit) as e:
            console_cli.onecmd('become_user')
        assert e.type == SystemExit
        assert console_cli.become_user is None

def test_invalid_input(console_cli):
    with patch('builtins.input', return_value='become_user'):
        with pytest.raises(SystemExit) as e:
            console_cli.onecmd('become_user')
        assert e.type == SystemExit
        assert console_cli.become_user is None
