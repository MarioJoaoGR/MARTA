
import pytest
from string_utils.validation import is_palindrome

def test_valid_input_happy_path():
    # Test palindromes without ignoring any character
    assert is_palindrome('LOL') == True
    assert is_palindrome('radar') == True
    assert is_palindrome("A man, a plan, a canal: Panama") == False  # Case sensitive but still not a palindrome
