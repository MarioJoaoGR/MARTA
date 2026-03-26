
import pytest
from string_utils.manipulation import __RomanNumbers

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

@pytest.mark.parametrize("input_number, expected", [
    (3, 'III'),
    (4, 'IV'),
    (9, 'IX'),
    (58, 'LVIII'),
    ('37', 'XXXVII'),  # Adding a test case for string input
])
def test_valid_case_1(input_number, expected):
    assert __RomanNumbers().encode(input_number) == expected

@pytest.mark.parametrize("input_number", [0, -1, 'abc', 4000])
def test_invalid_cases(input_number):
    with pytest.raises(ValueError):
        __RomanNumbers().encode(input_number)
