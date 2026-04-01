
import pytest
from string_utils.manipulation import shuffle
from string_utils.errors import InvalidInputError
import random

def test_valid_input():
    # Test with a valid input string
    input_string = "hello world"
    shuffled_string = shuffle(input_string)
    
    # Check that the output is not the same as the input
    assert input_string != shuffled_string
    
    # Check that the length of the output string is the same as the input string
    assert len(input_string) == len(shuffled_string)
    
    # Check that all characters from the input string are in the output string
    for char in input_string:
        assert char in shuffled_string
