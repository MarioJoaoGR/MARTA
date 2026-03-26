
import pytest
from flutes.iterator import Range

def test_range_basic():
    r = Range(10)
    assert list(r) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_range_with_start_and_stop():
    r = Range(1, 10 + 1)
    assert list(r) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_range_with_start_stop_and_step():
    r = Range(1, 11, 2)
    assert list(r) == [1, 3, 5, 7, 9]

def test_range_indexing():
    r = Range(1, 11, 2)
    assert r[0] == 1
    assert r[1] == 3
    assert r[2] == 5
    assert r[3] == 7
    assert r[4] == 9

def test_range_iteration():
    r = Range(1, 11, 2)
    itr = iter(r)
    assert next(itr) == 1
    assert next(itr) == 3
    assert next(itr) == 5
    assert next(itr) == 7
    assert next(itr) == 9
    with pytest.raises(StopIteration):
        next(itr)
