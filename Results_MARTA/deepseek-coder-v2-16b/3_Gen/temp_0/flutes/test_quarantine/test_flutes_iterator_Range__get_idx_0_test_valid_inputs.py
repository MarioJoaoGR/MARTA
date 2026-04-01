
import pytest
from your_module import Range  # Replace with the actual module name where Range is defined

def test_valid_inputs():
    r = Range(10)
    
    assert r[0] == 0, "Indexing at 0 should return start value"
    assert r[2] == 2, "Indexing at 2 should return the correct value"
    assert r[4] == 4, "Indexing at 4 should return the correct value"
    
    r = Range(1, 10 + 1)
    assert r[0] == 1, "Indexing at 0 should return start value"
    assert r[2] == 3, "Indexing at 2 should return the correct value"
    assert r[4] == 5, "Indexing at 4 should return the correct value"
    
    r = Range(1, 11, 2)
    assert r[0] == 1, "Indexing at 0 should return start value"
    assert r[2] == 5, "Indexing at 2 should return the correct value"
    assert r[4] == 9, "Indexing at 4 should return the correct value"
    
    # Testing negative indexing
    assert r[-1] == 9, "Negative indexing at -1 should return the last value"
    assert r[-3] == 7, "Negative indexing at -3 should return the third last value"
    assert r[-5] == 5, "Negative indexing at -5 should return the fifth last value"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_Range__get_idx_0_test_valid_inputs
flutes/Test4DT_tests/test_flutes_iterator_Range__get_idx_0_test_valid_inputs.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""