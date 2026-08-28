
import pytest
from ansible.errors import AnsibleParserError, AnsibleFileNotFound  # Corrected imports and added missing variables
from ansible.parsing.dataloader import DataLoader
import os

# Fixture for creating a DataLoader instance
@pytest.fixture
def dataloader():
    return DataLoader()

# Test case to check if the function raises an error with invalid file name type
def test_get_file_contents_invalid_type(dataloader):
    with pytest.raises(AnsibleParserError) as excinfo:
        dataloader._get_file_contents(None)
    assert str(excinfo.value) == "Invalid filename: 'None'"

# Test case to check if the function raises an error when file name is empty string
def test_get_file_contents_empty_string(dataloader):
    with pytest.raises(AnsibleParserError) as excinfo:
        dataloader._get_file_contents("")
    assert str(excinfo.value) == "Invalid filename: ''"

# Test case to check if the function correctly handles a non-existent file path
def test_get_file_contents_non_existent_file(dataloader):
    with pytest.raises(AnsibleFileNotFound) as excinfo:
        dataloader._get_file_contents("nonexistent_file")