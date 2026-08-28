
import pytest
from ansible.cli.console import ConsoleCLI

def test_missing_args(capsys):
    with pytest.raises(ValueError) as exc_info:
        console_cli = ConsoleCLI({})
    assert str(exc_info.value) == "A non-empty list for args is required"

def test_invalid_input(capsys):
    with pytest.raises(ValueError) as exc_info:
        console_cli = ConsoleCLI({})
    assert str(exc_info.value) == "A non-empty list for args is required"

def test_valid_input():
    console_cli = ConsoleCLI({'host-pattern': 'app*.dc*'})
    assert isinstance(console_cli, ConsoleCLI)
