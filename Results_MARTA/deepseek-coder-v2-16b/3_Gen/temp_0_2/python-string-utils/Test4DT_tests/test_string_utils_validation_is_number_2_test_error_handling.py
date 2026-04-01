
import re
from string_utils.validation import InvalidInputError, is_number
import pytest

def test_error_handling():
    with pytest.raises(InvalidInputError):
        assert not is_number(123)  # Test with an integer
        assert not is_number(True)  # Test with a boolean
        assert not is_number([1, 2, 3])  # Test with a list
        assert not is_number({'key': 'value'})  # Test with a dictionary
        assert not is_number(None)  # Test with None
