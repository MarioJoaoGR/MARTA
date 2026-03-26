
import os
from isort.deprecated.finders import RequirementsFinder
import pytest

@pytest.fixture
def finder():
    return RequirementsFinder()

def test_get_files_from_dir_cached(finder, tmp_path):
    # Create a temporary directory structure for testing
    requirements_dir = tmp_path / "requirements"
    requirements_dir.mkdir()
    
    # Add some files to the requirements directory
    (requirements_dir / "file1.txt").touch()
    (requirements_dir / "file2.in").touch()
    (requirements_dir / "otherfile.py").touch()  # This should not be included
    (requirements_dir / "subdir" / "file3.txt").touch()  # Subdirectory files should not be included unless directly in the requirements directory
    
    # Run the method and check the results
    files = finder._get_files_from_dir_cached(str(tmp_path))
    assert set(files) == {str(requirements_dir / "file1.txt"), str(requirements_dir / "file2.in")}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_cached_0_test_valid_case
isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_cached_0_test_valid_case.py:8:11: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""