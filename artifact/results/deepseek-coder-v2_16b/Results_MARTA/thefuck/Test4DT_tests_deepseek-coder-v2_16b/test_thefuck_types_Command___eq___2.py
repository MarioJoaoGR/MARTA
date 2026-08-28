
import pytest
from thefuck.types import Command

def test_error_case():
    with pytest.raises(TypeError):
        Command()  # This should raise TypeError because __init__ requires at least two arguments

def test_command_initialization():
    cmd = Command("print('Hello, World!')", "Hello, World!")
    assert isinstance(cmd, Command)
    assert cmd.script == "print('Hello, World!')"
    assert cmd.output == "Hello, World!"

def test_command_equality():
    cmd1 = Command("print('Hello, World!')", "Hello, World!")
    cmd2 = Command("print('Hello, World!')", "Hello, World!")
    assert cmd1 == cmd2  # Two commands with the same script and output should be equal

def test_command_inequality():
    cmd1 = Command("print('Hello, World!')", "Hello, World!")
    cmd2 = Command("echo 'Hello, Universe!'", "Hello, Universe!")
    assert cmd1 != cmd2  # Commands with different scripts should not be equal
