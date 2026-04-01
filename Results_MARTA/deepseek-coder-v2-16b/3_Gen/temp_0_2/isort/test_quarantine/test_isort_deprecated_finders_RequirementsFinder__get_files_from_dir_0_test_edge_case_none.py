
from isort.deprecated.finders import RequirementsFinder
import pytest
from unittest.mock import MagicMock

@pytest.fixture
def finder():
    config = MagicMock()  # Create a mock configuration object
    return RequirementsFinder(config=config)  # Pass the mock config to the constructor

def test_get_files_from_dir_edge_case_none(finder):
    path = 'test_directory'
    finder._get_files_from_dir_cached = MagicMock()  # Mock the cached method for testing
    finder._get_files_from_dir_cached.return_value = ['file1.txt', 'file2.in']  # Define what it should return

    result = list(finder._get_files_from_dir(path))
    
    assert result == ['file1.txt', 'file2.in']
    finder._get_files_from_dir_cached.assert_called_once_with(path)  # Ensure the mock method was called with the correct argument
