
import pytest
from isort.deprecated.finders import RequirementsFinder

@pytest.fixture
def finder():
    return RequirementsFinder()

def test_get_files_from_dir(finder, tmp_path):
    # Create a temporary directory with some mock requirement files
    (tmp_path / "requirements.txt").touch()
    (tmp_path / "requirements.in").touch()
    
    # Get the list of files from the temporary directory
    files = list(finder._get_files_from_dir(str(tmp_path)))
    
    # Assert that the number of files found matches what we expect
    assert len(files) == 2
    # Assert that the file names match what we expect
    assert "requirements.txt" in files
    assert "requirements.in" in files

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_0_test_valid_input
isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_0_test_valid_input.py:7:11: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""