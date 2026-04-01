
import pytest
from string_utils.manipulation import is_string
from custom_exceptions import InvalidInputError

def booleanize(input_string: str) -> bool:
    """
    Turns a string into a boolean based on its content (CASE INSENSITIVE).

    A positive boolean (True) is returned if the string value is one of the following:
    - "true"
    - "1"
    - "yes"
    - "y"

    Otherwise False is returned. The comparison is case insensitive.

    *Examples:*

    >>> booleanize('true') # returns True
    >>> booleanize('YES') # returns True
    >>> booleanize('nope') # returns False

    :param input_string: String to convert. This should be a string of text that you want to evaluate as a boolean value.
    :type input_string: str
    :return: True if the string contains a boolean-like positive value (case insensitive match), otherwise False.
    """
    if not is_string(input_string):
        raise InvalidInputError(input_string)

    return input_string.lower() in ('true', '1', 'yes', 'y')

def test_valid_input_YES():
    assert booleanize('YES') == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation_booleanize_0_test_valid_input_YES
python-string-utils/Test4DT_tests/test_string_utils_manipulation_booleanize_0_test_valid_input_YES.py:4:0: E0401: Unable to import 'custom_exceptions' (import-error)

"""