
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

# Test valid input scenario
def test_valid_input():
    formatter = __StringFormatter("hello world")
    assert formatter.input_string == "hello world"

# Test edge case scenario where the input is None
def test_edge_case_none():
    with pytest.raises(InvalidInputError):
        __StringFormatter(None)

# Test invalid input scenario where the input is not a string
def test_invalid_input():
    with pytest.raises(InvalidInputError):
        __StringFormatter(12345)
