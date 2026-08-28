
# Module: ansible.cli.console
import pytest
from unittest.mock import patch, MagicMock
from io import StringIO
import cmd

# Import the ConsoleCLI class from its module
from ansible.cli.console import ConsoleCLI

def test_do_diff_with_valid_arg():
    cli = ConsoleCLI({'host-pattern': 'app*.dc*:!app01*'})
    with patch('sys.stdout', new=StringIO()) as fake_output:
        cli.do_diff('yes')
        assert cli.diff is True
        assert fake_output.getvalue().strip() == "diff mode changed to True"

def test_do_diff_without_arg():
    cli = ConsoleCLI({'host-pattern': 'app*.dc*:!app01*'})
    with patch('sys.stdout', new=StringIO()) as fake_output:
        cli.do_diff('')
        assert fake_output.getvalue().strip() == "Please specify a diff value , e.g. `diff yes`"
        # The default value should not change if no argument is provided
        assert cli.diff is None

def test_do_diff_with_invalid_arg():
    cli = ConsoleCLI({'host-pattern': 'app*.dc*:!app01*'})
    with patch('sys.stdout', new=StringIO()) as fake_output:
        cli.do_diff('invalid')
        assert fake_output.getvalue().strip() == "Please specify a diff value , e.g. `diff yes`"
        # The default value should not change if an invalid argument is provided
        assert cli.diff is None

def test_do_diff_toggle():
    cli = ConsoleCLI({'host-pattern': 'app*.dc*:!app01*'})
    with patch('sys.stdout', new=StringIO()) as fake_output:
        # Initial state should be None (default)
        assert cli.diff is None
        
        # Toggle to True
        cli.do_diff('yes')
        assert cli.diff is True
        
        # Toggle back to False
        cli.do_diff('no')
        assert cli.diff is False

if __name__ == '__main__':
    pytest.main()
