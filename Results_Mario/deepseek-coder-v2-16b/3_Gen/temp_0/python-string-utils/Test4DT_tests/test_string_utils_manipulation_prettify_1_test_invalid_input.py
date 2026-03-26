
import pytest
from string_utils.manipulation import prettify
from string_utils.errors import InvalidInputError

def test_invalid_input():
    # Test with invalid input types (numbers, lists, etc.)
    with pytest.raises(InvalidInputError):
        assert prettify(123) == "123"  # Should handle numbers gracefully
