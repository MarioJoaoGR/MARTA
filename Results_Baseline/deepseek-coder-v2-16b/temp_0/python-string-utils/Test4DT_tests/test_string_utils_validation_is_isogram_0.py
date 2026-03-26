# Module: string_utils.validation
import pytest
from string_utils.validation import is_isogram

# Test cases for is_isogram function
def test_valid_isogram():
    assert is_isogram('dermatoglyphics')  # returns True

def test_not_isogram():
    assert not is_isogram('hello')  # returns False

def test_empty_or_spaces():
    assert not is_isogram(' ')  # returns False

def test_valid_isogram_lowercase():
    assert is_isogram('abcde')  # returns True

def test_valid_isogram_mixed_case():
    assert is_isogram('AaBbCc')  # returns True
