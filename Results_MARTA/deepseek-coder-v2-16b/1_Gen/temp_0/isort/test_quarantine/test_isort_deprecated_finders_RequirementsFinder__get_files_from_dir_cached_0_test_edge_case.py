
import os
from isort.deprecated.finders import RequirementsFinder
import pytest
from unittest.mock import patch, MagicMock

@pytest.fixture
def finder():
    return RequirementsFinder()

def test_get_files_from_dir_cached(finder):
    with patch('os.listdir', return_value=['requirements1.txt', 'requirements2.in', 'otherfile.txt']):
        with patch('os.path.join', side_effect=lambda path, fname: os.path.join(path, fname)):
            with patch('os.path.isdir', side_effect=[True, False]):
                with patch('os.listdir', return_value=['file1.txt', 'file2.in']):
                    assert finder._get_files_from_dir_cached('project') == [
                        'project/requirements1.txt', 
                        'project/requirements2.in', 
                        'project/requirements/file1.txt', 
                        'project/requirements/file2.in'
                    ]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_cached_0_test_edge_case
isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_cached_0_test_edge_case.py:9:11: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""