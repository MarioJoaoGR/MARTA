
import pytest
from isort.exceptions import FileSkipComment

def test_valid_input():
    file_path = "path/to/your/file.py"
    try:
        raise FileSkipComment(file_path)
    except FileSkipComment as e:
        assert str(e) == f"{file_path} contains a file skip comment and was skipped."
