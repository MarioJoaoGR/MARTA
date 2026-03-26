# Module: pytutils.iters
import pytest
from pytutils.iters import dedupe_iter

# Test cases for dedupe_iter function

def test_dedupe_iter_default_hash():
    """Test dedupe_iter with the default hash function."""
    result = list(dedupe_iter([1, 2, 3, 2, 1]))
    assert result == [1, 2, 3]

def test_dedupe_iter_custom_hash():
    """Test dedupe_iter with a custom hash function."""
    def custom_hash(x):
        return x % 10
    
    result = list(dedupe_iter([11, 22, 33, 22, 11], custom_hash))
    assert result == [11, 22, 33]

def test_dedupe_iter_generator():
    """Test dedupe_iter with a generator expression."""
    result = list(dedupe_iter((x * x for x in range(10))))
    expected = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    assert result == expected

def test_dedupe_iter_empty():
    """Test dedupe_iter with an empty iterator."""
    result = list(dedupe_iter([]))
    assert list(result) == []

def test_dedupe_iter_single_item():
    """Test dedupe_iter with a single item in the iterator."""
    result = list(dedupe_iter([1]))
    assert list(result) == [1]

def test_dedupe_iter_none_items():
    """Test dedupe_iter with None items in the iterator."""
    result = list(dedupe_iter([None, 2, None, 4]))
    assert list(result) == [None, 2, 4]

def test_dedupe_iter_large_data():
    """Test dedupe_iter with a large dataset to ensure it handles memory efficiently."""
    # Generate a large list of random numbers
    import random
    large_list = [random.randint(1, 1000) for _ in range(1000)]
    result = list(dedupe_iter(large_list))
    assert len(result) == len(set(large_list))

if __name__ == "__main__":
    pytest.main()
