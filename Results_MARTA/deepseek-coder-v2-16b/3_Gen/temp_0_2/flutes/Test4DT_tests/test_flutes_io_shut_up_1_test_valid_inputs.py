
import sys
import os
import pytest
from flutes.io import shut_up

@pytest.fixture
def capture_stdout():
    old_stdout = sys.stdout
    new_stdout = open(os.devnull, 'w')
    sys.stdout = new_stdout
    yield
    sys.stdout = old_stdout

@pytest.fixture
def capture_stderr():
    old_stderr = sys.stderr
    new_stderr = open(os.devnull, 'w')
    sys.stderr = new_stderr
    yield
    sys.stderr = old_stderr

def test_shut_up_with_stderr(capture_stdout, capture_stderr):
    @shut_up(stderr=True)
    def verbose_func():
        print("This should not be printed")
    verbose_func()

def test_shut_up_with_stdout(capture_stdout, capture_stderr):
    @shut_up(stdout=True)
    def verbose_func():
        print("This should not be printed", file=sys.stdout)
    verbose_func()

def test_shut_up_with_both(capture_stdout, capture_stderr):
    @shut_up(stderr=True, stdout=True)
    def verbose_func():
        print("This should not be printed", file=sys.stdout)
        print("Neither should this", file=sys.stderr)
    verbose_func()
