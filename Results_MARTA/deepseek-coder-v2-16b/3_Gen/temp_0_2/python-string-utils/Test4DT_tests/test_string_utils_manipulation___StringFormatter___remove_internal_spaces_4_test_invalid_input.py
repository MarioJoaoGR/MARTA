
import pytest
from unittest.mock import patch
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_invalid_input():
    with pytest.raises(InvalidInputError):
        formatter = __StringFormatter(12345)  # Providing an invalid input type (int instead of str)
