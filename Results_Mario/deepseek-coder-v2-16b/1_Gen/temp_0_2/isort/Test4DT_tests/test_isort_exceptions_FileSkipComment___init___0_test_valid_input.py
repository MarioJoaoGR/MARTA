
import pytest
from isort.exceptions import FileSkipComment

def test_valid_input():
    try:
        raise FileSkipComment('example/file/path.py')
    except FileSkipComment as e:
        assert str(e) == "example/file/path.py contains a file skip comment and was skipped."
