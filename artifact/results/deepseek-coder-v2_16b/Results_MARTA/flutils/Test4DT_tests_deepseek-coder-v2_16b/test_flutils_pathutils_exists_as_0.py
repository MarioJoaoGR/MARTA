
import pytest
from flutils.pathutils import exists_as
import pathlib

# Test for a valid directory
def test_valid_directory():
    # Setup
    path = pathlib.Path('/tmp')
    
    # Execution
    result = exists_as(str(path))
    
    # Assertion
    assert result == 'directory'

# Test for a valid file
def test_valid_file():
    # Setup
    path = pathlib.Path('/etc/passwd')
    
    # Execution
    result = exists_as(str(path))
    
    # Assertion
    assert result == 'file'

# Test for an invalid path
def test_invalid_path():
    # Setup
    path = 'nonexistent_path'
    
    # Execution
    result = exists_as(path)
    
    # Assertion
    assert result == ''
