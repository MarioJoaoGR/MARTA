
import pytest
import os
from ansible.module_utils.urls import atexit_remove_file

# Test cases for the atexit_remove_file function

def test_remove_existing_file():
    # Create a temporary file to be removed
    filename = 'test_file.txt'
    with open(filename, 'w') as f:
        f.write('Test content')
    
    # Call the function to remove the file at exit
    atexit_remove_file(filename)
    
    # Check if the file has been removed
    assert not os.path.exists(filename), "File should be removed upon script exit"

def test_remove_nonexistent_file():
    # Call the function for a non-existent file
    filename = 'nonexistent_file.txt'
    atexit_remove_file(filename)
    
    # Check if the file still does not exist
    assert not os.path.exists(filename), "File should not be removed if it doesn't exist"

def test_remove_file_with_error():
    # Create a temporary file that cannot be deleted due to permissions or being open by another process
    filename = 'test_file.txt'
    with open(filename, 'w') as f:
        f.write('Test content')
    
    # Call the function to remove the file at exit (which will fail silently)
    atexit_remove_file(filename)
    
    # Check if the file still exists (since deletion should have failed silently)