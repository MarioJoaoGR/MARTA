
import pytest

from isort.exceptions import FileSkipComment


def test_invalid_input():
    invalid_file_path = "nonexistent/path/to/file.py"
    with pytest.raises(FileSkipComment) as exc_info:
        raise FileSkipComment(invalid_file_path)
    
    assert str(exc_info.value) == f"{invalid_file_path} contains a file skip comment and was skipped."
