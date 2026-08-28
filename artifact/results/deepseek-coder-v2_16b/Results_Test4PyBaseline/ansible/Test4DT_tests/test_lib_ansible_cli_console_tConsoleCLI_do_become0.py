
import pytest
from unittest.mock import patch
from io import StringIO
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console_cli():
    return ConsoleCLI({'host-pattern': 'app*.dc*:!app01*'})

def test_do_become_with_valid_arg(console_cli):
    with patch('sys.stdout', new=StringIO()) as fake_output:
        console_cli.do_become('yes')
        assert console_cli.become is True
        assert fake_output.getvalue().strip() == "become changed to True"

def test_do_become_with_invalid_arg(console_cli):
    with patch('sys.stdout', new=StringIO()) as fake_output:
        console_cli.do_become('invalid')
        assert console_cli.become is None
        assert fake_output.getvalue().strip() == "Please specify become value, e.g. `become yes`"

def test_do_become_without_arg(console_cli):
    with patch('sys.stdout', new=StringIO()) as fake_output:
        console_cli.do_become('')
        assert console_cli.become is None
        assert fake_output.getvalue().strip() == "Please specify become value, e.g. `become yes`"
