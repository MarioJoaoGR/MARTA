
import pytest
from string_utils.validation import is_palindrome

def test_valid_palindrome():
    # Test cases for palindromes without ignoring any character
    assert is_palindrome('LOL') == True
    assert is_palindrome('madam') == True
    assert is_palindrome('noon') == True
    
    # Test cases for non-palindromes without ignoring any character
    assert is_palindrome('hello') == False
    assert is_palindrome('world') == False
    
    # Test cases for palindromes with case sensitivity
    assert is_palindrome('Lol', ignore_case=True) == True
    assert is_palindrome('Madam', ignore_case=True) == True
    assert is_palindrome('Noon', ignore_case=True) == True
    
    # Test cases for non-palindromes with case sensitivity
    assert is_palindrome('Hello', ignore_case=True) == False
    assert is_palindrome('World', ignore_case=True) == False
    
    # Test cases for palindromes ignoring spaces and case sensitivity
    assert is_palindrome('A man a plan a canal Panama', ignore_spaces=True, ignore_case=True) == True
    assert is_palindrome('No lemon no melon', ignore_spaces=True, ignore_case=True) == True
    
    # Test cases for non-palindromes ignoring spaces and case sensitivity
    assert is_palindrome('A man a plan a canal Panama with spaces', ignore_spaces=True, ignore_case=True) == False
    assert is_palindrome('No lemon no melon with extra words', ignore_spaces=True, ignore_case=True) == False
