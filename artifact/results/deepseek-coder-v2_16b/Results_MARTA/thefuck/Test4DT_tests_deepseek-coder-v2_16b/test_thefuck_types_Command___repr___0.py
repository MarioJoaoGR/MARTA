
import pytest
from thefuck.types import Command

def test_edge_case():
    with pytest.raises(TypeError):
        Command()  # This should raise a TypeError because __init__ requires at least two arguments

def test_invalid_input():
    with pytest.raises(AttributeError):
        cmd = Command("print('Hello, World!')", "Hello, World!")
        assert cmd.non_existent_attribute  # This should raise an AttributeError because the attribute does not exist

def test_valid_creation():
    cmd = Command("echo Hello, World!", "Hello, World!")
    assert cmd.script == "echo Hello, World!"
    assert cmd.output == "Hello, World!"

def test_update_command():
    cmd = Command("print('Hello, World!')", "Hello, World!")
    updated_cmd = cmd.update(script="echo Hello, World!")
    assert updated_cmd.script == "echo Hello, World!"
    assert updated_cmd.output == "Hello, World!"

def test_command_repr():
    cmd = Command("echo Hello, World!", "Hello, World!")
    assert repr(cmd) == "Command(script=echo Hello, World!, output=Hello, World!)"
