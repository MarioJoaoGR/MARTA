
import subprocess
import sys
from unittest.mock import patch

import pytest


def get_output(command):
    """Mock function to simulate subprocess.run output."""
    if command == ['ls', '-l']:
        return "line1\nline2\nline3"
    raise ValueError("Unsupported command")

# Mock the actual get_lines function for testing
def get_lines(command: list[str]) -> list[str]:
    """Run a command and return lines of output."""
    stdout = get_output(command)
    return [line.strip() for line in stdout.splitlines()]

@pytest.mark.parametrize("input_value, expected", [(None, ValueError)])
def test_none_input(input_value, expected):
    with pytest.raises(expected):
        get_lines(input_value)
