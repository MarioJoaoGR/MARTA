
import sys
import os
from io import StringIO
import pytest
from flutes.io import shut_up

# Mocking sys.stdout and sys.stderr to capture output
class MockStdout:
    def __init__(self):
        self.content = []

    def write(self, s):
        self.content.append(s)

    def getvalue(self):
        return ''.join(self.content)

class MockStderr:
    def __init__(self):
        self.content = []

    def write(self, s):
        self.content.append(s)

    def getvalue(self):
        return ''.join(self.content)

@pytest.fixture
def mock_stdout():
    original_stdout = sys.stdout
    sys.stdout = MockStdout()
    yield sys.stdout
    sys.stdout = original_stdout

@pytest.fixture
def mock_stderr():
    original_stderr = sys.stderr
    sys.stderr = MockStderr()
    yield sys.stderr
    sys.stderr = original_stderr

def test_shut_up_with_stderr(mock_stderr):
    @shut_up(stderr=True, stdout=False)
    def print_something():
        print("This should not be printed")
        sys.stderr.write("This should be suppressed\n")
    
    print_something()
    assert MockStderr().getvalue() == ""

def test_shut_up_with_stdout(mock_stdout):
    @shut_up(stderr=False, stdout=True)
    def print_something():
        print("This should not be printed")
        sys.stdout.write("This should be suppressed\n")
    
    print_something()
    assert MockStdout().getvalue() == ""

def test_shut_up_with_both(mock_stdout, mock_stderr):
    @shut_up(stderr=True, stdout=True)
    def print_something():
        print("This should not be printed")
        sys.stdout.write("This should be suppressed\n")
        sys.stderr.write("This should also be suppressed\n")
    
    print_something()
    assert MockStdout().getvalue() == ""
    assert MockStderr().getvalue() == ""
