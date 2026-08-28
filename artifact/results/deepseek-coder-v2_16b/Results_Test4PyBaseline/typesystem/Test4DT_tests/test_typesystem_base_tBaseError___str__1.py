
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

# Existing test cases:
def test_single_message_error(single_message_error):
    assert single_message_error._messages[0].text == "This field may not have more than 100 characters"
    assert len(single_message_error._messages) == 1
    assert isinstance(single_message_error, BaseError)

def test_multiple_messages_error(multiple_messages_error):
    messages = multiple_messages_error.messages()
    assert any(msg.text for msg in messages if msg.text == "Invalid username")
    assert any(msg.text for msg in messages if msg.text == "User not found")
    assert len(multiple_messages_error._messages) == 2

# Additional test cases to cover the __str__ method:
def test_single_message_error_str(single_message_error):
    expected_output = single_message_error._messages[0].text
    assert str(single_message_error) == expected_output

def test_multiple_messages_error_str(multiple_messages_error):
    messages = multiple_messages_error.messages()
    dict_representation = dict(multiple_messages_error)
    # Since the __str__ method should return a string representation of the dictionary, we need to check if it matches the expected format