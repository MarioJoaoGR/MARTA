
import pytest
from your_module import readable_size  # Replace 'your_module' with the actual module name where `readable_size` is defined.

def test_valid_input_large_size():
    assert readable_size(1024 * 1024) == "1.00M"
    assert readable_size(500000) == "488.28K"
    assert readable_size(123456789) == "117.74M"
    assert readable_size(1024**3) == "1.00G"  # Testing with a size of 1GB (1024^3 bytes)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_fs_readable_size_0_test_valid_input_large_size
flutes/Test4DT_tests/test_flutes_fs_readable_size_0_test_valid_input_large_size.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""