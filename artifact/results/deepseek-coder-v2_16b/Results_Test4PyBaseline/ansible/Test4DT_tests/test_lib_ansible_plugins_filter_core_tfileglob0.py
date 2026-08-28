# Module: ansible.plugins.filter.core
import pytest
import glob
import os
from ansible.plugins.filter import core

# Test case 1: Basic usage with a single pathname pattern
def test_fileglob_basic():
    result = core.fileglob('*.txt')
    assert isinstance(result, list), "Expected a list but got something else"
    for item in result:
        assert os.path.isfile(item), f"{item} is not a file"

# Test case 2: Using `os` and `glob` Modules with a specific pattern
def test_fileglob_specific_pattern():
    result = core.fileglob('data/*.csv')
    assert isinstance(result, list), "Expected a list but got something else"
    for item in result:
        assert os.path.isfile(item), f"{item} is not a file"

# Test case 3: Handling no matches case
def test_fileglob_no_matches():
    result = core.fileglob('nonexistentpattern.*')
    assert isinstance(result, list), "Expected an empty list but got something else"
    assert len(result) == 0, "Expected an empty list as there are no matches"

# Test case 4: Using `os` Module to Check File Type with a specific path
def test_fileglob_specific_path():
    result = core.fileglob('/path/to/directory/*.txt')
    assert isinstance(result, list), "Expected a list but got something else"
    for item in result:
        assert os.path.isfile(item), f"{item} is not a file"
