
import pytest
from flutes.iterator import Range




def test_single_argument():
    r10 = Range(10)
    assert list(r10) == list(range(10))

def test_two_arguments():
    r1_11 = Range(1, 11)
    assert list(r1_11) == list(range(1, 11))

def test_three_arguments():
    r1_11_2 = Range(1, 11, 2)
    assert list(r1_11_2) == list(range(1, 11, 2))

def test_indexing():
    r10 = Range(10)
    assert r10[0] == 0
    assert r10[5] == 5

def test_negative_indexing():
    r10 = Range(10)
    assert r10[-1] == 9
    assert r10[-2] == 8

def test_slicing():
    r10 = Range(10)
    assert list(r10[:3]) == [0, 1, 2]
    assert list(r10[::2]) == [0, 2, 4, 6, 8]

def test_length():
    r10 = Range(10)
    assert len(r10) == 10

def test_iteration():
    r10 = Range(10)
    result = []
    for number in r10:
        result.append(number)
    assert result == list(range(10))