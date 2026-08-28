
import pytest
from string_utils.manipulation import strip_margin, InvalidInputError

def is_string(obj):
    return isinstance(obj, str)

# Test for valid input

# Test for edge case where input is None
def test_edge_case_none():
    with pytest.raises(InvalidInputError):
        strip_margin(None)

# Test for invalid input type (int)
def test_invalid_input():
    with pytest.raises(InvalidInputError):
        strip_margin(12345)