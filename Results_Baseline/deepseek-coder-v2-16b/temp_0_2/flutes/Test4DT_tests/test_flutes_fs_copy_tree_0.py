
import pytest
from pathlib import Path
import os
import shutil
from flutes.fs import copy_tree

# Helper function to clean up temporary directories created during tests
def remove_test_dirs():
    test_dir = Path('test_copy')
    if test_dir.exists() and test_dir.is_dir():
        shutil.rmtree(test_dir)

# Test copying a directory without overwriting existing files
def test_copy_tree_without_overwrite():
    src = Path('test_source')
    dst = Path('test_destination')
    
    # Create source directory and populate it with some files
    os.makedirs(src, exist_ok=True)
    (src / 'file1').touch()
    (src / 'file2').touch()
    
    # Call the function to copy the directory
    copy_tree(src, dst)
    
    # Check if destination directory exists and has the same files as source
    assert dst.is_dir(), "Destination directory was not created."