
import os
from isort.deprecated.finders import RequirementsFinder

def test_invalid_input():
    finder = RequirementsFinder()
    
    # Test with invalid input (None)
    assert finder._get_files_from_dir_cached(None) == []
    
    # Test with invalid input (empty string)
    assert finder._get_files_from_dir_cached('') == []
    
    # Test with valid directory path
    current_dir = os.path.dirname(__file__)
    valid_path = os.path.join(current_dir, 'test_directory')
    if not os.path.exists(valid_path):
        os.makedirs(valid_path)
    
    # Add some files to simulate a valid directory with requirements files
    open(os.path.join(valid_path, 'requirements1.txt'), 'a').close()
    open(os.path.join(valid_path, 'requirements2.in'), 'a').close()
    
    assert finder._get_files_from_dir_cached(valid_path) == [
        os.path.join(valid_path, 'requirements1.txt'),
        os.path.join(valid_path, 'requirements2.in')
    ]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_cached_0_test_invalid_input
isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_cached_0_test_invalid_input.py:6:13: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""