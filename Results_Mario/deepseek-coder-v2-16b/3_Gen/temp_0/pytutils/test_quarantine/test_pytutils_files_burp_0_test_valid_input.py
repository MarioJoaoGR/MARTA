
import sys
from unittest.mock import patch
import pytest
from pytutils.files import burp

def test_valid_input():
    # Test writing to a file
    with patch('sys.stdout', new=StringIO()) as mock_stdout:
        burp('example.txt', 'Hello, world!')
        assert open('example.txt').read() == 'Hello, world!'
    
    # Test writing to stdout
    captured_output = StringIO()
    with patch('sys.stdout', new=captured_output):
        burp('-', 'Hello, world!', allow_stdout=True)
        assert captured_output.getvalue().strip() == 'Hello, world!'
    
    # Test expanding user home directory and environment variables in the filename
    with patch('os.path.expanduser', return_value='expanded_path'):
        with patch('os.path.expandvars', return_value='final_path'):
            burp('~/example.txt', 'Hello, world!', expanduser=True, expandvars=True)
            assert open('final_path').read() == 'Hello, world!'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_files_burp_0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_files_burp_0_test_valid_input.py:9:33: E0602: Undefined variable 'StringIO' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_files_burp_0_test_valid_input.py:14:22: E0602: Undefined variable 'StringIO' (undefined-variable)


"""