
import pytest
from pymonets.semigroups import Max  # Assuming the correct path to the module

def test_str_representation():
    max_monoid = Max()
    assert str(max_monoid) == 'Max[value=-inf]'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_semigroups_Max___str___0_test_edge_case
pyMonet/Test4DT_tests/test_pymonet_semigroups_Max___str___0_test_edge_case.py:3:0: E0401: Unable to import 'pymonets.semigroups' (import-error)


"""