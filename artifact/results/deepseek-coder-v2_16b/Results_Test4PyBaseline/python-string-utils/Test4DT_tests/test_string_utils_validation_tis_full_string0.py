# Module: string_utils.validation
import pytest
from string_utils.validation import is_full_string
from typing import Any

# Helper function to simulate the behavior of is_string from the original module
def is_string(value: Any) -> bool:
    return isinstance(value, str)

def test_is_full_string_valid():
    assert is_full_string('hello') == True

def test_is_full_string_empty():
    assert is_full_string('') == False

def test_is_full_string_none():
    assert is_full_string(None) == False

def test_is_full_string_whitespace():
    assert is_full_string(' ') == False

def test_is_full_string_with_leading_trailing_spaces():
    assert is_full_string('  hello  ') == True
