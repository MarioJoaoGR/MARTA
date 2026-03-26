
import subprocess
from pathlib import Path
import pytest
import os

# Import the function from the module
from flutes.fs import get_folder_size

def test_get_folder_size_string_path():
    # Test with a string representing a path
    folder_path = os.getcwd()  # Get the current working directory as a string
    result = get_folder_size(Path(folder_path))
    assert isinstance(result, int), "The function should return an integer."
    assert result >= 0, "The size of the folder should be non-negative."

def test_get_folder_size_path_object():
    # Test with a Path object
    folder_path = Path("/some/directory")  # Specify a directory path as a Path object
    with pytest.raises(subprocess.CalledProcessError):
        get_folder_size(folder_path)

def test_get_folder_size_alternative_directory():
    # Test with a different directory as a string
    folder_path = "/usr/local"  # Specify a different directory as a string
    result = get_folder_size(Path(folder_path))
    assert isinstance(result, int), "The function should return an integer."