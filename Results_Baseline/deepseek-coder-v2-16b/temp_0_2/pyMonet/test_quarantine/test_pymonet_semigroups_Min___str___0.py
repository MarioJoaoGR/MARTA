
# Module: pymonet.semigroups
# test_min_monoid.py
from pymonet.semigroups import Min
import pytest

@pytest.fixture
def min_monoid():
    return Min()

def test_combine_two_numbers(min_monoid):
    assert min_monoid.combine(5, 3) == 3
    assert min_monoid.combine(-1, -2) == -2
    assert min_monoid.combine(0, 0) == 0

def test_combine_same_numbers(min_monoid):
    assert min_monoid.combine(5, 5) == 5
    assert min_monoid.combine(-1, -1) == -1
    assert min_monoid.combine(0, 0) == 0

def test_combine_positive_negative(min_monoid):
    assert min_monoid.combine(-5, 3) == -5
    assert min_monoid.combine(5, -3) == -3
    assert min_monoid.combine(-1, 0) == -1
    assert min_monoid.combine(0, -1) == -1

def test_combine_zeroes(min_monoid):
    assert min_monoid.combine(0, 0) == 0
    assert min_monoid.combine(-0, 0) == 0
    assert min_monoid.combine(0, -0) == 0

def test_combine_large_numbers(min_monoid):
    assert min_monoid.combine(1e6, 2e6) == 1e6
    assert min_monoid.combine(-1e6, -2e6) == -2e6
    assert min_monoid.combine(3e6, -4e6) == -4e6

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_semigroups_Min___str___0
pyMonet/Test4DT_tests/test_pymonet_semigroups_Min___str___0.py:9:11: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""