
import pytest
import os
import sys
import functools
from pytutils.files import islurp

# Assuming LINEMODE is defined somewhere in the module or globally
LINEMODE = 1024

def test_islurp_local_text_file():
    # Test reading a local text file line by line
    with open('test_example.txt', 'w') as f:
        f.write("Line 1\nLine 2\nLine 3")
    
    lines = list(islurp('test_example.txt'))
    