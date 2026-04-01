
import pytest
from isort.hooks import get_lines  # Assuming this module contains the get_lines function

def test_get_lines():
    # Mock command
    command = ['ls', '-l']
    
    # Call the function with the mock command
    lines = get_lines(command)
    
    # Assert that the result is a list of strings (whitespace-stripped lines)
    assert isinstance(lines, list), "Expected a list of strings"
    for line in lines:
        assert isinstance(line, str), "Each line should be a string"
        assert line.strip() == line, "Lines should be whitespace-stripped"
