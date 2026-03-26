
import subprocess
from pathlib import Path
import pytest
import os

# Import the function from the module
from flutes.fs import get_folder_size

def test_get_folder_size_nonexistent_path():
    # Test with a non-existent path
    nonexistent_path = Path("/nonexistent/directory")
    with pytest.raises(subprocess.CalledProcessError):
        get_folder_size(nonexistent_path)

def test_get_folder_size_file_instead_of_directory():
    # Test with a file path instead of a directory
    temp_file = Path("test_temp_file.txt")
    temp_file.write_text("Test content")
    try:
        result = get_folder_size(temp_file)
        assert isinstance(result, int), "The function should return an integer."
        assert result >= 0, "The size of the file should be non-negative."
    finally:
        temp_file.unlink()

def test_get_folder_size_empty_directory():
    # Test with an empty directory
    temp_dir = Path("test_temp_dir")
    temp_dir.mkdir()
    try:
        result = get_folder_size(temp_dir)
        assert isinstance(result, int), "The function should return an integer."
        assert result == 0, "The size of an empty directory should be zero."
    finally:
        temp_dir.rmdir()

def test_get_folder_size_large_directory():
    # Test with a large directory (e.g., /usr/local)
    if os.name == 'posix' and os.path.exists('/usr/local'):
        result = get_folder_size(Path("/usr/local"))
        assert isinstance(result, int), "The function should return an integer."
        assert result >= 0, "The size of the directory should be non-negative."
