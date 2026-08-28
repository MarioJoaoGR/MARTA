# Module: string_utils.validation
import pytest
from string_utils.validation import is_palindrome

# Test cases for palindrome function with default parameters
def test_is_palindrome_basic():
    assert is_palindrome('LOL') == True, "Test failed for basic palindrome 'LOL'"

def test_is_palindrome_ignore_case():
    assert is_palindrome('Lol', ignore_case=True) == True, "Test failed for palindrome with case ignored 'Lol'"

def test_is_palindrome_ignore_spaces():
    assert is_palindrome('R o T F L', ignore_spaces=True) == False, "Test failed for non-palindrome with spaces ignored 'R o T F L'"

# Test cases for palindrome function with both parameters set to True
def test_is_palindrome_ignore_case_and_spaces():
    assert is_palindrome('Was it a car or a cat I saw', ignore_spaces=True, ignore_case=True) == True, "Test failed for palindrome with case and spaces ignored 'Was it a car or a cat I saw'"

# Test cases for non-palindromes
def test_is_palindrome_non_palindrome():
    assert is_palindrome('Hello') == False, "Test failed for non-palindrome 'Hello'"

# Edge case: empty string
def test_is_palindrome_empty_string():
    assert is_palindrome('') == False, "Test failed for empty string"
