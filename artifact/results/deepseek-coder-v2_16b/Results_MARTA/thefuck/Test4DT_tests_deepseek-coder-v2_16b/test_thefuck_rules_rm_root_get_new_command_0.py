
import pytest
from thefuck.rules.rm_root import get_new_command

def test_valid_input():
    class DummyCommand:
        def __init__(self, script):
            self.script = script
    
    cmd = DummyCommand("ls -l")
    assert get_new_command(cmd) == "ls -l --no-preserve-root"

def test_invalid_input():
    invalid_cmd = 'InvalidCommand'
    with pytest.raises(AttributeError):
        get_new_command(invalid_cmd)
