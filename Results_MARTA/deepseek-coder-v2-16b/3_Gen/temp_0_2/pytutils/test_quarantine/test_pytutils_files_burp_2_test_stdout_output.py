
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

@pytest.mark.parametrize("filename, contents, allow_stdout", [("-", "Hello, world!", True)])
def test_stdout_output(filename, contents, allow_stdout):
    with patch('sys.stdout', new=StringIO()) as mock_stdout:
        burp(filename, contents, allow_stdout=allow_stdout)
        assert mock_stdout.getvalue() == "Hello, world!"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_files_burp_2_test_stdout_output
pytutils/Test4DT_tests/test_pytutils_files_burp_2_test_stdout_output.py:24:33: E0602: Undefined variable 'StringIO' (undefined-variable)


"""