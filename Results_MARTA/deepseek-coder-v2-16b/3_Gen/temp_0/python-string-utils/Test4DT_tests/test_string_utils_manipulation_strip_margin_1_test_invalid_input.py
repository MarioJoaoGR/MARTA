
import pytest
from string_utils.manipulation import strip_margin, InvalidInputError

def test_invalid_input():
    with pytest.raises(InvalidInputError):
        strip_margin(12345)  # Providing an integer instead of a string should raise InvalidInputError
