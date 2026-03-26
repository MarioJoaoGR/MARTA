
import os
from isort.deprecated.finders import RequirementsFinder

class TestRequirementsFinder:
    def test_get_files_from_dir_cached(self, tmp_path):
        # Create a temporary directory with some files
        requirements_txt = tmp_path / "requirements.txt"
        requirements_in = tmp_path / "requirements.in"
        subdir = tmp_path / "subdir"
        subdir_req_txt = subdir / "subrequirements.txt"
        subdir_req_in = subdir / "subrequirements.in"
        
        requirements_txt.touch()
        requirements_in.touch()
        subdir.mkdir()
        subdir_req_txt.touch()
        subdir_req_in.touch()
        
        finder = RequirementsFinder()
        files = finder._get_files_from_dir_cached(str(tmp_path))
        
        assert len(files) == 2, f"Expected 2 files, got {len(files)}"
        assert str(requirements_txt) in files, f"Expected {requirements_txt} to be in the list"
        assert str(requirements_in) in files, f"Expected {requirements_in} to be in the list"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_cached_0_test_valid_input
isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_cached_0_test_valid_input.py:20:17: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""