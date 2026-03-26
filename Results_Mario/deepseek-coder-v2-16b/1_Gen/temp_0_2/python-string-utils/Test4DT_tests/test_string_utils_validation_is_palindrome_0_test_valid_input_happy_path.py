
import pytest
from string_utils import validation

def test_valid_input_happy_path():
    # Test a simple palindrome without ignoring case or spaces
    assert validation.is_palindrome('LOL') == True
    
    # Test a palindrome with different casing (should return False)
    assert validation.is_palindrome('Lol') == False
    
    # Test a palindrome with ignoring case
    assert validation.is_palindrome('Lol', ignore_case=True) == True
    
    # Test a non-palindrome string
    assert validation.is_palindrome('ROTFL') == False
