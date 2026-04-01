
import pytest
from string_utils.validation import is_palindrome

def test_invalid_inputs():
    # Test case for invalid input types
    assert not is_palindrome(12345)  # int should return False
    assert not is_palindrome(None)   # None should return False
    assert not is_palindrome([])     # list should return False
    assert not is_palindrome({})     # dict should return False
    assert not is_palindrome(True)   # bool should return False
