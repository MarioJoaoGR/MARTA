
import pytest
from unittest.mock import patch
from string_utils.manipulation import __StringFormatter, InvalidInputError

# Test valid input scenario
def test_valid_input():
    formatter = __StringFormatter("This is a test string.")
    assert formatter.input_string == "This is a test string."

# Test edge case with an empty string
def test_edge_case():
    formatter = __StringFormatter("")
    assert formatter.input_string == ""

# Test raising InvalidInputError with a non-string input
def test_invalid_input():
    with pytest.raises(InvalidInputError):
        formatter = __StringFormatter(12345)
