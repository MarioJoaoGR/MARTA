
import pytest
from isort.exceptions import FileSkipComment as IsortFileSkipComment

def test_valid_input():
    file_path = "valid/file/path"
    with pytest.raises(IsortFileSkipComment) as exc_info:
        raise IsortFileSkipComment(file_path)
    assert str(exc_info.value) == f"{file_path} contains a file skip comment and was skipped."
