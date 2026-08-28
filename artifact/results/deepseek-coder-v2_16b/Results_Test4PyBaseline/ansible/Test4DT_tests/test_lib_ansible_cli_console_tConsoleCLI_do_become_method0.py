
import pytest
from unittest.mock import patch
from io import StringIO
from ansible.cli.console import ConsoleCLI

@pytest.fixture(autouse=True)
def setup_console():
    args = {'host-pattern': 'app*.dc*:!app01*'}
    console = ConsoleCLI(args)
    yield console
    console.do_exit('')  # Exit the console after tests are done

def test_become_method_with_arg():
    with patch('sys.stdout', new=StringIO()) as fake_output:
        console = ConsoleCLI({'host-pattern': 'dbservers'})
        console.do_become_method('sudo')
        assert console.become_method == 'sudo'
        assert "become_method changed to sudo" in fake_output.getvalue().strip()

def test_become_method_without_arg():
    with patch('sys.stdout', new=StringIO()) as fake_output:
        console = ConsoleCLI({'host-pattern': 'dbservers'})
        console.do_become_method('')
        expected_message = "Please specify a become_method, e.g. `become_method su`"
        assert expected_message in fake_output.getvalue().strip()
        assert console.become_method is None

def test_help_for_become_method():
    with patch('sys.stdout', new=StringIO()) as fake_output:
        console = ConsoleCLI({'host-pattern': 'all'})
        console.do_help('become_method')
        expected_help = """Given a become_method, set the privilege escalation method when using become"""
        assert expected_help in fake_output.getvalue().strip()
