
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_valid_input():
    # Arrange
    input_string = "hello world"
    
    # Act
    formatter = __StringFormatter(input_string)
    
    # Assert
    assert isinstance(formatter, __StringFormatter), "The instance should be an instance of __StringFormatter"
    assert formatter.input_string == input_string, "The input string should match the provided input"
