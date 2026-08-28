
import pytest
from unittest.mock import patch
import string
import random
from string_utils.generation import random_string

# Test scenario 1: test_valid_input
def test_valid_input():
    with patch('random.choice', side_effect=lambda x: next(iter(x))):
        size = 9
        result = random_string(size)
        assert isinstance(result, str), "The result should be a string"
        assert len(result) == size, f"Expected string length to be {size}, but got {len(result)}"
        for char in result:
            assert char in (string.ascii_letters + string.digits), "All characters should be from the allowed set"

# Test scenario 2: test_edge_case
def test_edge_case():
    with pytest.raises(ValueError):
        random_string(0)
    with pytest.raises(ValueError):
        random_string(-1)
    with pytest.raises(ValueError):
        random_string(None)
    with pytest.raises(ValueError):
        random_string("invalid")

# Test scenario 3: test_invalid_input
def test_invalid_input():
    with pytest.raises(ValueError):
        random_string("9")
    with pytest.raises(ValueError):
        random_string(9.5)
    with pytest.raises(ValueError):
        random_string([1, 2, 3])
