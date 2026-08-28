
# Module: typesystem.base
# test_typesystem_base.py
from typesystem.base import Message
import pytest

def test_message_creation():
    msg = Message(text="This field must be at least 10 characters long.")
    assert msg.text == "This field must be at least 10 characters long."