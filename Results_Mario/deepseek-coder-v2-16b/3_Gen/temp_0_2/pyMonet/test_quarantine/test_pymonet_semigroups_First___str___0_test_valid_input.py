
import pytest
from your_module import First  # Replace 'your_module' with the actual module name where First is defined

def test_valid_input():
    first_instance = First(5)
    assert str(first_instance) == 'Fist[value=5]'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_semigroups_First___str___0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_semigroups_First___str___0_test_valid_input.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""