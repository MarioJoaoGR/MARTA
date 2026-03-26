
import pytest
from string_utils.manipulation import __StringFormatter
from string_utils.errors import InvalidInputError

def test_invalid_input():
    with pytest.raises(InvalidInputError):
        formatter = __StringFormatter(12345)  # Providing an invalid input type (int instead of str)
