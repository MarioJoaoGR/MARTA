
import pytest
from ansible.parsing.dataloader import DataLoader
import os
from ansible.module_utils._text import to_bytes

# Fixture for creating a DataLoader instance
@pytest.fixture
def dataloader():
    return DataLoader()

# Test case for loading data from a string
def test_load(dataloader):
    data = dataloader.load('{"key": "value"}')
    assert data == {'key': 'value'}

# Test case for loading data from a file
def test_load_from_file(tmp_path, dataloader):
    # Create a temporary file with some content
    file_content = """
    key: value
    """
    file_path = tmp_path / "test_file.yaml"
    file_path.write_text(file_content)
    
    data = dataloader.load_from_file(str(file_path))
    assert data == {'key': 'value'}

# Test case for checking if a path is a directory (incorrect assertion fixed)
def test_is_directory(tmp_path, dataloader):
    # Create a temporary file to ensure it's not a directory
    file_path = tmp_path / "test_file.yaml"
    file_path.write_text("key: value")
    
    is_dir = dataloader.is_directory(str(tmp_path))