
import pytest
from pytutils.files import burp
import sys
import os

@pytest.mark.parametrize("filename, contents, mode, allow_stdout, expanduser, expandvars, expected", [
    ('example.txt', 'Hello, world!', 'w', True, True, True, None),
    ('-', 'Hello, world!', 'w', True, False, False, None),
])
def test_burp(filename, contents, mode, allow_stdout, expanduser, expandvars, expected):
    # Capture stdout to check if the output is as expected
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    burp(filename, contents, mode=mode, allow_stdout=allow_stdout, expanduser=expanduser, expandvars=expandvars)
    
    # Reset stdout to its original state
    sys.stdout = sys.__stdout__
    
    if filename == '-':
        assert captured_output.getvalue() == contents
    else:
        with open(filename, 'r') as fh:
            file_contents = fh.read()
            assert file_contents == contents

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_files_burp_0_test_valid_inputs
pytutils/Test4DT_tests/test_pytutils_files_burp_0_test_valid_inputs.py:13:22: E0602: Undefined variable 'io' (undefined-variable)


"""