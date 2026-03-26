
import pytest
from pymonet.semigroups import Max

def test_valid_case():
    max_monoid = Max()
    assert str(max_monoid) == 'Max[value=-inf]'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_semigroups_Max___str___0_test_valid_case
pyMonet/Test4DT_tests/test_pymonet_semigroups_Max___str___0_test_valid_case.py:6:17: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""