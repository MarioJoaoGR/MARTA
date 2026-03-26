
from isort.exceptions import FileSkipComment
import pytest

def test_invalid_input():
    with pytest.raises(FileSkipComment) as excinfo:
        raise FileSkipComment("example/file/path.py")
    
    assert str(excinfo.value) == "example/file/path.py contains a file skip comment and was skipped."
