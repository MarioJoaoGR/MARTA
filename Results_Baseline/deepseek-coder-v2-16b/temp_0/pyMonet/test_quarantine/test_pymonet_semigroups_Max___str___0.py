
# Module: pymonet.semigroups
# test_pymonet_semigroups.py
import pytest
from pymonet.semigroups import Max

@pytest.fixture
def max_monoid():
    return Max()

def test_max_combine_initial(max_monoid):
    assert max_monoid.combine(5) == 5
    assert max_monoid.combine(10) == 10
    assert max_monoid.combine(-3) == 10

def test_max_neutral_element(max_monoid):
    assert max_monoid.combine(float('inf')) == float('inf')
    assert max_monoid.combine(-float('inf')) == -float('inf')

def test_str_representation(max_monoid):
    assert str(max_monoid) == 'Max[value=-inf]'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_semigroups_Max___str___0
pyMonet/Test4DT_tests/test_pymonet_semigroups_Max___str___0.py:9:11: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""