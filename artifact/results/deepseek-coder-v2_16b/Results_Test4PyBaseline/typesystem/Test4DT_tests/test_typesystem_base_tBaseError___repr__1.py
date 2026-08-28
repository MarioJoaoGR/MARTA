
# Module: typesystem.base
# test_baseerror.py
from typesystem.base import BaseError, Message, Position
import pytest

def test_baseerror__repr__single_message():
    message = Message(text="Invalid input", code="invalid_input")
    error = BaseError(messages=[message])
    assert repr(error) == "BaseError(text='Invalid input', code='invalid_input')"

def test_baseerror__repr__multiple_messages():
    messages = [Message(text="First error", code="e1"), Message(text="Second error", code="e2")]
    error = BaseError(messages=messages)