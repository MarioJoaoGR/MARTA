
import pytest
from ansible.cli.console import ConsoleCLI
from unittest.mock import patch

@pytest.fixture(scope="module")
def console_cli():
    return ConsoleCLI({'host-pattern': 'app*.dc*'})

# Test the 'cd' command with a valid host pattern
def test_valid_input_cd_command(console_cli):
    with patch('builtins.input', return_value='cd app*.dc*'):
        console_cli.cmdloop()
        assert console_cli.cwd == 'app*.dc*'

# Test the behavior when no input is provided to the 'cd' command
def test_edge_case_none_input(console_cli):
    with patch('builtins.input', return_value=''):
        with pytest.raises(EOFError):
            console_cli.cmdloop()

# Test handling invalid inputs for the 'cd' command
def test_invalid_input_error_handling(console_cli):
    with patch('builtins.input', return_value='cd invalid*pattern'):
        with pytest.raises(SystemExit):
            console_cli.cmdloop()
