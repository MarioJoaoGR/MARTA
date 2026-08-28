
import pytest
from typesystem.base import BaseError, Message

# Scenario 1: Test instantiation with a single message
def test_valid_single_message():
    error = BaseError(text='This field may not be blank.', code='required', key='username')
    assert isinstance(error, BaseError)
    assert len(error.messages()) == 1
    assert error.messages()[0].text == 'This field may not be blank.'

# Scenario 2: Test instantiation with multiple messages
def test_valid_multiple_messages():
    errors = [Message(text='Invalid username.', code='invalid_key', key='username'), Message(text='Username too long.', code='max_length', key='username')]
    error_with_multiple_messages = BaseError(messages=errors)
    assert isinstance(error_with_multiple_messages, BaseError)
    assert len(error_with_multiple_messages.messages()) == 2
    messages = error_with_multiple_messages.messages()
    assert all([msg.text in ['Invalid username.', 'Username too long.'] for msg in messages])

# Scenario 3: Test instantiation without providing any message details
def test_error_case_missing_message():
    with pytest.raises(AssertionError):
        error = BaseError()
