
from isort.deprecated.finders import LocalFinder
import pytest

def test_valid_input_happy_path():
    finder = LocalFinder()
    assert finder.find("mymodule") == None
    assert finder.find(".mymodule") == "LOCALFOLDER"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_LocalFinder_find_0_test_valid_input_happy_path
isort/Test4DT_tests/test_isort_deprecated_finders_LocalFinder_find_0_test_valid_input_happy_path.py:6:13: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""