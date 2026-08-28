
import pytest
from flutes.iterator import Range

def test_range_single_argument():
    r = Range(10)
    assert r[5] == 5

def test_range_two_arguments():
    r = Range(1, 11)
    assert r[3] == 4

def test_range_three_arguments():
    r = Range(1, 11, 2)
    assert r[2] == 5
