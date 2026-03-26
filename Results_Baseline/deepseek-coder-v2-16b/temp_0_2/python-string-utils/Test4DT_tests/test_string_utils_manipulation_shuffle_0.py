# Module: string_utils.manipulation
import pytest
from string_utils.manipulation import shuffle
from string_utils.errors import InvalidInputError
import random

# Helper function to check if a variable is a string
def is_string(input_var):
    return isinstance(input_var, str)

# Test cases for the shuffle function
def test_shuffle_simple_string():
    result = shuffle('hello world')
    assert is_string(result), "Expected a string but got a different type"
    assert len(result) == 11, "Expected the shuffled string to have the same length as the original"
    # Check that all characters are present in the shuffled string
    for char in 'hello world':
        assert char in result, f"Character {char} not found in the shuffled string"

def test_shuffle_non_string():
    with pytest.raises(InvalidInputError):
        shuffle(12345)

# Additional tests can be added to cover more edge cases or specific scenarios as needed.
