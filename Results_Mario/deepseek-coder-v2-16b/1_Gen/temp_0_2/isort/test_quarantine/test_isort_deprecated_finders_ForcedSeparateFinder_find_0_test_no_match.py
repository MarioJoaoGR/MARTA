
from isort.deprecated.finders import ForcedSeparateFinder
import fnmatch

class TestForcedSeparateFinderFind0TestNoMatch:
    def test_no_match(self):
        finder = ForcedSeparateFinder()
        result = finder.find("some_module")
        assert result is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ForcedSeparateFinder_find_0_test_no_match
isort/Test4DT_tests/test_isort_deprecated_finders_ForcedSeparateFinder_find_0_test_no_match.py:7:17: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""