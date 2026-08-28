
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError
from uuid import uuid4

# Mocking is not necessary for this task as we are directly instantiating and testing the class with simple values

def test_valid_input():
    # Setup: Real instance of __StringFormatter with minimal args
    formatter = __StringFormatter("hello world")
    
    # Assertions
    assert isinstance(formatter.input_string, str)
    assert formatter.input_string == "hello world"

def test_none_input():
    # Setup: None input
    with pytest.raises(InvalidInputError):
        __StringFormatter(None)

def test_invalid_input():
    # Setup: Non-string input
    with pytest.raises(InvalidInputError):
        __StringFormatter(12345)
