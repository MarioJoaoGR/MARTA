# Module: isort.parse
import pytest

from isort.parse import _infer_line_separator


# Test cases for _infer_line_separator function
def test_infer_line_separator_crlf():
    assert _infer_line_separator("Line 1\r\nLine 2\r\nLine 3") == "\r\n"

def test_infer_line_separator_cr():
    assert _infer_line_separator("Line 1\rLine 2\rLine 3") == "\r"

def test_infer_line_separator_lf():
    assert _infer_line_separator("Line 1\nLine 2\nLine 3") == "\n"

# Additional test cases to cover different scenarios and edge cases
def test_infer_line_separator_mixed():
    # String contains a mix of line separators, should return the first detected one
    assert _infer_line_separator("Line 1\r\nLine 2\rLine 3") == "\r\n"

def test_infer_line_separator_empty():
    # Empty string should default to '\n' as per function logic
    assert _infer_line_separator("") == "\n"

def test_infer_line_separator_no_newlines():
    # String without any line separators, should default to '\n'
    assert _infer_line_separator("NoNewLinesHere") == "\n"

# Test case for function documentation example
def test_infer_line_separator_example():
    assert _infer_line_separator("Line 1\r\nLine 2\r\nLine 3") == "\r\n"
    assert _infer_line_separator("Line 1\rLine 2\rLine 3") == "\r"
    assert _infer_line_separator("Line 1\nLine 2\nLine 3") == "\n"
