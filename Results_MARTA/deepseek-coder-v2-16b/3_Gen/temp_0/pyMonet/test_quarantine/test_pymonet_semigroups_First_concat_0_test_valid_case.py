
import pytest
from your_module import First  # Replace 'your_module' with the actual module name where First is defined

def test_valid_case():
    first1 = First(1)
    first2 = First(2)
    
    combined_first = first1.concat(first2)
    
    assert combined_first.value == 1

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_semigroups_First_concat_0_test_valid_case
pyMonet/Test4DT_tests/test_pymonet_semigroups_First_concat_0_test_valid_case.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""