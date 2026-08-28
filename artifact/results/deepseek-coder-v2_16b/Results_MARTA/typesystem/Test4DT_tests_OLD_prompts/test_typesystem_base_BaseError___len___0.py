
import pytest
from typesystem.base import BaseError, Message, Position

# Test instantiating with a single message
def test_instantiate_with_single_message():
    error = BaseError(text="This field may not be blank.", code="required", key="username")
    assert len(error) == 1

# Test instantiating with multiple messages

# Test instantiating with invalid inputs (should raise AssertionError)