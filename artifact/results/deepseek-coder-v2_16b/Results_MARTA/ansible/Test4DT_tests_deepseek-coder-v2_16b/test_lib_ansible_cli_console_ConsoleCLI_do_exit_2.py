
import pytest
from ansible.cli.console import ConsoleCLI
import cmd
import sys

@pytest.fixture(scope="module")
def console_cli():
    return ConsoleCLI({})

def test_valid_input_happy_path(console_cli):
    with pytest.raises(SystemExit) as e:
        console_cli.onecmd("cd app*.dc*:!app01*")
        assert console_cli.cwd == "app*.dc*:!app01*"
    assert str(e.value) == "-1"

def test_edge_cases(console_cli):
    with pytest.raises(SystemExit) as e:
        console_cli.onecmd("cd")  # Empty pattern should trigger edge case
        assert console_cli.cwd is None
    assert str(e.value) == "-1"

def test_invalid_inputs_error_handling(console_cli):
    with pytest.raises(SystemExit) as e:
        console_cli.onecmd("invalid_command")  # Invalid command should trigger error handling
    assert str(e.value) == "-1"
