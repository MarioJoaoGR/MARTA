
import pytest
from ansible.cli.console import ConsoleCLI



def test_invalid_input():
    with pytest.raises(ValueError):
        cli = ConsoleCLI({})