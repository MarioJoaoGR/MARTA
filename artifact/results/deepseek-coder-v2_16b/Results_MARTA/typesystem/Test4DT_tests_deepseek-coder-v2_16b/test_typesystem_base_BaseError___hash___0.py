
import pytest
from typesystem.base import BaseError, Message, Position

# Scenario 1: Test instantiation with a single error message
def test_valid_single_message():
    error = BaseError(text='Invalid input', code='invalid_input')
    assert isinstance(error, BaseError)
    assert len(error._messages) == 1
    assert error._messages[0].text == 'Invalid input'
    assert error._messages[0].code == 'invalid_input'

# Scenario 2: Test instantiation with multiple error messages
def test_valid_multiple_messages():
    errors = [Message(text='First error', key='field1'), Message(text='Second error', key='field2')]
    error_with_multiple_messages = BaseError(messages=errors)
    assert isinstance(error_with_multiple_messages, BaseError)
    assert len(error_with_multiple_messages._messages) == 2
    assert error_with_multiple_messages._messages[0].text == 'First error'
    assert error_with_multiple_messages._messages[1].text == 'Second error'

# Scenario 3: Test instantiation with missing required parameters
def test_invalid_instantiation():
    try:
        BaseError()
    except AssertionError as e:
        print(e)
