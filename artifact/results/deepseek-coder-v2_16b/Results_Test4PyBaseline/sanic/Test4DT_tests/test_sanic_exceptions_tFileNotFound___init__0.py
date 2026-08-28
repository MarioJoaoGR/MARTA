
# Module: sanic.exceptions
import pytest
from sanic.exceptions import FileNotFound

# Test Case 1: Basic Usage of FileNotFound Exception
def test_file_not_found_basic():
    with pytest.raises(FileNotFound) as excinfo:
        raise FileNotFound("File does not exist", "/path/to/file", "http://example.com/files/file.txt")
    
    assert str(excinfo.value) == "File does not exist"
    assert excinfo.value.path == "/path/to/file"