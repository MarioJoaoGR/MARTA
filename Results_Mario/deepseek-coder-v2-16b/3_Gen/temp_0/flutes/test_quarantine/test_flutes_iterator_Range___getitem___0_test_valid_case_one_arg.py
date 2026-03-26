
import pytest
from your_module import Range  # Replace 'your_module' with the actual module name where Range is defined

def test_valid_case_one_arg():
    r = Range(10)
    assert r[0] == 0
    assert r[2] == 2
    assert r[4] == 4

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_Range___getitem___0_test_valid_case_one_arg
flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___0_test_valid_case_one_arg.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""