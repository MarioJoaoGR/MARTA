
import pytest
from string_utils.manipulation import __StringFormatter

def test_valid_input():
    # Test that the formatter accepts a valid string input
    try:
        formatter = __StringFormatter("valid string")
        assert isinstance(formatter, __StringFormatter)
        assert formatter.input_string == "valid string"
    except Exception as e:
        pytest.fail(f"Unexpected error occurred: {e}")
