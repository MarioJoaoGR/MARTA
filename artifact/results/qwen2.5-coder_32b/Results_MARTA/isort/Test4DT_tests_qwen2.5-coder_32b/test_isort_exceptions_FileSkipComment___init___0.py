
import pytest
from isort.exceptions import FileSkipComment

def test_file_skip_comment_exception():
    file_path = '/path/to/skipped_file.py'
    with pytest.raises(FileSkipComment) as excinfo:
        raise FileSkipComment(file_path)
    assert str(excinfo.value) == f"{file_path} contains an file skip comment and was skipped."

def test_file_skip_comment_with_different_path():
    file_path = '/another/path/to/ignored_script.py'
    with pytest.raises(FileSkipComment) as excinfo:
        raise FileSkipComment(file_path)
    assert str(excinfo.value) == f"{file_path} contains an file skip comment and was skipped."
