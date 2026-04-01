
import pytest
from string_utils.manipulation import __RomanNumbers

def roman_decode(input_string: str) -> int:
    """
    Decode a Roman numeral string into an integer if the provided string is valid.

    *Example:*

    >>> roman_decode('VII') # returns 7

    :param input_string: (Assumed) Roman number
    :type input_string: str
    :return: Integer value
    """
    return __RomanNumbers.decode(input_string)

@pytest.mark.parametrize("input_string, expected", [('III', 3), ('IV', 4), ('IX', 9), ('LVIII', 58), ('MCMXCIV', 1994)])
def test_valid_roman_numeral(input_string, expected):
    assert roman_decode(input_string) == expected
