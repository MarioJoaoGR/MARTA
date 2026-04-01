
import sys
import os
from io import StringIO
import pytest
from pytutils.files import burp

def test_stdout_output():
    # Capture the standard output
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Test writing to stdout
    burp('-', 'Hello, world!', allow_stdout=True)
    assert captured_output.getvalue().strip() == 'Hello, world!'
    
    # Reset the standard output
    sys.stdout = sys.__stdout__
