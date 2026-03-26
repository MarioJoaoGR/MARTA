
import pytest
from your_module_name import Range  # Replace 'your_module_name' with the actual module name where Range is defined

def test_valid_case_one_argument():
    r = Range(10)
    assert len(r) == 10
    assert r[0] == 0
    assert r[2] == 2
    assert r[4] == 4
    assert r[9] == 9
    
    with pytest.raises(IndexError):
        r[10]  # Index out of range should raise an error

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_Range___init___0_test_valid_case_one_argument
flutes/Test4DT_tests/test_flutes_iterator_Range___init___0_test_valid_case_one_argument.py:3:0: E0401: Unable to import 'your_module_name' (import-error)


"""