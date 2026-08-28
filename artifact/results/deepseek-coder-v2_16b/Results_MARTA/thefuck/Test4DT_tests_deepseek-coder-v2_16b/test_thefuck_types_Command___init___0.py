
import pytest
from thefuck.types import Command

def test_valid_initialization():
    cmd = Command("print('Hello, World!')", "Hello, World!")
    assert isinstance(cmd, Command)
    assert cmd.script == "print('Hello, World!')"
    assert cmd.output == "Hello, World!"
