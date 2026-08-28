
import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.console import ConsoleCLI

@pytest.fixture(scope="module")
def console_instance():
    return ConsoleCLI(args={'host-pattern': 'app_servers'})

def test_valid_input_cd_list(console_instance):
    with patch('builtins.input', side_effect=['cd app*.dc*', 'list']):
        with patch('sys.stdout', new=MagicMock()) as mock_stdout:
            console_instance.cmdloop()
            assert "app*.dc*" in str(mock_stdout.write.call_args[0][0])

def test_edge_case_none_input():
    with patch('builtins.input', return_value=None):
        with pytest.raises(SystemExit) as e:
            cli = ConsoleCLI({})
            cli.cmdloop()
        assert e.type == SystemExit
        assert str(e.value) == '0'

def test_invalid_input_exit_command(console_instance):
    with patch('builtins.input', return_value='exit'):
        with pytest.raises(SystemExit) as e:
            console_instance.cmdloop()
        assert e.type == SystemExit
        assert str(e.value) == '0'
