
import pytest
from isort.exceptions import FileSkipped

def test_valid_inputs():
    message = "File is not in a supported format"
    file_path = "example/file/path.txt"
    
    try:
        raise FileSkipped(message, file_path)
    except FileSkipped as e:
        assert str(e) == message
        assert e.file_path == file_path
