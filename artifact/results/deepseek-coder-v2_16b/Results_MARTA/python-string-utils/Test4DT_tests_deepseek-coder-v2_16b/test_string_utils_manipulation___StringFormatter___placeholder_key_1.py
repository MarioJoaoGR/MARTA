
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError
from uuid import uuid4

# Mocking is not necessary for this task as we are directly instantiating and testing the class with simple values

def test_valid_input():
    # Arrange: Create an instance of __StringFormatter with a valid string input
    formatter = __StringFormatter("hello world")
    
    # Act: No action needed, just assert the result
    assert formatter.input_string == "hello world"

def test_none_input():
    # Arrange: Attempt to create an instance of __StringFormatter with None input
    with pytest.raises(InvalidInputError):
        __StringFormatter(None)

def test_invalid_input():
    # Arrange: Attempt to create an instance of __StringFormatter with a non-string input (e.g., integer)
    with pytest.raises(InvalidInputError):
        __StringFormatter(12345)
