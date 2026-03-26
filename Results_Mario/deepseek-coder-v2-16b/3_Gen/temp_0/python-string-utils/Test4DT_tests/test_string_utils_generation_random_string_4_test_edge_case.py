
import pytest
from string_utils.generation import random_string
import string
import random

def test_edge_case():
    with pytest.raises(ValueError):
        assert random_string(-1) is None  # This should raise a ValueError because size < 1
        assert random_string(0) is None   # This should also raise a ValueError because size == 0

    # Test with valid size
    size = 10
    random_str = random_string(size)
    assert isinstance(random_str, str), "The result should be a string"
    assert len(random_str) == size, f"Expected string length to be {size}, but got {len(random_str)}"
