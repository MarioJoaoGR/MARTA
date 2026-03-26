
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_valid_input():
    formatter = __StringFormatter("valid string")
    assert formatter.input_string == "valid string"

def test_invalid_input():
    with pytest.raises(InvalidInputError):
        __StringFormatter(12345)
