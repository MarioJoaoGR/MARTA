
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_valid_input():
    # Test that the formatter accepts a valid string input
    try:
        formatter = __StringFormatter("valid string")
        assert isinstance(formatter.input_string, str)
        assert formatter.input_string == "valid string"
    except InvalidInputError as e:
        pytest.fail(f"Unexpected InvalidInputError: {e}")

def test_invalid_input():
    # Test that the formatter raises an error for non-string input
    with pytest.raises(InvalidInputError):
        __StringFormatter(12345)
