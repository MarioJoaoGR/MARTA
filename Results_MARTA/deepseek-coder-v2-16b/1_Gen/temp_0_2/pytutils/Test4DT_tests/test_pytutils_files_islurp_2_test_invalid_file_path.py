
import pytest
from pytutils.files import islurp
import sys
import os

def test_invalid_file_path():
    # Test that islurp raises a FileNotFoundError when given an invalid file path
    with pytest.raises(FileNotFoundError):
        list(islurp('nonexistent_file.txt'))
