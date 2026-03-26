
import pytest
from pathlib import Path
from flutes.io import progress_open

def test_error_handling():
    with pytest.raises(FileNotFoundError):
        # Test for non-existent file path
        progress_open("nonexistent_file.txt")
    
    with pytest.raises(ValueError):
        # Test for unsupported mode
        progress_open(Path("existing_file.txt"), mode='w')
    
    with pytest.raises(FileNotFoundError):
        # Test for missing file path (should raise FileNotFoundError)
        progress_open(Path("nonexistent_file.txt"))
