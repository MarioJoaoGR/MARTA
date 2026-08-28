
import pytest
from string_utils.validation import is_full_string

# Helper function to simulate is_string check for testing purposes
def is_string(obj):
    return isinstance(obj, str)

def test_is_full_string_with_valid_string():
    assert is_full_string('hello') == True

def test_is_full_string_with_empty_string():
    assert is_full_string('') == False

def test_is_full_string_with_whitespace_only_string():
    assert is_full_string(' ') == False

def test_is_full_string_with_none():
    assert is_full_string(None) == False
