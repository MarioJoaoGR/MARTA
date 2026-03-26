
import os
from isort.deprecated.finders import RequirementsFinder
import pytest

@pytest.fixture
def finder():
    return RequirementsFinder()

def test_get_files_from_dir_cached(finder, mocker):
    # Mocking the behavior of os.listdir and os.path.join
    mocker.patch('os.listdir', side_effect=lambda path: [f'{path}/requirements1.txt', f'{path}/requirements2.in', f'{path}/otherfile'])
    mocker.patch('os.path.isdir', return_value=False)
    mocker.patch('os.path.isfile', side_effect=[True, True])  # Mocking isfile for both requirements files
    
    path = 'test_directory'
    expected_files = [f'{path}/requirements1.txt', f'{path}/requirements2.in']
    
    result = finder._get_files_from_dir_cached(path)
    
    assert sorted(result) == sorted(expected_files)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_cached_0_test_valid_case
isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_cached_0_test_valid_case.py:8:11: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""