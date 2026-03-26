
import pytest
from isort.exceptions import ExistingSyntaxErrors

def test_valid_input():
    """Test with a valid file path"""
    file_path = 'example.py'
    
    try:
        raise ExistingSyntaxErrors(file_path)
    except ExistingSyntaxErrors as e:
        assert e.file_path == 'example.py'
