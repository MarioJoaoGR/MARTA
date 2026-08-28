
import pytest
from unittest.mock import patch
from ansible.cli.console import ConsoleCLI

@pytest.fixture(scope="module")
def console_instance():
    return ConsoleCLI(args={'host-pattern': 'app*.dc*'})

def test_valid_input_cd_command(console_instance):
    with patch('builtins.input', side_effect=['cd app*.dc*']):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            console_instance.cmdloop()
            assert "Changed to host pattern 'app*.dc*'" in fake_output.getvalue().strip()

def test_edge_case_none_input():
    with patch('builtins.input', side_effect=['']):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            cli = ConsoleCLI(args={})
            cli.cmdloop()
            assert "Changed to host pattern '*'" in fake_output.getvalue().strip()

def test_invalid_input_error_handling():
    with patch('builtins.input', side_effect=['cd invalid*pattern']):
        with pytest.raises(Exception) as excinfo:
            cli = ConsoleCLI(args={})
            cli.cmdloop()
            assert "Invalid host pattern 'invalid*pattern'" in str(excinfo.value)
