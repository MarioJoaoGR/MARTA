
import pytest
from pytutils.files import islurp
import sys
import os
import functools

@pytest.mark.parametrize("filename", ["invalid_file_path"])
def test_invalid_file_path(filename):
    with pytest.raises(FileNotFoundError):
        list(islurp(filename))
