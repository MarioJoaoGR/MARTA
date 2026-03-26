
import pytest
from string_utils.validation import is_full_string

def is_palindrome(input_string: str, ignore_spaces: bool = False, ignore_case: bool = False) -> bool:
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
        input_string = SPACES_RE.sub('', input_string)

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
    # Test with non-string input
    assert not is_palindrome(12345)  # Should raise a TypeError or ValueError
    
    # Test with empty string
    assert not is_palindrome("")  # An empty string should not be considered a palindrome
    
    # Test with None input
    with pytest.raises(TypeError):  # Ensure the function raises a TypeError for non-string inputs
        is_palindrome(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_palindrome_2_test_invalid_inputs
python-string-utils/Test4DT_tests/test_string_utils_validation_is_palindrome_2_test_invalid_inputs.py:29:23: E0602: Undefined variable 'SPACES_RE' (undefined-variable)


"""