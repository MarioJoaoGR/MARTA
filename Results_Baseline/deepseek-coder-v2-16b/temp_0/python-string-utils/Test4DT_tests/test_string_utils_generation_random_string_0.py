# Module: string_utils.generation
import pytest
import random
import string
from string_utils import random_string

def test_random_string_valid():
    size = 10
    result = random_string(size)
    assert isinstance(result, str), "The result should be a string"
    assert len(result) == size, f"Expected string length to be {size}, but got {len(result)}"

def test_random_string_invalid():
    with pytest.raises(ValueError):
        random_string(-1)

def test_random_string_edge_case():
    size = 1
    result = random_string(size)
    assert isinstance(result, str), "The result should be a string"
    assert len(result) == size, f"Expected string length to be {size}, but got {len(result)}"
