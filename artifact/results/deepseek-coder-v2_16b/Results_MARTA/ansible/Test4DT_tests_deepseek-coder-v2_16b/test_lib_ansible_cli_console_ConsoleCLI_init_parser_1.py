
import pytest
from ansible.cli.console import ConsoleCLI


def test_invalid_input_error_handling():
    with pytest.raises(ValueError):
        invalid_instance = ConsoleCLI({})