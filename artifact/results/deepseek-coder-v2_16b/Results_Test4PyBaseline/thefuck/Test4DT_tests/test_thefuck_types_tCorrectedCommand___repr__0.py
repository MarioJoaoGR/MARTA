# Module: thefuck.types
import pytest
from thefuck.types import CorrectedCommand

# Example 1: Basic Usage
def test_basic_usage():
    def side_effect_function(command, message):
        print(f"Executing command: {command.script} with side effect: {message}")
    
    command = CorrectedCommand("ls", side_effect_function, 1)
    assert command.script == "ls"
    assert callable(command.side_effect)
    assert command.priority == 1

# Example 2: Using Lambda for Side Effect
def test_lambda_for_side_effect():
    command = CorrectedCommand("ls", lambda command, message: print(f"Executing command: {command.script} with side effect: {message}"), 1)
    assert command.script == "ls"
    assert callable(command.side_effect)
    assert command.priority == 1

# Example 3: Using Default Side Effect Function
def test_default_side_effect():
    command = CorrectedCommand("ls", lambda command, message: print(f"Executing command: {command.script} with side effect: {message}"), 1)
    assert command.script == "ls"
    assert callable(command.side_effect)
    assert command.priority == 1

# Example 4: Changing Priority
def test_changing_priority():
    command = CorrectedCommand("ls", lambda command, message: print(f"Executing command: {command.script} with side effect: {message}"), 2)
    assert command.script == "ls"
    assert callable(command.side_effect)
    assert command.priority == 2

# Example 5: Using Built-in Functions as Side Effect
def test_builtin_function_as_side_effect():
    command = CorrectedCommand("ls", print, 1)
    assert command.script == "ls"
    assert callable(command.side_effect)
    assert command.priority == 1
