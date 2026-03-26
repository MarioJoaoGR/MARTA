
import pytest
from isort.exceptions import FileSkipped

def test_edge_cases():
    with pytest.raises(FileSkipped) as exc_info:
        raise FileSkipped("File is not supported", "example/file/path.txt")
    
    assert str(exc_info.value) == "File is not supported"
    assert exc_info.value.file_path == "example/file/path.txt"
