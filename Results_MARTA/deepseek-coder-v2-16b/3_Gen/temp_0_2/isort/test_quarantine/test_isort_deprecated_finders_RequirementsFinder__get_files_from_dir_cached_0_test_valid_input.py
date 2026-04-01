
import os
from isort.deprecated.finders import RequirementsFinder
import pytest
from unittest.mock import patch

@pytest.fixture
def finder():
    return RequirementsFinder()

def test_get_files_from_dir_cached(finder):
    with patch('os.listdir', return_value=['requirements1.txt', 'requirements2.in', 'otherfile.txt']):
        with patch('os.path.isdir', side_effect=[False, True]):
            with patch('os.path.isfile', side_effect=[True, False]):
                with patch('os.listdir', return_value=['requirements1.txt', 'requirements2.in']):
                    files = finder._get_files_from_dir_cached('project')
                    assert files == ['project/requirements1.txt', 'project/requirements2.in']

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_cached_0_test_valid_input
isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_cached_0_test_valid_input.py:9:11: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""