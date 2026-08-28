
import pytest
from ansible.cli.console import ConsoleCLI


def test_invalid_input_error_handling():
    args = {}
    with pytest.raises(ValueError) as excinfo:
        ConsoleCLI(args)
    assert str(excinfo.value) == 'A non-empty list for args is required', "Expected ValueError message"