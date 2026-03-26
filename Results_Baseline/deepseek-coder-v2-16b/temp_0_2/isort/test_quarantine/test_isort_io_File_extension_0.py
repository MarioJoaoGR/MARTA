
import pytest
from pathlib import Path
from io import TextIOBase
from typing import TextIO

# Assuming the File class is defined as follows:
class File:
    stream: TextIO
    path: Path
    encoding: str
    
    def __init__(self, file_path: str, mode: str = 'r', encoding: str = 'utf-8'):
        self.path = Path(file_path)
        self.stream = open(file_path, mode, encoding=encoding)
        self.encoding = encoding
        
    def extension(self) -> str:
        return self.path.suffix.lstrip(".")

# Test cases for the File class
def test_file_extension():
    # Create a temporary file with an example extension
    temp_file_path = "example.txt"
    file_instance = File(temp_file_path)
    assert file_instance.extension() == "txt", f"Expected 'txt' but got {file_instance.extension()}"

def test_file_extension_with_dot():
    # Create a temporary file with an example extension including a dot
    temp_file_path = "example.txt"
    file_instance = File(temp_file_path)