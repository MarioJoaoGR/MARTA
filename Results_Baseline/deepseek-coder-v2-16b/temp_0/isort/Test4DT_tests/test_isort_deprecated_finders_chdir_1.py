
import os
from contextlib import contextmanager
import pytest

@contextmanager
def chdir(path):
    curdir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(curdir)

# Test cases for the chdir function
def test_chdir_basic():
    with chdir('/tmp'):
        assert os.getcwd() == '/tmp'

def test_chdir_exception():
    try:
        with chdir('/nonexistent'):
            assert False, "Expected an exception"
    except FileNotFoundError:
        assert True

def test_chdir_nested():
    with chdir('/tmp'):
        with chdir('/usr'):
            assert os.getcwd() == '/usr'

def test_chdir_restore():
    original_dir = os.getcwd()
    try:
        with chdir('/tmp'):
            pass
        assert os.getcwd() == original_dir
    finally:
        os.chdir(original_dir)

# New test cases to cover uncovered lines 39-42 and 44
def test_chdir_initial_directory():
    initial_dir = os.getcwd()
    with chdir('/tmp'):
        assert os.getcwd() == '/tmp'
    assert os.getcwd() == initial_dir

def test_chdir_nonexistent_directory():
    try:
        with chdir('/nonexistent'):
            pytest.fail("Expected an exception")
    except FileNotFoundError:
        pass

def test_chdir_nested_directories():
    initial_dir = os.getcwd()
    with chdir('/tmp'):
        assert os.getcwd() == '/tmp'
        with chdir('/usr'):
            assert os.getcwd() == '/usr'
    assert os.getcwd() == initial_dir

def test_chdir_context_manager_error():
    try:
        with chdir('/tmp') as cm:
            raise ValueError("Test error")
    except ValueError:
        pass