
import pytest
from thefuck.types import CorrectedCommand

# Test for rule matching with a command containing "old_command"

# Test for invalid inputs to CorrectedCommand initialization
def test_invalid_inputs():
    with pytest.raises(TypeError):
        CorrectedCommand()  # Missing required arguments

    with pytest.raises(TypeError):
        CorrectedCommand("echo 'Hello'")  # Missing side_effect and priority

    with pytest.raises(TypeError):
        CorrectedCommand("echo 'Hello'", "modify_command")  # Incorrect type for side_effect

# Test for equality comparison ignoring the priority field