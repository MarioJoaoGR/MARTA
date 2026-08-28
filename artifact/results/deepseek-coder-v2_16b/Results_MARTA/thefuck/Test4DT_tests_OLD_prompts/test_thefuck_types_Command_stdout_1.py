
import pytest
from unittest.mock import patch, MagicMock
from io import StringIO
from thefuck.types import Command

def test_valid_inputs():
    cmd = Command("print('Hello, World!')", "Hello, World!")
    with patch('sys.stdout', new=StringIO()) as fake_out:
        exec(cmd.script)
        assert fake_out.getvalue().strip() == cmd.output

def test_empty_inputs():
    cmd = Command('', '')
    with patch('sys.stdout', new=StringIO()) as fake_out:
        exec(cmd.script)
        assert fake_out.getvalue().strip() == cmd.output
