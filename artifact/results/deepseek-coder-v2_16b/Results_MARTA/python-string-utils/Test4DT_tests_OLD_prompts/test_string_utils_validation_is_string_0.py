
import pytest
from string_utils.validation import is_string

def test_valid_string():
    assert is_string('camelCaseString') == True

def test_none_input():
    assert is_string(None) == False

def test_invalid_type():
    assert is_string(12345) == False
