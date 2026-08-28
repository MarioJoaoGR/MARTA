
import pytest
from thefuck.types import Command

# Test for creating a Command object with valid script and output
def test_command_creation():
    cmd = Command("print('Hello, World!')", "Hello, World!")
    assert isinstance(cmd, Command)
    assert cmd.script == "print('Hello, World!')"
    assert cmd.output == "Hello, World!"

# Test for updating a Command object with new script and output values
def test_command_update():
    cmd = Command("print('Hello, World!')", "Hello, World!")
    updated_cmd = cmd.update(script="print('Greetings, Earth!')")
    assert isinstance(updated_cmd, Command)
    assert updated_cmd.script == "print('Greetings, Earth!')"
    assert updated_cmd.output == "Hello, World!"

# Test for updating a Command object with only new script value
def test_command_update_with_only_script():
    cmd = Command("print('Hello, World!')", "Hello, World!")
    updated_cmd = cmd.update(script="print('Greetings, Earth!')")
    assert isinstance(updated_cmd, Command)
    assert updated_cmd.script == "print('Greetings, Earth!')"
    assert updated_cmd.output == "Hello, World!"

# Test for updating a Command object with only new output value
def test_command_update_with_only_output():
    cmd = Command("print('Hello, World!')", "Hello, World!")
    updated_cmd = cmd.update(output="Greetings, Earth!")
    assert isinstance(updated_cmd, Command)
    assert updated_cmd.script == "print('Hello, World!')"
    assert updated_cmd.output == "Greetings, Earth!"

# Test for comparing two Command objects for equality
def test_command_equality():
    cmd1 = Command("print('Hello, World!')", "Hello, World!")
    cmd2 = Command("print('Hello, World!')", "Hello, World!")
    assert cmd1 == cmd2

# Test for comparing two unequal Command objects
def test_command_inequality():
    cmd1 = Command("print('Hello, World!')", "Hello, World!")
    cmd2 = Command("print('Greetings, Earth!')", "Greetings, Earth!")
    assert not (cmd1 == cmd2)
