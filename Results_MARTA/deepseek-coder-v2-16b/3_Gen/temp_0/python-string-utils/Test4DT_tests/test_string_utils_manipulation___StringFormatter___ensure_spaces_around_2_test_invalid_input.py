
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_invalid_input():
    with pytest.raises(InvalidInputError):
        formatter = __StringFormatter(12345)  # Providing an integer instead of a string
