# Module: flutes.fs
import pytest
from pathlib import Path
import os
from typing import Iterator, List

# Import the function from its module
from flutes.fs import scandir

def test_scandir_with_pathlib_path():
    # Define a temporary directory for testing
    temp_dir = Path('/tmp/test_directory')
    temp_dir.mkdir(parents=True, exist_ok=True)
    
    # Create some files and subdirectories to test the scandir function
    (temp_dir / 'file1').touch()
    (temp_dir / 'subdir1').mkdir()
    
    expected_paths = [temp_dir / 'file1', temp_dir / 'subdir1']
    result_paths = list(scandir(temp_dir))
    
    assert len(result_paths) == 2, "Expected two paths but got a different number."
    for path in expected_paths:
        assert str(path) in [str(p) for p in result_paths], f"Path {path} not found in the results."
    
    # Clean up by removing the temporary directory and its contents
    for item in temp_dir.iterdir():
        if item.is_file() or item.is_dir():
            item.unlink() if item.is_file() else item.rmdir()
    temp_dir.rmdir()

def test_scandir_with_string_path():
    # Define a temporary directory for testing
    temp_dir = '/tmp/test_directory'
    os.makedirs(temp_dir, exist_ok=True)
    
    # Create some files and subdirectories to test the scandir function
    (Path(temp_dir) / 'file1').touch()
    (Path(temp_dir) / 'subdir1').mkdir()
    
    expected_paths = [Path(temp_dir) / 'file1', Path(temp_dir) / 'subdir1']
    result_paths = list(scandir(temp_dir))
    
    assert len(result_paths) == 2, "Expected two paths but got a different number."
    for path in expected_paths:
        assert str(path) in [str(p) for p in result_paths], f"Path {path} not found in the results."
    
    # Clean up by removing the temporary directory and its contents
    for item in Path(temp_dir).iterdir():
        if item.is_file() or item.is_dir():
            item.unlink() if item.is_file() else item.rmdir()
    os.rmdir(temp_dir)

def test_scandir_with_invalid_path():
    with pytest.raises(FileNotFoundError):
        list(scandir('/nonexistent/directory'))
