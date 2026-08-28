
import pytest
from unittest.mock import patch, MagicMock
import os

def _read(path: str) -> str:
    """Read the script from file."""
    with open(path, 'r') as f:
        return f.read()

# Test reading a valid file
def test_valid_file_read():
    # Create a temporary file with known content
    temp_content = "This is a test content."
    with open('temp_test_file.txt', 'w') as f:
        f.write(temp_content)
    
    try:
        assert _read('temp_test_file.txt') == temp_content
    finally:
        os.remove('temp_test_file.txt')

# Test handling None input
def test_none_input():
    with pytest.raises(TypeError):
        _read(None)

# Test handling non-existent file
def test_non_existent_file():
    with pytest.raises(FileNotFoundError):
        _read('nonexistent_file.txt')
