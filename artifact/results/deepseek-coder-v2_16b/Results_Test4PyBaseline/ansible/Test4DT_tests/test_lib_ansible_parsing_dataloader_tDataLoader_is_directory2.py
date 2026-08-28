
import pytest
from ansible.parsing.dataloader import DataLoader
import os
from ansible.module_utils._text import to_bytes

# Fixture for creating a DataLoader instance
@pytest.fixture
def dataloader():
    return DataLoader()

# Test case for checking if a valid directory path is recognized as such
def test_is_directory_valid_dir(tmp_path, dataloader):
    # Create a temporary directory to ensure it's recognized as a directory
    dir_path = tmp_path / "test_dir"
    dir_path.mkdir()
    
    is_dir = dataloader.is_directory(str(dir_path))
    assert is_dir, f"Expected {dir_path} to be recognized as a directory."

# Test case for checking if a valid file path is not recognized as a directory
def test_is_directory_valid_file(tmp_path, dataloader):
    # Create a temporary file to ensure it's not a directory
    file_path = tmp_path / "test_file.txt"
    file_path.write_text("content")
    
    is_dir = dataloader.is_directory(str(file_path))