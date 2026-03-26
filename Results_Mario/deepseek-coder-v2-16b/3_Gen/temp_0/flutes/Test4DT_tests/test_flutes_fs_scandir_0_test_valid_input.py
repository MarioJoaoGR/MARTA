
import pytest
from pathlib import Path
from flutes.fs import scandir

def test_valid_input():
    # Test with a string representing a directory path
    test_dir_path = "/some/directory"
    
    # Mock the behavior of os.scandir to raise FileNotFoundError for non-existent paths
    from unittest.mock import patch, MagicMock
    
    with patch('os.scandir', side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            result = list(scandir(test_dir_path))
