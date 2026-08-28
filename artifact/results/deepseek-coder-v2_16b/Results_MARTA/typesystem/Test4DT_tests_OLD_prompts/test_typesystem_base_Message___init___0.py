
import pytest
from typesystem.base import Message, Position

def test_valid_inputs():
    msg = Message(text="This field may not be blank.")
    assert msg.text == "This field may not be blank."
    assert msg.code == "custom"
    assert msg.index == []
    assert msg.start_position is None
    assert msg.end_position is None


def test_with_code():
    msg = Message(text="This field may not be blank.", code="required")
    assert msg.text == "This field may not be blank."
    assert msg.code == "required"
    assert msg.index == []
    assert msg.start_position is None
    assert msg.end_position is None

def test_with_key():
    msg = Message(text="Invalid key", key='username')
    assert msg.text == "Invalid key"
    assert msg.code == "custom"
    assert msg.index == ['username']
    assert msg.start_position is None
    assert msg.end_position is None

def test_with_index():
    msg = Message(text="Error at index 2", index=['users', 1, 'username'])
    assert msg.text == "Error at index 2"
    assert msg.code == "custom"
    assert msg.index == ['users', 1, 'username']
    assert msg.start_position is None
    assert msg.end_position is None

