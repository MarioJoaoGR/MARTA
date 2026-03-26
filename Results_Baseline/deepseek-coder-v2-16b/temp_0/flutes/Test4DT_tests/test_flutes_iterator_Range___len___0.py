
import pytest
from flutes.iterator import Range

# Test initialization with different numbers of arguments
def test_range_init():
    r1 = Range(10)
    assert len(r1) == 10, "Range with end value should have length equal to the end value."
    
    r2 = Range(1, 10 + 1)
    assert len(r2) == 10, "Range with start and end values should have length equal to (end - start)."
    
    r3 = Range(1, 11, 2)
    assert len(r3) == 5, "Range with start, end, and step values should have correct length."

# Test initialization with invalid number of arguments
def test_range_init_invalid():
    with pytest.raises(ValueError):
        Range()
    with pytest.raises(ValueError):
        Range(1, 2, 3, 4)

# Test indexing in the range
def test_range_indexing():
    r = Range(1, 11, 2)
    assert r[0] == 1, "Indexing should return correct value at position 0."
    assert r[1] == 3, "Indexing should return correct value at position 1."
    assert r[2] == 5, "Indexing should return correct value at position 2."
    assert r[3] == 7, "Indexing should return correct value at position 3."
    assert r[4] == 9, "Indexing should return correct value at position 4."

# Test slicing in the range
def test_range_slicing():
    r = Range(1, 11, 2)
    sliced_r = [r[i] for i in range(len(r)) if i % 2 == 0]