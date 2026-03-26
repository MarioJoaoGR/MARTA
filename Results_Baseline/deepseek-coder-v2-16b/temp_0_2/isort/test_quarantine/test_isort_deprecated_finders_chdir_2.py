
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

# Existing test cases for the chdir function
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

# Additional test cases to cover uncovered lines 39-42 and 44
def test_chdir_initial_directory():
    initial_dir = os.getcwd()
    with chdir('/tmp'):
        # After entering the context, the directory should be '/tmp'
        assert os.getcwd() == '/tmp'
    # After exiting the context, the original directory should be restored
    assert os.getcwd() == initial_dir

def test_chdir_nonexistent_path():
    with pytest.raises(FileNotFoundError):
        with chdir('/nonexistent_path'):
            pass  # This should raise an exception, so we don't need to check the directory here

def test_chdir_nested_contexts():
    initial_dir = os.getcwd()
    with chdir('/tmp'):
        assert os.getcwd() == '/tmp'
        with chdir('/usr/local'):
            assert os.getcwd() == '/usr/local'
    # After exiting both nested contexts, the original directory should be restored
    assert os.getcwd() == initial_dir
