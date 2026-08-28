
import pytest
from typesystem.base import BaseError, Message

# Scenario 1: Test instantiation with a single message using positional arguments

# Scenario 2: Test instantiation with multiple messages using keyword arguments
def test_instantiate_with_multiple_messages():
    errors = [
        Message(text="Invalid username.", code="invalid_key", key="username"),
        Message(text="Username too long.", code="max_length", key="username")
    ]
    error_with_multiple_messages = BaseError(messages=errors)
    assert isinstance(error_with_multiple_messages, BaseError)
    assert len(error_with_multiple_messages.messages()) == 2
    assert [msg.text for msg in error_with_multiple_messages.messages()] == ["Invalid username.", "Username too long."]

# Scenario 3: Test instantiation with a single message using keyword arguments only