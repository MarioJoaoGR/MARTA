
from isort.deprecated.finders import DefaultFinder
import pytest

def test_invalid_input():
    finder = DefaultFinder()
    with pytest.raises(AttributeError):
        finder.find("some_module")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_DefaultFinder_find_0_test_invalid_input
isort/Test4DT_tests/test_isort_deprecated_finders_DefaultFinder_find_0_test_invalid_input.py:6:13: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""