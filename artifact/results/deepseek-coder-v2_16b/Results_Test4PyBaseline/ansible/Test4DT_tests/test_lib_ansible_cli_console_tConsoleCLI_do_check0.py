
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

def test_check_with_valid_argument(setup_console):
    console = setup_console
    console.do_check('yes')
    assert console.check_mode is True
    captured_output = console.stdout.getvalue().strip()
    assert captured_output == "check mode changed to True"

def test_check_with_invalid_argument(setup_console):
    console = setup_console
    with pytest.raises(ValueError) as excinfo:
        console.do_check('invalid')
    assert str(excinfo.value) == "Invalid value for check mode: invalid"
    captured_output = console.stdout.getvalue().strip()
    assert captured_output == "Please specify check mode value, e.g. `check yes`"

def test_check_without_argument(setup_console):
    console = setup_console
    with pytest.raises(ValueError) as excinfo:
        console.do_check('')
    assert str(excinfo.value) == "Please specify check mode value, e.g. `check yes`"
    captured_output = console.stdout.getvalue().strip()
    assert captured_output == "Please specify check mode value, e.g. `check yes`"
