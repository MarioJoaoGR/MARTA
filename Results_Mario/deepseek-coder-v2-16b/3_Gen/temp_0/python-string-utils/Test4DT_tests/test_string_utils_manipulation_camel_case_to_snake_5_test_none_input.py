
import pytest
from string_utils.manipulation import camel_case_to_snake, InvalidInputError

def test_none_input():
    # Test case for when the input is None
    input_string = None
    expected_output = input_string
    
    with pytest.raises(InvalidInputError):
        result = camel_case_to_snake(input_string)
