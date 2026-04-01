
import pytest
from isort.exceptions import FileSkipComment
import os

def test_invalid_input():
    with pytest.raises(FileSkipComment) as exc_info:
        raise FileSkipComment("non/existent/file.py")
    
    assert str(exc_info.value) == "non/existent/file.py contains a file skip comment and was skipped."
