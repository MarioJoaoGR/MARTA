
import pytest
from flutes.iterator import Range




def test_single_argument_range():
    r = Range(10)
    assert list(r) == list(range(10))

def test_two_arguments_range():
    r = Range(1, 11)
    assert list(r) == list(range(1, 11))

def test_three_arguments_range():
    r = Range(1, 11, 2)
    assert list(r) == list(range(1, 11, 2))

def test_indexing():
    r = Range(1, 11, 2)
    assert r[0] == 1
    assert r[2] == 5

def test_slicing():
    r = Range(1, 11)
    assert list(r[:3]) == [1, 2, 3]
    assert list(r[::2]) == [1, 3, 5, 7, 9]

def test_reverse_iteration():
    r = Range(1, 11)
    assert list(reversed(r)) == list(range(10, 0, -1))

def test_length():
    r = Range(1, 11, 2)
    assert len(r) == 5