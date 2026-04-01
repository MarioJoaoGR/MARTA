
import pytest
from string_utils.generation import random_string
import string
import random

@pytest.mark.parametrize("size", [1, 5, 10])
def test_valid_input(size):
    result = random_string(size)
    assert isinstance(result, str), "The function should return a string"
    assert len(result) == size, f"Expected string length to be {size}, but got {len(result)}"
    for char in result:
        assert char in (string.ascii_letters + string.digits), "String contains invalid characters"
