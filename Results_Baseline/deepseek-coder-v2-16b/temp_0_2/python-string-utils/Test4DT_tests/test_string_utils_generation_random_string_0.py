# Module: string_utils.generation
import pytest
import random
import string
from string_utils import random_string

# Test cases for the random_string function
def test_random_string_valid():
    # Test with a valid size
    result = random_string(9)
    assert isinstance(result, str), "The result should be a string"
    assert len(result) == 9, f"Expected string length of 9, but got {len(result)}"

def test_random_string_invalid():
    # Test with an invalid size (should raise ValueError)
    with pytest.raises(ValueError):
        random_string(-1)
    with pytest.raises(ValueError):
        random_string(0)
    with pytest.raises(ValueError):
        random_string('a')

def test_random_string_length():
    # Test multiple sizes to ensure randomness and length consistency
    size = 15
    results = [random_string(size) for _ in range(10)]
    lengths = [len(result) for result in results]
    assert all(length == size for length in lengths), "All generated strings should have the specified length"

def test_random_string_character_set():
    # Test if characters are within the expected set (uppercase, lowercase, digits)
    size = 10
    result = random_string(size)
    assert all(char in string.ascii_letters + string.digits for char in result), "All characters should be either uppercase/lowercase letters or digits"
