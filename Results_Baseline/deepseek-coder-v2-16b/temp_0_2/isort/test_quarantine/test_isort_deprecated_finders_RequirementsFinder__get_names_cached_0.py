
# Module: isort.deprecated.finders
import os
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
import pytest
from isort.deprecated.finders import RequirementsFinder, parse_requirements

@pytest.fixture(scope="module")
def finder():
    return RequirementsFinder()

@patch('isort.deprecated.finders.parse_requirements', side_effect=lambda path: ["package1", "package2"])
def test_get_names_cached(mock_parse_requirements, finder):
    with TemporaryDirectory() as temp_dir:
        req_file_path = Path(temp_dir) / 'requirements.txt'
        with open(req_file_path, 'w') as file:
            file.write("package1\npackage2")
        
        names = finder._get_names_cached(str(req_file_path))
        assert names == ['package1', 'package2']

@patch('isort.deprecated.finders.parse_requirements', side_effect=lambda path: ["package3", "package4"])
def test_get_names_cached_different_content(mock_parse_requirements, finder):
    with TemporaryDirectory() as temp_dir:
        req_file_path = Path(temp_dir) / 'requirements.txt'
        with open(req_file_path, 'w') as file:
            file.write("package3\npackage4")
        
        names = finder._get_names_cached(str(req_file_path))
        assert names == ['package3', 'package4']

def test_get_names_cached_invalid_extension(finder):
    with TemporaryDirectory() as temp_dir:
        req_file_path = Path(temp_dir) / 'requirements.bad'
        with open(req_file_path, 'w') as file:
            file.write("package1\npackage2")
        
        with pytest.raises(Exception):  # Assuming the function raises an exception for unsupported extensions
            finder._get_names_cached(str(req_file_path))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_RequirementsFinder__get_names_cached_0
isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_names_cached_0.py:12:11: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""