
import pytest
from pymonet.semigroups import Max

@pytest.fixture
def max_monoid():
    return Max()

def test_str_representation(max_monoid):
    assert str(max_monoid) == 'Max[value=-inf]'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_semigroups_Max___str___1_test_edge_case
pyMonet/Test4DT_tests/test_pymonet_semigroups_Max___str___1_test_edge_case.py:7:11: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""