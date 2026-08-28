
# Module: pytutils.files
import pytest
import sys
import os
from pytutils.files import burp
import io  # Importing io module for StringIO usage

# Test writing to a file
def test_burp_file():
    with open('test_example.txt', 'w') as fh:
        pass  # Ensure the file is created for testing purposes
    
    burp('test_example.txt', 'Hello, world!')
    
    with open('test_example.txt', 'r') as fh:
        assert fh.read() == 'Hello, world!'
    os.remove('test_example.txt')  # Clean up the test file

# Test writing to stdout
def test_burp_stdout():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    burp('-', 'Hello, world!', allow_stdout=True)
    
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == 'Hello, world!'

# Test expanding user home directory in the filename
def test_burp_expanduser():
    home_dir = os.path.expanduser('~')
    burp(f'{home_dir}/test_example.txt', 'Hello, world!', expanduser=True)
    
    with open(f'{home_dir}/test_example.txt', 'r') as fh:
        assert fh.read() == 'Hello, world!'
    os.remove(f'{home_dir}/test_example.txt')  # Clean up the test file

# Test expanding environment variables in the filename
def test_burp_expandvars():
    expanded_path = os.path.expandvars('$HOME/test_example.txt')
    burp(expanded_path, 'Hello, world!', expandvars=True)
    
    home_dir = os.getenv('HOME')
    with open(f'{home_dir}/test_example.txt', 'r') as fh:
        assert fh.read() == 'Hello, world!'
    os.remove(f'{home_dir}/test_example.txt')  # Clean up the test file
