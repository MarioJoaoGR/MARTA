
import pytest

from isort.output import _normalize_empty_lines, _output_as_string


# Test case for joining lines with a newline character as separator
def test_output_as_string_with_newline():
    result = _output_as_string(["line1", "line2"], "\n")
    assert result == 'line1\nline2\n'

# Corrected test case for joining lines with a space character as separator
def test_output_as_string_with_space():
    result = _output_as_string(["line1", "", "", "line2"], " ")