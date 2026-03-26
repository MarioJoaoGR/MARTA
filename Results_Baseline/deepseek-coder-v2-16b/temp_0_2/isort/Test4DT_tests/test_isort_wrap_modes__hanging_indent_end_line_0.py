
import pytest

from isort.wrap_modes import _hanging_indent_end_line


# Test case 1: The input string does not end with a space
def test_hanging_indent_end_line_no_space():
    line = "This is a test"
    expected_output = 'This is a test \\'
    assert _hanging_indent_end_line(line) == expected_output, f"Expected '{expected_output}', but got '{_hanging_indent_end_line(line)}'"

# Test case 2: The input string already ends with a space
def test_hanging_indent_end_line_with_space():
    line = "This is a test "
    expected_output = 'This is a test  \\'