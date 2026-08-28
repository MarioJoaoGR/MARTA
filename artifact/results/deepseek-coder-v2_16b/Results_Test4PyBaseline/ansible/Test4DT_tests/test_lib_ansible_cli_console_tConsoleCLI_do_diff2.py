
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