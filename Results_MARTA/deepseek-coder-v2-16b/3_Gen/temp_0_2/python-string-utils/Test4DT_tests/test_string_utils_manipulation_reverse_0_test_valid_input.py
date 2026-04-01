
import pytest
from string_utils.manipulation import is_string
from string_utils.errors import InvalidInputError

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

def test_valid_input():
    assert reverse('hello') == 'olleh'
    assert reverse('Python') == 'nohtyP'
