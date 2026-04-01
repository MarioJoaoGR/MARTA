
import pytest
from isort.output import _output_as_string as output_as_string

def test_empty_list():
    lines = []
    line_separator = "\n"
    expected_output = ""
    
    result = output_as_string(lines, line_separator)
    
    assert result == expected_output
