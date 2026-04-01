
import pytest
from string_utils.manipulation import is_string, InvalidInputError

def booleanize(input_string: str) -> bool:
    """
    Turns a string into a boolean based on its content (CASE INSENSITIVE).

    A positive boolean (True) is returned if the string value is one of the following:

    - "true"
    - "1"
    - "yes"
    - "y"

    Otherwise False is returned.

    *Examples:*

    >>> booleanize('true') # returns True
    >>> booleanize('YES') # returns True
    >>> booleanize('nope') # returns False

    :param input_string: String to convert
    :type input_string: str
    :return: True if the string contains a boolean-like positive value, false otherwise
    """
    if not is_string(input_string):
        raise InvalidInputError(input_string)

    return input_string.lower() in ('true', '1', 'yes', 'y')

def test_valid_inputs():
    assert booleanize('true') == True
    assert booleanize('YES') == True
    assert booleanize('1') == True
    assert booleanize('Yes') == True
    assert booleanize('Y') == True
    assert booleanize('nope') == False
    assert booleanize('false') == False
    assert booleanize('0') == False
    assert booleanize('no') == False
    assert booleanize('N') == False
