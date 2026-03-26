
from string_utils.validation import is_palindrome

def test_edge_cases():
    # Test cases for empty strings, single characters, and palindromes with different spacings and case sensitivity
    
    assert is_palindrome('') == False  # Empty string should not be a palindrome
    assert is_palindrome('a') == True   # Single character string is always a palindrome
    assert is_palindrome('LOL') == True # Case-sensitive palindrome
    assert is_palindrome('Lol', ignore_case=True) == True  # Case-insensitive palindrome
    assert is_palindrome('ROTFL') == False  # Not a palindrome due to different characters at the same position
    assert is_palindrome('No lemon, no melon', ignore_spaces=True, ignore_case=True) == True  # Palindrome ignoring spaces and case
