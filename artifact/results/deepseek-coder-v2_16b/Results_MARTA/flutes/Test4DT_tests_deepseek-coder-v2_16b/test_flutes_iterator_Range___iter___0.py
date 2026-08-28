
import pytest
from flutes.iterator import Range

def test_single_argument_range():
    r = Range(10)
    assert list(r) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_three_arguments_range():
    r = Range(1, 11, 2)
    assert list(r) == [1, 3, 5, 7, 9]

def test_index_access_range():
    r = Range(1, 11, 2)
    assert r[0] == 1
    assert r[2] == 5
    assert r[4] == 9