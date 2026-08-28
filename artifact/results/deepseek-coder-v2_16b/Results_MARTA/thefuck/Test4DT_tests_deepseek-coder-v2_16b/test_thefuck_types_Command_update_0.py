
import pytest
from thefuck.types import Command

def test_invalid_input():
    with pytest.raises(TypeError):
        Command()  # Should raise TypeError because __init__ requires at least two arguments

def test_update_command():
    cmd = Command("echo Hello", "Hello")
    updated_cmd = cmd.update(script="echo Greetings")
    assert updated_cmd.script == "echo Greetings"  # Assert that the script has been updated correctly
    assert updated_cmd.output == "Hello"  # Ensure other fields are not modified by default
