
import pytest
from flutes.iterator import drop

def test_invalid_inputs_negative_n():
    """Test with negative n raises ValueError."""
    with pytest.raises(ValueError):
        list(drop(-1, [1, 2, 3]))

def test_valid_input_zero_n():
    """Test with n=0 returns the original iterable."""
    result = list(drop(0, [1, 2, 3]))
    assert result == [1, 2, 3]

def test_valid_input_positive_n():
    """Test with positive n drops the first n elements."""
    result = list(drop(2, [1, 2, 3, 4, 5]))
    assert result == [3, 4, 5]

def test_valid_input_exceeding_length():
    """Test with n greater than length of iterable returns empty iterator."""
    result = list(drop(10, [1, 2, 3]))
    assert result == []

def test_valid_input_with_generator():
    """Test with a generator as input."""
    gen = (x for x in range(5))
    result = list(drop(2, gen))
    assert result == [2, 3, 4]

def test_valid_input_with_tuple():
    """Test with a tuple as input."""
    result = list(drop(1, (10, 20, 30)))
    assert result == [20, 30]

def test_valid_input_with_lazy_list():
    """Test with LazyList as input."""
    from flutes.iterator import LazyList
    lazy_list = LazyList(range(5))
    result = list(drop(3, lazy_list))
    assert result == [3, 4]
