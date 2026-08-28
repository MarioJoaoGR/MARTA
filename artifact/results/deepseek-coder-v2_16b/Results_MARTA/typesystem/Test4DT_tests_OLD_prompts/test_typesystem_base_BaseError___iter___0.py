
import pytest
from typesystem.base import BaseError, Message

# Test instantiating with a single message
def test_instantiate_with_single_message():
    error = BaseError(text="This field may not be blank.", code="required", key="username")
    assert isinstance(error, BaseError)
    assert len(error.messages()) == 1
    assert error['username'] == 'This field may not be blank.'

# Test instantiating with multiple messages

# Test iterating over messages

# Test comparing errors for equality