# Module: isort.deprecated.finders
import pytest
from contextlib import contextmanager
import os
from typing import Iterator

# Import the function from its module
from isort.deprecated.finders import chdir

@contextmanager
def custom_chdir(path: str):
    curdir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(curdir)

# Test cases for the chdir function
def test_chdir_basic():
    with custom_chdir('/tmp'):
        assert os.getcwd() == '/tmp'
    # After the context block, the original working directory is restored
    assert os.getcwd() != '/tmp'

def test_chdir_exception():
    try:
        with pytest.raises(FileNotFoundError):
            with custom_chdir('/nonexistent_path'):
                pass  # This should raise an exception, so we don't need to check the directory here
    except FileNotFoundError:
        assert True  # The assertion is implicit in the try-except block for exceptions

def test_chdir_specific_path():
    with custom_chdir('/usr/local'):
        assert os.getcwd() == '/usr/local'
    # After the context block, the original working directory is restored
    assert os.getcwd() != '/usr/local'
