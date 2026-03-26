
from isort.deprecated.finders import ForcedSeparateFinder
import fnmatch

class TestForcedSeparateFinderFind:
    def test_invalid_input(self):
        finder = ForcedSeparateFinder()
        assert finder.find("some_module") is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ForcedSeparateFinder_find_0_test_invalid_input
isort/Test4DT_tests/test_isort_deprecated_finders_ForcedSeparateFinder_find_0_test_invalid_input.py:7:17: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""