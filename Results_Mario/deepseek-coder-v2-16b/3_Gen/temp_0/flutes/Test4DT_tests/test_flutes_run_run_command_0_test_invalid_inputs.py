
import pytest
from unittest.mock import patch
from flutes.run import run_command, CommandResult  # Correctly import the run_command function

# Define a fixture for CommandResult if not already defined in your test suite
@pytest.fixture
def command_result():
    return CommandResult("dummy_args", 0, b"dummy_output")

def test_run_command_invalid_inputs(command_result):
    with pytest.raises(TypeError):  # Assuming invalid inputs should raise a TypeError
        run_command(123)  # Example of an invalid input (int instead of str or list)
