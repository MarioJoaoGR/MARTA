
import pytest
from isort.exceptions import FileSkipped

def test_invalid_inputs():
    # Test case 1: Non-string message
    with pytest.raises(FileSkipped) as excinfo:
        raise FileSkipped("Non-string message", "example/file/path.txt")
    assert str(excinfo.value) == "Non-string message"
    
    # Test case 2: Non-string file_path
    with pytest.raises(FileSkipped) as excinfo:
        raise FileSkipped("Error message", b"example/file/path.txt")
    assert str(excinfo.value) == "Error message"
