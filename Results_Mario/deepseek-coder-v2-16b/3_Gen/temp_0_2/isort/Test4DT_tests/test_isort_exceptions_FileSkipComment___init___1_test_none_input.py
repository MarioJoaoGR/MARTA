
from isort.exceptions import FileSkipComment
import pytest

def test_none_input():
    with pytest.raises(FileSkipComment) as exc_info:
        raise FileSkipComment("path/to/your/file.py")
    
    assert str(exc_info.value) == "path/to/your/file.py contains a file skip comment and was skipped."
