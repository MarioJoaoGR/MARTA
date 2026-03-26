
import re
import pytest
from string_utils.manipulation import camel_case_to_snake, InvalidInputError

def test_edge_case_none_input():
    # Arrange
    input_string = None
    
    # Act and Assert
    with pytest.raises(InvalidInputError):
        camel_case_to_snake(input_string)
