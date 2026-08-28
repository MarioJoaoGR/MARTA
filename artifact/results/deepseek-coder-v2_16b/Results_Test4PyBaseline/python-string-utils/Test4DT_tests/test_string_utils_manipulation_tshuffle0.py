# Module: string_utils.manipulation
import pytest
from string_utils.manipulation import shuffle
from string_utils.errors import InvalidInputError
import random

# Helper function to check if an object is a string
def is_string(obj):
    return isinstance(obj, str)

@pytest.mark.parametrize("input_string, expected", [
    ('hello world', 'l wodheorll'),  # Shuffling a simple string
    ('123!@#', '21@!#3'),             # Shuffling a string with special characters
    ('', ''),                        # Shuffling an empty string
    ('a', 'a')                       # Shuffling a single character string
])
def test_shuffle(input_string, expected):
    assert is_string(input_string), "Input should be a string"
    result = shuffle(input_string)
    assert len(result) == len(expected), f"Shuffled string length does not match: {len(result)} != {len(expected)}"
    # Check if all characters are present in the shuffled string
    for char in expected:
        assert char in result, f"Character '{char}' missing from shuffled string"

def test_shuffle_invalid_input():
    with pytest.raises(InvalidInputError):
        shuffle(42)  # Attempting to shuffle a non-string input should raise InvalidInputError
