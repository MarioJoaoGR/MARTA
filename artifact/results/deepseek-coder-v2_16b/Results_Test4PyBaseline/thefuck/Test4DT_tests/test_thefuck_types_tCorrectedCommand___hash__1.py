
import pytest
from thefuck.types import CorrectedCommand

# Test __hash__ method with different scripts and side effects
def test_hash_different_scripts():
    def side_effect_function(command, message):
        print(f"Executing command: {command.script} with side effect: {message}")
    
    command1 = CorrectedCommand("ls", side_effect_function, 1)
    command2 = CorrectedCommand("pwd", side_effect_function, 1)
    
    assert hash(command1) != hash(command2)

# Test __hash__ method with same script but different side effects
def test_hash_same_script_different_side_effects():
    def side_effect_function1(command, message):
        print(f"Executing command: {command.script} with side effect: {message}")
    
    def side_effect_function2(command, message):
        print(f"Different side effect for command: {command.script} - Message: {message}")
    
    command1 = CorrectedCommand("ls", side_effect_function1, 1)
    command2 = CorrectedCommand("ls", side_effect_function2, 1)
    
    assert hash(command1) != hash(command2)

# Test __hash__ method with same script and same side effect but different priorities
def test_hash_same_script_same_side_effect_different_priorities():
    def side_effect_function(command, message):
        print(f"Executing command: {command.script} with side effect: {message}")
    
    command1 = CorrectedCommand("ls", side_effect_function, 1)
    command2 = CorrectedCommand("ls", side_effect_function, 2)
    