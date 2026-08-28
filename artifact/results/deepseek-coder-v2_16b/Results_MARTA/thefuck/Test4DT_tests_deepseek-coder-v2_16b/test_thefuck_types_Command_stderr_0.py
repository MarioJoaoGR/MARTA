
import pytest
from thefuck.types import Command

def test_valid_input():
    cmd = Command("print('Hello, World!')", "Hello, World!")
    assert cmd.script == "print('Hello, World!')"
    assert cmd.output == "Hello, World!"

def test_none_input():
    cmd = Command(None, None)
    assert cmd.script is None
    assert cmd.output is None

def test_empty_input():
    cmd = Command('', '')
    assert cmd.script == ''
    assert cmd.output == ''
