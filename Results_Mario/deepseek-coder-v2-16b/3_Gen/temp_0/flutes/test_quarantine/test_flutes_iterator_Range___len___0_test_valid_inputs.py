
import pytest
from your_module import Range  # Replace `your_module` with the actual module name where `Range` is defined

def test_valid_inputs():
    r = Range(10)
    assert len(r) == 10, "Length of range should be 10"
    
    r = Range(1, 10 + 1)
    assert len(r) == 10, "Length of range should be 10"
    
    r = Range(1, 11, 2)
    assert len(r) == 5, "Length of range should be 5"
    
    r = Range(0, 10, 2)
    assert len(r) == 5, "Length of range should be 5"
    
    r = Range(5, 15, 3)
    assert len(r) == 4, "Length of range should be 4"
    
    with pytest.raises(ValueError):
        Range()
        
    with pytest.raises(ValueError):
        Range(1, 2, 3, 4)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_Range___len___0_test_valid_inputs
flutes/Test4DT_tests/test_flutes_iterator_Range___len___0_test_valid_inputs.py:3:0: E0401: Unable to import 'your_module' (import-error)

"""