
import pytest
from flutes.iterator import Range

def test_range_indexing():
    r = Range(10)
    assert r[0] == 0
    assert r[2] == 2
    assert r[4] == 4

def test_range_negative_indexing():
    r = Range(10)
    assert r[-1] == 9
    assert r[-3] == 7
    assert r[-5] == 5

def test_range_with_start_end():
    r = Range(1, 11)
    assert r[0] == 1
    assert r[2] == 3
    assert r[4] == 5

def test_range_with_start_end_step():
    r = Range(1, 11, 2)
    assert r[0] == 1
    assert r[2] == 5
    assert r[4] == 9

def test_range_invalid_arguments():
    with pytest.raises(ValueError):
        Range()
    with pytest.raises(ValueError):
        Range(1, 2, 3, 4)
