
import pytest
from pymonets.semigroups import Last

def test_valid_inputs():
    l1 = Last(5)
    l2 = Last('hello')
    
    combined = l1.concat(l2)
    
    assert combined.value == 'hello'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_semigroups_Last_concat_0_test_valid_inputs
pyMonet/Test4DT_tests/test_pymonet_semigroups_Last_concat_0_test_valid_inputs.py:3:0: E0401: Unable to import 'pymonets.semigroups' (import-error)


"""