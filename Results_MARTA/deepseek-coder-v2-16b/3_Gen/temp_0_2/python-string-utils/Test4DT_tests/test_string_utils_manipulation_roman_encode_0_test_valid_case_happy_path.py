
from typing import Union
import pytest
from string_utils.manipulation import __RomanNumbers  # Assuming this is the correct module path

def roman_encode(input_number: Union[str, int]) -> str:
    """
    Convert the given number/string into a roman number.

    The passed input must represents a positive integer in the range 1-3999 (inclusive).

    Why this limit? You may be wondering:

    1. zero is forbidden since there is no related representation in roman numbers
    2. the upper bound 3999 is due to the limitation in the ascii charset\
    (the higher quantity sign displayable in ascii is "M" which is equal to 1000, therefore based on\
    roman numbers rules we can use 3 times M to reach 3000 but we can't go any further in thousands without\
    special "boxed chars").

    *Examples:*

    >>> roman_encode(37) # returns 'XXXVIII'
    >>> roman_encode('2020') # returns 'MMXX'

    :param input_number: An integer or a string to be converted.
    :type input_number: Union[str, int]
    :return: Roman number string.
    """
    return __RomanNumbers.encode(input_number)

def test_valid_case_happy_path():
    assert roman_encode('37') == 'XXXVII'
    assert roman_encode(37) == 'XXXVII'
    assert roman_encode('2020') == 'MMXX'
    assert roman_encode(2020) == 'MMXX'
