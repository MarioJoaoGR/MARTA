
import pytest
from flutes.iterator import Range

# Test cases for the Range class initialization with different sets of parameters

def test_range_with_stop():
    r = Range(10)
    assert r.l == 0
    assert r.r == 10
    assert r.step == 1
    assert r.val == 0