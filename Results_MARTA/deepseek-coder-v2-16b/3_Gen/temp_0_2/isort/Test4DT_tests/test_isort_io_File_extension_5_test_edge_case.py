
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

def test_edge_case():
    # Create a mock file object with None values for path and stream
    my_file = File(None, None, 'utf-8')
    
    # Test the extension method when both path and stream are None
    with pytest.raises(AttributeError):
        assert my_file.extension() is None
