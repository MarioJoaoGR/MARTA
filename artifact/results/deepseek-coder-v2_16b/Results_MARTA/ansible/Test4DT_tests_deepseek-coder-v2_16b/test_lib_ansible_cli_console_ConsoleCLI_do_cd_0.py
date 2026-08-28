
import pytest
from ansible.cli.console import ConsoleCLI
from unittest.mock import patch

@pytest.fixture(scope="module")
def console_cli():
    return ConsoleCLI(args={'host-pattern': 'app*.dc*'})

# Test for valid input for 'cd' command
def test_valid_input_cd_command(console_cli):
    with patch('builtins.input', return_value='cd app1.dc1'):
        console_cli.onecmd('cd app1.dc1')
        assert console_cli.cwd == 'app1.dc1'

# Test for edge case with empty input for 'cd' command
def test_edge_case_empty_input_cd_command(console_cli):
    with patch('builtins.input', return_value=''):
        console_cli.onecmd('cd')
        assert console_cli.cwd == '*'

# Test for invalid input for 'cd' command
def test_invalid_input_cd_command(console_cli):
    with patch('builtins.input', return_value='cd nonexistent*'):
        console_cli.onecmd('cd nonexistent*')
        assert "no host matched" in console_cli.stdout
