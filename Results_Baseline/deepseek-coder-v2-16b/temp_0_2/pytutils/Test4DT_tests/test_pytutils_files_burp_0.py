
# Module: pytutils.files
import pytest
import sys
import os
from pytutils.files import burp
import io  # Importing io module to resolve pylint error

# Test cases for the burp function
def test_burp_file_write():
    # Write to a file
    filename = 'test_file.txt'
    contents = 'Hello, world!'
    burp(filename, contents)
    with open(filename, 'r') as f:
        assert f.read() == contents
    os.remove(filename)  # Clean up the file after test

def test_burp_stdout_write():
    # Write to stdout
    filename = '-'
    contents = 'Hello, world!'
    captured_output = io.StringIO()
    sys.stdout = captured_output
    burp(filename, contents, allow_stdout=True)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == contents

def test_burp_expanduser():
    # Expand user home directory in the filename
    filename = '~/test_file.txt'
    contents = 'Hello, world!'
    expanded_filename = os.path.expanduser(filename)
    burp(filename, contents, expanduser=True)
    with open(expanded_filename, 'r') as f:
        assert f.read() == contents
    os.remove(expanded_filename)  # Clean up the file after test

def test_burp_expandvars():
    # Expand environment variables in the filename
    filename = '$HOME/test_file.txt'
    contents = 'Hello, world!'
    expanded_filename = os.path.expandvars(filename)
    burp(filename, contents, expandvars=True)
    with open(expanded_filename, 'r') as f:
        assert f.read() == contents
    os.remove(expanded_filename)  # Clean up the file after test

if __name__ == "__main__":
    pytest.main()
