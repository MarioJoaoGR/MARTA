
import pytest
from flutes.iterator import Range

# Test cases for initializing a Range object with different numbers of arguments

def test_range_one_argument():
    r = Range(10)  # Creates a range from 0 to 9 (exclusive).
    assert r[0] == 0, "Indexing the first element should return 0"
    assert r[2] == 2, "Indexing the third element should return 2"
    assert r[4] == 4, "Indexing the fifth element should return 4"

def test_range_two_arguments():
    r = Range(1, 10 + 1)  # Creates a range from 1 to 10 (exclusive).
    assert r[0] == 1, "Indexing the first element should return 1"
    assert r[2] == 3, "Indexing the third element should return 3"
    assert r[4] == 5, "Indexing the fifth element should return 5"

def test_range_three_arguments():
    r = Range(1, 11, 2)  # Creates a range from 1 to 10 with a step of 2.
    assert r[0] == 1, "Indexing the first element should return 1"
    assert r[2] == 5, "Indexing the third element should return 5"
    assert r[4] == 9, "Indexing the fifth element should return 9"

# Test case for invalid number of arguments
def test_range_invalid_number_of_arguments():
    with pytest.raises(ValueError):
        Range()  # No arguments provided
    with pytest.raises(ValueError):
        Range(1, 2, 3, 4)  # More than three arguments provided
