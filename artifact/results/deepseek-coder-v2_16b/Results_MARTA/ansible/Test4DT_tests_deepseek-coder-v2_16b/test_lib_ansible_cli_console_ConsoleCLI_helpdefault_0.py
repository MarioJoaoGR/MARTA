
import pytest
from ansible.cli.console import ConsoleCLI

def test_invalid_input_verbosity_command():
    console = ConsoleCLI(args=['-i', 'inventory/hosts', 'verbosity', 'abc'])
    with pytest.raises(AttributeError):
        console._ConsoleCLI__execute_command()
