
import pytest
from flutes.iterator import Range

# Initialization tests
def test_range_one_argument():
    r = Range(10)
    assert r.l == 0
    assert r.r == 10
    assert r.step == 1
    assert r.val == 0
    assert r.length == 10

def test_range_two_arguments():
    r = Range(1, 10)
    assert r.l == 1
    assert r.r == 10
    assert r.step == 1
    assert r.val == 1
    assert r.length == 9

def test_range_three_arguments():
    r = Range(1, 11, 2)
    assert r.l == 1
    assert r.r == 11
    assert r.step == 2
    assert r.val == 1
    assert r.length == 5

def test_range_invalid_number_of_arguments():
    with pytest.raises(ValueError):
        Range()
    with pytest.raises(ValueError):
        Range(1, 2, 3, 4)

# Indexing tests
def test_range_index_access():
    r = Range(1, 11, 2)
    assert r[0] == 1
    assert r[1] == 3
    assert r[2] == 5
    assert r[3] == 7