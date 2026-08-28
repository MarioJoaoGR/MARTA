
import pytest
from thefuck.types import CorrectedCommand

# Test for __eq__ method when other is not a CorrectedCommand instance
def test_equality_method_with_non_correctedcommand():
    def side_effect_function(command, message):
        print(f"Executing command: {command.script} with side effect: {message}")
    
    # Create an instance of CorrectedCommand
    cmd1 = CorrectedCommand("echo Hello", side_effect_function, 1)
    
    # Compare with a non-CorrectedCommand instance (e.g., int)
    assert not (cmd1 == 123)
    
    # Compare with another type of non-CorrectedCommand instance (e.g., str)
    assert not (cmd1 == "echo Hello")
    
    # Compare with a NoneType
    assert not (cmd1 == None)

# Additional Test for Equality Method to cover line 223 directly
def test_equality_method_coverage():
    def side_effect_function(command, message):
        print(f"Executing command: {command.script} with side effect: {message}")
    
    # Create an instance of CorrectedCommand
    cmd1 = CorrectedCommand("echo Hello", side_effect_function, 1)
    
    # Compare with another instance of CorrectedCommand with different script but same side effect function
    cmd2 = CorrectedCommand("ls", side_effect_function, 1)
    assert not (cmd1 == cmd2)
    
    # Compare with an identical instance of CorrectedCommand
    cmd3 = CorrectedCommand("echo Hello", side_effect_function, 1)
    assert cmd1 == cmd3

# Test for __eq__ method when other is a CorrectedCommand instance but has different priority
def test_equality_method_with_different_priority():
    def side_effect_function(command, message):
        print(f"Executing command: {command.script} with side effect: {message}")
    
    # Create two instances of CorrectedCommand with the same script and side effect but different priorities
    cmd1 = CorrectedCommand("echo Hello", side_effect_function, 1)
    cmd2 = CorrectedCommand("echo Hello", side_effect_function, 2)
    