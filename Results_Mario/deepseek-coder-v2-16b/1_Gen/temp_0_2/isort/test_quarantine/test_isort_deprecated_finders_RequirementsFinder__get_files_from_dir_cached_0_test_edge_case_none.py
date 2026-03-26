
import os
from isort.deprecated.finders import RequirementsFinder

class TestRequirementsFinder:
    def test_get_files_from_dir_cached(self):
        finder = RequirementsFinder()
        
        # Test with a directory that contains requirements files
        path = 'test_project'
        os.makedirs(os.path.join(path, 'requirements'))
        open(os.path.join(path, 'requirements', 'requirements1.txt'), 'a').close()
        open(os.path.join(path, 'requirements', 'requirements2.in'), 'a').close()
        
        files = finder._get_files_from_dir_cached(path)
        assert len(files) == 2
        assert os.path.basename(files[0]) in ['requirements1.txt', 'requirements2.in']
        
        # Clean up the test directory and its contents
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(path)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_cached_0_test_edge_case_none
isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_cached_0_test_edge_case_none.py:7:17: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""