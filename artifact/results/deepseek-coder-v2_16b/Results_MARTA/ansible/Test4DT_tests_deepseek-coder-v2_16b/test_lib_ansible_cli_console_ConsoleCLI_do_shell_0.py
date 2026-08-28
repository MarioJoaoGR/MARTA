
import pytest
from unittest.mock import patch
from ansible.cli.console import ConsoleCLI



def test_invalid_input_verbosity_command():
    with pytest.raises(ValueError):
        ConsoleCLI({})