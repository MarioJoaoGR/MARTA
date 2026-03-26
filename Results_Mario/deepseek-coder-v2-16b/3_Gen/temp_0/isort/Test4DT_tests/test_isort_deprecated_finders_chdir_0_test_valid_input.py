
import os
from isort.deprecated.finders import chdir
import pytest

def test_valid_input():
    # Save current working directory
    initial_cwd = os.getcwd()
    
    # Define the temporary directory to change to
    temp_dir = "/tmp"
    
    # Use the chdir context manager
    with chdir(temp_dir) as cm:
        assert os.getcwd() == temp_dir, f"Expected current working directory to be {temp_dir}, but got {os.getcwd()}"
    
    # After the context block, check if the cwd is restored
    assert os.getcwd() == initial_cwd, f"Expected current working directory to be {initial_cwd} after exiting context manager, but got {os.getcwd()}"
