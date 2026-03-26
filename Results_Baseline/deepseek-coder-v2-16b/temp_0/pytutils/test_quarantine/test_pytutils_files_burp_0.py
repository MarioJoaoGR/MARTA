
import pytest
import sys
import os
from pytutils.files import burp

# Test writing to a file
def test_burp_file():
    # Create an empty file for testing purposes
    with open('test_example.txt', 'w') as fh:
        pass
    
    burp('test_example.txt', 'Hello, world!')
    
    with open('test_example.txt', 'r') as fh:
        assert fh.read() == 'Hello, world!'
    os.remove('test_example.txt')  # Clean up the test file

# Test writing to stdout
def test_burp_stdout(capsys):
    burp('-', 'Hello, world!', allow_stdout=True)
    captured = capsys.readouterr()
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_files_burp_0
pytutils/Test4DT_tests/test_pytutils_files_burp_0.py:15:46: E0001: Parsing failed: 'expected an indented block after 'with' statement on line 15 (Test4DT_tests.test_pytutils_files_burp_0, line 15)' (syntax-error)


"""