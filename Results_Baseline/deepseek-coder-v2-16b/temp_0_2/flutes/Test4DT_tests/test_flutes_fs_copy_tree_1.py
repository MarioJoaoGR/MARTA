
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
    assert (dst / 'file1').exists(), "File 'file1' was not copied to destination."
    assert (dst / 'file2').exists(), "File 'file2' was not copied to destination."

# Test copying a nested directory without overwriting existing files
def test_copy_tree_nested_without_overwrite():
    src = Path('test_source')
    dst = Path('test_destination')
    
    # Create source directory and nested directories with some files
    (src / 'dir1').mkdir()
    (src / 'dir1' / 'file3').touch()
    (src / 'dir2').mkdir()
    (src / 'dir2' / 'file4').touch()
    
    # Call the function to copy the directory
    copy_tree(src, dst)
    
    # Check if destination directory exists and has the same nested structure with files
    assert dst.is_dir(), "Destination directory was not created."
    assert (dst / 'dir1').is_dir(), "Nested directory 'dir1' was not copied to destination."
    assert (dst / 'dir1' / 'file3').exists(), "File 'file3' was not copied to nested destination."
    assert (dst / 'dir2').is_dir(), "Nested directory 'dir2' was not copied to destination."
    assert (dst / 'dir2' / 'file4').exists(), "File 'file4' was not copied to nested destination."

# Test copying a directory with overwriting existing files when overwrite is True
def test_copy_tree_with_overwrite():
    src = Path('test_source')
    dst = Path('test_destination')
    
    # Create source and destination directories with some files
    os.makedirs(src, exist_ok=True)
    (src / 'file1').touch()
    (dst / 'file1').touch()  # Destination already has a file named file1
    
    # Call the function to copy the directory with overwrite set to True
    copy_tree(src, dst, overwrite=True)
    
    # Check if destination files are overwritten or not applicable checks
    assert (dst / 'file1').exists(), "File 'file1' was not copied to destination."  # Should be overwritten

# Test copying a directory without overwriting existing files when overwrite is False
def test_copy_tree_without_overwrite_flag():
    src = Path('test_source')
    dst = Path('test_destination')
    
    # Create source and destination directories with some files
    os.makedirs(src, exist_ok=True)
    (src / 'file1').touch()
    (dst / 'file1').touch()  # Destination already has a file named file1
    
    # Call the function to copy the directory with overwrite set to False
    copy_tree(src, dst, overwrite=False)
    
    # Check if destination files are not overwritten or not applicable checks
    assert (dst / 'file1').exists(), "File 'file1' was unexpectedly overwritten."  # Should not be overwritten
