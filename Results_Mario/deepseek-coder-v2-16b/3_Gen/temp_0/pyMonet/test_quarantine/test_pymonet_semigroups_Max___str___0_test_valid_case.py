
import pytest
from pymonet.semigroups import Max

@pytest.fixture
def max_monoid():
    return Max()

def test_combine(max_monoid):
    assert max_monoid.combine(5) == 5
    assert max_monoid.combine(10) == 10
    assert max_monoid.combine(-3) == 10

def test_str_(max_monoid):
    assert str(max_monoid) == 'Max[value=inf]'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_semigroups_Max___str___0_test_valid_case
pyMonet/Test4DT_tests/test_pymonet_semigroups_Max___str___0_test_valid_case.py:7:11: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""