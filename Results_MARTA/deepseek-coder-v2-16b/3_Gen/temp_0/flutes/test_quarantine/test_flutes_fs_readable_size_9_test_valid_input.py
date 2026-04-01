
import pytest
from your_module import readable_size  # Replace 'your_module' with the actual module name where readable_size is defined

@pytest.mark.parametrize("size, n_digits, expected", [
    (1024 * 1024, 2, "1.00M"),
    (500000, 2, "488.28K"),
    (123456789, 2, "117.74M"),
    (1024 * 1024 * 1024, 2, "1.00G"),
    (1024 * 1024 * 1024 * 1024, 2, "1.00T"),
    (1024 * 1024 * 1024 * 1024 * 1024, 2, "1.00P"),
    (987654321, 2, "942.29M"),
    (1024, 2, "1.00K"),
    (1024 * 1024 + 500000, 2, "1.50M"),
])
def test_valid_input(size, n_digits, expected):
    assert readable_size(size, n_digits) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_fs_readable_size_9_test_valid_input
flutes/Test4DT_tests/test_flutes_fs_readable_size_9_test_valid_input.py:3:0: E0401: Unable to import 'your_module' (import-error)

"""