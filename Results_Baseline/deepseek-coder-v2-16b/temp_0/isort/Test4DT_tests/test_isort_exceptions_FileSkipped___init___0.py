# Module: isort.exceptions
# test_isort_exceptions.py
from isort.exceptions import FileSkipped


def test_file_skipped_exception():
    try:
        raise FileSkipped("File is not supported", "example/file/path.txt")
    except FileSkipped as e:
        assert e.message == "File is not supported"
        assert e.file_path == "example/file/path.txt"

def test_file_skipped_exception_with_different_values():
    try:
        raise FileSkipped("Another reason for skipping", "another/file/path.txt")
    except FileSkipped as e:
        assert e.message == "Another reason for skipping"
        assert e.file_path == "another/file/path.txt"
