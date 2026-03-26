
import pytest
from pathlib import Path
from io import StringIO
from typing import TextIO

class File:
    stream: TextIO
    path: Path
    encoding: str
    
    def __init__(self, path: Path, stream: TextIO, encoding: str):
        self.path = path
        self.stream = stream
        self.encoding = encoding
        
    def extension(self) -> str:
        return self.path.suffix.lstrip(".")

def test_valid_input():
    # Setup
    mock_content = 'content'
    mock_path = Path('/some/file/path.txt')
    mock_stream = StringIO(mock_content)
    my_file = File(mock_path, mock_stream, 'utf-8')
    
    # Test
    assert my_file.extension() == 'txt'
