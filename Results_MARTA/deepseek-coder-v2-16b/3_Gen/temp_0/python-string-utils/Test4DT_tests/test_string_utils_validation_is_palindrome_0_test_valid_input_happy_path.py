
import pytest
from string_utils.validation import is_palindrome

def test_valid_input_happy_path():
    # Test a simple palindrome without ignoring any character
    assert is_palindrome('LOL') == True
    
    # Test a palindrome with case sensitivity
    assert is_palindrome('Lol') == False
    
    # Ignore case and check if it's still a palindrome
    assert is_palindrome('Lol', ignore_case=True) == True
    
    # Check a non-palindrome string
    assert is_palindrome('ROTFL') == False
