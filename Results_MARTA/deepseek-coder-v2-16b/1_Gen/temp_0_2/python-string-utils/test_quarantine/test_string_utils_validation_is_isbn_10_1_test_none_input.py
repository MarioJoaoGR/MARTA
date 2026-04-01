
import pytest
from string_utils.validation import ISBNChecker

def is_isbn_10(input_string: str, normalize: bool = True) -> bool:
    """
    Checks if the given string represents a valid ISBN 10 (International Standard Book Number).
    By default hyphens in the string are ignored, so digits can be separated in different ways, by calling this
    function with `normalize=False` only digit-only strings will pass the validation.

    *Examples:*

    >>> is_isbn_10('1506715214') # returns true
    >>> is_isbn_10('150-6715214') # returns true
    >>> is_isbn_10('150-6715214', normalize=False) # returns false

    :param input_string: String to check.
    :param normalize: True to ignore hyphens ("-") in the string (default), false otherwise.
    :return: True if valid ISBN 10, False otherwise.
    """
    checker = ISBNChecker(input_string, normalize)
    return checker.is_isbn_10()

def test_none_input():
    with pytest.raises(TypeError):
        is_isbn_10(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_isbn_10_1_test_none_input
python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_10_1_test_none_input.py:3:0: E0611: No name 'ISBNChecker' in module 'string_utils.validation' (no-name-in-module)


"""