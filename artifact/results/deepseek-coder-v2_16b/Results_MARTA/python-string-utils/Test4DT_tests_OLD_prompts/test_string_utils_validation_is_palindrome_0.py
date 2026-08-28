
import pytest
from string_utils.validation import is_palindrome, is_full_string
from unittest.mock import patch

# Test valid palindrome without ignoring any character
def test_valid_case():
    assert is_palindrome('LOL') == True

# Test invalid palindrome with case differences (should be ignored)
def test_invalid_case():
    assert is_palindrome('Lol', ignore_case=True) == True

# Test non-palindrome string
def test_non_palindrome():
    assert is_palindrome('ROTFL') == False

# Test palindrome with spaces (should be ignored)
def test_ignore_spaces():
    assert is_palindrome('i topi non avevano nipoti', ignore_spaces=True) == True

# Test invalid type input raises TypeError

# Test palindrome function with full string mock

# Test palindrome function with full string mock failing
@patch('string_utils.validation.is_full_string', return_value=False)
def test_invalid_input(mock_is_full_string):
    assert is_palindrome('i topi non avevano nipoti') == False