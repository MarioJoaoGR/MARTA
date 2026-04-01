
import pytest
import sys
import os
from unittest.mock import patch

def burp(filename, contents, mode='w', allow_stdout=True, expanduser=True, expandvars=True):
    """
    Write `contents` to `filename`.
    """
    if filename == '-' and allow_stdout:
        sys.stdout.write(contents)
    else:
        if expanduser:
            filename = os.path.expanduser(filename)
        if expandvars:
            filename = os.path.expandvars(filename)

        with open(filename, mode) as fh:
            fh.write(contents)

@pytest.mark.parametrize("filename", [None])
def test_invalid_filename(filename):
    with pytest.raises(TypeError):
        burp(filename, "test content")
