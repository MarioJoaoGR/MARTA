
import pytest
from flutes.iterator import Range

# Test initialization with one argument (end value)
def test_range_one_argument():
    r = Range(10)
    assert r.l == 0
    assert r.r == 10
    assert r.step == 1
    assert r.val == 0
    assert r.length == 10
    assert list(r) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Test initialization with two arguments (start and end values)
def test_range_two_arguments():
    r = Range(1, 10 + 1)
    assert r.l == 1