
import random
from string_utils.manipulation import shuffle, InvalidInputError
import pytest

def test_valid_input():
    # Test with a typical string input
    input_string = "hello world"
    shuffled_string = shuffle(input_string)
    
    # Check that the output is not equal to the input (to ensure it's actually shuffled)
    assert input_string != shuffled_string, f"Expected a different order of characters but got {shuffled_string}"
    
    # Check that the length of the strings are the same
    assert len(input_string) == len(shuffled_string), "Lengths of input and output strings should be equal"
