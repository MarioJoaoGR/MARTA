
import pytest
from flutes.iterator import Range

def test_range_init_without_args():
    with pytest.raises(ValueError):
        r = Range()

def test_range_init_with_one_arg():
    r = Range(10)
    assert r.l == 0
    assert r.r == 10
    assert r.step == 1
    assert len(list(r)) == 10

def test_range_init_with_two_args():
    r = Range(1, 10)
    assert r.l == 1
    assert r.r == 10
    assert r.step == 1
    assert len(list(r)) == 9

def test_range_init_with_three_args():
    r = Range(1, 10, 2)
    assert r.l == 1
    assert r.r == 10
    assert r.step == 2
    expected_sequence = [1, 3, 5, 7, 9]
    assert list(r) == expected_sequence
