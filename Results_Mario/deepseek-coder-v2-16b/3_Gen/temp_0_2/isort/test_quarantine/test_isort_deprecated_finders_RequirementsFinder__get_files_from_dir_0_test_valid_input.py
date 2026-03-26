
import pytest
from isort.deprecated.finders import RequirementsFinder

@pytest.fixture
def finder():
    return RequirementsFinder()

def test_get_files_from_dir(finder, tmp_path):
    # Create a directory structure and files as if 'requirements' dir contains '.txt' and '.in' files
    requirements_dir = tmp_path / "requirements"
    requirements_dir.mkdir()
    (requirements_dir / "requirements1.txt").touch()
    (requirements_dir / "requirements2.in").touch()
    
    # Test the function with the created directory
    files = list(finder._get_files_from_dir(str(tmp_path)))
    assert len(files) == 2, f"Expected 2 files in {tmp_path}, but found {len(files)}"
    assert any("requirements1.txt" in str(file) for file in files), "Did not find 'requirements1.txt'"
    assert any("requirements2.in" in str(file) for file in files), "Did not find 'requirements2.in'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_0_test_valid_input
isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_0_test_valid_input.py:7:11: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""