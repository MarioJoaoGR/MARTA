
import pytest
from string_utils.validation import is_palindrome

def test_is_palindrome():
    # Test cases for palindromes without ignoring any character
    assert is_palindrome('LOL') == True
    assert is_palindrome('radar') == True
    assert is_palindrome('level') == True
    
    # Test cases for non-palindromes without ignoring any character
    assert is_palindrome('hello') == False
    assert is_palindrome('world') == False
    
    # Test cases for palindromes with case sensitivity
    assert is_palindrome('Lol', ignore_case=True) == True
    assert is_palindrome('rotor', ignore_case=True) == True
    assert is_palindrome('repaper', ignore_case=True) == True
    
    # Test cases for non-palindromes with case sensitivity
    assert is_palindrome('Hello', ignore_case=True) == False
    assert is_palindrome('World', ignore_case=True) == False
    
    # Test cases for palindromes ignoring spaces
    assert is_palindrome('a man a plan a canal panama', ignore_spaces=True) == True
    assert is_palindrome('madam im adam', ignore_spaces=True) == True
    
    # Test cases for non-palindromes ignoring spaces
    assert is_palindrome('this is not a palindrome') == False
    assert is_palindrome('racecar nope') == False
    
    # Test cases for palindromes with case sensitivity and ignoring spaces
    assert is_palindrome('A man a plan a canal Panama', ignore_case=True, ignore_spaces=True) == True
    assert is_palindrome('No lemon no melon', ignore_case=True, ignore_spaces=True) == True
    
    # Test cases for non-palindromes with case sensitivity and ignoring spaces
    assert is_palindrome('Hello world') == False
    assert is_palindrome('Radar mirror') == False
