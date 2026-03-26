
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

@pytest.mark.parametrize("filename, contents, expected_exception", [
    (None, 'Invalid input', TypeError),
])
def test_invalid_input(filename, contents, expected_exception):
    with pytest.raises(expected_exception):
        burp(filename, contents)
