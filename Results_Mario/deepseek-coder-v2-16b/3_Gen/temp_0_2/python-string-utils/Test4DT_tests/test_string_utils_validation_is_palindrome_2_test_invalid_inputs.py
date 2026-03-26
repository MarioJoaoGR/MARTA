
import pytest
from string_utils.validation import is_palindrome

# Assuming SPACES_RE is defined in a module named 'string_utils.validation'
from string_utils.validation import SPACES_RE

def test_invalid_inputs():
    # Test cases for invalid inputs
    assert not is_palindrome(''), "Empty string should not be a palindrome"
    assert not is_palindrome(None), "None should not be a palindrome"
    assert not is_palindrome(' '), "String with only spaces should not be a palindrome"
    assert not is_palindrome('12345'), "Non-palindromic string should return False"
    assert not is_palindrome('A man, a plan, a canal: Panama', ignore_spaces=True), "String with spaces and case sensitivity should return False"
