
import os
from isort.deprecated.finders import RequirementsFinder

class TestRequirementsFinder:
    def test_get_files_from_dir_cached(self, tmp_path):
        # Create a temporary directory structure for testing
        requirements_dir = tmp_path / "requirements"
        requirements_dir.mkdir()
        
        # Add some files to the requirements directory
        (requirements_dir / "file1.txt").touch()
        (requirements_dir / "file2.in").touch()
        (requirements_dir / "subdir" / "file3.txt").touch()
        (requirements_dir / "subdir" / "file4.in").touch()
        
        # Create a file that does not match the criteria
        (tmp_path / "otherfile.txt").touch()
        
        finder = RequirementsFinder()
        files = finder._get_files_from_dir_cached(str(requirements_dir))
        
        assert len(files) == 4
        assert str(requirements_dir / "file1.txt") in files
        assert str(requirements_dir / "file2.in") in files
        assert str(requirements_dir / "subdir" / "file3.txt") in files
        assert str(requirements_dir / "subdir" / "file4.in") in files

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_cached_0_test_error_handling
isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_cached_0_test_error_handling.py:20:17: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""