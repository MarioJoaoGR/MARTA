
import pytest
from unittest.mock import patch
from io import StringIO
from ansible.cli.console import ConsoleCLI

@pytest.fixture(autouse=True)
def setup_console():
    args = {'host-pattern': 'all'}
    console = ConsoleCLI(args)
    console.stdout = StringIO()
    yield console
    # Teardown code, if needed

# Test case for toggling check mode with a valid argument
def test_do_check_with_valid_argument(setup_console):
    console = setup_console
    console.do_check('yes')
    assert console.check_mode is True
    captured_output = console.stdout.getvalue().strip()