
import sys
import os
from unittest.mock import patch
import pytest
from pytutils.files import burp

def test_valid_input_file():
    with patch('sys.stdout', new=open('/tmp/output.txt', 'w')) as mock_stdout:
        # Test writing to a file
        burp('example.txt', 'Hello, world!')
        with open('example.txt', 'r') as f:
            assert f.read() == 'Hello, world!'
        
        # Test writing to stdout
        burp('-', 'Hello, world!', allow_stdout=True)
        mock_stdout.write('Hello, world!')
        with open('/tmp/output.txt', 'r') as f:
            assert f.read() == 'Hello, world!'
        
        # Test expanding user home directory and environment variables in the filename
        with patch.dict(os.environ, {'USER': 'testuser'}):
            burp('~/documents/report.txt', 'Data for {user}', expanduser=True, expandvars=True)
            assert os.path.expanduser('~/documents/report.txt') == '~'
            assert os.path.expandvars('~/documents/report.txt') == '/home/testuser/documents/report.txt'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_files_burp_0_test_valid_input_file.py F [100%]

=================================== FAILURES ===================================
____________________________ test_valid_input_file _____________________________

    def test_valid_input_file():
        with patch('sys.stdout', new=open('/tmp/output.txt', 'w')) as mock_stdout:
            # Test writing to a file
            burp('example.txt', 'Hello, world!')
            with open('example.txt', 'r') as f:
                assert f.read() == 'Hello, world!'
    
            # Test writing to stdout
            burp('-', 'Hello, world!', allow_stdout=True)
            mock_stdout.write('Hello, world!')
            with open('/tmp/output.txt', 'r') as f:
>               assert f.read() == 'Hello, world!'
E               AssertionError: assert '' == 'Hello, world!'
E                 
E                 - Hello, world!

pytutils/Test4DT_tests/test_pytutils_files_burp_0_test_valid_input_file.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_files_burp_0_test_valid_input_file.py::test_valid_input_file
============================== 1 failed in 0.06s ===============================
"""