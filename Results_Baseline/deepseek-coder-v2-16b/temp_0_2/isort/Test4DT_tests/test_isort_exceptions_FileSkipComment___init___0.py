# Module: isort.exceptions
import pytest

from isort.exceptions import FileSkipComment


# Test case to check the initialization of the exception with a valid file path
def test_file_skip_comment_with_valid_file_path():
    try:
        raise FileSkipComment("example/file/path.py")
    except FileSkipComment as e:
        assert str(e) == "example/file/path.py contains a file skip comment and was skipped."

# Test case to check the initialization of the exception with an invalid file path
def test_file_skip_comment_with_invalid_file_path():
    try:
        raise FileSkipComment("non/existent/file/path.py")
    except FileSkipComment as e:
        assert str(e) == "non/existent/file/path.py contains a file skip comment and was skipped."

# Test case to check the initialization of the exception with an empty string file path
def test_file_skip_comment_with_empty_string_file_path():
    try:
        raise FileSkipComment("")
    except FileSkipComment as e:
        assert str(e) == " contains a file skip comment and was skipped."

# Test case to check the initialization of the exception with None as file path
def test_file_skip_comment_with_none_as_file_path():
    try:
        raise FileSkipComment(None)
    except FileSkipComment as e:
        assert str(e) == "None contains a file skip comment and was skipped."
