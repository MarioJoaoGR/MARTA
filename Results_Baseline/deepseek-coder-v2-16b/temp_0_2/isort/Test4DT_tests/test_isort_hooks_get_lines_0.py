# Module: isort.hooks
import subprocess

import pytest

from isort.hooks import get_lines


# Helper function to run a command and capture its output
def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.splitlines()

@pytest.mark.parametrize("command", [
    (['ls', '-l']),
    (['find', '.', '-name', '*.py']),
    (['true']),
    (['echo', 'line1\nline2']),
    (['cat', '/dev/null'])
])
def test_get_lines(command):
    # Run the command and get its output
    expected = run_command(command)
    
    # Call the function with the same command
    result = get_lines(command)
    
    # Assert that the result matches the expected output
    assert result == expected
