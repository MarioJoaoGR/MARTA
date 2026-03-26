
import sys
from io import StringIO
import os
import pytest
from pytutils.files import burp

def test_valid_input():
    # Test writing to a file
    filename = 'testfile.txt'
    contents = 'Hello, world!'
    expected_output = 'Hello, world!'
    
    with StringIO() as output:
        sys.stdout = output
        burp(filename, contents)
        assert output.getvalue() == expected_output
        
    # Test writing to stdout
    filename = '-'
    contents = 'Hello, world!'
    expected_output = 'Hello, world!'
    
    with StringIO() as output:
        sys.stdout = output
        burp(filename, contents)
        assert output.getvalue() == expected_output
        
    # Test expanding user home directory and environment variables in the filename
    filename = os.path.expanduser('~/testfile.txt')
    filename = os.path.expandvars(filename)
    contents = 'Hello, world!'
    expected_output = 'Hello, world!'
    
    with StringIO() as output:
        sys.stdout = output
        burp(filename, contents)
        assert output.getvalue() == expected_output

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

pytutils/Test4DT_tests/test_pytutils_files_burp_0_test_valid_input.py F  [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Test writing to a file
        filename = 'testfile.txt'
        contents = 'Hello, world!'
        expected_output = 'Hello, world!'
    
        with StringIO() as output:
            sys.stdout = output
            burp(filename, contents)
>           assert output.getvalue() == expected_output
E           AssertionError: assert '' == 'Hello, world!'
E             
E             - Hello, world!

pytutils/Test4DT_tests/test_pytutils_files_burp_0_test_valid_input.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_files_burp_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.06s ===============================
"""