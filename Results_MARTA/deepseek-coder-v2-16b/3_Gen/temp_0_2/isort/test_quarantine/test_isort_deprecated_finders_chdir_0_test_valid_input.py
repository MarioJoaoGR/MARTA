
import os
from contextlib import contextmanager
import pytest

@contextmanager
def chdir(path: str):
    curdir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(curdir)

def test_valid_input():
    # Define the path to switch to (a valid directory)
    new_path = "/tmp"  # Using /tmp as an example, ensure this is a valid directory in your environment
    
    # Use the chdir context manager
    with chdir(new_path):
        assert os.getcwd() == new_path
        
    # After the with block, the original directory should be restored
    assert os.getcwd() != new_path
