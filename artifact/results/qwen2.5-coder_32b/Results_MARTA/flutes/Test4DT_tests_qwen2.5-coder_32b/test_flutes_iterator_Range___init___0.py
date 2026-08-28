
import pytest
from flutes.iterator import Range

def test_single_argument():
    r = Range(10)
    assert list(r) == list(range(10))

def test_two_arguments():
    r = Range(1, 11)
    assert list(r) == list(range(1, 11))

def test_three_arguments():
    r = Range(1, 11, 2)
    assert list(r) == list(range(1, 11, 2))

def test_index_access():
    r = Range(10)
    assert r[0] == 0
    assert r[2] == 2



def test_length_calculation():
    r = Range(10)
    assert len(r) == 10

def test_length_with_negative_step():
    r = Range(10, 0, -2)
    assert len(r) == 5

def test_iteration():
    r = Range(3)
    result = []
    for value in r:
        result.append(value)
    assert result == [0, 1, 2]

def test_slicing():
    r = Range(10)
    assert list(r[:3]) == [0, 1, 2]