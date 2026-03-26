
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
    ('example.txt', 'Hello, world!', None),
    ('-', 'Hello, world!', None),
    (os.path.expanduser('~/example.txt'), 'Hello, world!', None)
])
def test_valid_inputs(filename, contents, expected):
    with patch('sys.stdout') as mock_stdout:
        burp(filename, contents)
        if filename == '-':
            assert mock_stdout.write.called_with(contents)
        else:
            with open(filename, 'r') as fh:
                assert fh.read() == contents
