
import pytest
from flutes.iterator import Range

# Test cases for the __init__ method
def test_range_one_argument():
    r = Range(10)
    assert r.l == 0
    assert r.r == 10
    assert r.step == 1
    assert r.length == 10

def test_range_two_arguments():
    r = Range(1, 10 + 1)
    assert r.l == 1