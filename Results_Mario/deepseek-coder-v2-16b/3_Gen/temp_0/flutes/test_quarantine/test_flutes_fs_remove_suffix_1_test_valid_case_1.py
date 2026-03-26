
import pytest
from your_module import remove_suffix  # Replace with the actual module name where `remove_suffix` is defined

def test_valid_case_1():
    s = 'https://github.com/huzecong/flutes'
    suffix = '/flutes'
    assert remove_suffix(s, suffix) == "https://github.com/huzecong"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_fs_remove_suffix_1_test_valid_case_1
flutes/Test4DT_tests/test_flutes_fs_remove_suffix_1_test_valid_case_1.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""