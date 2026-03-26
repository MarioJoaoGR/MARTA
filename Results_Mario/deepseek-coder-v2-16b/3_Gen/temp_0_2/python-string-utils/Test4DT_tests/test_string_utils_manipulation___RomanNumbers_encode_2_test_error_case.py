
import pytest
from string_utils.manipulation import __RomanNumbers

def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

@pytest.mark.parametrize("input_number, expected_exception", [
    ('abc', ValueError),
    (0, ValueError),
    (-1, ValueError),
    (4000, ValueError),
])
def test_encode_error_cases(input_number, expected_exception):
    with pytest.raises(expected_exception):
        __RomanNumbers().encode(input_number)
