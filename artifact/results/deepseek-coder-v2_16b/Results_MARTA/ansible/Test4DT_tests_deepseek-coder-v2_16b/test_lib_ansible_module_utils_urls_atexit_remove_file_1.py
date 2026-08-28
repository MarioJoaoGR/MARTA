
import pytest
import os
from ansible.module_utils.urls import atexit_remove_file


def test_atexit_remove_file_existent():
    # Create a temporary file for testing
    temp_file_path = 'temp_file.txt'
    open(temp_file_path, 'w').close()
    
    try:
        atexit_remove_file(temp_file_path)
        assert not os.path.exists(temp_file_path), "File should have been removed"
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_file_path):
            os.unlink(temp_file_path)