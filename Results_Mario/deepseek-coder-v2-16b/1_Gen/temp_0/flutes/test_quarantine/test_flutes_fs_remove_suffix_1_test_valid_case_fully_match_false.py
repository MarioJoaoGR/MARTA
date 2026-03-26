
import pytest
from your_module import remove_suffix  # Replace 'your_module' with the actual module name

def test_valid_case_fully_match_false():
    assert remove_suffix("https://github.com/huzecong/flutes", "/flutes") == "https://github.com/huzecong"
    assert remove_suffix("bugfix", "fix", fully_match=False) == "bug"
    assert remove_suffix("https://github.com/huzecong/flutes", "/flutes", fully_match=False) == "https://github.com/huzecong"
    assert remove_suffix("bugfix", "suffix", fully_match=False) == "bug"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_fs_remove_suffix_1_test_valid_case_fully_match_false
flutes/Test4DT_tests/test_flutes_fs_remove_suffix_1_test_valid_case_fully_match_false.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""