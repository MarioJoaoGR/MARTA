
import pytest
from isort.exceptions import FileSkipped

def test_file_skipped_with_valid_arguments():
    message = "File does not exist"
    file_path = "/path/to/file.py"
    with pytest.raises(FileSkipped) as excinfo:
        raise FileSkipped(message, file_path)
    
    assert str(excinfo.value) == message
    assert excinfo.value.file_path == file_path



def test_file_skipped_with_empty_string_message():
    file_path = "/path/to/file.py"
    with pytest.raises(FileSkipped) as excinfo:
        raise FileSkipped("", file_path)
    
    assert str(excinfo.value) == ""
    assert excinfo.value.file_path == file_path
