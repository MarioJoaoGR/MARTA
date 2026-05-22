
import pytest
from httpie.cli.argtypes import readable_file_arg
import os
import argparse

def test_valid_file():
    # Test with a valid file path
    filename = 'example.txt'
    assert readable_file_arg(filename) == 'example.txt'
    
    # Test with an invalid file path
    with pytest.raises(argparse.ArgumentTypeError):
        readable_file_arg('nonexistent.txt')
