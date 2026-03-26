# Module: string_utils.manipulation
import pytest
from string_utils.manipulation import __RomanNumbers

# Helper function to check if a string is an integer
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Test cases for the encode method of __RomanNumbers class
@pytest.mark.parametrize("input_number, expected", [
    (3, 'III'),
    ('42', 'XLII'),
    (1976, 'MCMLXXVI'),
])
def test_encode(input_number, expected):
    assert __RomanNumbers.encode(input_number) == expected

# Test case for invalid input that should raise ValueError
@pytest.mark.parametrize("input_number", [0, '0', 4000, '-1'])
def test_encode_invalid_input(input_number):
    with pytest.raises(ValueError):
        __RomanNumbers.encode(input_number)

# Test case for string input that should be converted to integer and then encoded
@pytest.mark.parametrize("input_string, expected", [
    ('3', 'III'),
    ('42', 'XLII'),
    ('1976', 'MCMLXXVI'),
])
def test_encode_from_string(input_string, expected):
    assert __RomanNumbers.encode(input_string) == expected

# Test case for the edge cases of the input range
@pytest.mark.parametrize("edge_case", [1, 3999])
def test_encode_edge_cases(edge_case):
    assert __RomanNumbers.encode(edge_case) == str(__RomanNumbers.encode(edge_case))

# Test case for non-integer input that should raise ValueError
@pytest.mark.parametrize("non_integer", ['a', '1.5', 'abc'])
def test_encode_non_integer(non_integer):
    with pytest.raises(ValueError):
        __RomanNumbers.encode(non_integer)
