
import pytest
from unittest.mock import patch
from isort.deprecated.finders import RequirementsFinder
import os

def test_invalid_input():
    finder = RequirementsFinder()
    
    # Mock the path that does not exist
    with patch('os.listdir', return_value=[]):
        with pytest.raises(FileNotFoundError):
            list(finder._get_files_from_dir("non_existent_directory"))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_1_test_invalid_input
isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_1_test_invalid_input.py:8:13: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""