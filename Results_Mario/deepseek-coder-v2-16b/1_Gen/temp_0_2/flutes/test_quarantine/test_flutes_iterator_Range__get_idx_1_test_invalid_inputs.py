
import pytest
from your_module_name import Range  # Replace 'your_module_name' with the actual module name where Range is defined

def test_invalid_inputs():
    r = Range(1, 10)
    
    # Test non-integer index
    with pytest.raises(TypeError):
        r['invalid']  # Accessing with a string which should raise TypeError
    
    # Test out-of-range positive index
    with pytest.raises(IndexError):
        r[10]  # Index 10 is out of range for the created range (1, 2, ..., 9)
    
    # Test out-of-range negative index
    with pytest.raises(IndexError):
        r[-11]  # Negative index -11 is also out of range

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_Range__get_idx_1_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_iterator_Range__get_idx_1_test_invalid_inputs.py:3:0: E0401: Unable to import 'your_module_name' (import-error)


"""