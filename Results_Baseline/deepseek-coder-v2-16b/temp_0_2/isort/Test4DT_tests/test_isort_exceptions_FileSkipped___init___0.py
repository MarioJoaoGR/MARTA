# Module: isort.exceptions
# test_isort_exceptions.py
import pytest

from isort.exceptions import FileSkipped


def test_file_skipped_exception():
    with pytest.raises(FileSkipped) as excinfo:
        raise FileSkipped("File contains invalid data", "path/to/file.txt")
    assert str(excinfo.value) == "File contains invalid data"
    assert excinfo.value.file_path == "path/to/file.txt"

def test_file_skipped_exception_different_message():
    with pytest.raises(FileSkipped) as excinfo:
        raise FileSkipped("File exceeds size limit", "path/to/another_file.txt")
    assert str(excinfo.value) == "File exceeds size limit"
    assert excinfo.value.file_path == "path/to/another_file.txt"

def test_file_skipped_exception_unexpected_error():
    with pytest.raises(FileSkipped) as excinfo:
        raise FileSkipped("Unexpected system error", "path/to/unexpected_file.txt")
    assert str(excinfo.value) == "Unexpected system error"
    assert excinfo.value.file_path == "path/to/unexpected_file.txt"
