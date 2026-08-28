
import pytest
from typesystem.base import BaseError, Message, Position

# Test for valid inputs

# Test for edge cases

# Test for invalid inputs
def test_invalid_inputs():
    with pytest.raises(AssertionError):
        BaseError(text=None)