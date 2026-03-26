# Module: flutes.iterator
# test_range.py
from flutes.iterator import Range

def test_range_with_end_only():
    r = Range(10)
    assert len(r) == 10, "Length of range should be 10"
    assert r[0] == 0, "First element should be 0"
    assert r[2] == 2, "Third element should be 2"
    assert r[4] == 4, "Fifth element should be 4"

def test_range_with_start_and_end():
    r = Range(1, 10 + 1)
    assert len(r) == 10, "Length of range should be 10"
    assert r[0] == 1, "First element should be 1"
    assert r[2] == 3, "Third element should be 3"
    assert r[4] == 5, "Fifth element should be 5"

def test_range_with_start_end_and_step():
    r = Range(1, 11, 2)
    assert len(r) == 5, "Length of range should be 5"
    assert r[0] == 1, "First element should be 1"
    assert r[1] == 3, "Second element should be 3"
    assert r[2] == 5, "Third element should be 5"
    assert r[3] == 7, "Fourth element should be 7"
    assert r[4] == 9, "Fifth element should be 9"

def test_range_invalid_arguments():
    try:
        Range()
        assert False, "Expected ValueError for no arguments"
    except ValueError:
        pass
    
    try:
        Range(1, 2, 3, 4)
        assert False, "Expected ValueError for more than three arguments"
    except ValueError:
        pass
