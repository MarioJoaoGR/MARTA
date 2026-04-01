
import pytest

from isort.exceptions import FileSkipped


def test_valid_inputs():
    message = "This file is not supported"
    file_path = "/path/to/file.py"
    
    try:
        raise FileSkipped(message, file_path)
    except FileSkipped as e:
        assert e.message == message
        assert e.file_path == file_path
