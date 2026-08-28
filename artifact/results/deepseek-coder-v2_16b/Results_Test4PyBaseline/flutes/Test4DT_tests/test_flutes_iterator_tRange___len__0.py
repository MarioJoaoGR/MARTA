# Module: flutes.iterator
import pytest
from flutes.iterator import Range

# Test cases for initializing the Range class with different numbers of arguments
def test_range_one_argument():
    r = Range(10)
    assert len(r) == 10, "Range length should be 10 when initialized with one argument."
    assert r[0] == 0, "The first element should be 0."
    assert r[2] == 2, "The third element should be 2."
    assert r[4] == 4, "The fifth element should be 4."

def test_range_two_arguments():
    r = Range(1, 10)
    assert len(r) == 9, "Range length should be 9 when initialized with two arguments."
    assert r[0] == 1, "The first element should be 1."
    assert r[2] == 3, "The third element should be 3."
    assert r[4] == 5, "The fifth element should be 5."

def test_range_three_arguments():
    r = Range(1, 11, 2)
    assert len(r) == 5, "Range length should be 5 when initialized with three arguments."
    assert r[0] == 1, "The first element should be 1."
    assert r[1] == 3, "The second element should be 3."
    assert r[2] == 5, "The third element should be 5."

# Test cases for handling invalid number of arguments
def test_range_invalid_number_of_arguments():
    with pytest.raises(ValueError):
        Range()
    with pytest.raises(ValueError):
        Range(1, 2, 3, 4)

# Additional tests to ensure the class behaves as expected for different ranges
def test_range_indexing():
    r = Range(10)
    assert r[9] == 9, "The last element should be 9."
    
    r = Range(1, 10 + 1)
    assert r[0] == 1, "The first element should be 1."
    assert r[2] == 3, "The third element should be 3."
    assert r[4] == 5, "The fifth element should be 5."
    
    r = Range(1, 11, 2)
    assert r[0] == 1, "The first element should be 1."
    assert r[1] == 3, "The second element should be 3."
    assert r[2] == 5, "The third element should be 5."

if __name__ == "__main__":
    pytest.main()
