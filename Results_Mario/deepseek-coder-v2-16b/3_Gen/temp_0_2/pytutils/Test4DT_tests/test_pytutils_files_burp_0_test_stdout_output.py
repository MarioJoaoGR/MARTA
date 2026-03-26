
import sys
import os
import pytest
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

@pytest.mark.parametrize("filename, contents, expected", [
    ('-', 'Hello, world!', 'Hello, world!'),
])
def test_stdout_output(capsys, filename, contents, expected):
    burp(filename, contents)
    captured = capsys.readouterr()
    assert captured.out == expected
