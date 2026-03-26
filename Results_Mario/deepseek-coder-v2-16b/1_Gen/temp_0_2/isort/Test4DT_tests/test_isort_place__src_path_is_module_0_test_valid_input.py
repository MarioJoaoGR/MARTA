
from pathlib import Path
from unittest.mock import MagicMock, patch
import pytest
from isort.place import _src_path_is_module

@pytest.fixture
def mock_dir():
    mock_dir = MagicMock()
    mock_dir.name = 'modulename'
    mock_dir.is_dir.return_value = True
    return mock_dir

@patch('isort.place.exists_case_sensitive')
def test_valid_input(mock_exists_case_sensitive, mock_dir):
    # Mock the exists_case_sensitive function to return True for any path
    mock_exists_case_sensitive.return_value = True
    
    assert _src_path_is_module(mock_dir, "modulename") == True
