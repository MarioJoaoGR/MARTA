
import pytest
from flutes.iterator import Range



def test_single_argument():
    r = Range(5)
    assert len(r) == 5

def test_two_arguments():
    r = Range(1, 6)
    assert len(r) == 5



def test_start_equals_end():
    r = Range(5, 5)
    assert len(r) == 0


def test_indexing_single_argument():
    r = Range(5)
    assert r[2] == 2

def test_indexing_two_arguments():
    r = Range(1, 6)
    assert r[2] == 3

def test_indexing_three_arguments_positive_step():
    r = Range(1, 10, 2)
    assert r[2] == 5

def test_indexing_three_arguments_negative_step():
    r = Range(10, 1, -2)
    assert r[2] == 6