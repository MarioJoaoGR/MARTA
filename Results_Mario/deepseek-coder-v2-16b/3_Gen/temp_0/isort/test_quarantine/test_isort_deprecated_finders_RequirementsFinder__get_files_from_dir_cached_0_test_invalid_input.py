
import os
from isort.deprecated.finders import RequirementsFinder

def test_invalid_input():
    finder = RequirementsFinder()
    assert not finder._get_files_from_dir_cached('nonexistent_directory') == []

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_cached_0_test_invalid_input
isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_cached_0_test_invalid_input.py:6:13: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""