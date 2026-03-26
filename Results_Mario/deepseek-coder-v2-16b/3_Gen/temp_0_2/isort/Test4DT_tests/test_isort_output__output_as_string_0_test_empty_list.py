
import pytest
from isort.output import _output_as_string  # Assuming the function is in this module

def test_empty_list():
    lines = []
    line_separator = "\n"
    expected_output = ""
    
    result = _output_as_string(lines, line_separator)
    
    assert result == expected_output
