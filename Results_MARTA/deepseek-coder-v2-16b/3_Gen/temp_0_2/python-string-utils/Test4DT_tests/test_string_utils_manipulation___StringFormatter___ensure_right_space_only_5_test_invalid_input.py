
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

# Mocking the external function or class that might be used in __ensure_right_space_only
class MockIsString:
    @staticmethod
    def is_string(input_str):
        return isinstance(input_str, str)

def test_invalid_input():
    # Given an invalid input (not a string), we expect an InvalidInputError to be raised.
    with pytest.raises(InvalidInputError):
        formatter = __StringFormatter(12345)  # Passing an integer instead of a string
