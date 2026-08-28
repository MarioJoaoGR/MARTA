
import pytest
from string_utils.validation import is_palindrome

# Test scenario 1: Valid palindrome without spaces or case sensitivity
def test_valid_case_no_spaces_or_case():
    input_string = 'LOL'
    assert is_palindrome(input_string) == True

# Test scenario 2: Valid palindrome with spaces and case sensitivity
def test_valid_case_with_spaces_and_case():
    input_string = 'i topi non avevano nipoti'
    assert is_palindrome(input_string, ignore_spaces=True) == True

# Test scenario 3: Invalid palindrome
def test_invalid_case():
    input_string = 'ROTFL'
    assert is_palindrome(input_string) == False
