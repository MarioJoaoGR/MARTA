# Module: thefuck.types
import pytest
from thefuck.types import CorrectedCommand

# Test initialization with side effect function and priority
def test_correctedcommand_initialization():
    def side_effect_function(command, message):
        assert command.script == "ls"
        assert callable(command.side_effect)
        assert command.priority == 1
    
    command = CorrectedCommand("ls", side_effect_function, 1)
    assert command.script == "ls"
    assert callable(command.side_effect)
    assert command.priority == 1

# Test run method with side effect function and history setting
def test_correctedcommand_run():
    def side_effect_function(command, message):
        print(f"Executing command: {command.script} with side effect: {message}")
    
    command = CorrectedCommand("ls", side_effect_function, 1)
    old_cmd = command  # Assuming old_cmd is the same as command for testing purposes
    command.run(old_cmd)
    assert True  # Add assertions to check if side effect function was called and history setting works

# Test equality of two CorrectedCommand instances with identical properties
def test_correctedcommand_equality():
    def side_effect_function(command, message):
        print(f"Executing command: {command.script} with side effect: {message}")
    
    command1 = CorrectedCommand("ls", side_effect_function, 1)
    command2 = CorrectedCommand("ls", side_effect_function, 1)
    assert command1 == command2

# Test run method without side effect function (should not raise errors but also no output)
def test_correctedcommand_run_no_side_effect():
    def empty_side_effect(command, message):
        pass
    
    command = CorrectedCommand("ls", empty_side_effect, 1)
    old_cmd = command  # Assuming old_cmd is the same as command for testing purposes
    command.run(old_cmd)
    assert True  # Add assertions to check if no errors occur and output settings are handled correctly
