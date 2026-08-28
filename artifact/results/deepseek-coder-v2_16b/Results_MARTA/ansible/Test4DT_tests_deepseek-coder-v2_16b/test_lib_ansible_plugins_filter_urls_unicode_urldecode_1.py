
import pytest
from urllib.parse import unquote_plus

# Assuming PY3 is defined somewhere in a standard library or context where it can be used as expected by the function
PY3 = True  # This should be replaced with actual detection of Python version in real code

def unicode_urldecode(string):
    if PY3:
        return unquote_plus(string)
    return to_text(unquote_plus(to_bytes(string)))

# Test cases for the function

def test_valid_input():
    string = 'Hello%20World'
    expected_output = 'Hello World'
    assert unicode_urldecode(string) == expected_output

def test_edge_case_none():
    string = None
    with pytest.raises(TypeError):
        unicode_urldecode(string)

def test_error_handling():
    string = 'Hello%20World!@#'
    with pytest.raises(UnicodeDecodeError):
        unicode_urldecode(string)
