
import pytest
from unittest.mock import patch
from io import StringIO
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console():
    return ConsoleCLI({'host-pattern': 'app*.dc*:!app01*'})

def test_verbosity_with_valid_number(console):
    with patch('sys.stdout', new=StringIO()) as fake_output:
        console.do_verbosity("3")
        assert "verbosity level set to 3" in fake_output.getvalue().strip()

def test_verbosity_with_invalid_number(console):
    with patch('sys.stdout', new=StringIO()) as fake_output:
        console.do_verbosity("abc")
        assert "The verbosity must be a valid integer" in fake_output.getvalue().strip()

def test_verbosity_without_argument(console):
    with patch('sys.stdout', new=StringIO()) as fake_output:
        console.do_verbosity("")
        assert "Usage: verbosity <number>" in fake_output.getvalue().strip()
