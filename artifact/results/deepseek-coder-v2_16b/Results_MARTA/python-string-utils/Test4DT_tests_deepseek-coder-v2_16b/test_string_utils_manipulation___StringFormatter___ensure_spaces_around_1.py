
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

# Test valid input scenario
def test_valid_input():
    formatter = __StringFormatter("Hello, world!")
    assert formatter.input_string == "Hello, world!"

# Test edge case with None input
def test_edge_case_none():
    with pytest.raises(InvalidInputError):
        __StringFormatter(None)

# Test invalid input type scenario
def test_invalid_input():
    with pytest.raises(InvalidInputError):
        __StringFormatter(12345)
