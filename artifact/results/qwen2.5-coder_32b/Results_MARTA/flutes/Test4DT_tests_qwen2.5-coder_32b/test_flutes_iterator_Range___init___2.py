
import pytest
from flutes.iterator import Range

def test_single_argument():
    # Test with a single argument, should create range(10)
    r = Range(10)
    assert len(r) == 10
    assert r[0] == 0
    assert r[9] == 9

def test_two_arguments():
    # Test with two arguments, should create range(1, 11)
    r = Range(1, 11)
    assert len(r) == 10
    assert r[0] == 1
    assert r[9] == 10

def test_three_arguments():
    # Test with three arguments, should create range(1, 11, 2)
    r = Range(1, 11, 2)
    assert len(r) == 5
    assert r[0] == 1
    assert r[4] == 9


def test_negative_step():
    # Test with negative step, should create range(10, 0, -1)
    r = Range(10, 0, -1)
    assert len(r) == 10
    assert r[0] == 10
    assert r[9] == 1


def test_large_range():
    # Test with a large range, should create range(0, 1000000)
    r = Range(1000000)
    assert len(r) == 1000000
    assert r[0] == 0
    assert r[999999] == 999999

def test_large_step():
    # Test with a large step, should create range(0, 100, 25)
    r = Range(0, 100, 25)
    assert len(r) == 4
    assert r[0] == 0
    assert r[3] == 75

def test_single_element_range():
    # Test with a single element range, should create range(5, 6)
    r = Range(5, 6)
    assert len(r) == 1
    assert r[0] == 5