
# Module: typesystem.base
# test_baseerror.py
from typesystem.base import BaseError, Message
import pytest

@pytest.fixture
def single_message_error():
    return BaseError(text="This field may not have more than 100 characters")

@pytest.fixture
def multiple_messages_error():
    errors = [Message(text="Invalid username", code="max_length"), Message(text="User not found", index=['users', 3, 'username'])]
    return BaseError(messages=errors)

# Test initialization with a single message
def test_baseerror_single_message():
    error = BaseError(text="This field may not have more than 100 characters")
    assert len(error._messages) == 1