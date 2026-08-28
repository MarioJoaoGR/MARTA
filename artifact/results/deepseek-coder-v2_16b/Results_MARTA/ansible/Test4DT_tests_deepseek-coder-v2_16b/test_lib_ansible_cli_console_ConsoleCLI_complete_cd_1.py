
import pytest
from ansible.cli.console import ConsoleCLI
from unittest.mock import patch

# Test for valid case where input has a valid pattern for 'cd' command
def test_valid_case():
    with patch('builtins.input', side_effect=['cd app*.dc*']):
        cli = ConsoleCLI(args={'host-pattern': 'app*.dc*'})
        with pytest.raises(SystemExit) as e:
            cli.cmdloop()
        assert cli.cwd == 'app*.dc*'

# Test for edge case where no specific host or group is provided for 'cd' command
def test_edge_case():
    with patch('builtins.input', side_effect=['cd']):
        cli = ConsoleCLI(args={})
        with pytest.raises(SystemExit) as e:
            cli.cmdloop()
        assert cli.cwd == '*'

# Test for invalid input that raises an error for 'cd' command
def test_invalid_input():
    with patch('builtins.input', side_effect=['cd *invalid*pattern*']):
        cli = ConsoleCLI(args={})
        with pytest.raises(SystemExit) as e:
            cli.cmdloop()
        assert 'Invalid pattern' in str(e.value)
