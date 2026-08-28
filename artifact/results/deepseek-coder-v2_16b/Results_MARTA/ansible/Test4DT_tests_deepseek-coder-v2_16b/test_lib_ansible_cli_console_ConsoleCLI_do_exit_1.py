
import pytest
from ansible.cli.console import ConsoleCLI



def test_invalid_inputs_error_handling():
    with pytest.raises(ValueError):
        cli = ConsoleCLI({})