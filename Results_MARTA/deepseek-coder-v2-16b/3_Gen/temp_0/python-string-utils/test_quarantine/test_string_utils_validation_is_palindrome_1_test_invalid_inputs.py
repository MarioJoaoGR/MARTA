
import pytest
from string_utils.validation import is_full_string
from re import sub as SPACES_RE
from typing import Any

def is_palindrome(input_string: Any, ignore_spaces: bool = False, ignore_case: bool = False) -> bool:
    """
    Checks if the string is a palindrome (https://en.wikipedia.org/wiki/Palindrome).

    *Examples:*

    >>> is_palindrome('LOL') # returns true
    >>> is_palindrome('Lol') # returns false
    >>> is_palindrome('Lol', ignore_case=True) # returns true
    >>> is_palindrome('ROTFL') # returns false

    :param input_string: String to check.
    :type input_string: str
    :param ignore_spaces: False if white spaces matter (default), true otherwise.
    :type ignore_spaces: bool
    :param ignore_case: False if char case matters (default), true otherwise.
    :type ignore_case: bool
    :return: True if the string is a palindrome (like "otto", or "i topi non avevano nipoti" if strict=False),\
    False otherwise
    """
    if not is_full_string(input_string):
        return False

    if ignore_spaces:
        input_string = SPACES_RE('', input_string)

    string_len = len(input_string)

    # Traverse the string one char at step, and for each step compares the
    # "head_char" (the one on the left of the string) to the "tail_char" (the one on the right).
    # In this way we avoid to manipulate the whole string in advance if not necessary and provide a faster
    # algorithm which can scale very well for long strings.
    for index in range(string_len):
        head_char = input_string[index]
        tail_char = input_string[string_len - index - 1]

        if ignore_case:
            head_char = head_char.lower()
            tail_char = tail_char.lower()

        if head_char != tail_char:
            return False

    return True

def test_invalid_inputs():
    # Test with non-string inputs
    assert not is_palindrome(12345)  # Non-string input should return False
    assert not is_palindrome(None)   # None type should return False
    
    # Test with empty string
    assert not is_palindrome('')  # Empty string should return False
    
    # Test with palindrome but different cases
    assert not is_palindrome('Lol', ignore_case=False)  # Case sensitive, so it's not a palindrome
    assert is_palindrome('Lol', ignore_case=True)      # Case insensitive, so it is a palindrome
    
    # Test with string containing spaces
    assert not is_palindrome('i topi non avevano nipoti', ignore_spaces=False)  # Spaces matter
    assert is_palindrome('i topi non avevano nipoti', ignore_spaces=True)       # Ignore spaces
    
    # Test with palindrome string but different cases and spaces
    assert not is_palindrome('i topi non avevano nipoti', ignore_case=False, ignore_spaces=False)  # Case and space sensitive
    assert is_palindrome('i topi non avevano nipoti', ignore_case=True, ignore_spaces=True)       # Ignore case and spaces

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_palindrome_1_test_invalid_inputs
python-string-utils/Test4DT_tests/test_string_utils_validation_is_palindrome_1_test_invalid_inputs.py:31:23: E1120: No value for argument 'string' in function call (no-value-for-parameter)


"""