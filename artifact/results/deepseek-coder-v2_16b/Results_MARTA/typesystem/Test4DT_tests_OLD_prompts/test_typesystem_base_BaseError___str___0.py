
import pytest
from typesystem.base import BaseError, Message, Position

# Test valid inputs scenario

# Test edge cases scenario

# Test invalid initialization scenario
def test_invalid_initialization():
    with pytest.raises(AssertionError):
        BaseError()
    with pytest.raises(AssertionError):
        BaseError(text=None, code=None, key=None)