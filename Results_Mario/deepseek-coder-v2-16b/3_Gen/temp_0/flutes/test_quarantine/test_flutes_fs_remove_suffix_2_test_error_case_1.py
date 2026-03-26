
import pytest
from your_module import remove_suffix  # Replace 'your_module' with the actual module name

def test_error_case_1():
    assert remove_suffix("https://github.com/huzecong/flutes", "/flutes") == "https://github.com/huzecong"
    assert remove_suffix("bugfix", "suffix", fully_match=False) == "bug"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_fs_remove_suffix_2_test_error_case_1
flutes/Test4DT_tests/test_flutes_fs_remove_suffix_2_test_error_case_1.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""