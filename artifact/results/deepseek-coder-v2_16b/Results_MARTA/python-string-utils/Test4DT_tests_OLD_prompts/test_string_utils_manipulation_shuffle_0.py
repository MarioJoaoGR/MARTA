
import pytest
from unittest.mock import patch
from string_utils.manipulation import shuffle
from string_utils.errors import InvalidInputError

# Test valid input

# Test invalid input (non-string)
def test_invalid_input():
    with pytest.raises(InvalidInputError):
        shuffle(12345)  # Should raise InvalidInputError since 12345 is not a string