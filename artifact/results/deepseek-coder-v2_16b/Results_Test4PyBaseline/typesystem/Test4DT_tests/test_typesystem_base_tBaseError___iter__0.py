
# Module: typesystem.base
from typesystem.base import BaseError, Message  # Importing Message class as it was undefined
import pytest

# Test cases for BaseError class initialization and error handling.
def test_BaseError_single_message():
    # Create a BaseError instance with a single message.
    error = BaseError(text="This field may not have more than 100 characters")
    
    # Assert that the error message is correctly set.
    assert error._messages[0].text == "This field may not have more than 100 characters"

def test_BaseError_multiple_messages():
    # Create a BaseError instance with multiple messages.
    errors = [Message(text="Invalid username", code="max_length"), Message(text="User not found", index=['users', 3, 'username'])]
    error = BaseError(messages=errors)
    
    # Assert that the list of messages is correctly set and iterable.
    assert len(error._messages) == 2
    for msg in error._messages:
        print(msg.text)  # Output will include both messages

def test_BaseError_validate():
    # Assuming MySchema is a schema class that uses BaseError for validation.
    class MySchema:
        @staticmethod
        def validate(data):
            if not isinstance(data, str) or len(data) > 100:
                raise BaseError(text="The input must be a string with no more than 100 characters.")
            return data  # Assuming validation passes

    try:
        data = "A" * 150  # This will trigger the validation error
        value = MySchema.validate(data)
    except BaseError as e:
        assert str(e) == "The input must be a string with no more than 100 characters."

def test_BaseError_validate_or_error():
    # Assuming MySchema is a schema class that uses BaseError for validation.
    class MySchema:
        @staticmethod
        def validate(data):
            if not isinstance(data, str) or len(data) > 100:
                raise BaseError(text="The input must be a string with no more than 100 characters.")
            return data  # Assuming validation passes
        
        @staticmethod
        def validate_or_error(data):
            try:
                value = MySchema.validate(data)
                return value, None
            except BaseError as e:
                return None, e

    data = "A" * 150  # This will trigger the validation error
    value, error = MySchema.validate_or_error(data)
    assert error is not None