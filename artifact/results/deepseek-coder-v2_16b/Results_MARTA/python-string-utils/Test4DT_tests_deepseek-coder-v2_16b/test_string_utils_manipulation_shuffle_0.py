
import pytest
from string_utils.manipulation import shuffle
from string_utils.errors import InvalidInputError
import random

# Test for valid input
def test_valid_input():
    # Setup: Real instance of shuffle with minimal args
    input_string = "hello world"
    
    # Call the function
    shuffled_string = shuffle(input_string)
    
    # Assert that the output is a string and has the same length as the input
    assert isinstance(shuffled_string, str), "Expected a string but got a different type"
    assert len(shuffled_string) == len(input_string), "Expected strings to be of equal length"
    
    # Assert that the shuffled string contains the same characters as the input
    for char in input_string:
        assert char in shuffled_string, f"Character '{char}' not found in shuffled string"

# Test handling None input
def test_edge_case_none():
    # Setup: None
    input_string = None
    
    # Call the function and expect an InvalidInputError to be raised
    with pytest.raises(InvalidInputError):
        shuffle(input_string)

# Test raising InvalidInputError with non-string input
def test_invalid_input():
    # Setup: Real instance of shuffle with a non-string argument
    input_string = 12345
    
    # Call the function and expect an InvalidInputError to be raised
    with pytest.raises(InvalidInputError):
        shuffle(input_string)
