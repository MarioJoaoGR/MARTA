
import pytest
from ansible.cli.console import ConsoleCLI
from unittest.mock import patch
import cmd

# Test valid input scenario
def test_valid_input():
    cli = ConsoleCLI(args={'host-pattern': 'app*.dc*'})
    with patch('builtins.input', side_effect=['help', 'exit']):
        with pytest.raises(SystemExit):
            cli.cmdloop()
    assert cli.cwd == 'app*.dc*'

# Test edge case scenario
def test_edge_case():
    cli = ConsoleCLI(args={})
    with patch('builtins.input', side_effect=['help', 'exit']):
        with pytest.raises(SystemExit):
            cli.cmdloop()
    assert cli.cwd == '*'

# Test invalid input scenario
def test_invalid_input():
    cli = ConsoleCLI(args={'host-pattern': ''})
    with patch('builtins.input', side_effect=['help', 'exit']):
        with pytest.raises(SystemExit):
            cli.cmdloop()
    assert cli.cwd == '*'
