
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

def test_invalid_input():
    mock_file = File(path=None, stream=StringIO('content'), encoding='utf-8')
    with pytest.raises(AttributeError):
        mock_file.extension()
