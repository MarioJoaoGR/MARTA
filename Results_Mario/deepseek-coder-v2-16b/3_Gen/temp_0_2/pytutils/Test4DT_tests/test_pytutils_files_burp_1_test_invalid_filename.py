
import os
import sys
from unittest.mock import patch
import pytest

# Assuming 'burp' is defined in a module named 'pytutils.files'
from pytutils.files import burp

def test_invalid_filename():
    invalid_path = "/nonexistent/directory/file.txt"
    contents = "Test content"
    
    with pytest.raises(FileNotFoundError):
        burp(invalid_path, contents)
