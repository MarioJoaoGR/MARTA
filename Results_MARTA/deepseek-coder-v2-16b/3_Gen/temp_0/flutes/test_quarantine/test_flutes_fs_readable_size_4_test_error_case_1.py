
import pytest
from your_module import readable_size  # Replace with the actual module name where readable_size is defined

def test_error_case_1():
    with pytest.raises(TypeError):
        size = 'not a float'
        readable_size(size)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_fs_readable_size_4_test_error_case_1
flutes/Test4DT_tests/test_flutes_fs_readable_size_4_test_error_case_1.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""