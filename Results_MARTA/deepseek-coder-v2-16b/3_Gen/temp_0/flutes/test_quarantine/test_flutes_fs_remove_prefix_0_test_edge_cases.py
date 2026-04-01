
import pytest
from your_module import remove_prefix  # Replace 'your_module' with the actual module name

def test_remove_prefix_fully_match():
    assert remove_prefix("https://github.com/huzecong/flutes", "https://") == "github.com/huzecong/flutes"
    assert remove_prefix("preface", "prefix", fully_match=False) == "face"

def test_remove_prefix_not_fully_match():
    assert remove_prefix("https://github.com/huzecong/flutes", "https://", fully_match=False) == "github.com/huzecong/flutes"
    assert remove_prefix("prefixedtext", "fix", fully_match=False) == "edtext"

def test_remove_prefix_default_fully_match():
    assert remove_prefix("https://github.com/huzecong/flutes") == "https://github.com/huzecong/flutes"
    assert remove_prefix("prefixedtext") == "prefixedtext"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_fs_remove_prefix_0_test_edge_cases
flutes/Test4DT_tests/test_flutes_fs_remove_prefix_0_test_edge_cases.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""