
import pytest
from pymonet import One

def test_valid_input():
    one = One(42)
    assert str(one) == 'One[value=42]'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_semigroups_One___str___0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_semigroups_One___str___0_test_valid_input.py:3:0: E0611: No name 'One' in module 'pymonet' (no-name-in-module)


"""