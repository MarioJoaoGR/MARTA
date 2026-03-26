
import pytest
from pymonet.semigroups import Map

def test_valid_input():
    m = Map()
    m.value = ["a", "b"]
    assert str(m) == 'Map[value=[\'a\', \'b\']]'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_semigroups_Map___str___0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_semigroups_Map___str___0_test_valid_input.py:6:8: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""