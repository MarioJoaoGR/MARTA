
import pytest
import glob
import os
from ansible.plugins.filter.core import fileglob as core_fileglob

def test_fileglob_basic():
    # Test basic usage of fileglob function
    matched_files = core_fileglob('*.py')
    assert isinstance(matched_files, list), "Expected a list"
    for file in matched_files:
        assert os.path.isfile(file), f"{file} is not a regular file"

def test_fileglob_different_extension():
    # Test finding files with a different extension
    matched_files = core_fileglob('*.txt')
    assert isinstance(matched_files, list), "Expected a list"
    for file in matched_files:
        assert os.path.isfile(file), f"{file} is not a regular file"

def test_fileglob_specific_directory():
    # Test using glob pattern to find files in a specific directory
    current_directory = '.'
    matched_files = core_fileglob(os.path.join(current_directory, '*.py'))
    assert isinstance(matched_files, list), "Expected a list"
    for file in matched_files:
        assert os.path.isfile(file), f"{file} is not a regular file"
