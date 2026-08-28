
# Module: typesystem.base
# test_baseerror.py
from typesystem.base import BaseError, Message, Position
import pytest

def test_baseerror_single_message():
    error = BaseError(text="Invalid input", code="invalid_input")
    assert len(error._messages) == 1
    assert error._messages[0].text == "Invalid input"
    assert error._messages[0].code == "invalid_input"

def test_baseerror_multiple_messages():
    errors = [Message(text="First error", code="e1"), Message(text="Second error", code="e2")]
    error_with_multiple = BaseError(messages=errors)
    assert len(error_with_multiple._messages) == 2
    for i, msg in enumerate(error_with_multiple._messages):
        if i == 0:
            assert msg.text == "First error"