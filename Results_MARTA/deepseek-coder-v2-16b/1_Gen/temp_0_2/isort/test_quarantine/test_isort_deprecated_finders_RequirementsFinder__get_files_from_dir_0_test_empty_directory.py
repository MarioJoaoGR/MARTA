
import pytest
from isort.deprecated.finders import RequirementsFinder
from unittest.mock import MagicMock

@pytest.fixture
def finder():
    return RequirementsFinder()

def test_get_files_from_dir_empty_directory(tmp_path):
    # Create an empty directory for testing
    dir_to_scan = tmp_path / "empty_dir"
    dir_to_scan.mkdir()
    
    finder = RequirementsFinder()
    files = list(finder._get_files_from_dir(str(dir_to_scan)))
    
    assert len(files) == 0, f"Expected no files in an empty directory but found {files}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_0_test_empty_directory
isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_0_test_empty_directory.py:8:11: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)
isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_0_test_empty_directory.py:15:13: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""