
import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console():
    return ConsoleCLI({'host-pattern': 'app*.dc*:!app01*'})

def test_initialization(console):
    assert isinstance(console, ConsoleCLI)
    assert console.cwd == '*'
    assert console.modules is None

@patch('ansible.cli.console.cmd')
def test_cmdloop(mock_cmd):
    mock_instance = MagicMock()
    with patch.object(ConsoleCLI, '__init__', return_value=None)(mock_instance):
        ConsoleCLI({'host-pattern': 'app*.dc*:!app01*'}).cmdloop()
    assert mock_cmd.Cmd.cmdloop.called

def test_do_exit(console):
    with patch('builtins.input', return_value='exit'):
        console.onecmd('exit')