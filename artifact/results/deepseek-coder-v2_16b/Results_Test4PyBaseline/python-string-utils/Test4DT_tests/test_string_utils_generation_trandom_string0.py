# Module: string_utils.generation
import pytest
import random
import string
from string_utils import generation as sut  # Assuming the module is named accordingly

# Test cases for random_string function
def test_random_string_valid_size():
    size = 9
    result = sut.random_string(size)
    assert isinstance(result, str), "The result should be a string"
    assert len(result) == size, f"Expected string length to be {size}, but got {len(result)}"

def test_random_string_invalid_size():
    invalid_sizes = [-1, 0, -5, 'a']
    for size in invalid_sizes:
        with pytest.raises(ValueError):
            sut.random_string(size)

def test_random_string_minimum_valid_size():
    size = 1
    result = sut.random_string(size)
    assert isinstance(result, str), "The result should be a string"
    assert len(result) == size, f"Expected string length to be {size}, but got {len(result)}"
