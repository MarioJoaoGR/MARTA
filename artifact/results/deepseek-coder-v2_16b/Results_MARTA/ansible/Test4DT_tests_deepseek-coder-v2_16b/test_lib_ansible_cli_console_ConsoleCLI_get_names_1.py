
import pytest
from ansible.cli.console import ConsoleCLI
from unittest.mock import patch

@pytest.fixture(scope="module")
def console_cli():
    return ConsoleCLI({'host-pattern': 'app*.dc*', 'command': None})

# Test valid input for 'cd' command
def test_valid_input_cd_pattern(console_cli):
    with patch('builtins.input', side_effect=['cd app*.dc*']):
        console_cli.cmdloop()
        assert console_cli.cwd == 'app*.dc*'

# Test edge case with no input for 'cd' command
def test_edge_case_none_input(console_cli):
    with patch('builtins.input', side_effect=['cd']):
        console_cli.cmdloop()
        assert console_cli.cwd == '*'

# Test invalid input for 'exit' command
def test_invalid_input_exit_command(console_cli):
    with patch('builtins.input', side_effect=['exit']):
        with pytest.raises(SystemExit):
            console_cli.cmdloop()
