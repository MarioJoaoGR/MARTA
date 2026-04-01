
import pytest
from string_utils.generation import random_string
import string
import random

def test_valid_input():
    size = 10
    result = random_string(size)
    assert isinstance(result, str), "The result should be a string"
    assert len(result) == size, f"Expected length {size}, but got {len(result)}"
    for char in result:
        assert char in (string.ascii_letters + string.digits), "All characters should be either uppercase/lowercase ASCII letters or digits"
