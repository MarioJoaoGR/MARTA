
import pytest
from your_module import remove_suffix  # Replace with the actual module name where `remove_suffix` is defined

def test_valid_case_2():
    s = 'bugfix'
    suffix = 'suffix'
    fully_match = False
    
    result = remove_suffix(s, suffix, fully_match)
    assert result == 'bug', f"Expected 'bug', but got {result}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_fs_remove_suffix_2_test_valid_case_2
flutes/Test4DT_tests/test_flutes_fs_remove_suffix_2_test_valid_case_2.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""