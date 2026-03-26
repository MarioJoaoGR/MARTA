
import pytest
from your_module import First  # Replace 'your_module' with the actual module name where First class is defined

def test_valid_case_1():
    f1 = First(1)
    f2 = First(2)
    
    combined = f1.concat(f2)
    
    assert combined.value == 1

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_semigroups_First_concat_0_test_valid_case_1
pyMonet/Test4DT_tests/test_pymonet_semigroups_First_concat_0_test_valid_case_1.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""