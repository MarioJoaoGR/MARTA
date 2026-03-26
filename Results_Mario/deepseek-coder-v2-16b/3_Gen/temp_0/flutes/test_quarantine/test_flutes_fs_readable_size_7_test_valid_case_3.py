
import pytest
from your_module import readable_size  # Replace 'your_module' with the actual module name where readable_size is defined

def test_valid_case_3():
    size = 123456789
    expected_output = "117.74M"
    assert readable_size(size) == expected_output

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_fs_readable_size_7_test_valid_case_3
flutes/Test4DT_tests/test_flutes_fs_readable_size_7_test_valid_case_3.py:3:0: E0401: Unable to import 'your_module' (import-error)

"""