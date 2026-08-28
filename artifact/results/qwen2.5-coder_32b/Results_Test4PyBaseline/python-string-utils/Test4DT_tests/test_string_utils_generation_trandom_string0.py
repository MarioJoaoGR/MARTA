# Module: string_utils.generation
import pytest
from string_utils.generation import random_string

def test_random_string_valid_sizes():
    # Test with minimum size
    result = random_string(1)
    assert len(result) == 1
    assert result.isalnum()

    # Test with a typical size
    result = random_string(9)
    assert len(result) == 9
    assert result.isalnum()

    # Test with a larger size
    result = random_string(15)
    assert len(result) == 15
    assert result.isalnum()

def test_random_string_invalid_sizes():
    # Test with zero size
    with pytest.raises(ValueError):
        random_string(0)

    # Test with negative size
    with pytest.raises(ValueError):
        random_string(-5)

    # Test with non-integer size
    with pytest.raises(ValueError):
        random_string(3.5)

def test_random_string_consistency():
    # Check that the function generates different strings for multiple calls of the same size
    results = {random_string(10) for _ in range(10)}
    assert len(results) == 10, "Generated strings should be unique"

def test_random_string_characters():
    # Test that the generated string contains only alphanumeric characters
    result = random_string(20)
    assert all(c.isalnum() for c in result)
