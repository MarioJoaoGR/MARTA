
import pytest

from isort.exceptions import FileSkipComment


def test_missing_file_path():
    with pytest.raises(FileSkipComment) as exc_info:
        raise FileSkipComment(None)
    
    assert str(exc_info.value) == "None contains a file skip comment and was skipped."
