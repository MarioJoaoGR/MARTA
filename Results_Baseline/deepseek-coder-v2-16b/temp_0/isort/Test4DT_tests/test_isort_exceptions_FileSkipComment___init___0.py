# Module: isort.exceptions
import pytest

from isort.exceptions import FileSkipComment


# Test case for FileSkipComment exception with a valid file path
def test_file_skip_comment_with_valid_file_path():
    try:
        raise FileSkipComment("path/to/your/file.py")
    except FileSkipComment as e:
        assert str(e) == "path/to/your/file.py contains a file skip comment and was skipped."

# Test case for FileSkipComment exception with an invalid file path
def test_file_skip_comment_with_invalid_file_path():
    try:
        raise FileSkipComment("non/existent/file.py")
    except FileSkipComment as e:
        assert str(e) == "non/existent/file.py contains a file skip comment and was skipped."

# Test case for FileSkipComment exception with an empty string file path
def test_file_skip_comment_with_empty_string():
    try:
        raise FileSkipComment("")
    except FileSkipComment as e:
        assert str(e) == " contains a file skip comment and was skipped."
