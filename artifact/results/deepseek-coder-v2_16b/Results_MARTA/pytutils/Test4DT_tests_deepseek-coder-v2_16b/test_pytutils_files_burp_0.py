
import pytest
import os
import sys
from io import StringIO

# Assuming the burp function is defined in a module named pytutils.files
# from pytutils.files import burp

def burp(filename, contents, mode='w', allow_stdout=True, expanduser=True, expandvars=True):
    if filename == '-' and allow_stdout:
        sys.stdout.write(contents)
    else:
        if expanduser:
            filename = os.path.expanduser(filename)
        if expandvars:
            filename = os.path.expandvars(filename)

        with open(filename, mode) as fh:
            fh.write(contents)

# Test function for valid input scenario
def test_valid_input():
    # Redirect stdout to capture output
    captured_output = StringIO()
    sys.stdout = captured_output
    
    burp('example.txt', 'Hello, world!')
    
    # Reset redirect.
    sys.stdout = sys.__stdout__
    
    # Check if the file was created and contains the expected content
    with open('example.txt', 'r') as f:
        assert f.read() == 'Hello, world!'
    
    # Clean up by removing the test file
    os.remove('example.txt')

# Test function for stdout output scenario
def test_stdout_output():
    # Redirect stdout to capture output
    captured_output = StringIO()
    sys.stdout = captured_output
    
    burp('-', 'Hello, world!')
    
    # Reset redirect.
    sys.stdout = sys.__stdout__
    
    assert captured_output.getvalue().strip() == 'Hello, world!'

# Test function for invalid input scenario
def test_invalid_input():
    with pytest.raises(TypeError):  # Expect a TypeError since None and '' are not valid inputs
        burp(None, '')
