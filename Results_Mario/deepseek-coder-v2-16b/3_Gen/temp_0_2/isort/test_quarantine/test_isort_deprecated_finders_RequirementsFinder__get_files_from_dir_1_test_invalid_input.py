
from unittest.mock import patch
import pytest
from isort.deprecated.finders import RequirementsFinder

@pytest.fixture
def finder():
    return RequirementsFinder()

def test_invalid_input(finder):
    with pytest.raises(TypeError):
        list(finder._get_files_from_dir("invalid_path"))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_1_test_invalid_input
isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_1_test_invalid_input.py:8:11: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""