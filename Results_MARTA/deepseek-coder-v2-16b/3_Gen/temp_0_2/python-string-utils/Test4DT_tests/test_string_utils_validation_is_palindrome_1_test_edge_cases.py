
from string_utils.validation import is_palindrome

def test_edge_cases():
    # Test for None input
    assert not is_palindrome(None)
    
    # Test for empty string
    assert not is_palindrome('')
