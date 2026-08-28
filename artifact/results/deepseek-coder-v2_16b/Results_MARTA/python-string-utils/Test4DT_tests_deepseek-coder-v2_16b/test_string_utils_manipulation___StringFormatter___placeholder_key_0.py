
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError
from uuid import uuid4

# Test valid input scenario
def test_valid_input():
    formatter = __StringFormatter("hello world")
    assert formatter.input_string == "hello world"

# Test handling None input scenario
def test_none_input():
    with pytest.raises(InvalidInputError):
        __StringFormatter(None)

# Test raising InvalidInputError with non-string input scenario
def test_invalid_input():
    with pytest.raises(InvalidInputError):
        __StringFormatter(12345)
