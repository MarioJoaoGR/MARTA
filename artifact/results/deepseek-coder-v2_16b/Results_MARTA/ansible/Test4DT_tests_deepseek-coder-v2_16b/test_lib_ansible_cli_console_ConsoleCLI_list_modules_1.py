
import pytest
from ansible.cli.console import ConsoleCLI
from unittest.mock import patch, MagicMock

@pytest.fixture(autouse=True)
def setup_console():
    console = ConsoleCLI({})
    yield console

def test_valid_input(setup_console):
    with patch('ansible.cli.console.context', {'CLIARGS': {'module_path': ['test']}}):
        assert set(['mod1', 'mod2']) == setup_console.list_modules()

def test_edge_case():
    console = ConsoleCLI({})
    with patch('ansible.cli.console.context', {'CLIARGS': {'module_path': None}}):
        assert set() == console.list_modules()

def test_invalid_input(setup_console):
    with pytest.raises(TypeError):
        setup_console.list_modules('invalid')
