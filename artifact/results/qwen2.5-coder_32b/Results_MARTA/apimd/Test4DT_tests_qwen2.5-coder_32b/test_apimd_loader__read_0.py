
import os
import pytest
from apimd.loader import _read

# Setup for test_valid_case
with open('example.txt', 'w') as f:
    f.write("This is a sample text file.")

# Setup for test_edge_case_empty_file
open('empty.txt', 'a').close()

def teardown_module(module):
    # Cleanup after all tests are done
    os.remove('example.txt')
    os.remove('empty.txt')

def test_valid_case():
    """Test reading from an existing file with valid content."""
    content = _read('example.txt')
    assert content == "This is a sample text file."

def test_edge_case_empty_file():
    """Test reading from an empty file."""
    content = _read('empty.txt')
    assert content == ""

def test_invalid_case_nonexistent_file():
    """Test attempting to read from a non-existent file."""
    with pytest.raises(FileNotFoundError):
        _read('non_existent_file.txt')
