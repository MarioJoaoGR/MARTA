
import pytest
from thefuck.rules.sudo_command_from_user_path import _get_command_name

class Command:
    def __init__(self, command, output):
        self.command = command
        self.output = output

# Test cases for _get_command_name function

def test_basic_usage():
    command = Command("print('Hello, World!')", "sudo: print('Hello, World!'): command not found")
    result = _get_command_name(command)
    assert result == 'print(\'Hello, World!\')', f"Expected 'print(\'Hello, World!\')' but got {result}"

def test_no_match():
    command = Command("This is a normal output without sudo error", "This is a normal output without sudo error")
    result = _get_command_name(command)
    assert result is None, f"Expected None but got {result}"

def test_empty_output():
    command = Command("", "")  # Assuming an empty command object for demonstration
    result = _get_command_name(command)
    assert result is None, f"Expected None but got {result}"

def test_multiple_commands():
    command = Command("sudo: multiple: command not found", "sudo: multiple: command not found")
    result = _get_command_name(command)
    assert result == 'multiple', f"Expected 'multiple' but got {result}"

def test_special_characters():
    command = Command("sudo: command!@#: command not found", "sudo: command!@#: command not found")
    result = _get_command_name(command)
    assert result == 'command!@#', f"Expected 'command!@#' but got {result}"
