
import pytest
from pymonet.semigroups import Min

@pytest.fixture
def min_monoid():
    return Min()

def test_valid_inputs(min_monoid):
    assert str(min_monoid) == 'Min[value=inf]'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_semigroups_Min___str___0_test_valid_inputs
pyMonet/Test4DT_tests/test_pymonet_semigroups_Min___str___0_test_valid_inputs.py:7:11: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""