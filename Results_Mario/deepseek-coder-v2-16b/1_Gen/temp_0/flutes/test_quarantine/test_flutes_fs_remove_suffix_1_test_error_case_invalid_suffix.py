
import pytest
from your_module import remove_suffix  # Replace 'your_module' with the actual module name

def test_error_case_invalid_suffix():
    # Test case for when the suffix is not fully matched and `fully_match` is False
    assert remove_suffix("https://github.com/huzecong/flutes", "/flutes") == "https://github.com/huzecong"
    
    # Additional test to ensure that only the matching part is removed when `fully_match` is False
    assert remove_suffix("bugfix", "fix", fully_match=False) == "bug"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_fs_remove_suffix_1_test_error_case_invalid_suffix
flutes/Test4DT_tests/test_flutes_fs_remove_suffix_1_test_error_case_invalid_suffix.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""