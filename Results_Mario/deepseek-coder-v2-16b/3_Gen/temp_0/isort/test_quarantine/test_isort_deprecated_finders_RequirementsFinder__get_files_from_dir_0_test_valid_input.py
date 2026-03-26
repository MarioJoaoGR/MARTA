
import os
import pytest
from isort.deprecated.finders import RequirementsFinder

@pytest.fixture
def finder():
    return RequirementsFinder()

def test_valid_input(finder, mocker):
    # Mocking os.listdir to return a list of files that exist
    mock_listdir = mocker.patch('os.listdir')
    mock_listdir.return_value = ['requirements1.txt', 'requirements2.in']
    
    path = 'some/directory'
    # Ensure the directory exists for the test to pass
    os.makedirs(path, exist_ok=True)
    
    files = list(finder._get_files_from_dir(path))
    
    assert len(files) == 2
    assert 'requirements1.txt' in files
    assert 'requirements2.in' in files

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_0_test_valid_input
isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_0_test_valid_input.py:8:11: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""