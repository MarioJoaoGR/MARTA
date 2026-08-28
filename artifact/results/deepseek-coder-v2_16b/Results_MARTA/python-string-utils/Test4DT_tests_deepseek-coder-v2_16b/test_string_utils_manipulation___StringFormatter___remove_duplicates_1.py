
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

# Test for valid input
def test_valid_input():
    formatter = __StringFormatter("hello world")
    assert formatter.input_string == "hello world"

# Test for edge case with None input
def test_edge_case():
    with pytest.raises(InvalidInputError):
        __StringFormatter(None)

# Test for raising InvalidInputError for non-string input
def test_invalid_input():
    with pytest.raises(InvalidInputError):
        __StringFormatter(12345)
