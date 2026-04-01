
import pytest
from pymonet.semigroups import Max

@pytest.fixture
def max_monoid():
    return Max()

def test_combine(max_monoid):
    assert str(max_monoid) == 'Max[value=-inf]'
    
    # Combine with a number larger than the neutral element
    max_monoid.combine(10)
    assert str(max_monoid) == 'Max[value=10]'
    
    # Combine with a number smaller than the current value
    max_monoid.combine(5)
    assert str(max_monoid) == 'Max[value=10]'
    
    # Combine with a number larger than the current value
    max_monoid.combine(20)
    assert str(max_monoid) == 'Max[value=20]'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_semigroups_Max___str___0_test_valid_inputs
pyMonet/Test4DT_tests/test_pymonet_semigroups_Max___str___0_test_valid_inputs.py:7:11: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""