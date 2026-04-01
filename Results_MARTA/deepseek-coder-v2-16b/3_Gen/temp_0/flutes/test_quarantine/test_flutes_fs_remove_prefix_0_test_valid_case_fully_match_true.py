
import pytest
from your_module import remove_prefix  # Replace 'your_module' with the actual module name

def test_valid_case_fully_match_true():
    assert remove_prefix("https://github.com/huzecong/flutes", "https://") == "github.com/huzecong/flutes"
    assert remove_prefix("preface", "prefix", fully_match=False) == "face"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_fs_remove_prefix_0_test_valid_case_fully_match_true
flutes/Test4DT_tests/test_flutes_fs_remove_prefix_0_test_valid_case_fully_match_true.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""