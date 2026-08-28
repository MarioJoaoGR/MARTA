
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

# Example 2: Using a Different Script and Side Effect Function
def test_different_script_and_side_effect():
    def custom_side_effect(command, message):
        print(f"Custom side effect for command '{command.script}': {message}")
    
    command = CorrectedCommand("pwd", custom_side_effect, 2)
    assert command.script == "pwd"
    assert callable(command.side_effect)
    assert command.priority == 2

# Example 3: Using a Lambda for Side Effect Function
def test_lambda_for_side_effect():
    command = CorrectedCommand("date", lambda command, message: print(f"The current date is: {message}"), 1)
    assert command.script == "date"
    assert callable(command.side_effect)
    assert command.priority == 1

# Example 4: Comparing Two Commands
def test_comparing_commands():
    def side_effect_function(command, message):
        print(f"Executing command: {command.script} with side effect: {message}")
    
    cmd1 = CorrectedCommand("echo Hello", side_effect_function, 1)
    cmd2 = CorrectedCommand("echo Hi", side_effect_function, 2)
    
    assert not (cmd1 == cmd2)
    
    cmd3 = CorrectedCommand("echo Hello", side_effect_function, 1)
    assert cmd1 == cmd3

# Additional Test for Equality Method
def test_equality_method():
    def side_effect_function(command, message):
        print(f"Executing command: {command.script} with side effect: {message}")
    
    # Create two instances with the same script and side effect but different priorities
    cmd1 = CorrectedCommand("echo Hello", side_effect_function, 1)
    cmd2 = CorrectedCommand("echo Hello", side_effect_function, 2)
    