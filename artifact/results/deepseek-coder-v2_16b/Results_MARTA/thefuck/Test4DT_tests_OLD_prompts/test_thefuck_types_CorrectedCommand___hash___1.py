
import pytest
from unittest.mock import patch, MagicMock
from thefuck.types import CorrectedCommand

# Test for CorrectedCommand initialization and basic functionality
def test_correctedcommand_initialization():
    def example_side_effect(command, arg):
        print(f"Executing script with side effect: {arg}")
    
    cmd = CorrectedCommand("echo 'Hello, World!'", example_side_effect, 1)
    
    assert cmd.script == "echo 'Hello, World!'"
    assert callable(cmd.side_effect)
    assert cmd.priority == 1

# Test for CorrectedCommand side effect execution

# Test for CorrectedCommand hash method
def test_correctedcommand_hash():
    def example_side_effect(command, arg):
        print(f"Executing script with side effect: {arg}")
    
    cmd1 = CorrectedCommand("echo 'Hello, World!'", example_side_effect, 1)
    cmd2 = CorrectedCommand("echo 'Hello, World!'", example_side_effect, 1)
    
    assert hash(cmd1) == hash(cmd2)