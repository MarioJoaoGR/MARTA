# Module: string_utils.validation
import pytest
from string_utils.validation import is_isogram

# Test cases for the is_isogram function
def test_is_isogram_basic():
    assert is_isogram('dermatoglyphics') == True

def test_is_isogram_non_isogram():
    assert is_isogram('hello') == False

def test_is_isogram_case_insensitive():
    assert is_isogram('Dermatoglyphics') == True

# Edge case: empty string should not be an isogram
def test_is_isogram_empty_string():
    with pytest.raises(AssertionError):
        assert is_isogram('')

# Test for a string containing spaces
def test_is_isogram_with_spaces():
    assert is_isogram('dermatoglyphics society') == False
