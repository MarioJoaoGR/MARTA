
import pytest

from isort.parse import _infer_line_separator

# Test cases for _infer_line_separator function

def test_infer_line_separator_crlf():
    # Test case with "\r\n" as the line separator
    assert _infer_line_separator("Line 1\r\nLine 2\r\nLine 3") == '\r\n'

def test_infer_line_separator_cr():
    # Test case with "\r" as the line separator
    assert _infer_line_separator("Line 1\rLine 2\rLine 3") == '\r'

def test_infer_line_separator_lf():
    # Test case with "\n" as the line separator
    assert _infer_line_separator("Line 1\nLine 2\nLine 3") == '\n'

# Edge cases to consider:
# - Empty string
# - String without any line separators
# - String containing multiple different line separators

def test_infer_line_separator_empty():
    # Test case with an empty string
    assert _infer_line_separator("") == '\n'  # Default to "\n" for empty strings

def test_infer_line_separator_no_separators():
    # Test case with a string that does not contain any line separators
    assert _infer_line_separator("Line without separator") == '\n'  # Default to "\n"
