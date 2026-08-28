
import pytest
from string_utils.validation import is_palindrome

# Test Scenario 1: Valid palindrome without ignoring any character
def test_valid_palindrome_no_ignore():
    input_string = 'LOL'
    assert is_palindrome(input_string) == True, f"Expected {input_string} to be a valid palindrome."

# Test Scenario 2: Valid palindrome with case differences which can be ignored
def test_valid_palindrome_with_case_ignore():
    input_string = 'Lol'
    ignore_case = True
    assert is_palindrome(input_string, ignore_case=ignore_case) == True, f"Expected {input_string} to be a valid palindrome when ignoring case."

# Test Scenario 3: Invalid palindrome
def test_invalid_palindrome():
    input_string = 'ROTFL'
    assert is_palindrome(input_string) == False, f"Expected {input_string} to be an invalid palindrome."
