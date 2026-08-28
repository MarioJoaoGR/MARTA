
import pytest
from flutes.iterator import Range

def test_invalid_arguments():
    # Test with 0 arguments
    with pytest.raises(ValueError, match="Range should be called the same way as the builtin `range`"):
        Range()
    
    # Test with more than 3 arguments
    with pytest.raises(ValueError, match="Range should be called the same way as the builtin `range`"):
        Range(1, 2, 3, 4)

def test_range_one_argument():
    r = Range(10)
    assert list(r) == list(range(10))
    assert r[0] == 0
    assert r[9] == 9

def test_range_two_arguments():
    r = Range(1, 11)
    assert list(r) == list(range(1, 11))
    assert r[0] == 1
    assert r[9] == 10

def test_range_three_arguments():
    r = Range(1, 11, 2)
    assert list(r) == list(range(1, 11, 2))
    assert r[0] == 1
    assert r[4] == 9

def test_indexing():
    r = Range(1, 11, 2)
    assert r[0] == 1