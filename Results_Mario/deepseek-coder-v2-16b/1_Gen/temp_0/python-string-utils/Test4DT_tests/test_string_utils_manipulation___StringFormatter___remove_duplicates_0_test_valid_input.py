
import pytest
from string_utils.manipulation import __StringFormatter

def test_valid_input():
    # Arrange
    input_string = "valid string"
    
    # Act
    formatter = __StringFormatter(input_string)
    
    # Assert
    assert formatter.input_string == input_string
