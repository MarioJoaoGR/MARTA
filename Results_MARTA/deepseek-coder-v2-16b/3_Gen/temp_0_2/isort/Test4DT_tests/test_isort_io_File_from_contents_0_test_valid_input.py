
import pytest
from io import StringIO, BytesIO
from pathlib import Path
from isort.io import File

def test_valid_input():
    contents = 'print("Hello, World!")'
    filename = 'example_file.py'
    
    file = File.from_contents(contents, filename)
    
    assert isinstance(file, File), "The result should be an instance of the File class."
    assert file.path == Path(filename).resolve(), f"Expected path to be {Path(filename).resolve()}, but got {file.path}"
    assert file.encoding is not None, "Encoding should be detected and assigned."
    assert file.stream.read() == contents, "The content of the stream should match the provided contents."
