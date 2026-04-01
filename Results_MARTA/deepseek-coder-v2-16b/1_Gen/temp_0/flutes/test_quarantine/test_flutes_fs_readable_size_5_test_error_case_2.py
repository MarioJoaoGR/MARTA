
import pytest
from your_module import readable_size  # Replace 'your_module' with the actual module name where readable_size is defined

def test_error_case_2():
    size = -1024
    with pytest.raises(ValueError):
        readable_size(size)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_fs_readable_size_5_test_error_case_2
flutes/Test4DT_tests/test_flutes_fs_readable_size_5_test_error_case_2.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""