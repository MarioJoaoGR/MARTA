
import pytest
import os
from pytutils.path import join_each  # Assuming this is a hypothetical module for path joining

# Scenario 1: Test standard input with valid directory and file names
def test_valid_input():
    parent = '/path/to/directory'
    files = ['file1.txt', 'file2.txt', 'file3.txt']
    expected_paths = [os.path.join(parent, f) for f in files]
    
    paths = list(join_each(parent, files))
    assert paths == expected_paths

# Scenario 2: Test with None input to check error handling
def test_edge_case_none():
    parent = None
    files = ['file1.txt', 'file2.txt']
    
    with pytest.raises(TypeError):
        list(join_each(parent, files))

# Scenario 3: Test with invalid directory path to ensure proper error handling
def test_error_handling():
    parent = 123
    files = ['file1.txt', 'file2.txt']
    
    with pytest.raises(TypeError):
        list(join_each(parent, files))
