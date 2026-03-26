
import pytest
from pathlib import Path
from io import StringIO

class File:
    stream: StringIO
    path: Path
    encoding: str
    
    def __init__(self, path: Path, stream: StringIO, encoding: str):
        self.path = path
        self.stream = stream
        self.encoding = encoding
        
    def extension(self) -> str:
        return self.path.suffix.lstrip(".")

def test_edge_case():
    # Create a File object with an empty file path
    file_path = Path("")
    file_stream = StringIO()
    my_file = File(file_path, file_stream, "utf-8")
    
    # Assert that the extension method returns an empty string for an empty file path
    assert my_file.extension() == ""
