
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_valid_input():
    # Arrange
    input_string = "hello world"
    
    # Act
    formatter = __StringFormatter(input_string)
    
    # Assert
    assert isinstance(formatter.input_string, str), f"Expected a string but got {type(formatter.input_string).__name__}"
    assert formatter.input_string == input_string, "The stored input string does not match the provided input."
