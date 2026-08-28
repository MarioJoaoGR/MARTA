
import pytest
from unittest.mock import patch
import sys
from io import StringIO
from ansible.cli.console import ConsoleCLI

@pytest.fixture(scope="module")
def console_cli():
    # Create an instance of ConsoleCLI with a default host pattern
    return ConsoleCLI({'host-pattern': '*'})

def test_initialization(console_cli):
    assert console_cli.cwd == '*'
    assert console_cli.intro == 'Welcome to the ansible console. Type help or ? to list commands.\n'
    assert isinstance(console_cli.passwords, dict)
    assert console_cli.modules is None

def test_do_exit(console_cli):
    with patch('sys.stdout', new=StringIO()) as fake_output:
        # Call the do_exit method
        result = console_cli.do_exit('')
        # Check if the output matches the expected message
        assert fake_output.getvalue() == '\nAnsible-console was exited.\n'
        # Check if the return value is -1, indicating exit