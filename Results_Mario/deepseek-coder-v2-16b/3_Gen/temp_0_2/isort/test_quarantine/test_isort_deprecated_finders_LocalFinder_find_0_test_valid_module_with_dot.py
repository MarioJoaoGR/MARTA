
from isort.deprecated.finders import LocalFinder
import pytest

def test_valid_module_with_dot():
    finder = LocalFinder()
    assert finder.find(".mymodule") == "LOCALFOLDER"
    assert finder.find("mymodule") is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_LocalFinder_find_0_test_valid_module_with_dot
isort/Test4DT_tests/test_isort_deprecated_finders_LocalFinder_find_0_test_valid_module_with_dot.py:6:13: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""