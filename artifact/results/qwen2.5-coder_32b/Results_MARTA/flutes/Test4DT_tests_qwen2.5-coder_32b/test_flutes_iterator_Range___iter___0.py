
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



def test_indexing_single_argument():
    r = Range(10)
    assert r[0] == 0
    assert r[5] == 5

def test_indexing_two_arguments():
    r = Range(1, 11)
    assert r[0] == 1
    assert r[5] == 6

def test_indexing_three_arguments():
    r = Range(1, 11, 2)
    assert r[0] == 1
    assert r[2] == 5

def test_slicing_single_argument():
    r = Range(10)
    assert list(r[:3]) == [0, 1, 2]

def test_slicing_two_arguments():
    r = Range(1, 11)
    assert list(r[::2]) == [1, 3, 5, 7, 9]

def test_slicing_three_arguments():
    r = Range(1, 11, 2)
    assert list(r[::-1]) == [9, 7, 5, 3, 1]

def test_length_single_argument():
    r = Range(10)
    assert len(r) == 10

def test_length_two_arguments():
    r = Range(1, 11)
    assert len(r) == 10

def test_length_three_arguments():
    r = Range(1, 11, 2)
    assert len(r) == 5