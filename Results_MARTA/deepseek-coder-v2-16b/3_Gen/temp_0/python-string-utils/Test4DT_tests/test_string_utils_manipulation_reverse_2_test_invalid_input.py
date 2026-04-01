
import pytest
from string_utils.manipulation import InvalidInputError, is_string

def reverse(input_string: str) -> str:
    """
    Returns the string with its chars reversed.

    *Example:*

    >>> reverse('hello') # returns 'olleh'

    :param input_string: String to revert.
    :type input_string: str
    :return: Reversed string.
    """
    if not is_string(input_string):
        raise InvalidInputError(input_string)

    return input_string[::-1]

def test_invalid_input():
    with pytest.raises(InvalidInputError):
        reverse(12345)  # Passing an integer, which should raise InvalidInputError
