
import pytest
from your_module import readable_size  # Replace 'your_module' with the actual module name where readable_size is defined

def test_edge_cases():
    assert readable_size(0) == "0.00B"
    assert readable_size(1023) == "1023.00B"
    assert readable_size(1024) == "1.00K"
    assert readable_size(1024 * 1024 - 1) == "1023.98K"
    assert readable_size(1024 * 1024) == "1.00M"
    assert readable_size(1024 * 1024 * 1024 - 1) == "1023.98M"
    assert readable_size(1024 * 1024 * 1024) == "1.00G"
    assert readable_size(1024 * 1024 * 1024 * 1024 - 1) == "1023.98G"
    assert readable_size(1024 * 1024 * 1024 * 1024) == "1.00T"
    assert readable_size(1024 * 1024 * 1024 * 1024 * 1024 - 1) == "1023.98T"
    assert readable_size(1024 * 1024 * 1024 * 1024 * 1024) == "1.00P"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_fs_readable_size_10_test_edge_cases
flutes/Test4DT_tests/test_flutes_fs_readable_size_10_test_edge_cases.py:3:0: E0401: Unable to import 'your_module' (import-error)

"""