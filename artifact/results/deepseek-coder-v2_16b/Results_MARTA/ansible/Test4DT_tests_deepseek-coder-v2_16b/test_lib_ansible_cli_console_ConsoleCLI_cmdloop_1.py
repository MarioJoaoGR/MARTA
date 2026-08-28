
import pytest
from ansible.cli.console import ConsoleCLI
from unittest.mock import patch


def test_invalid_input_error_handling():
    cli = ConsoleCLI(args={'host-pattern': 'invalid*pattern'})
    with patch('builtins.input', side_effect=['cd invalid*pattern', 'exit']):
        with pytest.raises(AttributeError):
            cli.cmdloop()