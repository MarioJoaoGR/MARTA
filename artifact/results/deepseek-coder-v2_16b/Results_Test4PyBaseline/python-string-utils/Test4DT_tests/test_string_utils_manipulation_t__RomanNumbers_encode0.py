# Module: string_utils.manipulation
# test_string_utils.manipulation.py
from string_utils.manipulation import __RomanNumbers
import pytest

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

@pytest.mark.parametrize("input_number, expected", [
    (3, 'III'),
    (42, 'XLII'),
    (1994, 'MCMXCIV'),
])
def test_encode_valid_inputs(input_number, expected):
    assert __RomanNumbers.encode(input_number) == expected

@pytest.mark.parametrize("input_number", [
    0,  # out of range
    'abc',  # invalid string input
])
def test_encode_invalid_inputs(input_number):
    with pytest.raises(ValueError):
        __RomanNumbers.encode(input_number)

@pytest.mark.parametrize("input_string, expected", [
    ('3', 'III'),  # string representation of an integer
    ('42', 'XLII'),  # string representation of an integer
    ('1994', 'MCMXCIV'),  # string representation of an integer
])
def test_encode_string_inputs(input_string, expected):
    assert __RomanNumbers.encode(input_string) == expected
