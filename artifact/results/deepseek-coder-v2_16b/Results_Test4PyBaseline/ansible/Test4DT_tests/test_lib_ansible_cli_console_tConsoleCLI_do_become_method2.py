
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
        expected_message = "become_method changed to sudo"