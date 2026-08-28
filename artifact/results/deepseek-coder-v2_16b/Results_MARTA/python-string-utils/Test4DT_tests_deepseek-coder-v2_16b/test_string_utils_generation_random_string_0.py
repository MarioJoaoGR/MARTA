
import pytest
from string_utils.generation import random_string
import string
import random

def test_random_string_valid_size():
    size = 10
    result = random_string(size)
    assert len(result) == size

def test_random_string_invalid_size():
    with pytest.raises(ValueError):
        random_string(-1)

def test_random_string_zero_size():
    with pytest.raises(ValueError):
        random_string(0)

def test_random_string_large_size():
    size = 50
    result = random_string(size)
    assert len(result) == size

def test_random_string_contains_only_letters_and_digits():
    size = 15
    result = random_string(size)
    assert all(c in string.ascii_letters + string.digits for c in result)
