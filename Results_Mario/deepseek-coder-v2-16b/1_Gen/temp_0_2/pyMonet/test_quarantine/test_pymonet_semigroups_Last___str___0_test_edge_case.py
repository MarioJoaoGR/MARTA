
from pymonet.semigroups import Last
import pytest

def test_edge_case():
    last1 = Last()
    last2 = Last()
    
    # Set different values to ensure the latest one is taken
    last1.value = 10
    last2.value = 20
    
    combined_last = last1 + last2
    assert str(combined_last) == 'Last[value=20]', f"Expected 'Last[value=20]', but got {str(combined_last)}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_semigroups_Last___str___0_test_edge_case
pyMonet/Test4DT_tests/test_pymonet_semigroups_Last___str___0_test_edge_case.py:6:12: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)
pyMonet/Test4DT_tests/test_pymonet_semigroups_Last___str___0_test_edge_case.py:7:12: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""