
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_valid_input():
    # Test that a valid string input does not raise an error
    formatter = __StringFormatter("valid string")
    assert formatter.input_string == "valid string"

    # Additional assertion to ensure the class handles strings correctly
    with pytest.raises(InvalidInputError):
        bad_formatter = __StringFormatter(12345)  # This should raise InvalidInputError
