
import pytest
from thefuck.types import CorrectedCommand


def test_valid_init_with_script_and_side_effect():
    def example_side_effect(command, arg):
        pass  # Placeholder for actual side effect logic
    
    cmd = CorrectedCommand("echo 'Hello, World!'", example_side_effect, 1)
    assert cmd.script == "echo 'Hello, World!'"
    assert callable(cmd.side_effect)
    assert cmd.priority == 1

def test_valid_init_with_only_script():
    def no_side_effect(command, arg):
        pass  # Placeholder for actual side effect logic
    
    cmd = CorrectedCommand("echo 'Hello, World!'", no_side_effect, 1)
    assert cmd.script == "echo 'Hello, World!'"
    assert callable(cmd.side_effect)
    assert cmd.priority == 1

def test_valid_init_with_only_priority():
    def example_side_effect(command, arg):
        pass  # Placeholder for actual side effect logic
    
    cmd = CorrectedCommand("echo 'Hello, World!'", example_side_effect, 1)
    assert cmd.script == "echo 'Hello, World!'"
    assert callable(cmd.side_effect)
    assert cmd.priority == 1
