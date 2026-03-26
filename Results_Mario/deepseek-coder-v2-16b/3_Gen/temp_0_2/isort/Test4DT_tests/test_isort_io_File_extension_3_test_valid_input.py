
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

def test_valid_input():
    # Create a mock file path and stream
    file_path = Path("/some/file/path.txt")
    file_stream = StringIO()
    
    # Initialize the File object with the mock file path and stream
    my_file = File(file_path, file_stream, "utf-8")
    
    # Assert that the extension method returns the correct file extension
    assert my_file.extension() == "txt"
