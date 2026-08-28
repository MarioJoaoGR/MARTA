
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
    command = CorrectedCommand("pwd", lambda command, message: print(f"Executing command: {command.script} with side effect: {message}"), 1)
    assert command.script == "pwd"
    assert callable(command.side_effect)
    assert command.priority == 1

# Example 3: Different Priority
def test_different_priority():
    def side_effect_function(command, message):
        print(f"Executing command: {command.script} with side effect: {message}")
    
    command = CorrectedCommand("date", side_effect_function, 2)
    assert command.script == "date"
    assert callable(command.side_effect)
    assert command.priority == 2

# Example 4: Using Built-in Functions as Side Effect
def test_builtin_functions_as_side_effect():
    command = CorrectedCommand("clear", lambda command, message: print(f"Executing command: {command.script} with side effect: {message}"), 1)
    assert command.script == "clear"
    assert callable(command.side_effect)
    assert command.priority == 1

# Example 5: Custom Side Effect Function
def test_custom_side_effect():
    def custom_side_effect(command, message):
        print(f"Custom side effect for command: {command.script} - Message: {message}")
    
    command = CorrectedCommand("echo Hello", custom_side_effect, 1)
    assert command.script == "echo Hello"
    assert callable(command.side_effect)
    assert command.priority == 1

# Test __hash__ method
def test_hash():
    def side_effect_function(command, message):
        print(f"Executing command: {command.script} with side effect: {message}")
    
    command1 = CorrectedCommand("ls", side_effect_function, 1)
    command2 = CorrectedCommand("pwd", lambda command, message: print(f"Executing command: {command.script} with side effect: {message}"), 1)
    