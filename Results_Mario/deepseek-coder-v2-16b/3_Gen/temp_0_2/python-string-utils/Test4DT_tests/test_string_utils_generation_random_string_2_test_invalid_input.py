
import pytest
from string_utils.generation import random_string
import random
import string

def test_invalid_input():
    with pytest.raises(ValueError):
        assert random_string(None)  # Test with None
        assert random_string(-1)   # Test with negative number
        assert random_string("test")  # Test with a string
