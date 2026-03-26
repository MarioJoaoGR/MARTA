# Module: isort.api
from pathlib import Path

import pytest

from isort.api import _tmp_file  # Import the function from its module


# Test cases for _tmp_file function
def test_basic_usage():
    class FileMock:
        def __init__(self, path):
            self.path = Path(path)
        
        def with_suffix(self, suffix):
            return self.path.with_suffix(suffix)
    
    file_obj = FileMock(path='/path/to/original/file.txt')
    sorted_file_path = _tmp_file(source_file=file_obj)
    assert str(sorted_file_path) == '/path/to/original/file.txt.isorted'

def test_different_path():
    class FileMock:
        def __init__(self, path):
            self.path = Path(path)
        
        def with_suffix(self, suffix):
            return self.path.with_suffix(suffix)
    
    another_file_obj = FileMock(path='/different/path/example.csv')
    sorted_file_path = _tmp_file(source_file=another_file_obj)
    assert str(sorted_file_path) == '/different/path/example.csv.isorted'

def test_with_specific_suffix():
    class FileMock:
        def __init__(self, path):
            self.path = Path(path)
        
        def with_suffix(self, suffix):
            return self.path.with_suffix(suffix)
    
    file_obj = FileMock(path='/another/path/example.txt')
    sorted_file_path = _tmp_file(source_file=file_obj)
    assert str(sorted_file_path) == '/another/path/example.txt.isorted'
